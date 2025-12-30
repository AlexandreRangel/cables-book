# Ops.Devices.Midi

*Part of the [All Operators Reference](13-_AllOps.md)*

---

## Ops.Devices.Midi

### DeviceList
![DeviceList op](images/ops/Ops_Devices_Midi_DeviceList.svg)

**Full Name:** `Ops.Devices.Midi.DeviceList`
**Description:** list of midi devices

**> Input Ports:**
- *Visit [Ops.Devices.Midi.DeviceList documentation](https://cables.gl/op/Ops.Devices.Midi.DeviceList) for input port details*

**< Output Ports:**
- **Num Devices** (Number): *See documentation*
- **Midi Support** (booleanNumber): *See documentation*
- **Device Names** (Array): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/EEHSl5)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "DeviceList"*
**Docs:** [https://cables.gl/op/Ops.Devices.Midi.DeviceList](https://cables.gl/op/Ops.Devices.Midi.DeviceList)

---

### MidiCC_v3
![MidiCC_v3 op](images/ops/Ops_Devices_Midi_MidiCC_v3.svg)

**Full Name:** `Ops.Devices.Midi.MidiCC_v3`
**Description:** read CC value from Midi controller

**> Input Ports:**
- **MIDI Event In** (Object): *See documentation*
- **MIDI Channel Index** (Number: Integer): *See documentation*
- **CC Index** (Number: Integer): *See documentation*
- **Speed** (Number): *See documentation*
- **Learn** (Trigger): *See documentation*
- **Clear** (Trigger): *See documentation*

**< Output Ports:**
- **CC Value Out** (Number): *See documentation*
- **Event** (Object): *See documentation*
- **Trigger Out** (Trigger): *See documentation*
- **CC Index Out** (Number): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/dfF3DI)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "MidiCC_v3"*
**Docs:** [https://cables.gl/op/Ops.Devices.Midi.MidiCC_v3](https://cables.gl/op/Ops.Devices.Midi.MidiCC_v3)

---

### MidiCCOut_v2
![MidiCCOut_v2 op](images/ops/Ops_Devices_Midi_MidiCCOut_v2.svg)

**Full Name:** `Ops.Devices.Midi.MidiCCOut_v2`
**Description:** send MIDI CC data to a midi output

**> Input Ports:**
- **Send** (Trigger): *See documentation*
- **MIDI Channel Index** (Number: Integer): *See documentation*
- **CC Index** (Number: Integer): *See documentation*
- **CC Value** (Number: Integer): *See documentation*
- **Auto Send Value Change** (Number: Boolean): *See documentation*

**< Output Ports:**
- **MIDI Event Out** (Object): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/VbaQXU)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "MidiCCOut_v2"*
**Docs:** [https://cables.gl/op/Ops.Devices.Midi.MidiCCOut_v2](https://cables.gl/op/Ops.Devices.Midi.MidiCCOut_v2)

---

### MidiChord3
![MidiChord3 op](images/ops/Ops_Devices_Midi_MidiChord3.svg)

**Full Name:** `Ops.Devices.Midi.MidiChord3`
**Description:** Map 3 midi notes to values

**> Input Ports:**
- **MIDI Event In** (Object): *See documentation*
- **MIDI Channel Index** (Number: Integer): *See documentation*
- **Note 1 Index** (Number: Integer): *See documentation*
- **Note 2 Index** (Number: Integer): *See documentation*
- **Note 3 Index** (Number: Integer): *See documentation*
- **Normalize Velocity Index** (Number: Integer): *See documentation*
- **Learn** (Trigger): *See documentation*
- **Reset** (Trigger): *See documentation*

**< Output Ports:**
- **MIDI Event Out** (Object): *See documentation*
- **Trigger Out** (Trigger): *See documentation*
- **Note Out 1** (Number): *See documentation*
- **Velocity 1** (Number): *See documentation*
- **Gate 1** (booleanNumber): *See documentation*
- **Note Out 2** (Number): *See documentation*
- **Velocity 2** (Number): *See documentation*
- **Gate 2** (booleanNumber): *See documentation*
- **Note Out 3** (Number): *See documentation*
- **Velocity 3** (Number): *See documentation*
- **Gate 3** (booleanNumber): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/dfF3DI)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "MidiChord3"*
**Docs:** [https://cables.gl/op/Ops.Devices.Midi.MidiChord3](https://cables.gl/op/Ops.Devices.Midi.MidiChord3)

---

### MidiClock
![MidiClock op](images/ops/Ops_Devices_Midi_MidiClock.svg)

**Full Name:** `Ops.Devices.Midi.MidiClock`
**Description:** sends out midi clock signals as triggers

**> Input Ports:**
- **MIDI Event In** (Object): *See documentation*
- **Timing Index** (Number: Integer): *See documentation*

**< Output Ports:**
- **MIDI Event Out** (Object): *See documentation*
- **Tick Out** (Trigger): *See documentation*
- **Clock Start** (Trigger): *See documentation*
- **Clock Stop** (Trigger): *See documentation*
- **Clock Continue** (Trigger): *See documentation*
- **BPM** (Number): *See documentation*
- **Tick Duration** (Number): *See documentation*
- **Sub Tick** (Number): *See documentation*
- **current subtick** (value between 0 - 24): *See documentation*
- **outputs a trigger every bar** (dotted: 1.5 bars, triplet: full-note triplet): *See documentation*
- **outputs a trigger every half note** (dotted: trigger every 3/4, triplet: half-note triplet): *See documentation*
- **outputs a trigger every quarter note** (dotted: trigger every 3/8, triplet: quarter-note triplet): *See documentation*
- **outputs a trigger every eigth note** (dotted: trigger every 3/16, triplet: eigth-note triplet): *See documentation*
- **outputs a trigger every sixteenth note** (dotted: trigger every 3/32, triplet: sixteenth-note triplet): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/dfF3DI)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "MidiClock"*
**Docs:** [https://cables.gl/op/Ops.Devices.Midi.MidiClock](https://cables.gl/op/Ops.Devices.Midi.MidiClock)

---

### MidiInputDevice_v2
![MidiInputDevice_v2 op](images/ops/Ops_Devices_Midi_MidiInputDevice_v2.svg)

**Full Name:** `Ops.Devices.Midi.MidiInputDevice_v2`
**Description:** connect to MIDI device output port

**> Input Ports:**
- **Device Index** (Number: Integer): *See documentation*
- **Learn** (Trigger): *See documentation*

**< Output Ports:**
- **Event** (Object): *See documentation*
- **Note** (Object): *See documentation*
- **CC** (Object): *See documentation*
- **NRPN** (Object): *See documentation*
- **Program Change** (Object): *See documentation*
- **Clock** (Object): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/dfF3DI)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "MidiInputDevice_v2"*
**Docs:** [https://cables.gl/op/Ops.Devices.Midi.MidiInputDevice_v2](https://cables.gl/op/Ops.Devices.Midi.MidiInputDevice_v2)

---

### MidiMonitor
![MidiMonitor op](images/ops/Ops_Devices_Midi_MidiMonitor.svg)

**Full Name:** `Ops.Devices.Midi.MidiMonitor`
**Description:** detailed information about Midi events being sent

**> Input Ports:**
- **Event** (Object): *See documentation*

**< Output Ports:**
- **MIDI Event Out** (Object): *See documentation*
- **Trigger Out** (Trigger): *See documentation*
- **Device** (Number): *See documentation*
- **MIDI Channel** (Number): *See documentation*
- **Message Type** (Number): *See documentation*
- **the type of the message** (CC, Note, NRPN, Clock, ...): *See documentation*
- **Note** (Number): *See documentation*
- **Note Velocity** (Number): *See documentation*
- **CC Number** (Number): *See documentation*
- **CC Value** (Number): *See documentation*
- **Pitch Bend Value** (Number): *See documentation*
- **NRPN Number** (Number): *See documentation*
- **NRPN Value** (Number): *See documentation*
- **Program Change Value** (Number): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/dfF3DI)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "MidiMonitor"*
**Docs:** [https://cables.gl/op/Ops.Devices.Midi.MidiMonitor](https://cables.gl/op/Ops.Devices.Midi.MidiMonitor)

---

### MidiNote
![MidiNote op](images/ops/Ops_Devices_Midi_MidiNote.svg)

**Full Name:** `Ops.Devices.Midi.MidiNote`
**Description:** Read a single midi note

**> Input Ports:**
- **MIDI Event In** (Object): *See documentation*
- **MIDI Channel Index** (Number: Integer): *See documentation*
- **Note Index** (Number: Integer): *See documentation*
- **Normalize Velocity Index** (Number: Integer): *See documentation*
- **Toggle Gate** (Number: Boolean): *See documentation*
- **Learn** (Trigger): *See documentation*
- **Clear** (Trigger): *See documentation*

**< Output Ports:**
- **MIDI Event Out** (Object): *See documentation*
- **Trigger Out** (Trigger): *See documentation*
- **Current Note** (Number): *See documentation*
- **Velocity** (Number): *See documentation*
- **Gate** (booleanNumber): *See documentation*
- **Velocity Array** (Array): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/dfF3DI)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "MidiNote"*
**Docs:** [https://cables.gl/op/Ops.Devices.Midi.MidiNote](https://cables.gl/op/Ops.Devices.Midi.MidiNote)

---

### MidiNoteFilter
![MidiNoteFilter op](images/ops/Ops_Devices_Midi_MidiNoteFilter.svg)

**Full Name:** `Ops.Devices.Midi.MidiNoteFilter`
**Description:** Only read a range of notes (e.g. C1 to C2)

**> Input Ports:**
- **MIDI Event** (Object): *See documentation*
- **MIDI Channel Index** (Number: Integer): *See documentation*
- **Note Start Index** (Number: Integer): *See documentation*
- **Note End Index** (Number: Integer): *See documentation*
- **Normalize Velocity Index** (Number: Integer): *See documentation*
- **Learn** (Trigger): *See documentation*
- **Reset** (Trigger): *See documentation*

**< Output Ports:**
- **Event** (Object): *See documentation*
- **Trigger Out** (Trigger): *See documentation*
- **Current Note** (Number): *See documentation*
- **Velocity** (Number): *See documentation*
- **Gate** (booleanNumber): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/dfF3DI)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "MidiNoteFilter"*
**Docs:** [https://cables.gl/op/Ops.Devices.Midi.MidiNoteFilter](https://cables.gl/op/Ops.Devices.Midi.MidiNoteFilter)

---

### MidiNoteOut
![MidiNoteOut op](images/ops/Ops_Devices_Midi_MidiNoteOut.svg)

**Full Name:** `Ops.Devices.Midi.MidiNoteOut`
**Description:** send midi note data to a midi output

**> Input Ports:**
- **MIDI Channel Index** (Number: Integer): *See documentation*
- **Note Index** (Number: Integer): *See documentation*
- **Note Number** (Number: Integer): *See documentation*
- **Velocity** (Number: Integer): *See documentation*
- **Min In Velocity** (Number): *See documentation*
- **Max In Velocity** (Number): *See documentation*
- **Velocity Array In** (Array): *See documentation*

**< Output Ports:**
- **MIDI Event Out** (Object): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/VbaQXU)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "MidiNoteOut"*
**Docs:** [https://cables.gl/op/Ops.Devices.Midi.MidiNoteOut](https://cables.gl/op/Ops.Devices.Midi.MidiNoteOut)

---

### MidiNRPN
![MidiNRPN op](images/ops/Ops_Devices_Midi_MidiNRPN.svg)

**Full Name:** `Ops.Devices.Midi.MidiNRPN`
**Description:** read NRPN value from controller

**> Input Ports:**
- **MIDI Event In** (Object): *See documentation*
- **MIDI Channel Index** (Number: Integer): *See documentation*
- **NRPN Index** (Number: Integer): *See documentation*
- **Normalize Index** (Number: Integer): *See documentation*
- **Learn** (Trigger): *See documentation*
- **Clear** (Trigger): *See documentation*

**< Output Ports:**
- **MIDI Event Out** (Object): *See documentation*
- **Trigger Out** (Trigger): *See documentation*
- **NRPN Index Out** (Number): *See documentation*
- **NRPN Value** (Number): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/dfF3DI)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "MidiNRPN"*
**Docs:** [https://cables.gl/op/Ops.Devices.Midi.MidiNRPN](https://cables.gl/op/Ops.Devices.Midi.MidiNRPN)

---

### MidiNRPNOut
![MidiNRPNOut op](images/ops/Ops_Devices_Midi_MidiNRPNOut.svg)

**Full Name:** `Ops.Devices.Midi.MidiNRPNOut`
**Description:** send midi NRPN data to a midi output

**> Input Ports:**
- **MIDI Channel Index** (Number: Integer): *See documentation*
- **NRPN Index** (Number: Integer): *See documentation*
- **NRPN Value** (Number: Integer): *See documentation*
- **Min In Value** (Number): *See documentation*
- **Max In Value** (Number): *See documentation*

**< Output Ports:**
- **MIDI Event Out** (Object): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/VbaQXU)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "MidiNRPNOut"*
**Docs:** [https://cables.gl/op/Ops.Devices.Midi.MidiNRPNOut](https://cables.gl/op/Ops.Devices.Midi.MidiNRPNOut)

---

### MidiOutputDevice
![MidiOutputDevice op](images/ops/Ops_Devices_Midi_MidiOutputDevice.svg)

**Full Name:** `Ops.Devices.Midi.MidiOutputDevice`
**Description:** Connect to MIDI device input port

**> Input Ports:**
- **Device Index** (Number: Integer): *See documentation*
- **Note** (Object): *See documentation*
- **CC** (Object): *See documentation*
- **NRPN** (Object): *See documentation*

**< Output Ports:**
- *Visit [Ops.Devices.Midi.MidiOutputDevice documentation](https://cables.gl/op/Ops.Devices.Midi.MidiOutputDevice) for output port details*

**Example Patch:** [Open in Editor](https://cables.gl/edit/VbaQXU)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "MidiOutputDevice"*
**Docs:** [https://cables.gl/op/Ops.Devices.Midi.MidiOutputDevice](https://cables.gl/op/Ops.Devices.Midi.MidiOutputDevice)

---

### MidiTranspose
![MidiTranspose op](images/ops/Ops_Devices_Midi_MidiTranspose.svg)

**Full Name:** `Ops.Devices.Midi.MidiTranspose`
**Description:** transpose incoming midi notes

**> Input Ports:**
- **MIDI Event In** (Object): *See documentation*
- **MIDI Channel Index** (Number: Integer): *See documentation*
- **Transpose Amount** (Number: Integer): *See documentation*
- **Learn** (Trigger): *See documentation*

**< Output Ports:**
- **MIDI Event Out** (Object): *See documentation*
- **Trigger Out** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/dfF3DI)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "MidiTranspose"*
**Docs:** [https://cables.gl/op/Ops.Devices.Midi.MidiTranspose](https://cables.gl/op/Ops.Devices.Midi.MidiTranspose)

---

### MidiValueToNote_v2
![MidiValueToNote_v2 op](images/ops/Ops_Devices_Midi_MidiValueToNote_v2.svg)

**Full Name:** `Ops.Devices.Midi.MidiValueToNote_v2`
**Description:** Converts a MIDI value to a note string

**> Input Ports:**
- **Midi Value** (Number): *See documentation*

**< Output Ports:**
- **Note** (String): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/PfZk-4)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "MidiValueToNote_v2"*
**Docs:** [https://cables.gl/op/Ops.Devices.Midi.MidiValueToNote_v2](https://cables.gl/op/Ops.Devices.Midi.MidiValueToNote_v2)

---

