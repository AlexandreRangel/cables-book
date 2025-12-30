# Ops.Audio

*Part of the [All Operators Reference](13-_AllOps.md)*

---

## Ops.Audio

### BpmTap
![BpmTap op](images/ops/Ops_Audio_BpmTap.svg)

**Full Name:** `Ops.Audio.BpmTap`
**Description:** Let’s you tap in a beat, useful to synchronise visuals to music (VJ, sync, sound)

**> Input Ports:**
- **Exe** (Trigger)
- **Tap** (Trigger)
- **Sync** (Trigger)
- **NudgeLeft** (Trigger)
- **NudgeRight** (Trigger)
- **Active** (Number: Boolean)

**< Output Ports:**
- **Beat** (Trigger)
- **Bpm** (Number)
- **The resulting BPM** (beats per minute)
- **States** (Array)
- **Beat Index** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/edit/vwdfqX)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "BpmTap"*
**Docs:** [https://cables.gl/op/Ops.Audio.BpmTap](https://cables.gl/op/Ops.Audio.BpmTap)

---

### MidiJson
![MidiJson op](images/ops/Ops_Audio_MidiJson.svg)

**Full Name:** `Ops.Audio.MidiJson`
**Description:** read MIDI information at time x

**> Input Ports:**
- **MidiJson** (Object)
- **Time** (Number)

**< Output Ports:**
- **Beat** (Number)
- **Track Names** (Array)
- **Names** (Array)
- **Progress** (Array)
- **Velocity** (Array)
- **Num Tracks** (Number)
- **BPM** (Number)
- **Data** (Object)

**Example Patch:** [Open in Editor](https://cables.gl/edit/yJPMCV)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "MidiJson"*
**Docs:** [https://cables.gl/op/Ops.Audio.MidiJson](https://cables.gl/op/Ops.Audio.MidiJson)

---

### MidiJsonNote_v2
![MidiJsonNote_v2 op](images/ops/Ops_Audio_MidiJsonNote_v2.svg)

**Full Name:** `Ops.Audio.MidiJsonNote_v2`
**Description:** Filter MidiJson for notes

**> Input Ports:**
- **Data** (Object)
- **Note** (String)
- **Channel** (Number: String)
- **Beat Start** (Number: Integer)
- **Beat End** (Number: Integer)

**< Output Ports:**
- **Count** (Number)
- **Progress** (Number)
- **Time Since Last** (Number)
- **Trigger** (Trigger)
- **Reseted** (Trigger)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Audio.MidiJsonNote_v2#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "MidiJsonNote_v2"*
**Docs:** [https://cables.gl/op/Ops.Audio.MidiJsonNote_v2](https://cables.gl/op/Ops.Audio.MidiJsonNote_v2)

---

