# Ops.Anim

---

## Ops.Anim

### AnimNumber
![AnimNumber op](images/ops/Ops_Anim_AnimNumber.svg)

**Full Name:** `Ops.Anim.AnimNumber`

**Description:** Always animates to the current value

**`\inputsymbol`{=latex} Input Ports:**

- **Exe** (Trigger)
- **Value** (Number)
- **Duration** (Number)
- **Easing Index** (Number: Integer)

**`\outputsymbol`{=latex} Output Ports:**

- **Next** (Trigger)
- **Result** (Number)
- **Finished** (Trigger)

**Example Patch:** [Open in Editor](https://cables.gl/edit/lntUQx)

**Docs:** [https://cables.gl/op/Ops.Anim.AnimNumber](https://cables.gl/op/Ops.Anim.AnimNumber)

### Bang
![Bang op](images/ops/Ops_Anim_Bang.svg)

**Full Name:** `Ops.Anim.Bang`

**Description:** Trigger a simple bang animation going from 1 to 0

**`\inputsymbol`{=latex} Input Ports:**

- **Update** (Trigger)
- **Bang** (Trigger)
- **Duration** (Number)
- **Invert** (Number: Boolean)

**`\outputsymbol`{=latex} Output Ports:**

- **Trigger Out** (Trigger)
- **Value** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/edit/TctR5r)

**Docs:** [https://cables.gl/op/Ops.Anim.Bang](https://cables.gl/op/Ops.Anim.Bang)

### BoolAnim
![BoolAnim op](images/ops/Ops_Anim_BoolAnim.svg)

**Full Name:** `Ops.Anim.BoolAnim`

**Description:** Animate between two numbers based on a boolean value

**`\inputsymbol`{=latex} Input Ports:**

- **Exe** (Trigger)
- **Bool** (Number: Boolean)
- **Easing Index** (Number: Integer)
- **Duration** (Number)
- **Direction Index** (Number: Integer)
- **Value False** (Number)
- **Value True** (Number)

**`\outputsymbol`{=latex} Output Ports:**

- **Trigger** (Trigger)
- **Value** (Number)
- **Finished** (booleanNumber)
- **Finished Trigger** (Trigger)

**Example Patch:** [Open in Editor](https://cables.gl/edit/ofPcTo)

**Docs:** [https://cables.gl/op/Ops.Anim.BoolAnim](https://cables.gl/op/Ops.Anim.BoolAnim)

### Crossfade
![Crossfade op](images/ops/Ops_Anim_Crossfade.svg)

**Full Name:** `Ops.Anim.Crossfade`

**Description:** Crossfade between 2 values

**`\inputsymbol`{=latex} Input Ports:**

- **Crossfade** (Number)
- **Out Min** (Number)
- **Out Max** (Number)
- **Easing Index** (Number: Integer)

**`\outputsymbol`{=latex} Output Ports:**

- **A** (Number)
- **B** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/edit/U_a2d-)

**Docs:** [https://cables.gl/op/Ops.Anim.Crossfade](https://cables.gl/op/Ops.Anim.Crossfade)

### FrameRangeAnim_v2
![FrameRangeAnim_v2 op](images/ops/Ops_Anim_FrameRangeAnim_v2.svg)

**Full Name:** `Ops.Anim.FrameRangeAnim_v2`

**Description:** Parses string containing ranges of frames and play as coherent animation

**`\inputsymbol`{=latex} Input Ports:**

- **Time** (Number)
- **Frames** (String)
- **frame range** (ex. "0-10")
- **Loop** (Number: Boolean)
- **Rewind** (Trigger)

**`\outputsymbol`{=latex} Output Ports:**

- **Result Time** (Number)
- **Expanded Frames** (Array)
- **Finished** (booleanNumber)
- **Finished Trigger** (Trigger)
- **Anim Length** (Number)
- **Progress** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Anim.FrameRangeAnim_v2#example)

**Docs:** [https://cables.gl/op/Ops.Anim.FrameRangeAnim_v2](https://cables.gl/op/Ops.Anim.FrameRangeAnim_v2)

### FrameRangeAnimSwitcher
![FrameRangeAnimSwitcher op](images/ops/Ops_Anim_FrameRangeAnimSwitcher.svg)

**Full Name:** `Ops.Anim.FrameRangeAnimSwitcher`

**Description:** Switch between multiple anim ranges of a keyframed 3d scene

**`\inputsymbol`{=latex} Input Ports:**

- **Index** (Number: Integer)
- **Duration** (Number)
- **Easing Index** (Number: Integer)
- **Value 0** (Number)
- **Value 1** (Number)
- **Value 2** (Number)
- **Value 3** (Number)
- **Value 4** (Number)
- **Value 5** (Number)
- **Value 6** (Number)
- **Value 7** (Number)
- **Value 8** (Number)
- **Value 9** (Number)

**`\outputsymbol`{=latex} Output Ports:**

- **Time 1** (Number)
- **Time Fade** (Number)
- **Time 2** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Anim.FrameRangeAnimSwitcher#example)

**Docs:** [https://cables.gl/op/Ops.Anim.FrameRangeAnimSwitcher](https://cables.gl/op/Ops.Anim.FrameRangeAnimSwitcher)

### InOutInAnim
![InOutInAnim op](images/ops/Ops_Anim_InOutInAnim.svg)

**Full Name:** `Ops.Anim.InOutInAnim`

**Description:** Animates after a trigger from 1 to 0 to 1

**`\inputsymbol`{=latex} Input Ports:**

- **Update** (Trigger)
- **Duration In** (Number)
- **Easing In Index** (Number: Integer)
- **Value In** (Number)
- **Hold Duration** (Number)
- **Duration Out** (Number)
- **Easing Out Index** (Number: Integer)
- **Value Out** (Number)
- **Start** (Trigger)

**`\outputsymbol`{=latex} Output Ports:**

- **Next** (Trigger)
- **Result** (Number)
- **Started** (Trigger)
- **Middle** (Trigger)
- **Finished** (Trigger)

**Example Patch:** [Open in Editor](https://cables.gl/edit/HwVRrT)

**Docs:** [https://cables.gl/op/Ops.Anim.InOutInAnim](https://cables.gl/op/Ops.Anim.InOutInAnim)

### LFO_v3
![LFO_v3 op](images/ops/Ops_Anim_LFO_v3.svg)

**Full Name:** `Ops.Anim.LFO_v3`

**Description:** Low-frequency oscillation for animations

**`\inputsymbol`{=latex} Input Ports:**

- **Time** (Number)
- **Frequency** (Number)
- **Type Index** (Number: Integer)
- **Phase** (Number)
- **Range Min** (Number)
- **Range Max** (Number)

**`\outputsymbol`{=latex} Output Ports:**

- **Result** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/edit/9EOrS8)

**Docs:** [https://cables.gl/op/Ops.Anim.LFO_v3](https://cables.gl/op/Ops.Anim.LFO_v3)

### RandomAnim_v2
![RandomAnim_v2 op](images/ops/Ops_Anim_RandomAnim_v2.svg)

**Full Name:** `Ops.Anim.RandomAnim_v2`

**Description:** Animates between random values defined by a min and max value

**`\inputsymbol`{=latex} Input Ports:**

- **Exe** (Trigger)
- **Min** (Number)
- **Max** (Number)
- **Duration** (Number)
- **Pause Between** (Number)
- **Easing Index** (Number: Integer)

**`\outputsymbol`{=latex} Output Ports:**

- **Next** (Trigger)
- **Result** (Number)
- **Looped** (Trigger)

**Example Patch:** [Open in Editor](https://cables.gl/edit/nCSoG8)

**Docs:** [https://cables.gl/op/Ops.Anim.RandomAnim_v2](https://cables.gl/op/Ops.Anim.RandomAnim_v2)

### SimpleAnim
![SimpleAnim op](images/ops/Ops_Anim_SimpleAnim.svg)

**Full Name:** `Ops.Anim.SimpleAnim`

**Description:** Simple animation between two values

**`\inputsymbol`{=latex} Input Ports:**

- **Exe** (Trigger)
- **Reset** (Trigger)
- **Rewind** (Trigger)
- **Start** (Number)
- **End** (Number)
- **Duration** (Number)
- **Loop** (Number: Boolean)
- **Wait For Reset** (Number: Boolean)
- **Easing Index** (Number: Integer)

**`\outputsymbol`{=latex} Output Ports:**

- **Next** (Trigger)
- **Result** (Number)
- **Finished** (Number)
- **Finished Trigger** (Trigger)

**Example Patch:** [Open in Editor](https://cables.gl/edit/dOlV9L)

**Docs:** [https://cables.gl/op/Ops.Anim.SimpleAnim](https://cables.gl/op/Ops.Anim.SimpleAnim)

### SineAnim
![SineAnim op](images/ops/Ops_Anim_SineAnim.svg)

**Full Name:** `Ops.Anim.SineAnim`

**Description:** Animation in the form of a sine/cosine curve (sinus/cos)

**`\inputsymbol`{=latex} Input Ports:**

- **Exe** (Trigger)
- **Mode Index** (Number: Integer)
- **Phase** (Number)
- **Frequency** (Number)
- **Amplitude** (Number)

**`\outputsymbol`{=latex} Output Ports:**

- **Trigger Out** (Trigger)
- **Result** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/edit/3bbUfp)

**Docs:** [https://cables.gl/op/Ops.Anim.SineAnim](https://cables.gl/op/Ops.Anim.SineAnim)

### Smooth
![Smooth op](images/ops/Ops_Anim_Smooth.svg)

**Full Name:** `Ops.Anim.Smooth`

**Description:** Smooths out jumps in values (AverageInterpolation)

**`\inputsymbol`{=latex} Input Ports:**

- **Update** (Trigger)
- **Value** (Number)
- **Dec Factor** (Number)

**`\outputsymbol`{=latex} Output Ports:**

- **Next** (Trigger)
- **Result** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/edit/c9gqda)

**Docs:** [https://cables.gl/op/Ops.Anim.Smooth](https://cables.gl/op/Ops.Anim.Smooth)

### Snap
![Snap op](images/ops/Ops_Anim_Snap.svg)

**Full Name:** `Ops.Anim.Snap`

**Description:** Snap at certain points (e.g. while scrolling)

**`\inputsymbol`{=latex} Input Ports:**

- **Delta** (Number)
- **Snap At Values** (Array)
- **Snap Distance** (Number)
- **Snap Distance Release** (Number)
- **Slowdown** (Number)
- **Block Input After Snap** (Number)
- **Reset** (Trigger)
- **Min** (Number)
- **Max** (Number)
- **Value Mul** (Number)
- **Enabled** (Number: Boolean)

**`\outputsymbol`{=latex} Output Ports:**

- **Result** (Number)
- **Distance** (Number)
- **Snapped** (Number)
- **Was Snapped** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/edit/7B11U6)

**Docs:** [https://cables.gl/op/Ops.Anim.Snap](https://cables.gl/op/Ops.Anim.Snap)

### Spring
![Spring op](images/ops/Ops_Anim_Spring.svg)

**Full Name:** `Ops.Anim.Spring`

**Description:** Spring simulation based on input target value.

**`\inputsymbol`{=latex} Input Ports:**

- **Exe** (Trigger)
- **Value** (Number)
- **Damping** (Number)
- **Stiffness** (Number)

**`\outputsymbol`{=latex} Output Ports:**

- **Trigger** (Trigger)
- **Result** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/edit/bsbM2y)

**Docs:** [https://cables.gl/op/Ops.Anim.Spring](https://cables.gl/op/Ops.Anim.Spring)

### StringTypeAnimation_v2
![StringTypeAnimation_v2 op](images/ops/Ops_Anim_StringTypeAnimation_v2.svg)

**Full Name:** `Ops.Anim.StringTypeAnimation_v2`

**Description:** Animates a text/string, like it is being typed out by a person

**`\inputsymbol`{=latex} Input Ports:**

- **Text** (String)
- **Restart** (Trigger)
- **Speed** (Number)
- **Speed Variation** (Number)
- **Show Cursor** (Number: Boolean)

**`\outputsymbol`{=latex} Output Ports:**

- **Result** (String)
- **Changed** (Trigger)
- **Finished** (Trigger)

**Example Patch:** [Open in Editor](https://cables.gl/edit/8dB2eH)

**Docs:** [https://cables.gl/op/Ops.Anim.StringTypeAnimation_v2](https://cables.gl/op/Ops.Anim.StringTypeAnimation_v2)

### TimeDelta
![TimeDelta op](images/ops/Ops_Anim_TimeDelta.svg)

**Full Name:** `Ops.Anim.TimeDelta`

**Description:** Measure the time difference between two triggers

**`\inputsymbol`{=latex} Input Ports:**

- **Exe** (Trigger)
- **Smooth** (Number: Boolean)
- **Seconds** (Number: Boolean)

**`\outputsymbol`{=latex} Output Ports:**

- **Trigger** (Trigger)
- **Result** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/edit/omrKQm)

**Docs:** [https://cables.gl/op/Ops.Anim.TimeDelta](https://cables.gl/op/Ops.Anim.TimeDelta)

### Timer_v2
![Timer_v2 op](images/ops/Ops_Anim_Timer_v2.svg)

**Full Name:** `Ops.Anim.Timer_v2`

**Description:** A timer that can be started, paused and reset by triggering

**`\inputsymbol`{=latex} Input Ports:**

- **Speed** (Number)
- **Play** (Number: Boolean)
- **Reset** (Trigger)
- **Sync To Timeline** (Number: Boolean)

**`\outputsymbol`{=latex} Output Ports:**

- **Time** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/edit/YTuOQm)

**Docs:** [https://cables.gl/op/Ops.Anim.Timer_v2](https://cables.gl/op/Ops.Anim.Timer_v2)


