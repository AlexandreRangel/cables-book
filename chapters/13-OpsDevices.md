# Ops.Devices

*Part of the [All Operators Reference](13-_AllOps.md)*

---

## Ops.Devices

### TouchGesture
![TouchGesture op](images/ops/Ops_Devices_TouchGesture.svg)

**Full Name:** `Ops.Devices.TouchGesture`
**Description:** detect touch gestures like swipe and pan

**> Input Ports:**
- **Active** (Number: Boolean): *See documentation*
- **Vertical Swipe** (Number: Boolean): *See documentation*
- **Vertical Pan** (Number: Boolean): *See documentation*

**< Output Ports:**
- **Press** (Trigger): *See documentation*
- **Press Up** (Trigger): *See documentation*
- **Pan Left** (Trigger): *See documentation*
- **Pan Right** (Trigger): *See documentation*
- **Swipe Left** (Trigger): *See documentation*
- **Swipe Right** (Trigger): *See documentation*
- **Swipe Up** (Trigger): *See documentation*
- **Swipe Down** (Trigger): *See documentation*
- **Event** (Object): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Devices.TouchGesture#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "TouchGesture"*
**Docs:** [https://cables.gl/op/Ops.Devices.TouchGesture](https://cables.gl/op/Ops.Devices.TouchGesture)

---

### TouchScreen
![TouchScreen op](images/ops/Ops_Devices_TouchScreen.svg)

**Full Name:** `Ops.Devices.TouchScreen`
**Description:** touch screen input: e.g. position of fingers

**> Input Ports:**
- **Disable Scaling** (Number: Boolean): *See documentation*
- **Disable Scroll** (Number: Boolean): *See documentation*
- **HDPI Coordinates** (Number: Boolean): *See documentation*
- **Active** (Number: Boolean): *See documentation*
- **Normalize Coordinates** (Number: Boolean): *See documentation*
- **Flip Y** (Number: Boolean): *See documentation*

**< Output Ports:**
- **Touched** (Number): *See documentation*
- **Fingers** (Number): *See documentation*
- **Finger 1 X** (Number): *See documentation*
- **Finger 1 Y** (Number): *See documentation*
- **Finger 1 Force** (Number): *See documentation*
- **Finger 2 X** (Number): *See documentation*
- **Finger 2 Y** (Number): *See documentation*
- **Finger 2 Force** (Number): *See documentation*
- **Events** (Array): *See documentation*
- **Touch Start** (Trigger): *See documentation*
- **Touch End** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Devices.TouchScreen#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "TouchScreen"*
**Docs:** [https://cables.gl/op/Ops.Devices.TouchScreen](https://cables.gl/op/Ops.Devices.TouchScreen)

---

