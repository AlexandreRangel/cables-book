# Ops.Debug


```{=latex}
\OpsSubsubNoSubsectionNumbering\setcounter{subsubsection}{0}
```
### Console
![Console op](images/ops/Ops_Debug_Console.svg)

**Full Name:** `Ops.Debug.Console`

**Description:** Shows console log output on the screen

**`\inputsymbol`{=latex} Inputs**

- **Visible** (Number: Boolean)
- **Clear** (Trigger)

**`\outputsymbol`{=latex} Output**

- **Element** (Object)

**Example Patch:** [Open in Editor](https://cables.gl/edit/TVIL7f)

**Docs:** [https://cables.gl/op/Ops.Debug.Console](https://cables.gl/op/Ops.Debug.Console)

### ConsoleLog
![ConsoleLog op](images/ops/Ops_Debug_ConsoleLog.svg)

**Full Name:** `Ops.Debug.ConsoleLog`

**Description:** Log incoming values to the console/dev tools

**`\inputsymbol`{=latex} Inputs**

- **Number** (Number)
- **String** (String)

**`\outputsymbol`{=latex} Output**

- *Visit [Ops.Debug.ConsoleLog documentation](https://cables.gl/op/Ops.Debug.ConsoleLog) for output port details*

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Debug.ConsoleLog#example)

**Docs:** [https://cables.gl/op/Ops.Debug.ConsoleLog](https://cables.gl/op/Ops.Debug.ConsoleLog)

### CrashOp
![CrashOp op](images/ops/Ops_Debug_CrashOp.svg)

**Full Name:** `Ops.Debug.CrashOp`

**Description:** Crash the editor in many ways

**`\inputsymbol`{=latex} Inputs**

- **Async Crash** (Trigger)
- **Undefined Crash** (Trigger)
- **Throw Exception** (Trigger)
- **Float** (Number)
- **Array Exception** (Trigger)
- **Promise Fail** (Trigger)
- **Shader Error** (Trigger)

**`\outputsymbol`{=latex} Output**

- **NaN** (Number)
- **Infinity** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/edit/9TvUBq)

**Docs:** [https://cables.gl/op/Ops.Debug.CrashOp](https://cables.gl/op/Ops.Debug.CrashOp)

### GlLogErrors
![GlLogErrors op](images/ops/Ops_Debug_GlLogErrors.svg)

**Full Name:** `Ops.Debug.GlLogErrors`

**Description:** execute glGetError after every gl command and log to browser console

**`\inputsymbol`{=latex} Inputs**

- **Exec** (Trigger)
- **Limit Error Logs Num** (Number: Integer)
- **Stop Trigger After Limit** (Number: Boolean)
- **Show Gl History** (Trigger)

**`\outputsymbol`{=latex} Output**

- **Next** (Trigger)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Debug.GlLogErrors#example)

**Docs:** [https://cables.gl/op/Ops.Debug.GlLogErrors](https://cables.gl/op/Ops.Debug.GlLogErrors)

### GlStates
![GlStates op](images/ops/Ops_Debug_GlStates.svg)

**Full Name:** `Ops.Debug.GlStates`

**Description:** see current gl states and error message

**`\inputsymbol`{=latex} Inputs**

- **Update** (Trigger)

**`\outputsymbol`{=latex} Output**

- **Next** (Trigger)
- **GlGetError** (Number)
- **Depthtest** (Number)
- **Stack Depthtest** (Number)
- **Depth Writing** (Number)
- **Stack Depth Writing** (Number)
- **DepthFunc** (Number)
- **Stack DepthFunc** (Number)
- **Blend** (Number)
- **Blend Stack** (Number)
- **Cull Mode** (Number)
- **Face Culling** (Number)
- **Is Shadowpass** (booleanNumber)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Debug.GlStates#example)

**Docs:** [https://cables.gl/op/Ops.Debug.GlStates](https://cables.gl/op/Ops.Debug.GlStates)

### ProfileGL
![ProfileGL op](images/ops/Ops_Debug_ProfileGL.svg)

**Full Name:** `Ops.Debug.ProfileGL`

**Description:** dump all gl commands of one frame to console

**`\inputsymbol`{=latex} Inputs**

- **Exec** (Trigger)
- **Debug One Frame** (Trigger)

**`\outputsymbol`{=latex} Output**

- **Next** (Trigger)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Debug.ProfileGL#example)

**Docs:** [https://cables.gl/op/Ops.Debug.ProfileGL](https://cables.gl/op/Ops.Debug.ProfileGL)

### StopWatch
![StopWatch op](images/ops/Ops_Debug_StopWatch.svg)

**Full Name:** `Ops.Debug.StopWatch`

**Description:** Measure the time used to render all child nodes in milliseconds

**`\inputsymbol`{=latex} Inputs**

- **Exec** (Trigger)

**`\outputsymbol`{=latex} Output**

- **Next** (Trigger)
- **Time Used** (Number)
- **Times** (Array)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Debug.StopWatch#example)

**Docs:** [https://cables.gl/op/Ops.Debug.StopWatch](https://cables.gl/op/Ops.Debug.StopWatch)


