# JavaScript & Custom Ops in Cables.gl

## Introduction

While cables.gl's visual node system is powerful, sometimes you need custom functionality. JavaScript allows you to create your own operators (ops) and extend cables.gl's capabilities.

**Official reference:** if you ever wonder “is this a real API?”, start with [cables.gl docs](https://cables.gl/docs) and search for terms like **Custom Ops**, **JavaScript Op**, **Ports**, or **Standalone Export**. The editor/runtime evolves, so keeping one “source of truth” bookmark helps.

## When to Use Custom Ops

- Processing data in ways built-in ops don't support
- Integrating external APIs or libraries
- Creating reusable custom functionality
- Performance optimization for specific tasks
- Complex mathematical operations

## Creating Your First Op

### Step 1: Open the Op Editor

1. In your patch, click the "+" button
2. Select "Create Op"
3. Choose a name (e.g., `Ops.User.YourName.MyFirstOp`)

**Naming tip:** treat op names like package names. Keep them stable and descriptive (e.g. `Ops.User.Rangel.Math.ClampSmooth`), because you’ll likely reuse the op across patches and exports.

### Step 2: Understanding the Structure

```javascript
// Ports (inputs and outputs)
const inValue = op.inFloat("Input Value", 0);
const outResult = op.outNumber("Result");

// When input changes, recalculate
inValue.onChange = function() {
    outResult.set(inValue.get() * 2);
};
```

## Port Types

### Input Ports

```javascript
// Trigger (execution flow)
const inTrigger = op.inTrigger("Trigger");

// Numbers
const inFloat = op.inFloat("Float Value", 0.0);
const inInt = op.inInt("Integer", 0);
const inValue = op.inValue("Value", 0);

// Boolean
const inBool = op.inBool("Enabled", true);

// String
const inString = op.inString("Text", "default");

// Objects (textures, arrays, etc.)
const inObject = op.inObject("Object");
const inTexture = op.inTexture("Texture");
const inArray = op.inArray("Array");
```

### Output Ports

```javascript
// Trigger
const outTrigger = op.outTrigger("Trigger Out");

// Numbers
const outNumber = op.outNumber("Number Out");
const outValue = op.outValue("Value Out");

// Boolean
const outBool = op.outBool("Bool Out");

// String
const outString = op.outString("String Out");

// Objects
const outObject = op.outObject("Object Out");
const outTexture = op.outTexture("Texture Out");
const outArray = op.outArray("Array Out");
```

## Handling Events

### Trigger Execution

```javascript
const inTrigger = op.inTrigger("Execute");
const outNext = op.outTrigger("Next");

inTrigger.onTriggered = function() {
    // Do something when triggered
    console.log("Op was triggered!");
    
    // Continue the chain
    outNext.trigger();
};
```

### Value Changes

```javascript
const inValue = op.inFloat("Value", 0);
const outDouble = op.outNumber("Double");

inValue.onChange = function() {
    const val = inValue.get();
    outDouble.set(val * 2);
};
```

### Linking Ports

```javascript
// Automatically update output when input changes
const inValue = op.inFloat("Value", 0);
const outValue = op.outNumber("Value Out");

inValue.onChange = outValue.setRef.bind(outValue, inValue);
// or simply:
// inValue.onChange = () => outValue.set(inValue.get());
```

## Working with Arrays

```javascript
const inArray = op.inArray("Input Array");
const outArray = op.outArray("Output Array");

inArray.onChange = function() {
    const arr = inArray.get();
    if (!arr) return;
    
    // Process array
    const result = arr.map(x => x * 2);
    
    outArray.set(result);
};
```

## Working with Objects

```javascript
const inObject = op.inObject("Input");
const outObject = op.outObject("Output");

inObject.onChange = function() {
    const obj = inObject.get();
    if (!obj) return;
    
    // Process or wrap the object
    const processed = {
        ...obj,
        processed: true
    };
    
    outObject.set(processed);
};
```

## Render Loop Integration

For ops that need to run every frame:

```javascript
const inTrigger = op.inTrigger("Render");
const outNext = op.outTrigger("Next");

let time = 0;

inTrigger.onTriggered = function() {
    time += op.patch.timer.getDelta();
    
    // Do per-frame calculations
    
    outNext.trigger();
};
```

## UI Port Groups

Organize your ports into collapsible groups:

```javascript
// Create ports
const inX = op.inFloat("X", 0);
const inY = op.inFloat("Y", 0);
const inZ = op.inFloat("Z", 0);

// Group them
op.setPortGroup("Position", [inX, inY, inZ]);
```

## Port UI Types

Change how ports appear in the UI:

```javascript
// Slider
const inValue = op.inFloat("Value", 0.5);
op.setUiAttrib({ "type": "slider", "min": 0, "max": 1 });

// Color picker
const inR = op.inFloat("R", 1);
const inG = op.inFloat("G", 1);
const inB = op.inFloat("B", 1);
op.setPortGroup("Color", [inR, inG, inB]);
inR.setUiAttribs({ colorPick: true });

// Dropdown
const inMode = op.inSwitch("Mode", ["Option1", "Option2", "Option3"], "Option1");
```

## Accessing Patch Resources

### Timer and Time

```javascript
// Current time
const time = op.patch.timer.getTime();

// Delta time (time since last frame)
const delta = op.patch.timer.getDelta();

// FPS
const fps = op.patch.timer.getFPS();
```

### Canvas and Context

```javascript
// Canvas element
const canvas = op.patch.cgl.canvas;

// WebGL context
const gl = op.patch.cgl.gl;
```

### Loading External Resources

```javascript
const inUrl = op.inString("URL", "");
const outData = op.outObject("Data");

inUrl.onChange = function() {
    const url = inUrl.get();
    if (!url) return;
    
    fetch(url)
        .then(response => {
            if (!response.ok) throw new Error(`HTTP ${response.status}`);
            return response.json();
        })
        .then(data => {
            outData.set(data);
        })
        .catch(error => {
            op.logError("Failed to load:", error);
        });
};
```

Notes:

- Many APIs require CORS headers; if `fetch()` fails in the browser console, it’s often *not* your code.
- If this request should block “patch is ready”, pair it with `op.patch.loading.start()` / `finished()` (see the **Async Ops** section later in this chapter).

## Using External Libraries

### Including Libraries

```javascript
// In op's code, load an external script
const script = document.createElement("script");
script.src = "https://cdn.example.com/library.js";
script.onload = function() {
    // Library is ready
    initLibrary();
};
document.head.appendChild(script);
```

**Best practice:** prefer shipping a local copy for standalone exports (and environments with strict CSP), and load from CDN only when you control the hosting/security headers.

### Or use op.patch.loading for proper load tracking:

```javascript
op.patch.loading.start();

const script = document.createElement("script");
script.src = "https://cdn.example.com/library.js";
script.onload = function() {
    op.patch.loading.finished();
    initLibrary();
};
script.onerror = function() {
    op.patch.loading.finished();
    op.logError("Failed to load library");
};
document.head.appendChild(script);
```

## Integrating Hydra (by Olivia Jack)

**Hydra** (by Olivia Jack) is a live-coded, GPU-accelerated visual synth for the browser. In practice it’s a **shader graph you can write as code**: generators like `osc()` / `noise()` / `shape()` chained with modifiers like `kaleid()` / `rotate()` / `modulate()` and sent to buffers with `.out()`.

Hydra pairs extremely well with cables.gl because cables already has a strong “everything is a texture” workflow: you can treat Hydra as a **procedural texture source** (2D or 3D), then run it through your usual cables effects chain.

**Official resources:**
- Hydra editor: [Hydra](https://hydra.ojack.xyz/)
- Docs: [Hydra documentation](https://hydra.ojack.xyz/docs/)
- Source: [ojack/hydra](https://github.com/ojack/hydra)
- npm package commonly used in-browser: `hydra-synth` (often loaded as a single bundled JS file)

### Where Hydra fits in cables.gl

- **Procedural textures**: drive a `BasicMaterial` / `PBRMaterial` texture input with Hydra output.
- **2D overlays**: layer Hydra output over your render.
- **Feedback & post**: render-to-texture, then `TextureEffect` chains on Hydra output.
- **Audio-reactive visuals**: use cables audio analysis to drive Hydra parameters (without Hydra’s own audio system).

### Integration paths (choose based on your export target)

#### Option A: Fastest (editor / hosted patch) — load Hydra from a CDN

- **Pros**: quick, no build step.
- **Cons**: requires network, can be blocked by CSP, less deterministic for offline installs.

#### Option B: Standalone export — ship a local `hydra-synth.js`

If you export a standalone patch, you can include `hydra-synth.js` inside the exported folder and load it locally (no CDN). This is best for **galleries, offline installations, kiosks**.

#### Option C: npm package export / external JS project — bundle Hydra with your app

If you export as an npm package and integrate into another JS project, you can add Hydra as a dependency and bundle it with your build pipeline. That keeps everything versioned and reproducible.

### Most stable approach: Hydra > hidden `<canvas>` > `HtmlToTexture`

Instead of trying to push Hydra pixels into a custom WebGL texture manually (fragile, runtime-specific), use this pattern:

- **Hydra renders into a hidden HTML `<canvas>`**
- cables.gl uses **`Ops.Extension.HtmlToTexture.HtmlToTexture`** to capture that canvas as a texture

This stays close to cables.gl’s existing patterns and tends to survive exports better.

#### Step 1: Create a “Hydra Host” custom op (creates and runs the Hydra canvas)

This op:
- loads Hydra once (CDN or local)
- creates a canvas with a known `id`
- initializes Hydra to render into that canvas
- exposes a few numeric parameters you can drive from the patch

```javascript
// Op: Ops.User.Hydra.HydraHost
//
// Patch wiring idea:
// - Trigger this op from MainLoop (Render)
// - Use HtmlToTexture to capture the canvas by ID: #hydra-canvas

const inInit = op.inTriggerButton("Init");
const inRender = op.inTrigger("Render");

const inCanvasId = op.inString("Canvas Id", "hydra-canvas");
const inWidth = op.inInt("Width", 1024);
const inHeight = op.inInt("Height", 1024);

const inPreset = op.inSwitch("Preset", ["osc", "noise", "kaleid"], "osc");
const inP1 = op.inFloat("P1", 0.5);
const inP2 = op.inFloat("P2", 0.5);
const inP3 = op.inFloat("P3", 0.5);

const outReady = op.outBool("Ready");
const outError = op.outString("Error");
const outNext = op.outTrigger("Next");

let hydra = null;
let canvasEl = null;
let presetApplied = null;

// Keep params as plain JS variables so Hydra can read them via functions.
let p1 = inP1.get();
let p2 = inP2.get();
let p3 = inP3.get();
inP1.onChange = () => (p1 = inP1.get());
inP2.onChange = () => (p2 = inP2.get());
inP3.onChange = () => (p3 = inP3.get());

function ensureCanvas() {
  const id = inCanvasId.get();
  const w = Math.max(16, inWidth.get() | 0);
  const h = Math.max(16, inHeight.get() | 0);

  let el = document.getElementById(id);
  if (!el) {
    el = document.createElement("canvas");
    el.id = id;
    // keep it out of the way
    el.style.position = "fixed";
    el.style.left = "-10000px";
    el.style.top = "-10000px";
    document.body.appendChild(el);
  }
  el.width = w;
  el.height = h;
  return el;
}

function loadHydraScriptOnce(url) {
  // Cache the promise globally so multiple ops don’t race-load.
  if (window.__hydraSynthLoading) return window.__hydraSynthLoading;
  window.__hydraSynthLoading = new Promise((resolve, reject) => {
    const script = document.createElement("script");
    script.src = url;
    script.onload = resolve;
    script.onerror = () => reject(new Error("Failed to load Hydra script"));
    document.head.appendChild(script);
  });
  return window.__hydraSynthLoading;
}

function initHydra() {
  try {
    canvasEl = ensureCanvas();

    // If Hydra is already global, reuse it.
    if (window.__hydraInstance) {
      hydra = window.__hydraInstance;
      outReady.set(true);
      return;
    }

    // Hydra constructor is typically global after loading the script.
    // makeGlobal=true gives you global functions like osc(), noise(), shape(), etc.
    hydra = new Hydra({
      canvas: canvasEl,
      detectAudio: false,
      makeGlobal: true,
    });

    window.__hydraInstance = hydra;
    outReady.set(true);
    outError.set("");
  } catch (e) {
    outReady.set(false);
    outError.set(String(e && e.message ? e.message : e));
  }
}

function applyPreset(name) {
  // Only apply when changed; many Hydra params can be functions so they stay “live”.
  if (!outReady.get()) return;
  if (presetApplied === name) return;
  presetApplied = name;

  // Clear output first (simple “reset”).
  // solid(0,0,0,1).out() would be an alternative, depending on your desired baseline.
  try {
    if (name === "osc") {
      osc(
        () => 5 + p1 * 40,     // frequency
        () => p2 * 2,         // sync
        () => p3              // offset
      ).kaleid(() => 1 + Math.floor(p1 * 6)).out();
      return;
    }

    if (name === "noise") {
      noise(() => 1 + p1 * 8, () => p2).colorama(() => p3 * 4).out();
      return;
    }

    if (name === "kaleid") {
      shape(() => 3 + Math.floor(p1 * 8), () => p2 * 0.5, () => p3 * 0.5)
        .kaleid(() => 2 + Math.floor(p1 * 10))
        .rotate(() => p2 * Math.PI * 2)
        .out();
      return;
    }
  } catch (e) {
    outError.set(String(e && e.message ? e.message : e));
  }
}

inInit.onTriggered = async function () {
  outError.set("");
  outReady.set(false);

  op.patch.loading.start();
  try {
    // CDN option. For offline/standalone, point this to a local file you ship.
    await loadHydraScriptOnce("https://cdn.jsdelivr.net/npm/hydra-synth@latest/dist/hydra-synth.js");
    initHydra();
  } catch (e) {
    outError.set(String(e && e.message ? e.message : e));
  } finally {
    op.patch.loading.finished();
  }
};

inRender.onTriggered = function () {
  // Ensure canvas stays at chosen size even if width/height ports change.
  if (outReady.get()) {
    canvasEl = ensureCanvas();
    applyPreset(inPreset.get());
  }
  outNext.trigger();
};
```

#### Step 2: Capture the Hydra canvas as a texture

Use the op documentation entry for:

- `Ops.Extension.HtmlToTexture.HtmlToTexture` (see the corresponding ops chapter page)

The key idea is: configure `HtmlToTexture` to target the canvas id you created (default `#hydra-canvas`) and then treat the output like any other texture.

### Why presets (instead of “Hydra code as a string”)?

Running arbitrary code strings (via `eval` / `new Function`) is powerful, but it’s also:
- **unsafe** (especially in exported / embedded contexts)
- **hard to debug** (errors happen in dynamic code paths)
- **often blocked** by stricter Content Security Policy configurations

The preset approach gives you 90% of the creative power with better stability. If you *do* want live-coded strings, keep it as an explicit “advanced / unsafe” path and gate it behind a boolean toggle in the op UI.

### Audio-reactive Hydra (cables-driven)

Hydra has its own audio features, but in cables.gl it’s usually cleaner to drive Hydra using audio analysis you already have in the patch:

- Use cables FFT / RMS → map into `P1/P2/P3` → Hydra preset reads them via functions.

Example mapping:
- **bass** → `P1` (structure)
- **mid** → `P2` (motion)
- **treble** → `P3` (color/detail)

### Performance & quality tips

- **Resolution matters**: start at 512–1024 square for Hydra canvas; scale up only if needed.
- **Avoid re-building the Hydra graph every frame**: set up the chain once (preset), then let parameters be functions.
- **Export/offline**: prefer local Hydra JS file rather than CDN.
- **One Hydra instance**: with `makeGlobal=true`, treat Hydra like a singleton (simple + reliable).

### Troubleshooting

- **Hydra canvas exists but texture is blank**: confirm the canvas is in the DOM and its `id` matches your `HtmlToTexture` selector.
- **Nothing renders after export**: CDN might be blocked; switch to a local Hydra file shipped with the export.
- **Errors like “Hydra is not defined”**: the script didn’t load; check network/CSP and the script URL.

## Error Handling

```javascript
try {
    // Risky operation
    const result = riskyFunction();
    outResult.set(result);
} catch (error) {
    op.logError("Operation failed:", error);
    op.setUiError("error", error.message);
}

// Clear error when fixed
op.setUiError("error", null);
```

## Example: Custom Math Op

```javascript
// Custom clamp with smoothing

const inValue = op.inFloat("Value", 0);
const inMin = op.inFloat("Min", 0);
const inMax = op.inFloat("Max", 1);
const inSmoothing = op.inFloat("Smoothing", 0);
const outValue = op.outNumber("Result");

let currentValue = 0;

function update() {
    let val = inValue.get();
    const min = inMin.get();
    const max = inMax.get();
    const smooth = inSmoothing.get();
    
    // Clamp
    val = Math.max(min, Math.min(max, val));
    
    // Smooth
    if (smooth > 0) {
        currentValue += (val - currentValue) * (1 - smooth);
    } else {
        currentValue = val;
    }
    
    outValue.set(currentValue);
}

inValue.onChange = update;
inMin.onChange = update;
inMax.onChange = update;
inSmoothing.onChange = update;
```

## Example: Array Processor

```javascript
// Sum all values in an array

const inArray = op.inArray("Values");
const outSum = op.outNumber("Sum");
const outAverage = op.outNumber("Average");
const outCount = op.outNumber("Count");

inArray.onChange = function() {
    const arr = inArray.get();
    
    if (!Array.isArray(arr) || arr.length === 0) {
        outSum.set(0);
        outAverage.set(0);
        outCount.set(0);
        return;
    }
    
    const sum = arr.reduce((a, b) => a + b, 0);
    const count = arr.length;
    const average = sum / count;
    
    outSum.set(sum);
    outAverage.set(average);
    outCount.set(count);
};
```

## Example: API Fetcher

```javascript
// Fetch data from an API

const inUrl = op.inString("API URL", "");
const inFetch = op.inTriggerButton("Fetch");
const outData = op.outObject("Data");
const outLoading = op.outBool("Loading");
const outError = op.outString("Error");

inFetch.onTriggered = async function() {
    const url = inUrl.get();
    if (!url) return;
    
    outLoading.set(true);
    outError.set("");
    
    try {
        const response = await fetch(url);
        const data = await response.json();
        outData.set(data);
    } catch (error) {
        outError.set(error.message);
        outData.set(null);
    } finally {
        outLoading.set(false);
    }
};
```

## Debugging Tips

```javascript
// Log to console
console.log("Value:", inValue.get());

// Op-specific logging (shows in cables UI)
op.log("This is a log message");
op.logWarn("This is a warning");
op.logError("This is an error");

// Visual debugging
op.setUiAttrib({ "error": "Something went wrong" });
```

## Advanced Patterns (How to Build “Good” Ops)

Once you start writing more than a couple custom ops, quality becomes less about JavaScript syntax and more about **behavior**:

- **Determinism**: given the same inputs, the op produces the same outputs.
- **Clear execution model**: value changes vs trigger-based evaluation are intentional.
- **Performance**: avoid unnecessary allocations and expensive work per frame.
- **Good UI/UX**: errors are visible, defaults are sane, ports are grouped and labeled.

### Pattern: Separate “Compute” from “Trigger”

A clean approach is:

- collect values in `onChange`
- do the heavy compute in one `update()` function
- call `update()` from whichever events are relevant

```javascript
const inTrigger = op.inTrigger("Update");
const inA = op.inFloat("A", 0);
const inB = op.inFloat("B", 0);
const outResult = op.outNumber("Result");
const outNext = op.outTrigger("Next");

function update() {
  outResult.set(inA.get() + inB.get());
}

inA.onChange = update;
inB.onChange = update;

inTrigger.onTriggered = function () {
  update();
  outNext.trigger();
};
```

### Pattern: “Only Recompute When Dirty”

If an op gets triggered every frame but its inputs rarely change, cache the result:

```javascript
const inTrigger = op.inTrigger("Render");
const outNext = op.outTrigger("Next");

const inValue = op.inFloat("Value", 0);
const outProcessed = op.outNumber("Processed");

let dirty = true;
let cached = 0;

function recompute() {
  const v = inValue.get();
  // pretend this is expensive:
  cached = Math.sin(v) * Math.cos(v) * 1000;
  outProcessed.set(cached);
  dirty = false;
}

inValue.onChange = function () {
  dirty = true;
};

inTrigger.onTriggered = function () {
  if (dirty) recompute();
  outNext.trigger();
};
```

### Pattern: Debounce (Stabilize Noisy Inputs)

Useful for sliders, mouse input, or network-driven values.

```javascript
const inValue = op.inFloat("Value", 0);
const inDelayMs = op.inInt("Delay (ms)", 200);
const outValue = op.outNumber("Debounced");

let t = null;

inValue.onChange = function () {
  if (t) clearTimeout(t);
  const v = inValue.get();
  t = setTimeout(() => outValue.set(v), inDelayMs.get());
};
```

### Pattern: Rate-Limit (Prevent Flooding Downstream)

Useful when sending values to other systems (e.g., API calls, heavy compute, UI).

```javascript
const inTrigger = op.inTrigger("Trigger");
const inMinIntervalMs = op.inInt("Min Interval (ms)", 100);
const outNext = op.outTrigger("Next");

let last = 0;

inTrigger.onTriggered = function () {
  const now = performance.now();
  if (now - last >= inMinIntervalMs.get()) {
    last = now;
    outNext.trigger();
  }
};
```

### Pattern: Stateful Ops (Resettable Systems)

Any op that accumulates state should expose a reset trigger.

```javascript
const inAdd = op.inTrigger("Add");
const inReset = op.inTrigger("Reset");
const inValue = op.inFloat("Value", 1);
const outSum = op.outNumber("Sum");

let sum = 0;

function emit() {
  outSum.set(sum);
}

inAdd.onTriggered = function () {
  sum += inValue.get();
  emit();
};

inReset.onTriggered = function () {
  sum = 0;
  emit();
};
```

## Async Ops (Fetching Data Safely)

When you talk to the network, the two most important qualities are:

- **cancellation**: don’t keep old requests alive if the user changes the URL
- **loading/error UX**: surface the state to the patch (and optionally the UI)

### Example: Fetch JSON with Cancellation

```javascript
const inUrl = op.inString("URL", "");
const inFetch = op.inTriggerButton("Fetch");

const outData = op.outObject("Data");
const outLoading = op.outBool("Loading");
const outError = op.outString("Error");

let controller = null;

inFetch.onTriggered = async function () {
  const url = inUrl.get();
  if (!url) return;

  // cancel previous request
  if (controller) controller.abort();
  controller = new AbortController();

  outLoading.set(true);
  outError.set("");

  try {
    const res = await fetch(url, { signal: controller.signal });
    if (!res.ok) throw new Error(`HTTP ${res.status}`);
    const json = await res.json();
    outData.set(json);
  } catch (e) {
    // ignore abort errors as “expected”
    if (e && e.name === "AbortError") return;
    outError.set(String(e && e.message ? e.message : e));
    outData.set(null);
  } finally {
    outLoading.set(false);
  }
};
```

### Loading Semantics (Patch-Friendly)

If an op blocks the patch from being “ready” until something loads, use the patch loading tracking mechanism shown earlier (`op.patch.loading.start()` / `finished()`), and keep those calls paired even on error paths.

## Performance Tips for Custom Ops

- **Avoid allocations in per-frame triggers**: reuse arrays/objects when possible.
- **Minimize DOM work**: avoid creating elements repeatedly; cache references.
- **Don’t spam logs**: logging inside every-frame triggers will kill performance.
- **Prefer simple math**: it’s easy to do too much in JS when the GPU could do it (shader).

## Featured Videos

<!-- Add JavaScript/Ops videos here -->

<!-- Example:
```vid
https://youtu.be/XXXXX
Title: Creating Custom Ops in Cables.gl
Author: Channel Name
```
-->

## Exercises

1. Create a custom op that formats a number with a prefix and suffix
2. Build an array shuffler op
3. Create a simple state machine op
4. Build an op that fetches and parses CSV data

