# Ops.Debug


```{=latex}
\OpsSubsubNoSubsectionNumbering\setcounter{subsubsection}{0}
```
### Console
![Console op](images/ops/Ops_Debug_Console.svg)

**Full Name:** `Ops.Debug.Console`

Shows console log output on the screen.

**`\inputsymbol`{=latex} Inputs**

- **Visible** (Number: Boolean)
- **Clear** (Trigger)

**`\outputsymbol`{=latex} Output**

- **Element** (Object)

**Example Patch:** [cables.gl/edit/TVIL7f](https://cables.gl/edit/TVIL7f)

**Doc:** [cables.gl/op/Ops.Debug.Console](https://cables.gl/op/Ops.Debug.Console)

### ConsoleLog
![ConsoleLog op](images/ops/Ops_Debug_ConsoleLog.svg)

**Full Name:** `Ops.Debug.ConsoleLog`

Log incoming values to the console/dev tools.

**`\inputsymbol`{=latex} Inputs**

- **Number** (Number)
- **String** (String)

**Example Patch:** [cables.gl/op/Ops.Debug.ConsoleLog#example](https://cables.gl/op/Ops.Debug.ConsoleLog#example)

**Doc:** [cables.gl/op/Ops.Debug.ConsoleLog](https://cables.gl/op/Ops.Debug.ConsoleLog)

### CrashOp
![CrashOp op](images/ops/Ops_Debug_CrashOp.svg)

**Full Name:** `Ops.Debug.CrashOp`

Crash the editor in many ways.

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

**Example Patch:** [cables.gl/edit/9TvUBq](https://cables.gl/edit/9TvUBq)

**Doc:** [cables.gl/op/Ops.Debug.CrashOp](https://cables.gl/op/Ops.Debug.CrashOp)

### GlLogErrors
![GlLogErrors op](images/ops/Ops_Debug_GlLogErrors.svg)

**Full Name:** `Ops.Debug.GlLogErrors`

execute glGetError after every gl command and log to browser console.

**`\inputsymbol`{=latex} Inputs**

- **Exec** (Trigger)
- **Limit Error Logs Num** (Number: Integer)
- **Stop Trigger After Limit** (Number: Boolean)
- **Show Gl History** (Trigger)

**`\outputsymbol`{=latex} Output**

- **Next** (Trigger)

**Example Patch:** [cables.gl/op/Ops.Debug.GlLogErrors#example](https://cables.gl/op/Ops.Debug.GlLogErrors#example)

**Doc:** [cables.gl/op/Ops.Debug.GlLogErrors](https://cables.gl/op/Ops.Debug.GlLogErrors)

### GlStates
![GlStates op](images/ops/Ops_Debug_GlStates.svg)

**Full Name:** `Ops.Debug.GlStates`

see current gl states and error message.

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

**Example Patch:** [cables.gl/op/Ops.Debug.GlStates#example](https://cables.gl/op/Ops.Debug.GlStates#example)

**Doc:** [cables.gl/op/Ops.Debug.GlStates](https://cables.gl/op/Ops.Debug.GlStates)

### ProfileGL
![ProfileGL op](images/ops/Ops_Debug_ProfileGL.svg)

**Full Name:** `Ops.Debug.ProfileGL`

dump all gl commands of one frame to console.

**`\inputsymbol`{=latex} Inputs**

- **Exec** (Trigger)
- **Debug One Frame** (Trigger)

**`\outputsymbol`{=latex} Output**

- **Next** (Trigger)

**Example Patch:** [cables.gl/op/Ops.Debug.ProfileGL#example](https://cables.gl/op/Ops.Debug.ProfileGL#example)

**Doc:** [cables.gl/op/Ops.Debug.ProfileGL](https://cables.gl/op/Ops.Debug.ProfileGL)

### StopWatch
![StopWatch op](images/ops/Ops_Debug_StopWatch.svg)

**Full Name:** `Ops.Debug.StopWatch`

Measure the time used to render all child nodes in milliseconds.

**`\inputsymbol`{=latex} Inputs**

- **Exec** (Trigger)

**`\outputsymbol`{=latex} Output**

- **Next** (Trigger)
- **Time Used** (Number)
- **Times** (Array)

**Example Patch:** [cables.gl/op/Ops.Debug.StopWatch#example](https://cables.gl/op/Ops.Debug.StopWatch#example)

**Doc:** [cables.gl/op/Ops.Debug.StopWatch](https://cables.gl/op/Ops.Debug.StopWatch)


