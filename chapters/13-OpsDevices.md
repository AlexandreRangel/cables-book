# Ops.Devices

---

## Ops.Devices

### TouchGesture
![TouchGesture op](images/ops/Ops_Devices_TouchGesture.svg)

**Full Name:** `Ops.Devices.TouchGesture`

**Description:** detect touch gestures like swipe and pan

**`\inputsymbol`{=latex} Input Ports:**

- **Active** (Number: Boolean)
- **Vertical Swipe** (Number: Boolean)
- **Vertical Pan** (Number: Boolean)

**`\outputsymbol`{=latex} Output Ports:**

- **Press** (Trigger)
- **Press Up** (Trigger)
- **Pan Left** (Trigger)
- **Pan Right** (Trigger)
- **Swipe Left** (Trigger)
- **Swipe Right** (Trigger)
- **Swipe Up** (Trigger)
- **Swipe Down** (Trigger)
- **Event** (Object)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Devices.TouchGesture#example)

**Docs:** [https://cables.gl/op/Ops.Devices.TouchGesture](https://cables.gl/op/Ops.Devices.TouchGesture)

### TouchScreen
![TouchScreen op](images/ops/Ops_Devices_TouchScreen.svg)

**Full Name:** `Ops.Devices.TouchScreen`

**Description:** touch screen input: e.g. position of fingers

**`\inputsymbol`{=latex} Input Ports:**

- **Disable Scaling** (Number: Boolean)
- **Disable Scroll** (Number: Boolean)
- **HDPI Coordinates** (Number: Boolean)
- **Active** (Number: Boolean)
- **Normalize Coordinates** (Number: Boolean)
- **Flip Y** (Number: Boolean)

**`\outputsymbol`{=latex} Output Ports:**

- **Touched** (Number)
- **Fingers** (Number)
- **Finger 1 X** (Number)
- **Finger 1 Y** (Number)
- **Finger 1 Force** (Number)
- **Finger 2 X** (Number)
- **Finger 2 Y** (Number)
- **Finger 2 Force** (Number)
- **Events** (Array)
- **Touch Start** (Trigger)
- **Touch End** (Trigger)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Devices.TouchScreen#example)

**Docs:** [https://cables.gl/op/Ops.Devices.TouchScreen](https://cables.gl/op/Ops.Devices.TouchScreen)


