# Ops.Devices.GamePad

*Part of the [All Operators Reference](13-_AllOps.md)*

---

## Ops.Devices.GamePad

### GamePad
![GamePad op](images/ops/Ops_Devices_GamePad_GamePad.svg)

**Full Name:** `Ops.Devices.GamePad.GamePad`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Devices.GamePad.GamePad) for details*

**> Input Ports:**
- **GamePad Data** (Object)
- **Analog To Digital** (Number: Boolean)

**< Output Ports:**
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

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Devices.GamePad.GamePad#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "GamePad"*
**Docs:** [https://cables.gl/op/Ops.Devices.GamePad.GamePad](https://cables.gl/op/Ops.Devices.GamePad.GamePad)

---

### GamePadJoystickAxis
![GamePadJoystickAxis op](images/ops/Ops_Devices_GamePad_GamePadJoystickAxis.svg)

**Full Name:** `Ops.Devices.GamePad.GamePadJoystickAxis`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Devices.GamePad.GamePadJoystickAxis) for details*

**> Input Ports:**
- **Axis** (Array)
- **Index** (Number: Integer)

**< Output Ports:**
- **X** (Number)
- **Y** (Number)
- **DeadZone** (Number)
- **Angle** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Devices.GamePad.GamePadJoystickAxis#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "GamePadJoystickAxis"*
**Docs:** [https://cables.gl/op/Ops.Devices.GamePad.GamePadJoystickAxis](https://cables.gl/op/Ops.Devices.GamePad.GamePadJoystickAxis)

---

### GamePads
![GamePads op](images/ops/Ops_Devices_GamePad_GamePads.svg)

**Full Name:** `Ops.Devices.GamePad.GamePads`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Devices.GamePad.GamePads) for details*

**> Input Ports:**
- **Exe** (Trigger)

**< Output Ports:**
- **Num Gamepads** (Number)
- **Pad 0** (Object)
- **Pad 1** (Object)
- **Pad 2** (Object)
- **Pad 3** (Object)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Devices.GamePad.GamePads#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "GamePads"*
**Docs:** [https://cables.gl/op/Ops.Devices.GamePad.GamePads](https://cables.gl/op/Ops.Devices.GamePad.GamePads)

---

