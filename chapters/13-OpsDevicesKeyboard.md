# Ops.Devices.Keyboard


```{=latex}
\OpsSubsubNoSubsectionNumbering\setcounter{subsubsection}{0}
```
### CursorKeys
![CursorKeys op](images/ops/Ops_Devices_Keyboard_CursorKeys.svg)

**Full Name:** `Ops.Devices.Keyboard.CursorKeys`

get the state of your keyboards arrow keys.

**`\inputsymbol`{=latex} Inputs**

- **Canvas Only** (Number: Boolean)
- **Cursor Keys** (Number: Boolean)
- **WASD** (Number: Boolean)
- **Active** (Number: Boolean)

**`\outputsymbol`{=latex} Output**

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

**Example Patch:** [cables.gl/edit/m5V6VB](https://cables.gl/edit/m5V6VB)

**Doc:** [cables.gl/op/Ops.Devices.Keyboard.CursorKeys](https://cables.gl/op/Ops.Devices.Keyboard.CursorKeys)

### KeyPress_v2
![KeyPress_v2 op](images/ops/Ops_Devices_Keyboard_KeyPress_v2.svg)

**Full Name:** `Ops.Devices.Keyboard.KeyPress_v2`

Triggers when a key is pressed.

**`\inputsymbol`{=latex} Inputs**

- **Area Index** (Number: Integer)
- **Prevent Default** (Number: Boolean)
- **Enabled** (Number: Boolean)

**`\outputsymbol`{=latex} Output**

- **On Press** (Trigger)
- **Key Code** (Number)
- **Key** (String)

**Example Patch:** [cables.gl/edit/lmGgPZ](https://cables.gl/edit/lmGgPZ)

**Doc:** [cables.gl/op/Ops.Devices.Keyboard.KeyPress_v2](https://cables.gl/op/Ops.Devices.Keyboard.KeyPress_v2)

### KeyPressLearn
![KeyPressLearn op](images/ops/Ops_Devices_Keyboard_KeyPressLearn.svg)

**Full Name:** `Ops.Devices.Keyboard.KeyPressLearn`

Triggers when certain key is pressed or released.

**`\inputsymbol`{=latex} Inputs**

- **Key Code** (Number: Integer)
- **Canvas Only** (Number: Boolean)
- **Mod Key Index** (Number: Integer)
- **Enabled** (Number: Boolean)
- **Prevent Default** (Number: Boolean)
- **Learn** (Trigger)

**`\outputsymbol`{=latex} Output**

- **On Press** (Trigger)
- **On Release** (Trigger)
- **Pressed** (booleanNumber)
- **Key** (String)

**Example Patch:** [cables.gl/edit/ZRY-x3](https://cables.gl/edit/ZRY-x3)

**Doc:** [cables.gl/op/Ops.Devices.Keyboard.KeyPressLearn](https://cables.gl/op/Ops.Devices.Keyboard.KeyPressLearn)

### PersonController
![PersonController op](images/ops/Ops_Devices_Keyboard_PersonController.svg)

**Full Name:** `Ops.Devices.Keyboard.PersonController`

simple controller example op for game characters.

**`\inputsymbol`{=latex} Inputs**

- **Exe** (Trigger)
- **Speed** (Number)
- **North** (Number: Boolean)
- **East** (Number: Boolean)
- **South** (Number: Boolean)
- **West** (Number: Boolean)
- **Reset** (Trigger)

**`\outputsymbol`{=latex} Output**

- **X** (Number)
- **Y** (Number)
- **Dir** (Number)

**Example Patch:** [cables.gl/edit/m5V6VB](https://cables.gl/edit/m5V6VB)

**Doc:** [cables.gl/op/Ops.Devices.Keyboard.PersonController](https://cables.gl/op/Ops.Devices.Keyboard.PersonController)

### QWERTYtoMidi
![QWERTYtoMidi op](images/ops/Ops_Devices_Keyboard_QWERTYtoMidi.svg)

**Full Name:** `Ops.Devices.Keyboard.QWERTYtoMidi`

Emulates a MIDI keyboard using your regular keyboard.

**`\inputsymbol`{=latex} Inputs**

- **Canvas Only** (Number: Boolean)

**`\outputsymbol`{=latex} Output**

- **Note Number** (Number)
- **Velocity** (Number)
- **Channel** (Number)
- **Command** (Number)

**Example Patch:** [cables.gl/edit/PfZk-4](https://cables.gl/edit/PfZk-4)

**Doc:** [cables.gl/op/Ops.Devices.Keyboard.QWERTYtoMidi](https://cables.gl/op/Ops.Devices.Keyboard.QWERTYtoMidi)


