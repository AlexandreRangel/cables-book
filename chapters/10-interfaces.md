# Interfaces in Cables.gl

## Introduction

Cables.gl provides multiple ways to create user interfaces for your patches. You can build interfaces using HTML and CSS for full customization, or use native Cables sidebar interface operators for quick, integrated controls. This chapter covers both approaches in detail.

## Interface Approaches Overview

```
+------------------------------------------------+
|                    INTERFACE OPTIONS           |
+-------------------------------------------------------------+
|                                                |
|  1. HTML/CSS Interfaces                        |
|     +-------------------------------------+    |
|     | Full DOM control                    |    |
|     | Custom styling                      |    |
|     | Overlay on canvas                   |    |
|     | Complete flexibility                |    |
|     +-------------------------------------+    |
|                                                |
|  2. Native Sidebar Interface Ops               |
|     +-------------------------------------+    |
|     | Built-in UI elements                |    |
|     | Integrated with patch               |    |
|     | CSS-stylable                        |    |
|     | Quick to implement                  |    |
|     +-------------------------------------+    |
|                                                |
+------------------------------------------------+
```

## HTML/CSS Interfaces

### Overview

HTML/CSS interfaces give you complete control over the user interface. You can create custom overlays, forms, buttons, and any HTML element positioned over or alongside your canvas.

### The HTML Op

The HTML op allows you to create and manipulate DOM elements directly within your patch.

#### Basic HTML Op Setup

```
+-------------------------------------------------------------+
|                      HTML OP FLOW                            |
+-------------------------------------------------------------+
|                                                               |
|  MainLoop                                                     |
|    |                                                          |
|  HTML Op                                                      |
|    +-> HTML Content (string)                                  |
|    +-> CSS Styles (string)                                    |
|    +-> Position (x, y)                                        |
|    +-> Size (width, height)                                   |
|    +-> Visibility (bool)                                       |
|    |                                                          |
|  DOM Element (rendered on page)                              |
|                                                               |
+-------------------------------------------------------------+
```

#### Creating a Simple HTML Interface

**Step 1: Add HTML Op**

1. Add a `MainLoop` op
2. Add an `HTML` op
3. Connect `MainLoop` -> `HTML`

**Step 2: Define HTML Content**

In the HTML op's "HTML" parameter, enter your HTML:

```html
<div id="myInterface">
    <h1>My Interface</h1>
    <button id="myButton">Click Me</button>
    <input type="range" id="mySlider" min="0" max="100" value="50">
    <p id="myText">Value: <span id="valueDisplay">50</span></p>
</div>
```

**Step 3: Add CSS Styling**

In the HTML op's "CSS" parameter:

```css
#myInterface {
    position: absolute;
    top: 20px;
    left: 20px;
    background: rgba(30, 30, 30, 0.9);
    padding: 20px;
    border-radius: 8px;
    color: white;
    font-family: Arial, sans-serif;
    z-index: 1000;
}

#myButton {
    background: #4a9eff;
    color: white;
    border: none;
    padding: 10px 20px;
    border-radius: 4px;
    cursor: pointer;
    font-size: 16px;
}

#myButton:hover {
    background: #5aaeff;
}

#mySlider {
    width: 200px;
    margin: 10px 0;
}

#myText {
    margin-top: 10px;
    font-size: 14px;
}
```

**Step 4: Position the Interface**

Set the HTML op's position parameters:
- `X`: 0 (or desired x position)
- `Y`: 0 (or desired y position)
- `Width`: 300
- `Height`: 200

### Connecting HTML to Patch Logic

#### Using JavaScript Custom Op for Interaction

To make HTML elements interactive with your patch, use a JavaScript custom op:

```javascript
// Custom Op: HTML Controller
const inTrigger = op.inTrigger("Render");
const outSliderValue = op.outNumber("Slider Value");
const outButtonClicked = op.outTrigger("Button Clicked");

let sliderValue = 50;
let buttonClicked = false;

// Access DOM elements
op.onInit = function() {
    const slider = document.getElementById("mySlider");
    const button = document.getElementById("myButton");
    const display = document.getElementById("valueDisplay");
    
    if (slider) {
        slider.addEventListener("input", function(e) {
            sliderValue = parseFloat(e.target.value);
            if (display) {
                display.textContent = sliderValue;
            }
            outSliderValue.set(sliderValue);
        });
    }
    
    if (button) {
        button.addEventListener("click", function() {
            buttonClicked = true;
            outButtonClicked.trigger();
        });
    }
};

inTrigger.onTriggered = function() {
    outSliderValue.set(sliderValue);
    if (buttonClicked) {
        buttonClicked = false;
    }
};
```

#### Complete Example: Interactive Control Panel

```
+-------------------------------------------------------------+
|                    INTERACTIVE SETUP                          |
+-------------------------------------------------------------+
|                                                               |
|  MainLoop                                                     |
|    +-> HTML Op (UI elements)                                  |
|    +-> Custom Op (JavaScript controller)                      |
|         +-> Reads DOM events                                  |
|         +-> Outputs: Slider Value                            |
|         +-> Outputs: Button Trigger                          |
|         +-> Outputs: Text Input                              |
|              |                                                |
|         Patch Logic (uses values)                            |
|              |                                                |
|         Visual Output (canvas)                               |
|                                                               |
+-------------------------------------------------------------+
```

