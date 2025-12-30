# Ops.Devices.Keyboard

*Part of the [All Operators Reference](13-_AllOps.md)*

---

## Ops.Devices.Keyboard

### CursorKeys
![CursorKeys op](images/ops/Ops_Devices_Keyboard_CursorKeys.svg)

**Full Name:** `Ops.Devices.Keyboard.CursorKeys`
**Description:** get the state of your keyboards arrow keys

**> Input Ports:**
- **Canvas Only** (Number: Boolean)
- **Cursor Keys** (Number: Boolean)
- **WASD** (Number: Boolean)
- **Active** (Number: Boolean)

**< Output Ports:**
- **Degree** (Number)
- **Up** (booleanNumber)
- **Up Pressed** (Trigger)
- **Down** (booleanNumber)
- **Down Pressed** (Trigger)
- **Left** (booleanNumber)
- **Left Pressed** (Trigger)
- **Right** (booleanNumber)
- **Right Pressed** (Trigger)
- **Any Button Pressed** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/edit/m5V6VB)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "CursorKeys"*
**Docs:** [https://cables.gl/op/Ops.Devices.Keyboard.CursorKeys](https://cables.gl/op/Ops.Devices.Keyboard.CursorKeys)

---

### KeyPress_v2
![KeyPress_v2 op](images/ops/Ops_Devices_Keyboard_KeyPress_v2.svg)

**Full Name:** `Ops.Devices.Keyboard.KeyPress_v2`
**Description:** Triggers when a key is pressed

**> Input Ports:**
- **Area Index** (Number: Integer)
- **Prevent Default** (Number: Boolean)
- **Enabled** (Number: Boolean)

**< Output Ports:**
- **On Press** (Trigger)
- **Key Code** (Number)
- **Key** (String)

**Example Patch:** [Open in Editor](https://cables.gl/edit/lmGgPZ)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "KeyPress_v2"*
**Docs:** [https://cables.gl/op/Ops.Devices.Keyboard.KeyPress_v2](https://cables.gl/op/Ops.Devices.Keyboard.KeyPress_v2)

---

### KeyPressLearn
![KeyPressLearn op](images/ops/Ops_Devices_Keyboard_KeyPressLearn.svg)

**Full Name:** `Ops.Devices.Keyboard.KeyPressLearn`
**Description:** Triggers when certain key is pressed or released

**> Input Ports:**
- **Key Code** (Number: Integer)
- **Canvas Only** (Number: Boolean)
- **Mod Key Index** (Number: Integer)
- **Enabled** (Number: Boolean)
- **Prevent Default** (Number: Boolean)
- **Learn** (Trigger)

**< Output Ports:**
- **On Press** (Trigger)
- **On Release** (Trigger)
- **Pressed** (booleanNumber)
- **Key** (String)

**Example Patch:** [Open in Editor](https://cables.gl/edit/ZRY-x3)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "KeyPressLearn"*
**Docs:** [https://cables.gl/op/Ops.Devices.Keyboard.KeyPressLearn](https://cables.gl/op/Ops.Devices.Keyboard.KeyPressLearn)

---

### PersonController
![PersonController op](images/ops/Ops_Devices_Keyboard_PersonController.svg)

**Full Name:** `Ops.Devices.Keyboard.PersonController`
**Description:** simple controller example op for game characters

**> Input Ports:**
- **Exe** (Trigger)
- **Speed** (Number)
- **North** (Number: Boolean)
- **East** (Number: Boolean)
- **South** (Number: Boolean)
- **West** (Number: Boolean)
- **Reset** (Trigger)

**< Output Ports:**
- **X** (Number)
- **Y** (Number)
- **Dir** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/edit/m5V6VB)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "PersonController"*
**Docs:** [https://cables.gl/op/Ops.Devices.Keyboard.PersonController](https://cables.gl/op/Ops.Devices.Keyboard.PersonController)

---

### QWERTYtoMidi
![QWERTYtoMidi op](images/ops/Ops_Devices_Keyboard_QWERTYtoMidi.svg)

**Full Name:** `Ops.Devices.Keyboard.QWERTYtoMidi`
**Description:** Emulates a MIDI keyboard using your regular keyboard

**> Input Ports:**
- **Canvas Only** (Number: Boolean)

**< Output Ports:**
- **Note Number** (Number)
- **Velocity** (Number)
- **Channel** (Number)
- **Command** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/edit/PfZk-4)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "QWERTYtoMidi"*
**Docs:** [https://cables.gl/op/Ops.Devices.Keyboard.QWERTYtoMidi](https://cables.gl/op/Ops.Devices.Keyboard.QWERTYtoMidi)

---

