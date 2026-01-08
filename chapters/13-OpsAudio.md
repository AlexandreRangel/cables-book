# Ops.Audio


```{=latex}
\OpsSubsubNoSubsectionNumbering\setcounter{subsubsection}{0}
```
### BpmTap
![BpmTap op](images/ops/Ops_Audio_BpmTap.svg)

**Full Name:** `Ops.Audio.BpmTap`

Let’s you tap in a beat, useful to synchronise visuals to music (VJ, sync, sound).

**`\inputsymbol`{=latex} Inputs**

- **Exe** (Trigger)
- **Tap** (Trigger)
- **Sync** (Trigger)
- **NudgeLeft** (Trigger)
- **NudgeRight** (Trigger)
- **Active** (Number: Boolean)

**`\outputsymbol`{=latex} Output**

- **Beat** (Trigger)
- **Bpm** (Number)
- **The resulting BPM** (beats per minute)
- **States** (Array)
- **Beat Index** (Number)

**Example Patch:** [cables.gl/edit/vwdfqX](https://cables.gl/edit/vwdfqX)

**Doc:** [cables.gl/op/Ops.Audio.BpmTap](https://cables.gl/op/Ops.Audio.BpmTap)

### MidiJson
![MidiJson op](images/ops/Ops_Audio_MidiJson.svg)

**Full Name:** `Ops.Audio.MidiJson`

read MIDI information at time x.

**`\inputsymbol`{=latex} Inputs**

- **MidiJson** (Object)
- **Time** (Number)

**`\outputsymbol`{=latex} Output**

- **Beat** (Number)
- **Track Names** (Array)
- **Names** (Array)
- **Progress** (Array)
- **Velocity** (Array)
- **Num Tracks** (Number)
- **BPM** (Number)
- **Data** (Object)

**Example Patch:** [cables.gl/edit/yJPMCV](https://cables.gl/edit/yJPMCV)

**Doc:** [cables.gl/op/Ops.Audio.MidiJson](https://cables.gl/op/Ops.Audio.MidiJson)

### MidiJsonNote_v2
![MidiJsonNote_v2 op](images/ops/Ops_Audio_MidiJsonNote_v2.svg)

**Full Name:** `Ops.Audio.MidiJsonNote_v2`

Filter MidiJson for notes.

**`\inputsymbol`{=latex} Inputs**

- **Data** (Object)
- **Note** (String)
- **Channel** (Number: String)
- **Beat Start** (Number: Integer)
- **Beat End** (Number: Integer)

**`\outputsymbol`{=latex} Output**

- **Count** (Number)
- **Progress** (Number)
- **Time Since Last** (Number)
- **Trigger** (Trigger)
- **Reseted** (Trigger)

**Example Patch:** [cables.gl/op/Ops.Audio.MidiJsonNote_v2#example](https://cables.gl/op/Ops.Audio.MidiJsonNote_v2#example)

**Doc:** [cables.gl/op/Ops.Audio.MidiJsonNote_v2](https://cables.gl/op/Ops.Audio.MidiJsonNote_v2)


