# Ops.Number


```{=latex}
\OpsSubsubNoSubsectionNumbering\setcounter{subsubsection}{0}
```
### DelayedNumber
![DelayedNumber op](images/ops/Ops_Number_DelayedNumber.svg)

**Full Name:** `Ops.Number.DelayedNumber`

delay a value by seconds.

**`\inputsymbol`{=latex} Inputs**

- **Update** (Trigger)
- **Value** (Number)
- **Delay** (Number)
- **Clear On Change** (Number: Boolean)
- **Easing Index** (Number: Integer)

**`\outputsymbol`{=latex} Output**

- **Result** (Number)

**Example Patch:** [cables.gl/op/Ops.Number.DelayedNumber#example](https://cables.gl/op/Ops.Number.DelayedNumber#example)

**Doc:** [cables.gl/op/Ops.Number.DelayedNumber](https://cables.gl/op/Ops.Number.DelayedNumber)

### DelayNumberSimple
![DelayNumberSimple op](images/ops/Ops_Number_DelayNumberSimple.svg)

**Full Name:** `Ops.Number.DelayNumberSimple`

delay the value data flow by x seconds.

**`\inputsymbol`{=latex} Inputs**

- **Value** (Number)
- **Delay** (Number)

**`\outputsymbol`{=latex} Output**

- **Out Value** (Number)

**Example Patch:** [cables.gl/op/Ops.Number.DelayNumberSimple#example](https://cables.gl/op/Ops.Number.DelayNumberSimple#example)

**Doc:** [cables.gl/op/Ops.Number.DelayNumberSimple](https://cables.gl/op/Ops.Number.DelayNumberSimple)

### FilterValidNumber
![FilterValidNumber op](images/ops/Ops_Number_FilterValidNumber.svg)

**Full Name:** `Ops.Number.FilterValidNumber`

Filter valid numbers.

**`\inputsymbol`{=latex} Inputs**

- **Number** (Number)
- **Invalid When 0** (Number: Boolean)

**`\outputsymbol`{=latex} Output**

- **Last Valid Number** (Number)
- **Is Valid** (booleanNumber)

**Example Patch:** [cables.gl/op/Ops.Number.FilterValidNumber#example](https://cables.gl/op/Ops.Number.FilterValidNumber#example)

**Doc:** [cables.gl/op/Ops.Number.FilterValidNumber](https://cables.gl/op/Ops.Number.FilterValidNumber)

### FreezeNumber
![FreezeNumber op](images/ops/Ops_Number_FreezeNumber.svg)

**Full Name:** `Ops.Number.FreezeNumber`

capture the current input and copy it to the output, even after a reload.

**`\inputsymbol`{=latex} Inputs**

- **Number** (Number)
- **Button** (Trigger)

**`\outputsymbol`{=latex} Output**

- **Frozen Number** (Number)

**Example Patch:** [cables.gl/edit/MuPepX](https://cables.gl/edit/MuPepX)

**Doc:** [cables.gl/op/Ops.Number.FreezeNumber](https://cables.gl/op/Ops.Number.FreezeNumber)

### GateNumber
![GateNumber op](images/ops/Ops_Number_GateNumber.svg)

**Full Name:** `Ops.Number.GateNumber`

Let’s a number through only if control bool is true, like a gate.

**`\inputsymbol`{=latex} Inputs**

- **Value In** (Number)
- **Pass Through** (Number: Boolean)
- **Custom Value** (Number)

**`\outputsymbol`{=latex} Output**

- **Value Out** (Number)

**Example Patch:** [cables.gl/edit/JJSflJ](https://cables.gl/edit/JJSflJ)

**Doc:** [cables.gl/op/Ops.Number.GateNumber](https://cables.gl/op/Ops.Number.GateNumber)

### Integer
![Integer op](images/ops/Ops_Number_Integer.svg)

**Full Name:** `Ops.Number.Integer`

Number op which only outputs integers.

**`\inputsymbol`{=latex} Inputs**

- **Integer** (Number: Integer)

**`\outputsymbol`{=latex} Output**

- **Number Out** (Number)

**Example Patch:** [cables.gl/op/Ops.Number.Integer#example](https://cables.gl/op/Ops.Number.Integer#example)

**Doc:** [cables.gl/op/Ops.Number.Integer](https://cables.gl/op/Ops.Number.Integer)

### MaximumSafeInteger
![MaximumSafeInteger op](images/ops/Ops_Number_MaximumSafeInteger.svg)

**Full Name:** `Ops.Number.MaximumSafeInteger`

Returns the maximum safe integer (number, constant).

**`\inputsymbol`{=latex} Inputs**

- *Visit [Ops.Number.MaximumSafeInteger documentation](https://cables.gl/op/Ops.Number.MaximumSafeInteger) for input port details*

**`\outputsymbol`{=latex} Output**

- **Max Int** (Number)

**Example Patch:** [cables.gl/op/Ops.Number.MaximumSafeInteger#example](https://cables.gl/op/Ops.Number.MaximumSafeInteger#example)

**Doc:** [cables.gl/op/Ops.Number.MaximumSafeInteger](https://cables.gl/op/Ops.Number.MaximumSafeInteger)

### MinimumSafeInteger
![MinimumSafeInteger op](images/ops/Ops_Number_MinimumSafeInteger.svg)

**Full Name:** `Ops.Number.MinimumSafeInteger`

Returns the minimum safe integer (number, constant).

**`\inputsymbol`{=latex} Inputs**

- *Visit [Ops.Number.MinimumSafeInteger documentation](https://cables.gl/op/Ops.Number.MinimumSafeInteger) for input port details*

**`\outputsymbol`{=latex} Output**

- **Min Int** (Number)

**Example Patch:** [cables.gl/op/Ops.Number.MinimumSafeInteger#example](https://cables.gl/op/Ops.Number.MinimumSafeInteger#example)

**Doc:** [cables.gl/op/Ops.Number.MinimumSafeInteger](https://cables.gl/op/Ops.Number.MinimumSafeInteger)

### Number
![Number op](images/ops/Ops_Number_Number.svg)

**Full Name:** `Ops.Number.Number`

Stores a value, use the same value in different places (was: value.value).

**`\inputsymbol`{=latex} Inputs**

- **Value** (Number)

**`\outputsymbol`{=latex} Output**

- **Result** (Number)

**Example Patch:** [cables.gl/edit/0010r1](https://cables.gl/edit/0010r1)

**Doc:** [cables.gl/op/Ops.Number.Number](https://cables.gl/op/Ops.Number.Number)

### NumberSequence
![NumberSequence op](images/ops/Ops_Number_NumberSequence.svg)

**Full Name:** `Ops.Number.NumberSequence`

Copies the input value to the (value sequence).

**`\inputsymbol`{=latex} Inputs**

- **In Value** (Number)

**`\outputsymbol`{=latex} Output**

- **In Value** (Number)
- **Value Changed** (Trigger)
- **Out Value 0** (Number)
- **Out Value 1** (Number)
- **Out Value 2** (Number)
- **Out Value 3** (Number)

**Example Patch:** [cables.gl/edit/GfgpOb](https://cables.gl/edit/GfgpOb)

**Doc:** [cables.gl/op/Ops.Number.NumberSequence](https://cables.gl/op/Ops.Number.NumberSequence)

### Preset
![Preset op](images/ops/Ops_Number_Preset.svg)

**Full Name:** `Ops.Number.Preset`

State management of all parameters connected to it - Create presets of multiple ops.

**`\inputsymbol`{=latex} Inputs**

- **Data** (String)
- **Sets** (String)
- **Presetid** (String)
- **Interpolation Index** (Number: Integer)
- **Interpolation** (String)
- **Preset A** (Number)
- **Preset B** (Number)
- **Fade** (Number)
- **Preset Index** (Number: Integer)
- **Preset** (Number: String)
- **Create New** (Trigger)
- **Update** (Trigger)
- **Move** (Trigger)
- **Delete** (Trigger)
- **Rename** (Trigger)

**`\outputsymbol`{=latex} Output**

- **Create Variable** (Dynamic)
- **Num Presets** (Number)
- **Current Preset** (Number)
- **Dbg_data** (Array)
- **Dbg_sets** (Array)

**Example Patch:** [cables.gl/edit/KI3veT](https://cables.gl/edit/KI3veT)

**Doc:** [cables.gl/op/Ops.Number.Preset](https://cables.gl/op/Ops.Number.Preset)

### PreviousNumberStore
![PreviousNumberStore op](images/ops/Ops_Number_PreviousNumberStore.svg)

**Full Name:** `Ops.Number.PreviousNumberStore`

remember/store last set number.

**`\inputsymbol`{=latex} Inputs**

- **Value** (Number)

**`\outputsymbol`{=latex} Output**

- **Current Value** (Number)
- **Previous Value** (Number)

**Example Patch:** [cables.gl/edit/XhZWfo](https://cables.gl/edit/XhZWfo)

**Doc:** [cables.gl/op/Ops.Number.PreviousNumberStore](https://cables.gl/op/Ops.Number.PreviousNumberStore)

### RouteNumber
![RouteNumber op](images/ops/Ops_Number_RouteNumber.svg)

**Full Name:** `Ops.Number.RouteNumber`

Routes the value to one of the (based on index, relay).

**`\inputsymbol`{=latex} Inputs**

- **Index** (Number: Integer)
- **Value** (Number)

**`\outputsymbol`{=latex} Output**

- **Index** (Number: Integer)
- **Value** (Number)
- **Default VaonlyOnePortlue** (Number)
- **Set Inactive To Default** (Number: Boolean)
- **Index 0 Value** (Number)
- **Index 1 Value** (Number)
- **Index 2 Value** (Number)
- **Index 3 Value** (Number)
- **Index 4 Value** (Number)
- **Index 5 Value** (Number)
- **Index 6 Value** (Number)
- **Index 7 Value** (Number)
- **Index 8 Value** (Number)
- **Index 9 Value** (Number)

**Example Patch:** [cables.gl/edit/qJcKT6](https://cables.gl/edit/qJcKT6)

**Doc:** [cables.gl/op/Ops.Number.RouteNumber](https://cables.gl/op/Ops.Number.RouteNumber)

### SequenceNumbers
![SequenceNumbers op](images/ops/Ops_Number_SequenceNumbers.svg)

**Full Name:** `Ops.Number.SequenceNumbers`

control order and flow of numbers.

**`\inputsymbol`{=latex} Inputs**

- **Number 0** (Number)
- **Number 1** (Number)
- **Number 2** (Number)
- **Number 3** (Number)
- **Number 4** (Number)
- **Number 5** (Number)
- **Number 6** (Number)
- **Number 7** (Number)
- **Number 8** (Number)
- **Number 9** (Number)
- **Number 10** (Number)
- **Number 11** (Number)
- **Number 12** (Number)
- **Number 13** (Number)
- **Number 14** (Number)
- **Number 15** (Number)

**`\outputsymbol`{=latex} Output**

- **Output 0** (Number)
- **Output 1** (Number)
- **Output 2** (Number)
- **Output 3** (Number)
- **Output 4** (Number)
- **Output 5** (Number)
- **Output 6** (Number)
- **Output 7** (Number)
- **Output 8** (Number)
- **Output 9** (Number)
- **Output 10** (Number)
- **Output 11** (Number)
- **Output 12** (Number)
- **Output 13** (Number)
- **Output 14** (Number)
- **Output 15** (Number)

**Example Patch:** [cables.gl/op/Ops.Number.SequenceNumbers#example](https://cables.gl/op/Ops.Number.SequenceNumbers#example)

**Doc:** [cables.gl/op/Ops.Number.SequenceNumbers](https://cables.gl/op/Ops.Number.SequenceNumbers)

### SumMultiPort_v2
![SumMultiPort_v2 op](images/ops/Ops_Number_SumMultiPort_v2.svg)

**Full Name:** `Ops.Number.SumMultiPort_v2`

Switch between multiple number inputs.

**`\inputsymbol`{=latex} Inputs**

- **Numbers_0** (Number)
- **Add Port** (Number)

**`\outputsymbol`{=latex} Output**

- **Number** (Number)
- **Num Values** (Number)

**Example Patch:** [cables.gl/edit/fUoCu1](https://cables.gl/edit/fUoCu1)

**Doc:** [cables.gl/op/Ops.Number.SumMultiPort_v2](https://cables.gl/op/Ops.Number.SumMultiPort_v2)

### SwitchNumber
![SwitchNumber op](images/ops/Ops_Number_SwitchNumber.svg)

**Full Name:** `Ops.Number.SwitchNumber`

switch between number values by index.

**`\inputsymbol`{=latex} Inputs**

- **Index** (Number: Integer)
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
- **Value 10** (Number)
- **Value 11** (Number)
- **Value 12** (Number)
- **Value 13** (Number)
- **Value 14** (Number)
- **Value 15** (Number)

**`\outputsymbol`{=latex} Output**

- **Result** (Number)

**Example Patch:** [cables.gl/op/Ops.Number.SwitchNumber#example](https://cables.gl/op/Ops.Number.SwitchNumber#example)

**Doc:** [cables.gl/op/Ops.Number.SwitchNumber](https://cables.gl/op/Ops.Number.SwitchNumber)

### SwitchNumberMultiPort_v2
![SwitchNumberMultiPort_v2 op](images/ops/Ops_Number_SwitchNumberMultiPort_v2.svg)

**Full Name:** `Ops.Number.SwitchNumberMultiPort_v2`

Switch between multiple number inputs.

**`\inputsymbol`{=latex} Inputs**

- **Index** (Number: Integer)
- **Numbers_0** (Number)
- **Add Port** (Number)

**`\outputsymbol`{=latex} Output**

- **Number** (Number)
- **Num Values** (Number)

**Example Patch:** [cables.gl/op/Ops.Number.SwitchNumberMultiPort_v2#example](https://cables.gl/op/Ops.Number.SwitchNumberMultiPort_v2#example)

**Doc:** [cables.gl/op/Ops.Number.SwitchNumberMultiPort_v2](https://cables.gl/op/Ops.Number.SwitchNumberMultiPort_v2)

### SwitchNumberOnTrigger
![SwitchNumberOnTrigger op](images/ops/Ops_Number_SwitchNumberOnTrigger.svg)

**Full Name:** `Ops.Number.SwitchNumberOnTrigger`

Sets a specific output value on trigger.

**`\inputsymbol`{=latex} Inputs**

- **Trigger 0** (Trigger)
- **Value 0** (Number)
- **Trigger 1** (Trigger)
- **Value 1** (Number)
- **Trigger 2** (Trigger)
- **Value 2** (Number)
- **Trigger 3** (Trigger)
- **Value 3** (Number)
- **Trigger 4** (Trigger)
- **Value 4** (Number)
- **Trigger 5** (Trigger)
- **Value 5** (Number)
- **Trigger 6** (Trigger)
- **Value 6** (Number)
- **Trigger 7** (Trigger)
- **Value 7** (Number)
- **Default Value** (Number: String)

**`\outputsymbol`{=latex} Output**

- **Value** (Number)
- **Last Value** (Number)
- **Triggered** (Trigger)

**Example Patch:** [cables.gl/op/Ops.Number.SwitchNumberOnTrigger#example](https://cables.gl/op/Ops.Number.SwitchNumberOnTrigger#example)

**Doc:** [cables.gl/op/Ops.Number.SwitchNumberOnTrigger](https://cables.gl/op/Ops.Number.SwitchNumberOnTrigger)

### Trigger3Numbers
![Trigger3Numbers op](images/ops/Ops_Number_Trigger3Numbers.svg)

**Full Name:** `Ops.Number.Trigger3Numbers`

Stores a 3D coordinate (was Value3).

**`\inputsymbol`{=latex} Inputs**

- **Exe** (Trigger)
- **Value X** (Number)
- **Value Y** (Number)
- **Value Z** (Number)

**`\outputsymbol`{=latex} Output**

- **Exe** (Trigger)
- **Value X** (Number)
- **Value Y** (Number)
- **Value Z** (Number)
- **Result X** (Number)
- **Result Y** (Number)
- **Result Z** (Number)

**Example Patch:** [cables.gl/op/Ops.Number.Trigger3Numbers#example](https://cables.gl/op/Ops.Number.Trigger3Numbers#example)

**Doc:** [cables.gl/op/Ops.Number.Trigger3Numbers](https://cables.gl/op/Ops.Number.Trigger3Numbers)

### TriggerOnChangeNumber_v2
![TriggerOnChangeNumber_v2 op](images/ops/Ops_Number_TriggerOnChangeNumber_v2.svg)

**Full Name:** `Ops.Number.TriggerOnChangeNumber_v2`

triggers every time the input value changed.

**`\inputsymbol`{=latex} Inputs**

- **Value** (Number)

**`\outputsymbol`{=latex} Output**

- **Next** (Trigger)
- **Number** (Number)

**Example Patch:** [cables.gl/edit/8y5hVJ](https://cables.gl/edit/8y5hVJ)

**Doc:** [cables.gl/op/Ops.Number.TriggerOnChangeNumber_v2](https://cables.gl/op/Ops.Number.TriggerOnChangeNumber_v2)


