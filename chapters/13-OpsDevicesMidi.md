# Ops.Devices.Midi

---

## Ops.Devices.Midi

### DeviceList
![DeviceList op](images/ops/Ops_Devices_Midi_DeviceList.svg)

**Full Name:** `Ops.Devices.Midi.DeviceList`

**Description:** list of midi devices

**`\inputsymbol`{=latex} Inputs**

- *Visit [Ops.Devices.Midi.DeviceList documentation](https://cables.gl/op/Ops.Devices.Midi.DeviceList) for input port details*

**`\outputsymbol`{=latex} Output**

- **Num Devices** (Number)
- **Midi Support** (booleanNumber)
- **Device Names** (Array)

**Example Patch:** [Open in Editor](https://cables.gl/edit/EEHSl5)

**Docs:** [https://cables.gl/op/Ops.Devices.Midi.DeviceList](https://cables.gl/op/Ops.Devices.Midi.DeviceList)

### MidiCC_v3
![MidiCC_v3 op](images/ops/Ops_Devices_Midi_MidiCC_v3.svg)

**Full Name:** `Ops.Devices.Midi.MidiCC_v3`

**Description:** read CC value from Midi controller

**`\inputsymbol`{=latex} Inputs**

- **MIDI Event In** (Object)
- **MIDI Channel Index** (Number: Integer)
- **CC Index** (Number: Integer)
- **Speed** (Number)
- **Learn** (Trigger)
- **Clear** (Trigger)

**`\outputsymbol`{=latex} Output**

- **CC Value Out** (Number)
- **Event** (Object)
- **Trigger Out** (Trigger)
- **CC Index Out** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/edit/dfF3DI)

**Docs:** [https://cables.gl/op/Ops.Devices.Midi.MidiCC_v3](https://cables.gl/op/Ops.Devices.Midi.MidiCC_v3)

### MidiCCOut_v2
![MidiCCOut_v2 op](images/ops/Ops_Devices_Midi_MidiCCOut_v2.svg)

**Full Name:** `Ops.Devices.Midi.MidiCCOut_v2`

**Description:** send MIDI CC data to a midi output

**`\inputsymbol`{=latex} Inputs**

- **Send** (Trigger)
- **MIDI Channel Index** (Number: Integer)
- **CC Index** (Number: Integer)
- **CC Value** (Number: Integer)
- **Auto Send Value Change** (Number: Boolean)

**`\outputsymbol`{=latex} Output**

- **MIDI Event Out** (Object)

**Example Patch:** [Open in Editor](https://cables.gl/edit/VbaQXU)

**Docs:** [https://cables.gl/op/Ops.Devices.Midi.MidiCCOut_v2](https://cables.gl/op/Ops.Devices.Midi.MidiCCOut_v2)

### MidiChord3
![MidiChord3 op](images/ops/Ops_Devices_Midi_MidiChord3.svg)

**Full Name:** `Ops.Devices.Midi.MidiChord3`

**Description:** Map 3 midi notes to values

**`\inputsymbol`{=latex} Inputs**

- **MIDI Event In** (Object)
- **MIDI Channel Index** (Number: Integer)
- **Note 1 Index** (Number: Integer)
- **Note 2 Index** (Number: Integer)
- **Note 3 Index** (Number: Integer)
- **Normalize Velocity Index** (Number: Integer)
- **Learn** (Trigger)
- **Reset** (Trigger)

**`\outputsymbol`{=latex} Output**

- **MIDI Event Out** (Object)
- **Trigger Out** (Trigger)
- **Note Out 1** (Number)
- **Velocity 1** (Number)
- **Gate 1** (booleanNumber)
- **Note Out 2** (Number)
- **Velocity 2** (Number)
- **Gate 2** (booleanNumber)
- **Note Out 3** (Number)
- **Velocity 3** (Number)
- **Gate 3** (booleanNumber)

**Example Patch:** [Open in Editor](https://cables.gl/edit/dfF3DI)

**Docs:** [https://cables.gl/op/Ops.Devices.Midi.MidiChord3](https://cables.gl/op/Ops.Devices.Midi.MidiChord3)

### MidiClock
![MidiClock op](images/ops/Ops_Devices_Midi_MidiClock.svg)

**Full Name:** `Ops.Devices.Midi.MidiClock`

**Description:** sends out midi clock signals as triggers

**`\inputsymbol`{=latex} Inputs**

- **MIDI Event In** (Object)
- **Timing Index** (Number: Integer)

**`\outputsymbol`{=latex} Output**

- **MIDI Event Out** (Object)
- **Tick Out** (Trigger)
- **Clock Start** (Trigger)
- **Clock Stop** (Trigger)
- **Clock Continue** (Trigger)
- **BPM** (Number)
- **Tick Duration** (Number)
- **Sub Tick** (Number)
- **current subtick** (value between 0 - 24)
- **outputs a trigger every bar** (dotted: 1.5 bars, triplet: full-note triplet)
- **outputs a trigger every half note** (dotted: trigger every 3/4, triplet: half-note triplet)
- **outputs a trigger every quarter note** (dotted: trigger every 3/8, triplet: quarter-note triplet)
- **outputs a trigger every eigth note** (dotted: trigger every 3/16, triplet: eigth-note triplet)
- **outputs a trigger every sixteenth note** (dotted: trigger every 3/32, triplet: sixteenth-note triplet)

**Example Patch:** [Open in Editor](https://cables.gl/edit/dfF3DI)

**Docs:** [https://cables.gl/op/Ops.Devices.Midi.MidiClock](https://cables.gl/op/Ops.Devices.Midi.MidiClock)

### MidiInputDevice_v2
![MidiInputDevice_v2 op](images/ops/Ops_Devices_Midi_MidiInputDevice_v2.svg)

**Full Name:** `Ops.Devices.Midi.MidiInputDevice_v2`

**Description:** connect to MIDI device output port

**`\inputsymbol`{=latex} Inputs**

- **Device Index** (Number: Integer)
- **Learn** (Trigger)

**`\outputsymbol`{=latex} Output**

- **Event** (Object)
- **Note** (Object)
- **CC** (Object)
- **NRPN** (Object)
- **Program Change** (Object)
- **Clock** (Object)

**Example Patch:** [Open in Editor](https://cables.gl/edit/dfF3DI)

**Docs:** [https://cables.gl/op/Ops.Devices.Midi.MidiInputDevice_v2](https://cables.gl/op/Ops.Devices.Midi.MidiInputDevice_v2)

### MidiMonitor
![MidiMonitor op](images/ops/Ops_Devices_Midi_MidiMonitor.svg)

**Full Name:** `Ops.Devices.Midi.MidiMonitor`

**Description:** detailed information about Midi events being sent

**`\inputsymbol`{=latex} Inputs**

- **Event** (Object)

**`\outputsymbol`{=latex} Output**

- **MIDI Event Out** (Object)
- **Trigger Out** (Trigger)
- **Device** (Number)
- **MIDI Channel** (Number)
- **Message Type** (Number)
- **the type of the message** (CC, Note, NRPN, Clock, ...)
- **Note** (Number)
- **Note Velocity** (Number)
- **CC Number** (Number)
- **CC Value** (Number)
- **Pitch Bend Value** (Number)
- **NRPN Number** (Number)
- **NRPN Value** (Number)
- **Program Change Value** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/edit/dfF3DI)

**Docs:** [https://cables.gl/op/Ops.Devices.Midi.MidiMonitor](https://cables.gl/op/Ops.Devices.Midi.MidiMonitor)

### MidiNote
![MidiNote op](images/ops/Ops_Devices_Midi_MidiNote.svg)

**Full Name:** `Ops.Devices.Midi.MidiNote`

**Description:** Read a single midi note

**`\inputsymbol`{=latex} Inputs**

- **MIDI Event In** (Object)
- **MIDI Channel Index** (Number: Integer)
- **Note Index** (Number: Integer)
- **Normalize Velocity Index** (Number: Integer)
- **Toggle Gate** (Number: Boolean)
- **Learn** (Trigger)
- **Clear** (Trigger)

**`\outputsymbol`{=latex} Output**

- **MIDI Event Out** (Object)
- **Trigger Out** (Trigger)
- **Current Note** (Number)
- **Velocity** (Number)
- **Gate** (booleanNumber)
- **Velocity Array** (Array)

**Example Patch:** [Open in Editor](https://cables.gl/edit/dfF3DI)

**Docs:** [https://cables.gl/op/Ops.Devices.Midi.MidiNote](https://cables.gl/op/Ops.Devices.Midi.MidiNote)

### MidiNoteFilter
![MidiNoteFilter op](images/ops/Ops_Devices_Midi_MidiNoteFilter.svg)

**Full Name:** `Ops.Devices.Midi.MidiNoteFilter`

**Description:** Only read a range of notes (e.g. C1 to C2)

**`\inputsymbol`{=latex} Inputs**

- **MIDI Event** (Object)
- **MIDI Channel Index** (Number: Integer)
- **Note Start Index** (Number: Integer)
- **Note End Index** (Number: Integer)
- **Normalize Velocity Index** (Number: Integer)
- **Learn** (Trigger)
- **Reset** (Trigger)

**`\outputsymbol`{=latex} Output**

- **Event** (Object)
- **Trigger Out** (Trigger)
- **Current Note** (Number)
- **Velocity** (Number)
- **Gate** (booleanNumber)

**Example Patch:** [Open in Editor](https://cables.gl/edit/dfF3DI)

**Docs:** [https://cables.gl/op/Ops.Devices.Midi.MidiNoteFilter](https://cables.gl/op/Ops.Devices.Midi.MidiNoteFilter)

### MidiNoteOut
![MidiNoteOut op](images/ops/Ops_Devices_Midi_MidiNoteOut.svg)

**Full Name:** `Ops.Devices.Midi.MidiNoteOut`

**Description:** send midi note data to a midi output

**`\inputsymbol`{=latex} Inputs**

- **MIDI Channel Index** (Number: Integer)
- **Note Index** (Number: Integer)
- **Note Number** (Number: Integer)
- **Velocity** (Number: Integer)
- **Min In Velocity** (Number)
- **Max In Velocity** (Number)
- **Velocity Array In** (Array)

**`\outputsymbol`{=latex} Output**

- **MIDI Event Out** (Object)

**Example Patch:** [Open in Editor](https://cables.gl/edit/VbaQXU)

**Docs:** [https://cables.gl/op/Ops.Devices.Midi.MidiNoteOut](https://cables.gl/op/Ops.Devices.Midi.MidiNoteOut)

### MidiNRPN
![MidiNRPN op](images/ops/Ops_Devices_Midi_MidiNRPN.svg)

**Full Name:** `Ops.Devices.Midi.MidiNRPN`

**Description:** read NRPN value from controller

**`\inputsymbol`{=latex} Inputs**

- **MIDI Event In** (Object)
- **MIDI Channel Index** (Number: Integer)
- **NRPN Index** (Number: Integer)
- **Normalize Index** (Number: Integer)
- **Learn** (Trigger)
- **Clear** (Trigger)

**`\outputsymbol`{=latex} Output**

- **MIDI Event Out** (Object)
- **Trigger Out** (Trigger)
- **NRPN Index Out** (Number)
- **NRPN Value** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/edit/dfF3DI)

**Docs:** [https://cables.gl/op/Ops.Devices.Midi.MidiNRPN](https://cables.gl/op/Ops.Devices.Midi.MidiNRPN)

### MidiNRPNOut
![MidiNRPNOut op](images/ops/Ops_Devices_Midi_MidiNRPNOut.svg)

**Full Name:** `Ops.Devices.Midi.MidiNRPNOut`

**Description:** send midi NRPN data to a midi output

**`\inputsymbol`{=latex} Inputs**

- **MIDI Channel Index** (Number: Integer)
- **NRPN Index** (Number: Integer)
- **NRPN Value** (Number: Integer)
- **Min In Value** (Number)
- **Max In Value** (Number)

**`\outputsymbol`{=latex} Output**

- **MIDI Event Out** (Object)

**Example Patch:** [Open in Editor](https://cables.gl/edit/VbaQXU)

**Docs:** [https://cables.gl/op/Ops.Devices.Midi.MidiNRPNOut](https://cables.gl/op/Ops.Devices.Midi.MidiNRPNOut)

### MidiOutputDevice
![MidiOutputDevice op](images/ops/Ops_Devices_Midi_MidiOutputDevice.svg)

**Full Name:** `Ops.Devices.Midi.MidiOutputDevice`

**Description:** Connect to MIDI device input port

**`\inputsymbol`{=latex} Inputs**

- **Device Index** (Number: Integer)
- **Note** (Object)
- **CC** (Object)
- **NRPN** (Object)

**`\outputsymbol`{=latex} Output**

- *Visit [Ops.Devices.Midi.MidiOutputDevice documentation](https://cables.gl/op/Ops.Devices.Midi.MidiOutputDevice) for output port details*

**Example Patch:** [Open in Editor](https://cables.gl/edit/VbaQXU)

**Docs:** [https://cables.gl/op/Ops.Devices.Midi.MidiOutputDevice](https://cables.gl/op/Ops.Devices.Midi.MidiOutputDevice)

### MidiTranspose
![MidiTranspose op](images/ops/Ops_Devices_Midi_MidiTranspose.svg)

**Full Name:** `Ops.Devices.Midi.MidiTranspose`

**Description:** transpose incoming midi notes

**`\inputsymbol`{=latex} Inputs**

- **MIDI Event In** (Object)
- **MIDI Channel Index** (Number: Integer)
- **Transpose Amount** (Number: Integer)
- **Learn** (Trigger)

**`\outputsymbol`{=latex} Output**

- **MIDI Event Out** (Object)
- **Trigger Out** (Trigger)

**Example Patch:** [Open in Editor](https://cables.gl/edit/dfF3DI)

**Docs:** [https://cables.gl/op/Ops.Devices.Midi.MidiTranspose](https://cables.gl/op/Ops.Devices.Midi.MidiTranspose)

### MidiValueToNote_v2
![MidiValueToNote_v2 op](images/ops/Ops_Devices_Midi_MidiValueToNote_v2.svg)

**Full Name:** `Ops.Devices.Midi.MidiValueToNote_v2`

**Description:** Converts a MIDI value to a note string

**`\inputsymbol`{=latex} Inputs**

- **Midi Value** (Number)

**`\outputsymbol`{=latex} Output**

- **Note** (String)

**Example Patch:** [Open in Editor](https://cables.gl/edit/PfZk-4)

**Docs:** [https://cables.gl/op/Ops.Devices.Midi.MidiValueToNote_v2](https://cables.gl/op/Ops.Devices.Midi.MidiValueToNote_v2)


