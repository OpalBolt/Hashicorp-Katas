(() => {
  const dialog = document.createElement("dialog");
  dialog.className = "md-typeset mermaid-lightbox";
  dialog.setAttribute("aria-labelledby", "mermaid-lightbox-title");
  dialog.innerHTML = `
    <div class="mermaid-lightbox__toolbar">
      <strong id="mermaid-lightbox-title">Diagram</strong>
      <button type="button" data-zoom-out aria-label="Zoom out">-</button>
      <output aria-live="polite">100%</output>
      <button type="button" data-zoom-in aria-label="Zoom in">+</button>
      <button type="button" data-close autofocus>Close</button>
    </div>
    <div class="mermaid-lightbox__viewport" tabindex="0" role="region"
         aria-label="Expanded diagram. Use the zoom buttons, then scroll or drag to explore.">
      <div class="mermaid-lightbox__canvas"></div>
    </div>
  `;
  document.body.append(dialog);

  const viewport = dialog.querySelector(".mermaid-lightbox__viewport");
  const canvas = dialog.querySelector(".mermaid-lightbox__canvas");
  const zoomOut = dialog.querySelector("[data-zoom-out]");
  const zoomIn = dialog.querySelector("[data-zoom-in]");
  const output = dialog.querySelector("output");
  let placeholder;
  let zoom = 1;
  let drag;

  function setZoom(value) {
    zoom = value;
    canvas.style.zoom = zoom;
    output.value = `${Math.round(zoom * 100)}%`;
    zoomOut.disabled = zoom <= 0.5;
    zoomIn.disabled = zoom >= 8;
  }

  function endDrag(event) {
    if (!drag || (event && event.pointerId !== drag.pointerId)) return;
    const pointerId = drag.pointerId;
    drag = undefined;
    viewport.classList.remove("is-dragging");
    if (viewport.hasPointerCapture(pointerId)) viewport.releasePointerCapture(pointerId);
  }

  canvas.addEventListener("pointerdown", (event) => {
    if (drag || event.pointerType === "touch" || event.button !== 0) return;
    if (viewport.scrollWidth <= viewport.clientWidth && viewport.scrollHeight <= viewport.clientHeight) return;
    drag = {
      pointerId: event.pointerId,
      x: event.clientX,
      y: event.clientY,
      left: viewport.scrollLeft,
      top: viewport.scrollTop,
      moved: false,
    };
    event.preventDefault();
  });

  window.addEventListener("pointermove", (event) => {
    if (!drag || event.pointerId !== drag.pointerId) return;
    if (!(event.buttons & 1)) {
      endDrag(event);
      return;
    }
    const dx = event.clientX - drag.x;
    const dy = event.clientY - drag.y;
    if (!drag.moved) {
      if (Math.abs(dx) + Math.abs(dy) < 4) return;
      drag.moved = true;
      viewport.setPointerCapture(event.pointerId);
      viewport.classList.add("is-dragging");
    }
    viewport.scrollTo(drag.left - dx, drag.top - dy);
  });
  window.addEventListener("pointerup", endDrag);
  window.addEventListener("pointercancel", endDrag);
  window.addEventListener("blur", () => endDrag());
  viewport.addEventListener("lostpointercapture", endDrag);

  zoomOut.addEventListener("click", () => setZoom(zoom - 0.25));
  zoomIn.addEventListener("click", () => setZoom(zoom + 0.25));
  function closeDialog() {
    endDrag();
    dialog.close();
    if (placeholder.isConnected) {
      placeholder.replaceWith(canvas.firstElementChild);
    } else {
      canvas.firstElementChild.remove();
    }
    placeholder = null;
  }

  dialog.querySelector("[data-close]").addEventListener("click", closeDialog);
  dialog.addEventListener("cancel", (event) => {
    event.preventDefault();
    closeDialog();
  });
  dialog.addEventListener("click", (event) => {
    if (event.target === dialog) closeDialog();
  });

  const enhanced = new WeakSet();

  function enhanceDiagram(diagram) {
    if (!diagram.closest(".md-content") || enhanced.has(diagram)) return;
    enhanced.add(diagram);

    const button = document.createElement("button");
    button.type = "button";
    button.className = "mermaid-expand";
    button.textContent = "Expand diagram";
    button.addEventListener("click", () => {
      placeholder = document.createComment("Expanded diagram");
      diagram.replaceWith(placeholder);
      canvas.append(diagram);
      setZoom(1);
      dialog.showModal();
      canvas.style.width = `${viewport.clientWidth}px`;
      viewport.scrollTo(0, 0);
    });
    diagram.before(button);
  }

  // Material renders Mermaid asynchronously, including after instant navigation.
  new MutationObserver((records) => {
    if (placeholder && !placeholder.isConnected) closeDialog();
    for (const record of records) {
      for (const node of record.addedNodes) {
        if (!(node instanceof Element)) continue;
        if (node.matches("div.mermaid")) enhanceDiagram(node);
        node.querySelectorAll("div.mermaid").forEach(enhanceDiagram);
      }
    }
  }).observe(document.body, {
    childList: true,
    subtree: true,
  });
  document.querySelectorAll(".md-content div.mermaid").forEach(enhanceDiagram);
})();
