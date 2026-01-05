# Ops.Devices.GamePad

---

## Ops.Devices.GamePad

### GamePad
![GamePad op](images/ops/Ops_Devices_GamePad_GamePad.svg)

**Full Name:** `Ops.Devices.GamePad.GamePad`

**Description:** Outputs the button states of a gamepad

**`\inputsymbol`{=latex} Inputs**

- **GamePad Data** (Object)
- **Analog To Digital** (Number: Boolean)

**`\outputsymbol`{=latex} Output**

- **ID** (String)
- **Axes** (Array)
- **Pad Left** (booleanNumber)
- **Pad Right** (booleanNumber)
- **Pad Up** (booleanNumber)
- **Pad Down** (booleanNumber)
- **Button 1** (booleanNumber)
- **Button 2** (booleanNumber)
- **Button 3** (booleanNumber)
- **Button 4** (booleanNumber)
- **Left Shoulder** (Number)
- **Left Shoulder Bottom** (Number)
- **Right Shoulder** (Number)
- **Right Shoulder Bottom** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/edit/XHK7NH)

**Docs:** [https://cables.gl/op/Ops.Devices.GamePad.GamePad](https://cables.gl/op/Ops.Devices.GamePad.GamePad)

### GamePadJoystickAxis
![GamePadJoystickAxis op](images/ops/Ops_Devices_GamePad_GamePadJoystickAxis.svg)

**Full Name:** `Ops.Devices.GamePad.GamePadJoystickAxis`

**Description:** get axis and angle of a joystick/thumbstick

**`\inputsymbol`{=latex} Inputs**

- **Axis** (Array)
- **Index** (Number: Integer)

**`\outputsymbol`{=latex} Output**

- **X** (Number)
- **Y** (Number)
- **DeadZone** (Number)
- **Angle** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/edit/bDqHdN)

**Docs:** [https://cables.gl/op/Ops.Devices.GamePad.GamePadJoystickAxis](https://cables.gl/op/Ops.Devices.GamePad.GamePadJoystickAxis)

### GamePads
![GamePads op](images/ops/Ops_Devices_GamePad_GamePads.svg)

**Full Name:** `Ops.Devices.GamePad.GamePads`

**Description:** list connected gamepads - press a button to connect

**`\inputsymbol`{=latex} Inputs**

- **Exe** (Trigger)

**`\outputsymbol`{=latex} Output**

- **Num Gamepads** (Number)
- **Pad 0** (Object)
- **Pad 1** (Object)
- **Pad 2** (Object)
- **Pad 3** (Object)

**Example Patch:** [Open in Editor](https://cables.gl/edit/XHK7NH)

**Docs:** [https://cables.gl/op/Ops.Devices.GamePad.GamePads](https://cables.gl/op/Ops.Devices.GamePad.GamePads)