**HTML Content:**

```html
<div id="controlPanel">
    <h2>Animation Controls</h2>
    
    <div class="control-group">
        <label>Speed:</label>
        <input type="range" id="speedSlider" min="0.1" max="5" step="0.1" value="1">
        <span id="speedValue">1.0</span>
    </div>
    
    <div class="control-group">
        <label>Color:</label>
        <input type="color" id="colorPicker" value="#4a9eff">
    </div>
    
    <div class="control-group">
        <label>Mode:</label>
        <select id="modeSelect">
            <option value="normal">Normal</option>
            <option value="fast">Fast</option>
            <option value="slow">Slow</option>
        </select>
    </div>
    
    <button id="resetButton">Reset</button>
    <button id="playButton">Play/Pause</button>
</div>
```

**CSS Styling:**

```css
#controlPanel {
    position: fixed;
    top: 20px;
    right: 20px;
    width: 280px;
    background: linear-gradient(135deg, #1e1e1e 0%, #2d2d2d 100%);
    padding: 24px;
    border-radius: 12px;
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.4);
    border: 1px solid rgba(255, 255, 255, 0.1);
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    z-index: 1000;
}

#controlPanel h2 {
    margin: 0 0 20px 0;
    color: #ffffff;
    font-size: 20px;
    font-weight: 600;
    border-bottom: 2px solid #4a9eff;
    padding-bottom: 10px;
}

.control-group {
    margin-bottom: 20px;
}

.control-group label {
    display: block;
    color: #b0b0b0;
    font-size: 14px;
    margin-bottom: 8px;
    font-weight: 500;
}

#speedSlider {
    width: 100%;
    height: 6px;
    border-radius: 3px;
    background: #3a3a3a;
    outline: none;
    -webkit-appearance: none;
}

#speedSlider::-webkit-slider-thumb {
    -webkit-appearance: none;
    appearance: none;
    width: 18px;
    height: 18px;
    border-radius: 50%;
    background: #4a9eff;
    cursor: pointer;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.3);
}

#speedSlider::-moz-range-thumb {
    width: 18px;
    height: 18px;
    border-radius: 50%;
    background: #4a9eff;
    cursor: pointer;
    border: none;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.3);
}

#speedValue {
    color: #4a9eff;
    font-weight: 600;
    margin-left: 10px;
}

#colorPicker {
    width: 100%;
    height: 40px;
    border: 2px solid #3a3a3a;
    border-radius: 6px;
    cursor: pointer;
    background: transparent;
}

#modeSelect {
    width: 100%;
    padding: 10px;
    background: #3a3a3a;
    color: #ffffff;
    border: 2px solid #3a3a3a;
    border-radius: 6px;
    font-size: 14px;
    cursor: pointer;
}

#modeSelect:hover {
    border-color: #4a9eff;
}

#modeSelect:focus {
    outline: none;
    border-color: #4a9eff;
}

button {
    width: 100%;
    padding: 12px;
    margin-top: 10px;
    background: #4a9eff;
    color: white;
    border: none;
    border-radius: 6px;
    font-size: 14px;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.2s ease;
}

button:hover {
    background: #5aaeff;
    transform: translateY(-1px);
    box-shadow: 0 4px 12px rgba(74, 158, 255, 0.3);
}

button:active {
    transform: translateY(0);
}
```

### Advanced HTML Interface Patterns

#### Pattern 1: Responsive Overlay

```css
#myInterface {
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    background: rgba(0, 0, 0, 0.8);
    display: flex;
    align-items: center;
    justify-content: center;
    z-index: 10000;
}

#myInterface .content {
    background: #2d2d2d;
    padding: 40px;
    border-radius: 12px;
    max-width: 500px;
    width: 90%;
}
```

#### Pattern 2: Sidebar Panel

```css
#sidebar {
    position: fixed;
    top: 0;
    right: 0;
    width: 300px;
    height: 100vh;
    background: #1e1e1e;
    box-shadow: -4px 0 16px rgba(0, 0, 0, 0.3);
    padding: 20px;
    overflow-y: auto;
    z-index: 1000;
    transform: translateX(0);
    transition: transform 0.3s ease;
}

#sidebar.hidden {
    transform: translateX(100%);
}
```

#### Pattern 3: HUD (Heads-Up Display)

```css
#hud {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    pointer-events: none;
    z-index: 100;
}

#hud .info {
    position: absolute;
    top: 20px;
    left: 20px;
    color: white;
    font-family: monospace;
    font-size: 14px;
    text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.8);
}

#hud .crosshair {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    width: 20px;
    height: 20px;
    border: 2px solid rgba(255, 255, 255, 0.5);
    border-radius: 50%;
}
```

## Native Sidebar Interface Ops

### Overview

Cables.gl provides native interface operators that create UI elements directly in the sidebar. These are faster to set up and integrate seamlessly with the patch system.

### Available Interface Ops

