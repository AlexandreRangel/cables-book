# Ops.TimeLine

*Part of the [All Operators Reference](13-_AllOps.md)*

---

## Ops.TimeLine

### Anim
![Anim op](images/ops/Ops_TimeLine_Anim.svg)

**Full Name:** `Ops.TimeLine.Anim`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.TimeLine.Anim) for details*

**> Input Ports:**
- **Value** (Number)
- **Clip** (Number: Boolean)
- **Clip Name** (String)

**< Output Ports:**
- **Anim** (Object)
- **Loop Length** (Number)
- **Length** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.TimeLine.Anim#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "Anim"*
**Docs:** [https://cables.gl/op/Ops.TimeLine.Anim](https://cables.gl/op/Ops.TimeLine.Anim)

---

### AnimGetKey
![AnimGetKey op](images/ops/Ops_TimeLine_AnimGetKey.svg)

**Full Name:** `Ops.TimeLine.AnimGetKey`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.TimeLine.AnimGetKey) for details*

**> Input Ports:**
- **Anim** (Object)
- **Time** (Number)

**< Output Ports:**
- **Index** (Number)
- **Key Value** (Number)
- **Key Time** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.TimeLine.AnimGetKey#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "AnimGetKey"*
**Docs:** [https://cables.gl/op/Ops.TimeLine.AnimGetKey](https://cables.gl/op/Ops.TimeLine.AnimGetKey)

---

### AnimGetValue
![AnimGetValue op](images/ops/Ops_TimeLine_AnimGetValue.svg)

**Full Name:** `Ops.TimeLine.AnimGetValue`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.TimeLine.AnimGetValue) for details*

**> Input Ports:**
- **Anim** (Object)
- **Time** (Number)

**< Output Ports:**
- **Value** (Number)
- **Loop** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.TimeLine.AnimGetValue#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "AnimGetValue"*
**Docs:** [https://cables.gl/op/Ops.TimeLine.AnimGetValue](https://cables.gl/op/Ops.TimeLine.AnimGetValue)

---

### AnimInfo
![AnimInfo op](images/ops/Ops_TimeLine_AnimInfo.svg)

**Full Name:** `Ops.TimeLine.AnimInfo`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.TimeLine.AnimInfo) for details*

**> Input Ports:**
- **Anim** (Object)

