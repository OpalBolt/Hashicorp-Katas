from pathlib import Path
import shutil
import subprocess
import unittest


ROOT = Path(__file__).resolve().parents[1]


@unittest.skipUnless(shutil.which("node"), "Node.js is required for JavaScript tests")
class MermaidLightboxTests(unittest.TestCase):
    def test_zoom_steps_and_dragging(self):
        test = r"""
const assert = require("node:assert/strict");
const fs = require("node:fs");
const vm = require("node:vm");

function target(properties = {}) {
  return {
    ...properties,
    listeners: {},
    addEventListener(type, listener) { this.listeners[type] = listener; },
    fire(type, event = {}) { this.listeners[type]?.(event); },
  };
}

const classes = new Set();
const captured = new Set();
const viewport = target({
  scrollWidth: 1000, clientWidth: 500, scrollHeight: 1000, clientHeight: 500,
  scrollLeft: 200, scrollTop: 200,
  classList: { add: (name) => classes.add(name), remove: (name) => classes.delete(name) },
  scrollTo(left, top) { this.scrollLeft = left; this.scrollTop = top; },
  setPointerCapture(id) { captured.add(id); },
  hasPointerCapture(id) { return captured.has(id); },
  releasePointerCapture(id) { captured.delete(id); },
});
const canvas = target({ style: {} });
const elements = {
  ".mermaid-lightbox__viewport": viewport,
  ".mermaid-lightbox__canvas": canvas,
  "[data-zoom-out]": target(),
  "[data-zoom-in]": target(),
  "[data-close]": target(),
  output: {},
};
const dialog = target({
  setAttribute() {},
  querySelector(selector) { return elements[selector]; },
});
const document = {
  createElement() { return dialog; },
  body: { append() {} },
  querySelectorAll() { return []; },
};
const window = target();
class MutationObserver { observe() {} }
vm.runInNewContext(fs.readFileSync(process.argv[1], "utf8"), {
  document, window, MutationObserver, Element: class {},
});

function pointer(overrides = {}) {
  return {
    pointerId: 1, pointerType: "mouse", button: 0, buttons: 1,
    clientX: 100, clientY: 100, defaultPrevented: false,
    preventDefault() { this.defaultPrevented = true; },
    ...overrides,
  };
}

const down = pointer();
canvas.fire("pointerdown", down);
assert.equal(down.defaultPrevented, true);
window.fire("pointermove", pointer({ clientX: 98 }));
assert.equal(captured.size, 0);
window.fire("pointermove", pointer({ clientX: 60, clientY: 75 }));
assert.deepEqual([viewport.scrollLeft, viewport.scrollTop], [240, 225]);
assert.equal(classes.has("is-dragging"), true);
assert.equal(captured.has(1), true);
window.fire("pointerup", pointer());
assert.equal(classes.has("is-dragging"), false);
assert.equal(captured.size, 0);
window.fire("pointermove", pointer({ clientX: 20, clientY: 20 }));
assert.deepEqual([viewport.scrollLeft, viewport.scrollTop], [240, 225]);

for (const options of [{ pointerType: "touch" }, { button: 2 }]) {
  const other = pointer(options);
  canvas.fire("pointerdown", other);
  assert.equal(other.defaultPrevented, false);
  window.fire("pointermove", pointer({ clientX: 20, clientY: 20 }));
  assert.deepEqual([viewport.scrollLeft, viewport.scrollTop], [240, 225]);
}

canvas.fire("pointerdown", pointer());
window.fire("pointermove", pointer({ pointerId: 2, clientX: 20 }));
assert.deepEqual([viewport.scrollLeft, viewport.scrollTop], [240, 225]);
window.fire("pointermove", pointer({ clientX: 80 }));
window.fire("pointercancel", pointer());
assert.equal(classes.has("is-dragging"), false);
assert.equal(captured.size, 0);

viewport.scrollWidth = viewport.clientWidth;
viewport.scrollHeight = viewport.clientHeight;
const fits = pointer();
canvas.fire("pointerdown", fits);
assert.equal(fits.defaultPrevented, false);

const zoomIn = elements["[data-zoom-in]"];
const zoomOut = elements["[data-zoom-out]"];
zoomIn.fire("click");
assert.equal(elements.output.value, "125%");
assert.equal(canvas.style.zoom, 1.25);
zoomIn.fire("click");
assert.equal(elements.output.value, "150%");
zoomOut.fire("click");
assert.equal(elements.output.value, "125%");
for (let i = 0; i < 3; i++) zoomOut.fire("click");
assert.equal(elements.output.value, "50%");
assert.equal(zoomOut.disabled, true);
zoomIn.fire("click");
assert.equal(elements.output.value, "75%");
assert.equal(zoomOut.disabled, false);
for (let i = 0; i < 29; i++) zoomIn.fire("click");
assert.equal(elements.output.value, "800%");
assert.equal(zoomIn.disabled, true);
zoomOut.fire("click");
assert.equal(elements.output.value, "775%");
assert.equal(zoomIn.disabled, false);
"""
        result = subprocess.run(
            ["node", "-e", test, str(ROOT / "docs/javascripts/mermaid-lightbox.js")],
            cwd=ROOT,
            text=True,
            capture_output=True,
        )
        self.assertEqual(result.returncode, 0, result.stderr)


if __name__ == "__main__":
    unittest.main()
