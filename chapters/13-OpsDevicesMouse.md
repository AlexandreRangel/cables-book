# Ops.Devices.Mouse

*Part of the [All Operators Reference](13-_AllOps.md)*

---

## Ops.Devices.Mouse

### Mouse_v4
![Mouse_v4 op](images/ops/Ops_Devices_Mouse_Mouse_v4.svg)

**Full Name:** `Ops.Devices.Mouse.Mouse_v4`
**Description:** Get mouse/touchscreen/pointer coordinates and events

**> Input Ports:**
- **Area Index** (Number: Integer): *See documentation*
- **Flip Y** (Number: Boolean): *See documentation*
- **Right Click Prevent Default** (Number: Boolean): *See documentation*
- **Passive Events** (Number: Boolean): *See documentation*
- **Element** (Object): *See documentation*
- **Active** (Number: Boolean): *See documentation*

**< Output Ports:**
- **X** (Number): *See documentation*
- **Y** (Number): *See documentation*
- **Click** (Trigger): *See documentation*
- **Click Right** (Trigger): *See documentation*
- **Button Is Down** (booleanNumber): *See documentation*
- **Mouse Is Hovering** (booleanNumber): *See documentation*
- **Movement X** (Number): *See documentation*
- **Movement Y** (Number): *See documentation*
- **Event** (Object): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/mDiCq6)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "Mouse_v4"*
**Docs:** [https://cables.gl/op/Ops.Devices.Mouse.Mouse_v4](https://cables.gl/op/Ops.Devices.Mouse.Mouse_v4)

---

### MouseButtons
![MouseButtons op](images/ops/Ops_Devices_Mouse_MouseButtons.svg)

**Full Name:** `Ops.Devices.Mouse.MouseButtons`
**Description:** Get the state of mouse buttons

**> Input Ports:**
- **Area Index** (Number: Integer): *See documentation*
- **Active** (Number: Boolean): *See documentation*

**< Output Ports:**
- **Click Left** (Trigger): *See documentation*
- **Click Right** (Trigger): *See documentation*
- **Double Click** (Trigger): *See documentation*
- **Button Pressed Left** (Number): *See documentation*
- **Button Pressed Middle** (Number): *See documentation*
- **Button Pressed Right** (Number): *See documentation*
- **Mouse Down Left** (Trigger): *See documentation*
- **Mouse Down Middle** (Trigger): *See documentation*
- **Mouse Down Right** (Trigger): *See documentation*
- **Mouse Up Left** (Trigger): *See documentation*
- **Mouse Up Middle** (Trigger): *See documentation*
- **Mouse Up Right** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/cLtJLO)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "MouseButtons"*
**Docs:** [https://cables.gl/op/Ops.Devices.Mouse.MouseButtons](https://cables.gl/op/Ops.Devices.Mouse.MouseButtons)

---

### MouseDrag
![MouseDrag op](images/ops/Ops_Devices_Mouse_MouseDrag.svg)

**Full Name:** `Ops.Devices.Mouse.MouseDrag`
**Description:** get delta of mouse position while dragging

**> Input Ports:**
- **Active** (Number: Boolean): *See documentation*
- **Speed** (Number): *See documentation*
- **Input Type Index** (Number: Integer): *See documentation*
- **Area Index** (Number: Integer): *See documentation*

**< Output Ports:**
- **Delta X** (Number): *See documentation*
- **Delta Y** (Number): *See documentation*
- **Is Dragging** (Number): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/hH8f_6)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "MouseDrag"*
**Docs:** [https://cables.gl/op/Ops.Devices.Mouse.MouseDrag](https://cables.gl/op/Ops.Devices.Mouse.MouseDrag)

---

### MouseWheel_v2
![MouseWheel_v2 op](images/ops/Ops_Devices_Mouse_MouseWheel_v2.svg)

**Full Name:** `Ops.Devices.Mouse.MouseWheel_v2`
**Description:** outputs delta values controlled by the mousewheel (scroll, zoom)

**> Input Ports:**
- **Speed** (Number): *See documentation*
- **Prevent Scroll** (Number: Boolean): *See documentation*
- **Flip Direction** (Number: Boolean): *See documentation*
- **Simple Delta** (Number: Boolean): *See documentation*
- **Active** (Number: Boolean): *See documentation*

**< Output Ports:**
- **Delta** (Number): *See documentation*
- **Delta X** (Number): *See documentation*
- **Browser Event Delta** (Number): *See documentation*
- **Wheel Action** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/hH8f_6)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "MouseWheel_v2"*
**Docs:** [https://cables.gl/op/Ops.Devices.Mouse.MouseWheel_v2](https://cables.gl/op/Ops.Devices.Mouse.MouseWheel_v2)

---

### PointerLock
![PointerLock op](images/ops/Ops_Devices_Mouse_PointerLock.svg)

**Full Name:** `Ops.Devices.Mouse.PointerLock`
**Description:** locks the pointer to the canvas and hides the cursor

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Start** (Trigger): *See documentation*

**< Output Ports:**
- **Next** (Trigger): *See documentation*
- **Supported** (booleanNumber): *See documentation*
- **Is Locked** (booleanNumber): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/ds6IV2)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "PointerLock"*
**Docs:** [https://cables.gl/op/Ops.Devices.Mouse.PointerLock](https://cables.gl/op/Ops.Devices.Mouse.PointerLock)

---