```
+-------------------------------------------------------------+
|              NATIVE INTERFACE OPS                            |
+-------------------------------------------------------------+
|                                                               |
|  • Slider        - Numeric input with range                 |
|  • Button        - Clickable trigger                         |
|  • Toggle        - Boolean on/off switch                     |
|  • Text Input    - String input field                        |
|  • Color Picker  - Color selection                           |
|  • Dropdown      - Selection from options                    |
|  • Number Input  - Direct numeric input                      |
|  • Text Display  - Display text/values                       |
|                                                               |
+-------------------------------------------------------------+
```

### Basic Interface Op Setup

#### Example: Simple Control Panel

```
+-------------------------------------------------------------+
|                    SIDEBAR INTERFACE                          |
+-------------------------------------------------------------+
|                                                               |
|  Slider Op (Speed)                                           |
|    +-> Min: 0.1                                               |
|    +-> Max: 5.0                                               |
|    +-> Default: 1.0                                           |
|    +-> Output: Speed Value                                    |
|         |                                                     |
|    Patch Logic                                                |
|                                                               |
|  Button Op (Reset)                                            |
|    +-> Output: Trigger                                        |
|         |                                                     |
|    Reset Logic                                                |
|                                                               |
|  Toggle Op (Enabled)                                         |
|    +-> Output: Boolean                                         |
|         |                                                     |
|    Conditional Logic                                          |
|                                                               |
+-------------------------------------------------------------+
```

#### Step-by-Step: Creating a Sidebar Interface

**Step 1: Add Interface Ops**

1. Add a `Slider` op for speed control
2. Add a `Button` op for actions
3. Add a `Toggle` op for enable/disable
4. Add a `ColorPicker` op for color selection

**Step 2: Configure Each Op**

**Slider Op:**
- Name: "Speed"
- Min: 0.1
- Max: 5.0
- Default: 1.0
- Step: 0.1

**Button Op:**
- Name: "Reset"
- Label: "Reset Animation"

**Toggle Op:**
- Name: "Enabled"
- Default: true

**ColorPicker Op:**
- Name: "Base Color"
- Default: #4a9eff

**Step 3: Connect to Patch**

```
Speed Slider -> Multiply -> Animation Speed
Reset Button -> SetValue -> Reset Position
Enabled Toggle -> If -> Conditional Execution
ColorPicker -> SetColor -> Material Color
```

### Styling Native Sidebar with CSS

This is a powerful technique that allows you to customize the appearance of native sidebar interface ops using CSS.

#### Understanding the Sidebar Structure

The sidebar interface ops render in a specific DOM structure that you can target with CSS:

```
+-------------------------------------------------------------+
|              SIDEBAR DOM STRUCTURE                            |
+-------------------------------------------------------------+
|                                                               |
|  <div class="cables-sidebar">                                |
|    <div class="cables-sidebar-content">                      |
|      <div class="cables-op-slider" data-op-name="Speed">     |
|        <label>Speed</label>                                  |
|        <input type="range" ...>                               |
|        <span class="value">1.0</span>                        |
|      </div>                                                   |
|      <div class="cables-op-button" data-op-name="Reset">     |
|        <button>Reset</button>                                 |
|      </div>                                                   |
|      ...                                                      |
|    </div>                                                     |
|  </div>                                                       |
|                                                               |
+-------------------------------------------------------------+
```

#### Method 1: Global CSS Injection

Use an HTML op to inject CSS that styles the entire sidebar:

**HTML Op Setup:**

```html
<style id="sidebar-styles">
/* Sidebar styling will go here */
</style>
```

**CSS Content:**

