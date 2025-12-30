# Ops.Devices.GamePad

*Part of the [All Operators Reference](13-_AllOps.md)*

---

## Ops.Devices.GamePad

### GamePad
![GamePad op](images/ops/Ops_Devices_GamePad_GamePad.svg)

**Full Name:** `Ops.Devices.GamePad.GamePad`
**Description:** Outputs the button states of a gamepad

**> Input Ports:**
- **GamePad Data** (Object): *See documentation*
- **Analog To Digital** (Number: Boolean): *See documentation*

**< Output Ports:**
- **ID** (String): *See documentation*
- **Axes** (Array): *See documentation*
- **Pad Left** (booleanNumber): *See documentation*
- **Pad Right** (booleanNumber): *See documentation*
- **Pad Up** (booleanNumber): *See documentation*
- **Pad Down** (booleanNumber): *See documentation*
- **Button 1** (booleanNumber): *See documentation*
- **Button 2** (booleanNumber): *See documentation*
- **Button 3** (booleanNumber): *See documentation*
- **Button 4** (booleanNumber): *See documentation*
- **Left Shoulder** (Number): *See documentation*
- **Left Shoulder Bottom** (Number): *See documentation*
- **Right Shoulder** (Number): *See documentation*
- **Right Shoulder Bottom** (Number): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/XHK7NH)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "GamePad"*
**Docs:** [https://cables.gl/op/Ops.Devices.GamePad.GamePad](https://cables.gl/op/Ops.Devices.GamePad.GamePad)

---

### GamePadJoystickAxis
![GamePadJoystickAxis op](images/ops/Ops_Devices_GamePad_GamePadJoystickAxis.svg)

**Full Name:** `Ops.Devices.GamePad.GamePadJoystickAxis`
**Description:** get axis and angle of a joystick/thumbstick

**> Input Ports:**
- **Axis** (Array): *See documentation*
- **Index** (Number: Integer): *See documentation*

**< Output Ports:**
- **X** (Number): *See documentation*
- **Y** (Number): *See documentation*
- **DeadZone** (Number): *See documentation*
- **Angle** (Number): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/bDqHdN)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "GamePadJoystickAxis"*
**Docs:** [https://cables.gl/op/Ops.Devices.GamePad.GamePadJoystickAxis](https://cables.gl/op/Ops.Devices.GamePad.GamePadJoystickAxis)

---

### GamePads
![GamePads op](images/ops/Ops_Devices_GamePad_GamePads.svg)

**Full Name:** `Ops.Devices.GamePad.GamePads`
**Description:** list connected gamepads - press a button to connect

**> Input Ports:**
- **Exe** (Trigger): *See documentation*

**< Output Ports:**
- **Num Gamepads** (Number): *See documentation*
- **Pad 0** (Object): *See documentation*
- **Pad 1** (Object): *See documentation*
- **Pad 2** (Object): *See documentation*
- **Pad 3** (Object): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/XHK7NH)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "GamePads"*
**Docs:** [https://cables.gl/op/Ops.Devices.GamePad.GamePads](https://cables.gl/op/Ops.Devices.GamePad.GamePads)

---

