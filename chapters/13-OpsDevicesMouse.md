# Ops.Devices.Mouse

---

```{=latex}
\stepcounter{subsection}\setcounter{subsubsection}{0}
```
### Mouse_v4
![Mouse_v4 op](images/ops/Ops_Devices_Mouse_Mouse_v4.svg)

**Full Name:** `Ops.Devices.Mouse.Mouse_v4`

**Description:** Get mouse/touchscreen/pointer coordinates and events

**`\inputsymbol`{=latex} Inputs**

- **Area Index** (Number: Integer)
- **Flip Y** (Number: Boolean)
- **Right Click Prevent Default** (Number: Boolean)
- **Passive Events** (Number: Boolean)
- **Element** (Object)
- **Active** (Number: Boolean)

**`\outputsymbol`{=latex} Output**

- **X** (Number)
- **Y** (Number)
- **Click** (Trigger)
- **Click Right** (Trigger)
- **Button Is Down** (booleanNumber)
- **Mouse Is Hovering** (booleanNumber)
- **Movement X** (Number)
- **Movement Y** (Number)
- **Event** (Object)

**Example Patch:** [Open in Editor](https://cables.gl/edit/mDiCq6)

**Docs:** [https://cables.gl/op/Ops.Devices.Mouse.Mouse_v4](https://cables.gl/op/Ops.Devices.Mouse.Mouse_v4)

### MouseButtons
![MouseButtons op](images/ops/Ops_Devices_Mouse_MouseButtons.svg)

**Full Name:** `Ops.Devices.Mouse.MouseButtons`

**Description:** Get the state of mouse buttons

**`\inputsymbol`{=latex} Inputs**

- **Area Index** (Number: Integer)
- **Active** (Number: Boolean)

**`\outputsymbol`{=latex} Output**

- **Click Left** (Trigger)
- **Click Right** (Trigger)
- **Double Click** (Trigger)
- **Button Pressed Left** (Number)
- **Button Pressed Middle** (Number)
- **Button Pressed Right** (Number)
- **Mouse Down Left** (Trigger)
- **Mouse Down Middle** (Trigger)
- **Mouse Down Right** (Trigger)
- **Mouse Up Left** (Trigger)
- **Mouse Up Middle** (Trigger)
- **Mouse Up Right** (Trigger)

**Example Patch:** [Open in Editor](https://cables.gl/edit/cLtJLO)

**Docs:** [https://cables.gl/op/Ops.Devices.Mouse.MouseButtons](https://cables.gl/op/Ops.Devices.Mouse.MouseButtons)

### MouseDrag
![MouseDrag op](images/ops/Ops_Devices_Mouse_MouseDrag.svg)

**Full Name:** `Ops.Devices.Mouse.MouseDrag`

**Description:** get delta of mouse position while dragging

**`\inputsymbol`{=latex} Inputs**

- **Active** (Number: Boolean)
- **Speed** (Number)
- **Input Type Index** (Number: Integer)
- **Area Index** (Number: Integer)

**`\outputsymbol`{=latex} Output**

- **Delta X** (Number)
- **Delta Y** (Number)
- **Is Dragging** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/edit/hH8f_6)

**Docs:** [https://cables.gl/op/Ops.Devices.Mouse.MouseDrag](https://cables.gl/op/Ops.Devices.Mouse.MouseDrag)

### MouseWheel_v2
![MouseWheel_v2 op](images/ops/Ops_Devices_Mouse_MouseWheel_v2.svg)

**Full Name:** `Ops.Devices.Mouse.MouseWheel_v2`

**Description:** outputs delta values controlled by the mousewheel (scroll, zoom)

**`\inputsymbol`{=latex} Inputs**

- **Speed** (Number)
- **Prevent Scroll** (Number: Boolean)
- **Flip Direction** (Number: Boolean)
- **Simple Delta** (Number: Boolean)
- **Active** (Number: Boolean)

**`\outputsymbol`{=latex} Output**

- **Delta** (Number)
- **Delta X** (Number)
- **Browser Event Delta** (Number)
- **Wheel Action** (Trigger)

**Example Patch:** [Open in Editor](https://cables.gl/edit/hH8f_6)

**Docs:** [https://cables.gl/op/Ops.Devices.Mouse.MouseWheel_v2](https://cables.gl/op/Ops.Devices.Mouse.MouseWheel_v2)

### PointerLock
![PointerLock op](images/ops/Ops_Devices_Mouse_PointerLock.svg)

**Full Name:** `Ops.Devices.Mouse.PointerLock`

**Description:** locks the pointer to the canvas and hides the cursor

**`\inputsymbol`{=latex} Inputs**

- **Render** (Trigger)
- **Start** (Trigger)

**`\outputsymbol`{=latex} Output**

- **Next** (Trigger)
- **Supported** (booleanNumber)
- **Is Locked** (booleanNumber)

**Example Patch:** [Open in Editor](https://cables.gl/edit/ds6IV2)

**Docs:** [https://cables.gl/op/Ops.Devices.Mouse.PointerLock](https://cables.gl/op/Ops.Devices.Mouse.PointerLock)


