# Ops.TimeLine

---

## Ops.TimeLine

### Anim
![Anim op](images/ops/Ops_TimeLine_Anim.svg)

**Full Name:** `Ops.TimeLine.Anim`

**Description:** timeline keyframable animation object

**> Input Ports:**

- **Value** (Number)
- **Clip** (Number: Boolean)
- **Clip Name** (String)

**< Output Ports:**

- **Anim** (Object)
- **Loop Length** (Number)
- **Length** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/edit/sKguKJ)

**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "Anim"*

**Docs:** [https://cables.gl/op/Ops.TimeLine.Anim](https://cables.gl/op/Ops.TimeLine.Anim)


### AnimGetKey
![AnimGetKey op](images/ops/Ops_TimeLine_AnimGetKey.svg)

**Full Name:** `Ops.TimeLine.AnimGetKey`

**Description:** Get data from a single key in an animation

**> Input Ports:**

- **Anim** (Object)
- **Time** (Number)

**< Output Ports:**

- **Index** (Number)
- **Key Value** (Number)
- **Key Time** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/edit/gXgDz1)

**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "AnimGetKey"*

**Docs:** [https://cables.gl/op/Ops.TimeLine.AnimGetKey](https://cables.gl/op/Ops.TimeLine.AnimGetKey)


### AnimGetValue
![AnimGetValue op](images/ops/Ops_TimeLine_AnimGetValue.svg)

**Full Name:** `Ops.TimeLine.AnimGetValue`

**Description:** get the animated value at time x of an animation object

**> Input Ports:**

- **Anim** (Object)
- **Time** (Number)

**< Output Ports:**

- **Value** (Number)
- **Loop** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/edit/yEIpR1)

**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "AnimGetValue"*