**< Output Ports:**
- **Total Keys** (Number)
- **Length Seconds** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.TimeLine.AnimInfo#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "AnimInfo"*
**Docs:** [https://cables.gl/op/Ops.TimeLine.AnimInfo](https://cables.gl/op/Ops.TimeLine.AnimInfo)

---

### AutoPlay
![AutoPlay op](images/ops/Ops_TimeLine_AutoPlay.svg)

**Full Name:** `Ops.TimeLine.AutoPlay`

**Description:** *Visit [documentation](https://cables.gl/op/Ops.TimeLine.AutoPlay) for details*

**> Input Ports:**
- *Visit [Ops.TimeLine.AutoPlay documentation](https://cables.gl/op/Ops.TimeLine.AutoPlay) for input port details*

**< Output Ports:**
- *Visit [Ops.TimeLine.AutoPlay documentation](https://cables.gl/op/Ops.TimeLine.AutoPlay) for output port details*

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.TimeLine.AutoPlay#example)

**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "AutoPlay"*

**Docs:** [https://cables.gl/op/Ops.TimeLine.AutoPlay](https://cables.gl/op/Ops.TimeLine.AutoPlay)

---

### DemoPrerender
![DemoPrerender op](images/ops/Ops_TimeLine_DemoPrerender.svg)

**Full Name:** `Ops.TimeLine.DemoPrerender`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.TimeLine.DemoPrerender) for details*

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

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.TimeLine.DemoPrerender#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "DemoPrerender"*
**Docs:** [https://cables.gl/op/Ops.TimeLine.DemoPrerender](https://cables.gl/op/Ops.TimeLine.DemoPrerender)

---

### GotoFrame
![GotoFrame op](images/ops/Ops_TimeLine_GotoFrame.svg)

**Full Name:** `Ops.TimeLine.GotoFrame`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.TimeLine.GotoFrame) for details*

**> Input Ports:**
- **Frame** (Number)

**< Output Ports:**
- *Visit [Ops.TimeLine.GotoFrame documentation](https://cables.gl/op/Ops.TimeLine.GotoFrame) for output port details*

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.TimeLine.GotoFrame#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "GotoFrame"*
**Docs:** [https://cables.gl/op/Ops.TimeLine.GotoFrame](https://cables.gl/op/Ops.TimeLine.GotoFrame)

---

### PreRender
![PreRender op](images/ops/Ops_TimeLine_PreRender.svg)

**Full Name:** `Ops.TimeLine.PreRender`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.TimeLine.PreRender) for details*

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

---

### TimelineConfig
![TimelineConfig op](images/ops/Ops_TimeLine_TimelineConfig.svg)

**Full Name:** `Ops.TimeLine.TimelineConfig`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.TimeLine.TimelineConfig) for details*

**> Input Ports:**
- **FPS** (Number: Integer)
- **Restrict To Frames** (Number: Boolean)
- **Fade In Frames** (Number: Boolean)

**< Output Ports:**
- **Duration Seconds** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.TimeLine.TimelineConfig#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "TimelineConfig"*
**Docs:** [https://cables.gl/op/Ops.TimeLine.TimelineConfig](https://cables.gl/op/Ops.TimeLine.TimelineConfig)

---

### TimeLineControls
![TimeLineControls op](images/ops/Ops_TimeLine_TimeLineControls.svg)

**Full Name:** `Ops.TimeLine.TimeLineControls`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.TimeLine.TimeLineControls) for details*

**> Input Ports:**
- *Visit [Ops.TimeLine.TimeLineControls documentation](https://cables.gl/op/Ops.TimeLine.TimeLineControls) for input port details*

**< Output Ports:**
- **Time** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.TimeLine.TimeLineControls#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "TimeLineControls"*
**Docs:** [https://cables.gl/op/Ops.TimeLine.TimeLineControls](https://cables.gl/op/Ops.TimeLine.TimeLineControls)

---

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

---

### TimeLineFrame
![TimeLineFrame op](images/ops/Ops_TimeLine_TimeLineFrame.svg)

**Full Name:** `Ops.TimeLine.TimeLineFrame`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.TimeLine.TimeLineFrame) for details*

**> Input Ports:**
- *Visit [Ops.TimeLine.TimeLineFrame documentation](https://cables.gl/op/Ops.TimeLine.TimeLineFrame) for input port details*

**< Output Ports:**
- **Time** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.TimeLine.TimeLineFrame#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "TimeLineFrame"*
**Docs:** [https://cables.gl/op/Ops.TimeLine.TimeLineFrame](https://cables.gl/op/Ops.TimeLine.TimeLineFrame)

---

### TimeLineLength
![TimeLineLength op](images/ops/Ops_TimeLine_TimeLineLength.svg)

**Full Name:** `Ops.TimeLine.TimeLineLength`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.TimeLine.TimeLineLength) for details*

**> Input Ports:**
- **Update** (Trigger)

**< Output Ports:**
- **Length** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.TimeLine.TimeLineLength#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "TimeLineLength"*
**Docs:** [https://cables.gl/op/Ops.TimeLine.TimeLineLength](https://cables.gl/op/Ops.TimeLine.TimeLineLength)

---

### TimeLineLoop
![TimeLineLoop op](images/ops/Ops_TimeLine_TimeLineLoop.svg)

**Full Name:** `Ops.TimeLine.TimeLineLoop`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.TimeLine.TimeLineLoop) for details*

**> Input Ports:**
- **Execute** (Trigger)
- **Duration** (Number)
- **How long the loop should be** (in seconds)

**< Output Ports:**
- **Trigger** (Trigger)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.TimeLine.TimeLineLoop#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "TimeLineLoop"*
**Docs:** [https://cables.gl/op/Ops.TimeLine.TimeLineLoop](https://cables.gl/op/Ops.TimeLine.TimeLineLoop)

---

### TimeLineOverwrite
![TimeLineOverwrite op](images/ops/Ops_TimeLine_TimeLineOverwrite.svg)

**Full Name:** `Ops.TimeLine.TimeLineOverwrite`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.TimeLine.TimeLineOverwrite) for details*

**> Input Ports:**
- **Exe** (Trigger)
- **New Time** (Number)

**< Output Ports:**
- **Trigger** (Trigger)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.TimeLine.TimeLineOverwrite#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "TimeLineOverwrite"*
**Docs:** [https://cables.gl/op/Ops.TimeLine.TimeLineOverwrite](https://cables.gl/op/Ops.TimeLine.TimeLineOverwrite)

---

### TimeLinePlay
![TimeLinePlay op](images/ops/Ops_TimeLine_TimeLinePlay.svg)

**Full Name:** `Ops.TimeLine.TimeLinePlay`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.TimeLine.TimeLinePlay) for details*

**> Input Ports:**
- **Play** (Trigger)
- **Pause** (Trigger)

**< Output Ports:**
- **Next** (Trigger)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.TimeLine.TimeLinePlay#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "TimeLinePlay"*
**Docs:** [https://cables.gl/op/Ops.TimeLine.TimeLinePlay](https://cables.gl/op/Ops.TimeLine.TimeLinePlay)

---

### TimeLinePlayer
![TimeLinePlayer op](images/ops/Ops_TimeLine_TimeLinePlayer.svg)

**Full Name:** `Ops.TimeLine.TimeLinePlayer`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.TimeLine.TimeLinePlayer) for details*

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

---

### TimeLineRewind
![TimeLineRewind op](images/ops/Ops_TimeLine_TimeLineRewind.svg)

**Full Name:** `Ops.TimeLine.TimeLineRewind`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.TimeLine.TimeLineRewind) for details*

**> Input Ports:**
- **Exe** (Trigger)

**< Output Ports:**
- **Next** (Trigger)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.TimeLine.TimeLineRewind#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "TimeLineRewind"*
**Docs:** [https://cables.gl/op/Ops.TimeLine.TimeLineRewind](https://cables.gl/op/Ops.TimeLine.TimeLineRewind)

---

### TimeLineSetTime
![TimeLineSetTime op](images/ops/Ops_TimeLine_TimeLineSetTime.svg)

**Full Name:** `Ops.TimeLine.TimeLineSetTime`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.TimeLine.TimeLineSetTime) for details*

**> Input Ports:**
- **Update** (Trigger)
- **Time** (Number)

**< Output Ports:**
- **Next** (Trigger)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.TimeLine.TimeLineSetTime#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "TimeLineSetTime"*
**Docs:** [https://cables.gl/op/Ops.TimeLine.TimeLineSetTime](https://cables.gl/op/Ops.TimeLine.TimeLineSetTime)

---

### TimeLineTime
![TimeLineTime op](images/ops/Ops_TimeLine_TimeLineTime.svg)

**Full Name:** `Ops.TimeLine.TimeLineTime`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.TimeLine.TimeLineTime) for details*

**> Input Ports:**
- *Visit [Ops.TimeLine.TimeLineTime documentation](https://cables.gl/op/Ops.TimeLine.TimeLineTime) for input port details*

**< Output Ports:**
- **Time** (Number)
- **The current time of the timeline** (in seconds)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.TimeLine.TimeLineTime#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "TimeLineTime"*
**Docs:** [https://cables.gl/op/Ops.TimeLine.TimeLineTime](https://cables.gl/op/Ops.TimeLine.TimeLineTime)

---

### TimeLineTogglePlay
![TimeLineTogglePlay op](images/ops/Ops_TimeLine_TimeLineTogglePlay.svg)

**Full Name:** `Ops.TimeLine.TimeLineTogglePlay`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.TimeLine.TimeLineTogglePlay) for details*

**> Input Ports:**
- **Play** (Number: Boolean)
- **Public** (20): MY IDENTITY PATTERN

**< Output Ports:**
- *Visit [Ops.TimeLine.TimeLineTogglePlay documentation](https://cables.gl/op/Ops.TimeLine.TimeLineTogglePlay) for output port details*

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.TimeLine.TimeLineTogglePlay#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "TimeLineTogglePlay"*
**Docs:** [https://cables.gl/op/Ops.TimeLine.TimeLineTogglePlay](https://cables.gl/op/Ops.TimeLine.TimeLineTogglePlay)

---

### TimelineValue
![TimelineValue op](images/ops/Ops_TimeLine_TimelineValue.svg)

**Full Name:** `Ops.TimeLine.TimelineValue`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.TimeLine.TimelineValue) for details*

**> Input Ports:**
- **Time** (Number)
- **Value** (Number)
- **Unit Index** (Number: Integer)

**< Output Ports:**
- **Result** (Number)
- **Anim Array** (Array)
- **Anim Finished** (booleanNumber)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.TimeLine.TimelineValue#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "TimelineValue"*
**Docs:** [https://cables.gl/op/Ops.TimeLine.TimelineValue](https://cables.gl/op/Ops.TimeLine.TimelineValue)

---