```css
/* Target the entire sidebar */
.cables-sidebar {
    background: linear-gradient(180deg, #1a1a1a 0%, #2d2d2d 100%);
    border-left: 2px solid #4a9eff;
}

/* Style all interface ops */
.cables-sidebar-content > div {
    background: rgba(255, 255, 255, 0.05);
    border-radius: 8px;
    padding: 16px;
    margin-bottom: 12px;
    border: 1px solid rgba(255, 255, 255, 0.1);
    transition: all 0.2s ease;
}

.cables-sidebar-content > div:hover {
    background: rgba(255, 255, 255, 0.08);
    border-color: #4a9eff;
}

/* Style slider ops specifically */
.cables-op-slider {
    /* Custom slider container */
}

.cables-op-slider label {
    color: #b0b0b0;
    font-size: 14px;
    font-weight: 500;
    margin-bottom: 8px;
    display: block;
    text-transform: uppercase;
    letter-spacing: 0.5px;
}

.cables-op-slider input[type="range"] {
    width: 100%;
    height: 6px;
    border-radius: 3px;
    background: #3a3a3a;
    outline: none;
    -webkit-appearance: none;
    margin: 10px 0;
}

.cables-op-slider input[type="range"]::-webkit-slider-thumb {
    -webkit-appearance: none;
    appearance: none;
    width: 20px;
    height: 20px;
    border-radius: 50%;
    background: #4a9eff;
    cursor: pointer;
    box-shadow: 0 2px 8px rgba(74, 158, 255, 0.4);
    transition: all 0.2s ease;
}

.cables-op-slider input[type="range"]::-webkit-slider-thumb:hover {
    background: #5aaeff;
    transform: scale(1.1);
    box-shadow: 0 4px 12px rgba(74, 158, 255, 0.6);
}

.cables-op-slider input[type="range"]::-moz-range-thumb {
    width: 20px;
    height: 20px;
    border-radius: 50%;
    background: #4a9eff;
    cursor: pointer;
    border: none;
    box-shadow: 0 2px 8px rgba(74, 158, 255, 0.4);
}

.cables-op-slider .value {
    color: #4a9eff;
    font-weight: 600;
    font-size: 16px;
    float: right;
    margin-top: -24px;
}

/* Style button ops */
.cables-op-button button {
    width: 100%;
    padding: 12px 24px;
    background: linear-gradient(135deg, #4a9eff 0%, #3a8eef 100%);
    color: white;
    border: none;
    border-radius: 6px;
    font-size: 14px;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.2s ease;
    text-transform: uppercase;
    letter-spacing: 1px;
    box-shadow: 0 4px 12px rgba(74, 158, 255, 0.3);
}

.cables-op-button button:hover {
    background: linear-gradient(135deg, #5aaeff 0%, #4a9eff 100%);
    transform: translateY(-2px);
    box-shadow: 0 6px 16px rgba(74, 158, 255, 0.4);
}

.cables-op-button button:active {
    transform: translateY(0);
    box-shadow: 0 2px 8px rgba(74, 158, 255, 0.3);
}

/* Style toggle ops */
.cables-op-toggle {
    display: flex;
    align-items: center;
    justify-content: space-between;
}

.cables-op-toggle label {
    color: #b0b0b0;
    font-size: 14px;
    font-weight: 500;
}

.cables-op-toggle input[type="checkbox"] {
    width: 50px;
    height: 26px;
    -webkit-appearance: none;
    appearance: none;
    background: #3a3a3a;
    border-radius: 13px;
    position: relative;
    cursor: pointer;
    transition: background 0.3s ease;
    border: 2px solid #2a2a2a;
}

.cables-op-toggle input[type="checkbox"]:checked {
    background: #4a9eff;
    border-color: #4a9eff;
}

.cables-op-toggle input[type="checkbox"]::before {
    content: '';
    position: absolute;
    width: 20px;
    height: 20px;
    border-radius: 50%;
    background: white;
    top: 1px;
    left: 1px;
    transition: transform 0.3s ease;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.3);
}

.cables-op-toggle input[type="checkbox"]:checked::before {
    transform: translateX(24px);
}

/* Style color picker ops */
.cables-op-colorpicker {
    display: flex;
    align-items: center;
    gap: 12px;
}

.cables-op-colorpicker label {
    color: #b0b0b0;
    font-size: 14px;
    font-weight: 500;
    flex: 1;
}

.cables-op-colorpicker input[type="color"] {
    width: 60px;
    height: 40px;
    border: 2px solid #3a3a3a;
    border-radius: 6px;
    cursor: pointer;
    background: transparent;
    transition: border-color 0.2s ease;
}

.cables-op-colorpicker input[type="color"]:hover {
    border-color: #4a9eff;
}

/* Style text input ops */
.cables-op-textinput input[type="text"] {
    width: 100%;
    padding: 10px 12px;
    background: #3a3a3a;
    color: #ffffff;
    border: 2px solid #3a3a3a;
    border-radius: 6px;
    font-size: 14px;
    transition: all 0.2s ease;
}

.cables-op-textinput input[type="text"]:focus {
    outline: none;
    border-color: #4a9eff;
    background: #404040;
    box-shadow: 0 0 0 3px rgba(74, 158, 255, 0.1);
}

/* Style dropdown ops */
.cables-op-dropdown select {
    width: 100%;
    padding: 10px 12px;
    background: #3a3a3a;
    color: #ffffff;
    border: 2px solid #3a3a3a;
    border-radius: 6px;
    font-size: 14px;
    cursor: pointer;
    transition: all 0.2s ease;
}

.cables-op-dropdown select:hover {
    border-color: #4a9eff;
}

.cables-op-dropdown select:focus {
    outline: none;
    border-color: #4a9eff;
    box-shadow: 0 0 0 3px rgba(74, 158, 255, 0.1);
}
```

#### Method 2: Targeted Op Styling

Style specific ops by their data attributes:

```css
/* Style a specific slider by op name */
.cables-op-slider[data-op-name="Speed"] {
    background: rgba(74, 158, 255, 0.1);
    border: 2px solid #4a9eff;
}

.cables-op-slider[data-op-name="Speed"] label {
    color: #4a9eff;
    font-weight: 600;
}

/* Style a specific button */
.cables-op-button[data-op-name="Reset"] button {
    background: linear-gradient(135deg, #ff4a4a 0%, #ef3a3a 100%);
}

.cables-op-button[data-op-name="Reset"] button:hover {
    background: linear-gradient(135deg, #ff5a5a 0%, #ff4a4a 100%);
}
```

#### Method 3: Dynamic CSS with JavaScript Custom Op

Create a custom op that injects CSS based on patch state:

```javascript
// Custom Op: Dynamic Sidebar Styling
const inTheme = op.inSwitch("Theme", ["dark", "light", "neon"], "dark");
const inAccentColor = op.inString("Accent Color", "#4a9eff");

let currentTheme = "dark";
let currentAccent = "#4a9eff";

function updateStyles() {
    const theme = inTheme.get();
    const accent = inAccentColor.get();
    
    if (theme === currentTheme && accent === currentAccent) return;
    
    currentTheme = theme;
    currentAccent = accent;
    
    let styleElement = document.getElementById("dynamic-sidebar-styles");
    if (!styleElement) {
        styleElement = document.createElement("style");
        styleElement.id = "dynamic-sidebar-styles";
        document.head.appendChild(styleElement);
    }
    
    let css = "";
    
    if (theme === "dark") {
        css = `
            .cables-sidebar {
                background: linear-gradient(180deg, #1a1a1a 0%, #2d2d2d 100%);
            }
            .cables-sidebar-content > div {
                background: rgba(255, 255, 255, 0.05);
                border-color: rgba(255, 255, 255, 0.1);
            }
        `;
    } else if (theme === "light") {
        css = `
            .cables-sidebar {
                background: linear-gradient(180deg, #f5f5f5 0%, #e0e0e0 100%);
            }
            .cables-sidebar-content > div {
                background: rgba(0, 0, 0, 0.05);
                border-color: rgba(0, 0, 0, 0.1);
            }
            .cables-op-slider label,
            .cables-op-button label {
                color: #333;
            }
        `;
    } else if (theme === "neon") {
        css = `
            .cables-sidebar {
                background: #0a0a0a;
                border-left: 2px solid ${accent};
                box-shadow: -4px 0 20px ${accent}40;
            }
            .cables-sidebar-content > div {
                background: rgba(0, 0, 0, 0.5);
                border: 1px solid ${accent}40;
                box-shadow: 0 0 10px ${accent}20;
            }
        `;
    }
    
    // Apply accent color
    css += `
        .cables-op-slider input[type="range"]::-webkit-slider-thumb {
            background: ${accent};
            box-shadow: 0 2px 8px ${accent}60;
        }
        .cables-op-button button {
            background: linear-gradient(135deg, ${accent} 0%, ${adjustBrightness(accent, -20)} 100%);
        }
        .cables-op-toggle input[type="checkbox"]:checked {
            background: ${accent};
        }
    `;
    
    styleElement.textContent = css;
}

function adjustBrightness(color, percent) {
    // Simple brightness adjustment (simplified)
    const num = parseInt(color.replace("#", ""), 16);
    const r = Math.max(0, Math.min(255, (num >> 16) + percent));
    const g = Math.max(0, Math.min(255, ((num >> 8) & 0x00FF) + percent));
    const b = Math.max(0, Math.min(255, (num & 0x0000FF) + percent));
    return "#" + ((r << 16) | (g << 8) | b).toString(16).padStart(6, "0");
}

inTheme.onChange = updateStyles;
inAccentColor.onChange = updateStyles;

op.onInit = function() {
    updateStyles();
};
```

### Complete Styling Example: Professional Control Panel

Here's a complete example that styles all interface ops with a cohesive, professional design:

**HTML Op (CSS Injection):**

```html
<style id="professional-sidebar-styles">
/* Professional Sidebar Styling */

/* Sidebar Container */
.cables-sidebar {
    background: linear-gradient(180deg, 
        #1a1a1a 0%, 
        #1e1e1e 50%, 
        #2d2d2d 100%);
    border-left: 3px solid #4a9eff;
    box-shadow: -4px 0 24px rgba(0, 0, 0, 0.5);
    font-family: 'Inter', 'Segoe UI', system-ui, sans-serif;
}

/* Sidebar Header (if exists) */
.cables-sidebar-header {
    padding: 20px;
    border-bottom: 2px solid rgba(74, 158, 255, 0.2);
    background: rgba(74, 158, 255, 0.05);
}

.cables-sidebar-header h2 {
    margin: 0;
    color: #ffffff;
    font-size: 18px;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 1px;
}

/* Content Container */
.cables-sidebar-content {
    padding: 16px;
}

/* All Interface Op Containers */
.cables-sidebar-content > div {
    background: rgba(255, 255, 255, 0.03);
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 10px;
    padding: 18px;
    margin-bottom: 16px;
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    position: relative;
    overflow: hidden;
}

.cables-sidebar-content > div::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 2px;
    background: linear-gradient(90deg, 
        transparent 0%, 
        #4a9eff 50%, 
        transparent 100%);
    opacity: 0;
    transition: opacity 0.3s ease;
}

.cables-sidebar-content > div:hover {
    background: rgba(255, 255, 255, 0.06);
    border-color: rgba(74, 158, 255, 0.3);
    transform: translateX(4px);
    box-shadow: 0 4px 16px rgba(0, 0, 0, 0.3);
}

.cables-sidebar-content > div:hover::before {
    opacity: 1;
}

/* Slider Styling */
.cables-op-slider label {
    display: block;
    color: #b0b0b0;
    font-size: 12px;
    font-weight: 600;
    margin-bottom: 10px;
    text-transform: uppercase;
    letter-spacing: 0.5px;
}

.cables-op-slider input[type="range"] {
    width: 100%;
    height: 8px;
    border-radius: 4px;
    background: linear-gradient(90deg, 
        #2a2a2a 0%, 
        #3a3a3a 100%);
    outline: none;
    -webkit-appearance: none;
    margin: 12px 0;
    position: relative;
}

.cables-op-slider input[type="range"]::-webkit-slider-thumb {
    -webkit-appearance: none;
    appearance: none;
    width: 24px;
    height: 24px;
    border-radius: 50%;
    background: linear-gradient(135deg, #4a9eff 0%, #3a8eef 100%);
    cursor: pointer;
    box-shadow: 
        0 2px 8px rgba(74, 158, 255, 0.4),
        0 0 0 4px rgba(74, 158, 255, 0.1),
        inset 0 1px 0 rgba(255, 255, 255, 0.2);
    transition: all 0.2s ease;
    border: 2px solid rgba(255, 255, 255, 0.1);
}

.cables-op-slider input[type="range"]::-webkit-slider-thumb:hover {
    background: linear-gradient(135deg, #5aaeff 0%, #4a9eff 100%);
    transform: scale(1.15);
    box-shadow: 
        0 4px 12px rgba(74, 158, 255, 0.6),
        0 0 0 6px rgba(74, 158, 255, 0.15),
        inset 0 1px 0 rgba(255, 255, 255, 0.3);
}

.cables-op-slider input[type="range"]::-webkit-slider-thumb:active {
    transform: scale(1.05);
}

.cables-op-slider input[type="range"]::-moz-range-thumb {
    width: 24px;
    height: 24px;
    border-radius: 50%;
    background: linear-gradient(135deg, #4a9eff 0%, #3a8eef 100%);
    cursor: pointer;
    border: 2px solid rgba(255, 255, 255, 0.1);
    box-shadow: 
        0 2px 8px rgba(74, 158, 255, 0.4),
        0 0 0 4px rgba(74, 158, 255, 0.1);
}

.cables-op-slider .value {
    color: #4a9eff;
    font-weight: 700;
    font-size: 18px;
    float: right;
    margin-top: -32px;
    font-variant-numeric: tabular-nums;
    text-shadow: 0 0 8px rgba(74, 158, 255, 0.5);
}

/* Button Styling */
.cables-op-button button {
    width: 100%;
    padding: 14px 24px;
    background: linear-gradient(135deg, #4a9eff 0%, #3a8eef 100%);
    color: white;
    border: none;
    border-radius: 8px;
    font-size: 14px;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    text-transform: uppercase;
    letter-spacing: 1.2px;
    box-shadow: 
        0 4px 12px rgba(74, 158, 255, 0.3),
        inset 0 1px 0 rgba(255, 255, 255, 0.2);
    position: relative;
    overflow: hidden;
}

.cables-op-button button::before {
    content: '';
    position: absolute;
    top: 50%;
    left: 50%;
    width: 0;
    height: 0;
    border-radius: 50%;
    background: rgba(255, 255, 255, 0.3);
    transform: translate(-50%, -50%);
    transition: width 0.6s, height 0.6s;
}

.cables-op-button button:hover {
    background: linear-gradient(135deg, #5aaeff 0%, #4a9eff 100%);
    transform: translateY(-2px);
    box-shadow: 
        0 6px 20px rgba(74, 158, 255, 0.4),
        inset 0 1px 0 rgba(255, 255, 255, 0.3);
}

.cables-op-button button:hover::before {
    width: 300px;
    height: 300px;
}

.cables-op-button button:active {
    transform: translateY(0);
    box-shadow: 
        0 2px 8px rgba(74, 158, 255, 0.3),
        inset 0 1px 0 rgba(255, 255, 255, 0.1);
}

/* Toggle Styling */
.cables-op-toggle {
    display: flex;
    align-items: center;
    justify-content: space-between;
}

.cables-op-toggle label {
    color: #b0b0b0;
    font-size: 14px;
    font-weight: 500;
    flex: 1;
}

.cables-op-toggle input[type="checkbox"] {
    width: 56px;
    height: 30px;
    -webkit-appearance: none;
    appearance: none;
    background: #2a2a2a;
    border-radius: 15px;
    position: relative;
    cursor: pointer;
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    border: 2px solid #1a1a1a;
    box-shadow: inset 0 2px 4px rgba(0, 0, 0, 0.3);
}

.cables-op-toggle input[type="checkbox"]:checked {
    background: linear-gradient(135deg, #4a9eff 0%, #3a8eef 100%);
    border-color: #4a9eff;
    box-shadow: 
        inset 0 2px 4px rgba(0, 0, 0, 0.2),
        0 0 12px rgba(74, 158, 255, 0.4);
}

.cables-op-toggle input[type="checkbox"]::before {
    content: '';
    position: absolute;
    width: 24px;
    height: 24px;
    border-radius: 50%;
    background: linear-gradient(135deg, #ffffff 0%, #f0f0f0 100%);
    top: 1px;
    left: 1px;
    transition: transform 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    box-shadow: 
        0 2px 6px rgba(0, 0, 0, 0.3),
        inset 0 1px 0 rgba(255, 255, 255, 0.5);
}

.cables-op-toggle input[type="checkbox"]:checked::before {
    transform: translateX(26px);
}

/* Color Picker Styling */
.cables-op-colorpicker {
    display: flex;
    align-items: center;
    gap: 16px;
}

.cables-op-colorpicker label {
    color: #b0b0b0;
    font-size: 14px;
    font-weight: 500;
    flex: 1;
}

.cables-op-colorpicker input[type="color"] {
    width: 70px;
    height: 50px;
    border: 3px solid #3a3a3a;
    border-radius: 8px;
    cursor: pointer;
    background: transparent;
    transition: all 0.3s ease;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.3);
}

.cables-op-colorpicker input[type="color"]:hover {
    border-color: #4a9eff;
    transform: scale(1.05);
    box-shadow: 
        0 4px 12px rgba(0, 0, 0, 0.4),
        0 0 0 4px rgba(74, 158, 255, 0.1);
}

/* Text Input Styling */
.cables-op-textinput label {
    display: block;
    color: #b0b0b0;
    font-size: 12px;
    font-weight: 600;
    margin-bottom: 8px;
    text-transform: uppercase;
    letter-spacing: 0.5px;
}

.cables-op-textinput input[type="text"] {
    width: 100%;
    padding: 12px 16px;
    background: #2a2a2a;
    color: #ffffff;
    border: 2px solid #3a3a3a;
    border-radius: 8px;
    font-size: 14px;
    transition: all 0.3s ease;
    box-sizing: border-box;
}

.cables-op-textinput input[type="text"]:focus {
    outline: none;
    border-color: #4a9eff;
    background: #333333;
    box-shadow: 
        0 0 0 4px rgba(74, 158, 255, 0.1),
        inset 0 2px 4px rgba(0, 0, 0, 0.2);
}

/* Dropdown Styling */
.cables-op-dropdown label {
    display: block;
    color: #b0b0b0;
    font-size: 12px;
    font-weight: 600;
    margin-bottom: 8px;
    text-transform: uppercase;
    letter-spacing: 0.5px;
}

.cables-op-dropdown select {
    width: 100%;
    padding: 12px 16px;
    background: #2a2a2a;
    color: #ffffff;
    border: 2px solid #3a3a3a;
    border-radius: 8px;
    font-size: 14px;
    cursor: pointer;
    transition: all 0.3s ease;
    appearance: none;
    background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='12' height='12' viewBox='0 0 12 12'%3E%3Cpath fill='%234a9eff' d='M6 9L1 4h10z'/%3E%3C/svg%3E");
    background-repeat: no-repeat;
    background-position: right 12px center;
    padding-right: 40px;
}

.cables-op-dropdown select:hover {
    border-color: #4a9eff;
    background-color: #333333;
}

.cables-op-dropdown select:focus {
    outline: none;
    border-color: #4a9eff;
    box-shadow: 
        0 0 0 4px rgba(74, 158, 255, 0.1),
        inset 0 2px 4px rgba(0, 0, 0, 0.2);
}

/* Number Input Styling */
.cables-op-numberinput {
    display: flex;
    align-items: center;
    gap: 12px;
}

.cables-op-numberinput label {
    color: #b0b0b0;
    font-size: 14px;
    font-weight: 500;
    flex: 1;
}

.cables-op-numberinput input[type="number"] {
    width: 100px;
    padding: 10px 12px;
    background: #2a2a2a;
    color: #ffffff;
    border: 2px solid #3a3a3a;
    border-radius: 6px;
    font-size: 14px;
    text-align: center;
    transition: all 0.3s ease;
}

.cables-op-numberinput input[type="number"]:focus {
    outline: none;
    border-color: #4a9eff;
    background: #333333;
    box-shadow: 0 0 0 3px rgba(74, 158, 255, 0.1);
}

/* Text Display Styling */
.cables-op-textdisplay {
    padding: 12px;
    background: rgba(74, 158, 255, 0.1);
    border: 1px solid rgba(74, 158, 255, 0.3);
    border-radius: 6px;
    color: #4a9eff;
    font-family: 'Courier New', monospace;
    font-size: 14px;
    text-align: center;
    font-weight: 600;
}

/* Responsive adjustments */
@media (max-width: 768px) {
    .cables-sidebar {
        width: 100% !important;
        height: auto !important;
        position: relative !important;
    }
}
</style>
```

### Advanced CSS Techniques

#### Technique 1: Animated Transitions

```css
.cables-sidebar-content > div {
    animation: slideIn 0.3s ease-out;
}

@keyframes slideIn {
    from {
        opacity: 0;
        transform: translateX(-20px);
    }
    to {
        opacity: 1;
        transform: translateX(0);
    }
}

/* Stagger animation delays */
.cables-sidebar-content > div:nth-child(1) { animation-delay: 0.05s; }
.cables-sidebar-content > div:nth-child(2) { animation-delay: 0.10s; }
.cables-sidebar-content > div:nth-child(3) { animation-delay: 0.15s; }
.cables-sidebar-content > div:nth-child(4) { animation-delay: 0.20s; }
```

#### Technique 2: Custom Scrollbar

```css
.cables-sidebar-content::-webkit-scrollbar {
    width: 8px;
}

.cables-sidebar-content::-webkit-scrollbar-track {
    background: #1a1a1a;
    border-radius: 4px;
}

.cables-sidebar-content::-webkit-scrollbar-thumb {
    background: #4a9eff;
    border-radius: 4px;
    border: 2px solid #1a1a1a;
}

.cables-sidebar-content::-webkit-scrollbar-thumb:hover {
    background: #5aaeff;
}
```

#### Technique 3: Glassmorphism Effect

```css
.cables-sidebar {
    background: rgba(30, 30, 30, 0.7);
    backdrop-filter: blur(20px);
    -webkit-backdrop-filter: blur(20px);
    border-left: 1px solid rgba(255, 255, 255, 0.1);
}

.cables-sidebar-content > div {
    background: rgba(255, 255, 255, 0.05);
    backdrop-filter: blur(10px);
    -webkit-backdrop-filter: blur(10px);
    border: 1px solid rgba(255, 255, 255, 0.1);
}
```

## Combining HTML and Native Interfaces

You can combine both approaches for maximum flexibility:

```
+-------------------------------------------------------------+
|              HYBRID INTERFACE APPROACH                       |
+-------------------------------------------------------------+
|                                                               |
|  Native Sidebar Ops                                          |
|    +-> Quick controls (sliders, buttons)                     |
|    +-> Styled with CSS                                         |
|                                                               |
|  HTML Overlay                                                |
|    +-> Complex UI elements                                    |
|    +-> Custom layouts                                         |
|    +-> Interactive components                                  |
|                                                               |
|  JavaScript Custom Op                                         |
|    +-> Bridges both systems                                   |
|    +-> Syncs values                                           |
|    +-> Handles interactions                                   |
|                                                               |
+-------------------------------------------------------------+
```

## Best Practices

### 1. Performance

- **Minimize DOM Manipulation**: Cache element references
- **Use CSS Transforms**: For animations instead of position changes
- **Debounce Inputs**: For sliders and text inputs that trigger heavy computations

### 2. Accessibility

- **Labels**: Always provide clear labels for controls
- **Keyboard Navigation**: Ensure keyboard accessibility
- **Color Contrast**: Maintain sufficient contrast ratios
- **Focus States**: Provide visible focus indicators

### 3. Responsive Design

```css
/* Mobile-first approach */
.cables-sidebar {
    width: 100%;
    height: auto;
    position: relative;
}

@media (min-width: 768px) {
    .cables-sidebar {
        width: 320px;
        height: 100vh;
        position: fixed;
    }
}
```

### 4. Organization

- **Group Related Controls**: Use visual grouping
- **Clear Hierarchy**: Use size, color, and spacing
- **Consistent Spacing**: Maintain uniform margins and padding

## Practical Examples

### Example 1: Animation Control Panel

Create a comprehensive control panel for animation parameters:

```
Speed Slider -> Animation Speed
Color Picker -> Material Color
Toggle (Loop) -> Loop Animation
Button (Reset) -> Reset Animation
Text Display -> Current Frame
```

### Example 2: Game UI Overlay

HTML overlay for game-like interface:

```html
<div id="gameUI">
    <div class="hud-top">
        <div class="score">Score: <span id="score">0</span></div>
        <div class="health">Health: <span id="health">100</span></div>
    </div>
    <div class="hud-bottom">
        <button id="pauseBtn">Pause</button>
        <button id="menuBtn">Menu</button>
    </div>
</div>
```

### Example 3: Data Visualization Dashboard

Combine native ops with HTML for a data dashboard:

- Native sliders for filtering
- HTML charts and graphs
- Real-time data display

## Debugging Interface Issues

### Common Issues

1. **CSS Not Applying**
   - Check selector specificity
   - Verify CSS is injected after sidebar renders
   - Use `!important` sparingly

2. **Elements Not Visible**
   - Check z-index values
   - Verify position properties
   - Check for overflow: hidden

3. **Events Not Firing**
   - Ensure JavaScript runs after DOM is ready
   - Check event listener attachment
   - Verify element selectors

### Debugging Tools

```javascript
// Log sidebar structure
console.log(document.querySelector('.cables-sidebar'));

// Check computed styles
const element = document.querySelector('.cables-op-slider');
console.log(window.getComputedStyle(element));

// Monitor style changes
const observer = new MutationObserver((mutations) => {
    console.log('DOM changed:', mutations);
});
observer.observe(document.querySelector('.cables-sidebar'), {
    childList: true,
    subtree: true,
    attributes: true
});
```

## Exercises

1. **Basic HTML Interface**: Create a simple HTML overlay with a button and slider that control patch parameters

2. **Styled Sidebar**: Style native sidebar ops with a cohesive color scheme and modern design

3. **Responsive Panel**: Create a sidebar that adapts to different screen sizes

4. **Interactive Dashboard**: Build a complete control panel combining HTML and native ops

5. **Theme Switcher**: Create a custom op that dynamically changes sidebar styling based on user selection

6. **Advanced Styling**: Implement glassmorphism or other modern design trends in your sidebar

---