**Docs:** [https://cables.gl/op/Ops.TimeLine.AnimGetValue](https://cables.gl/op/Ops.TimeLine.AnimGetValue)


### AnimInfo
![AnimInfo op](images/ops/Ops_TimeLine_AnimInfo.svg)

**Full Name:** `Ops.TimeLine.AnimInfo`

**Description:** Get information about an anim object

**> Input Ports:**

- **Anim** (Object)

**< Output Ports:**

- **Total Keys** (Number)
- **Length Seconds** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.TimeLine.AnimInfo#example)

**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "AnimInfo"*

**Docs:** [https://cables.gl/op/Ops.TimeLine.AnimInfo](https://cables.gl/op/Ops.TimeLine.AnimInfo)


### AutoPlay
![AutoPlay op](images/ops/Ops_TimeLine_AutoPlay.svg)

**Full Name:** `Ops.TimeLine.AutoPlay`

**Description:** Automatically starts the timeline playback when opening patch

**> Input Ports:**

- *Visit [Ops.TimeLine.AutoPlay documentation](https://cables.gl/op/Ops.TimeLine.AutoPlay) for input port details*

**< Output Ports:**

- *Visit [Ops.TimeLine.AutoPlay documentation](https://cables.gl/op/Ops.TimeLine.AutoPlay) for output port details*

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.TimeLine.AutoPlay#example)

**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "AutoPlay"*

**Docs:** [https://cables.gl/op/Ops.TimeLine.AutoPlay](https://cables.gl/op/Ops.TimeLine.AutoPlay)


### DemoPrerender
![DemoPrerender op](images/ops/Ops_TimeLine_DemoPrerender.svg)

**Full Name:** `Ops.TimeLine.DemoPrerender`

**Description:** Prerenderer based on timeline progress

**> Input Ports:**

- **Render** (Trigger)
- **Manual Timestamps** (Array)
- **Record Events** (Number: Boolean)
- **Reset** (Trigger)
- **Clear** (Trigger)
- **ReRender On Resize** (Number: Boolean)

**< Output Ports:**

- **Next** (Trigger)
- **Prerendered Frame** (Trigger)
- **Progress** (Number)
- **Num Events** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/edit/sewM2h)

**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "DemoPrerender"*

**Docs:** [https://cables.gl/op/Ops.TimeLine.DemoPrerender](https://cables.gl/op/Ops.TimeLine.DemoPrerender)


### GotoFrame
![GotoFrame op](images/ops/Ops_TimeLine_GotoFrame.svg)

**Full Name:** `Ops.TimeLine.GotoFrame`

**Description:** jump to a key in the timeline

**> Input Ports:**

- **Frame** (Number)

**< Output Ports:**

- *Visit [Ops.TimeLine.GotoFrame documentation](https://cables.gl/op/Ops.TimeLine.GotoFrame) for output port details*

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.TimeLine.GotoFrame#example)

**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "GotoFrame"*

**Docs:** [https://cables.gl/op/Ops.TimeLine.GotoFrame](https://cables.gl/op/Ops.TimeLine.GotoFrame)


### PreRender
![PreRender op](images/ops/Ops_TimeLine_PreRender.svg)

**Full Name:** `Ops.TimeLine.PreRender`

**Description:** Render the patch at certain times

**> Input Ports:**

- **Render** (Trigger)
- **Max Time** (Number: Integer)
- **Step** (Number: Integer)
- **Reset** (Trigger)

**< Output Ports:**

- **Next** (Trigger)
- **Render Progress** (Trigger)
- **Done** (Trigger)
- **Progress** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.TimeLine.PreRender#example)

**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "PreRender"*

**Docs:** [https://cables.gl/op/Ops.TimeLine.PreRender](https://cables.gl/op/Ops.TimeLine.PreRender)


### TimelineConfig
![TimelineConfig op](images/ops/Ops_TimeLine_TimelineConfig.svg)

**Full Name:** `Ops.TimeLine.TimelineConfig`

**Description:** configure the timeline for the current patch

**> Input Ports:**

- **FPS** (Number: Integer)
- **Restrict To Frames** (Number: Boolean)
- **Fade In Frames** (Number: Boolean)

**< Output Ports:**

- **Duration Seconds** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.TimeLine.TimelineConfig#example)

**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "TimelineConfig"*

**Docs:** [https://cables.gl/op/Ops.TimeLine.TimelineConfig](https://cables.gl/op/Ops.TimeLine.TimelineConfig)


### TimeLineControls
![TimeLineControls op](images/ops/Ops_TimeLine_TimeLineControls.svg)

**Full Name:** `Ops.TimeLine.TimeLineControls`

**Description:** use position and play pause state of cables timeline

**> Input Ports:**

- *Visit [Ops.TimeLine.TimeLineControls documentation](https://cables.gl/op/Ops.TimeLine.TimeLineControls) for input port details*

**< Output Ports:**

- **Time** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.TimeLine.TimeLineControls#example)

**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "TimeLineControls"*

**Docs:** [https://cables.gl/op/Ops.TimeLine.TimeLineControls](https://cables.gl/op/Ops.TimeLine.TimeLineControls)


### TimelineDebug
![TimelineDebug op](images/ops/Ops_TimeLine_TimelineDebug.svg)

**Full Name:** `Ops.TimeLine.TimelineDebug`

**Description:** *Visit [documentation](https://cables.gl/op/Ops.TimeLine.TimelineDebug) for details*

**> Input Ports:**

- **Update** (Trigger)

**< Output Ports:**

- **Data** (Object)
- **Time Cursor** (Number)
- **Visible Duration** (Number)
- **Visible Time Start** (Number)
- **Loop Start** (Number)
- **Loop End** (Number)
- **Num Selected Keys** (Number)
- **Selected Values Min** (Number)
- **Selected Values Max** (Number)
- **Selected Times Min** (Number)
- **Selected Times Max** (Number)
- **Selected Keys** (Array)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.TimeLine.TimelineDebug#example)

**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "TimelineDebug"*

**Docs:** [https://cables.gl/op/Ops.TimeLine.TimelineDebug](https://cables.gl/op/Ops.TimeLine.TimelineDebug)


### TimeLineFrame
![TimeLineFrame op](images/ops/Ops_TimeLine_TimeLineFrame.svg)

**Full Name:** `Ops.TimeLine.TimeLineFrame`

**Description:** Returns the current frame number of the timeline

**> Input Ports:**

- *Visit [Ops.TimeLine.TimeLineFrame documentation](https://cables.gl/op/Ops.TimeLine.TimeLineFrame) for input port details*

**< Output Ports:**

- **Time** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.TimeLine.TimeLineFrame#example)

**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "TimeLineFrame"*

**Docs:** [https://cables.gl/op/Ops.TimeLine.TimeLineFrame](https://cables.gl/op/Ops.TimeLine.TimeLineFrame)


### TimeLineLength
![TimeLineLength op](images/ops/Ops_TimeLine_TimeLineLength.svg)

**Full Name:** `Ops.TimeLine.TimeLineLength`

**Description:** current set length of the timeline

**> Input Ports:**

- **Update** (Trigger)

**< Output Ports:**

- **Length** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/edit/qSMdck)

**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "TimeLineLength"*

**Docs:** [https://cables.gl/op/Ops.TimeLine.TimeLineLength](https://cables.gl/op/Ops.TimeLine.TimeLineLength)


### TimeLineLoop
![TimeLineLoop op](images/ops/Ops_TimeLine_TimeLineLoop.svg)

**Full Name:** `Ops.TimeLine.TimeLineLoop`

**Description:** Automatic rewind of timeline at a certain time

**> Input Ports:**

- **Execute** (Trigger)
- **Duration** (Number)
- **How long the loop should be** (in seconds)

**< Output Ports:**

- **Trigger** (Trigger)

**Example Patch:** [Open in Editor](https://cables.gl/edit/GbEqL-)

**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "TimeLineLoop"*

**Docs:** [https://cables.gl/op/Ops.TimeLine.TimeLineLoop](https://cables.gl/op/Ops.TimeLine.TimeLineLoop)


### TimeLineOverwrite
![TimeLineOverwrite op](images/ops/Ops_TimeLine_TimeLineOverwrite.svg)

**Full Name:** `Ops.TimeLine.TimeLineOverwrite`

**Description:** overwrite timeline time value

**> Input Ports:**

- **Exe** (Trigger)
- **New Time** (Number)

**< Output Ports:**

- **Trigger** (Trigger)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.TimeLine.TimeLineOverwrite#example)

**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "TimeLineOverwrite"*

**Docs:** [https://cables.gl/op/Ops.TimeLine.TimeLineOverwrite](https://cables.gl/op/Ops.TimeLine.TimeLineOverwrite)


### TimeLinePlay
![TimeLinePlay op](images/ops/Ops_TimeLine_TimeLinePlay.svg)

**Full Name:** `Ops.TimeLine.TimeLinePlay`

**Description:** *Visit [documentation](https://cables.gl/op/Ops.TimeLine.TimeLinePlay) for details*

**> Input Ports:**

- **Play** (Trigger)
- **Pause** (Trigger)

**< Output Ports:**

- **Next** (Trigger)

**Example Patch:** [Open in Editor](https://cables.gl/edit/3F6DOe)

**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "TimeLinePlay"*

**Docs:** [https://cables.gl/op/Ops.TimeLine.TimeLinePlay](https://cables.gl/op/Ops.TimeLine.TimeLinePlay)


### TimeLinePlayer
![TimeLinePlayer op](images/ops/Ops_TimeLine_TimeLinePlayer.svg)

**Full Name:** `Ops.TimeLine.TimeLinePlayer`

**Description:** Player controls for the timeline

**> Input Ports:**

- **Play** (Trigger)
- **Pause** (Trigger)
- **Rewind** (Trigger)
- **Set Current Time** (Number)

**< Output Ports:**

- **Play Trigger** (Trigger)
- **Pause Trigger** (Trigger)
- **Rewind Trigger** (Trigger)
- **Is Playing** (booleanNumber)
- **Current Time** (Number)
- **Current Frame** (Number)
- **Current time in frames** (30fps)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.TimeLine.TimeLinePlayer#example)

**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "TimeLinePlayer"*

**Docs:** [https://cables.gl/op/Ops.TimeLine.TimeLinePlayer](https://cables.gl/op/Ops.TimeLine.TimeLinePlayer)


### TimeLineRewind
![TimeLineRewind op](images/ops/Ops_TimeLine_TimeLineRewind.svg)

**Full Name:** `Ops.TimeLine.TimeLineRewind`

**Description:** set time of timeline to 0 (rewind, restart)

**> Input Ports:**

- **Exe** (Trigger)

**< Output Ports:**

- **Next** (Trigger)

**Example Patch:** [Open in Editor](https://cables.gl/edit/3F6DOe)

**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "TimeLineRewind"*

**Docs:** [https://cables.gl/op/Ops.TimeLine.TimeLineRewind](https://cables.gl/op/Ops.TimeLine.TimeLineRewind)


### TimeLineSetTime
![TimeLineSetTime op](images/ops/Ops_TimeLine_TimeLineSetTime.svg)

**Full Name:** `Ops.TimeLine.TimeLineSetTime`

**Description:** set current time of timeline

**> Input Ports:**

- **Update** (Trigger)
- **Time** (Number)

**< Output Ports:**

- **Next** (Trigger)

**Example Patch:** [Open in Editor](https://cables.gl/edit/3F6DOe)

**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "TimeLineSetTime"*

**Docs:** [https://cables.gl/op/Ops.TimeLine.TimeLineSetTime](https://cables.gl/op/Ops.TimeLine.TimeLineSetTime)


### TimeLineTime
![TimeLineTime op](images/ops/Ops_TimeLine_TimeLineTime.svg)

**Full Name:** `Ops.TimeLine.TimeLineTime`

**Description:** Returns the current time of the timeline

**> Input Ports:**

- *Visit [Ops.TimeLine.TimeLineTime documentation](https://cables.gl/op/Ops.TimeLine.TimeLineTime) for input port details*

**< Output Ports:**

- **Time** (Number)
- **The current time of the timeline** (in seconds)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.TimeLine.TimeLineTime#example)

**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "TimeLineTime"*

**Docs:** [https://cables.gl/op/Ops.TimeLine.TimeLineTime](https://cables.gl/op/Ops.TimeLine.TimeLineTime)


### TimeLineTogglePlay
![TimeLineTogglePlay op](images/ops/Ops_TimeLine_TimeLineTogglePlay.svg)

**Full Name:** `Ops.TimeLine.TimeLineTogglePlay`

**Description:** toggle between timeline playing and being paused

**> Input Ports:**

- **Play** (Number: Boolean)
- **Public** (20): MY IDENTITY PATTERN

**< Output Ports:**

- *Visit [Ops.TimeLine.TimeLineTogglePlay documentation](https://cables.gl/op/Ops.TimeLine.TimeLineTogglePlay) for output port details*

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.TimeLine.TimeLineTogglePlay#example)

**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "TimeLineTogglePlay"*

**Docs:** [https://cables.gl/op/Ops.TimeLine.TimeLineTogglePlay](https://cables.gl/op/Ops.TimeLine.TimeLineTogglePlay)


### TimelineValue
![TimelineValue op](images/ops/Ops_TimeLine_TimelineValue.svg)

**Full Name:** `Ops.TimeLine.TimelineValue`

**Description:** Animate and get value at "time" of timeline

**> Input Ports:**

- **Time** (Number)
- **Value** (Number)
- **Unit Index** (Number: Integer)

**< Output Ports:**

- **Result** (Number)
- **Anim Array** (Array)
- **Anim Finished** (booleanNumber)

**Example Patch:** [Open in Editor](https://cables.gl/edit/xAg8P6)

**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "TimelineValue"*

**Docs:** [https://cables.gl/op/Ops.TimeLine.TimelineValue](https://cables.gl/op/Ops.TimeLine.TimelineValue)


