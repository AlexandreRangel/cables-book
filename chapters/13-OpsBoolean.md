# Ops.Boolean


```{=latex}
\OpsSubsubNoSubsectionNumbering\setcounter{subsubsection}{0}
```
### And
![And op](images/ops/Ops_Boolean_And.svg)

**Full Name:** `Ops.Boolean.And`

Outputs `true` if both input values are `true` (boolean).

**`\inputsymbol`{=latex} Inputs**

- **Bool 1** (Number: Boolean)
- **Bool 2** (Number: Boolean)

**`\outputsymbol`{=latex} Output**

- **Result** (Number)

**Example Patch:** [cables.gl/edit/_B91Ms](https://cables.gl/edit/_B91Ms)

**Doc:** [cables.gl/op/Ops.Boolean.And](https://cables.gl/op/Ops.Boolean.And)

### AndMultiPort_v2
![AndMultiPort_v2 op](images/ops/Ops_Boolean_AndMultiPort_v2.svg)

**Full Name:** `Ops.Boolean.AndMultiPort_v2`

Outputs `true` if all input values are `true` (boolean).

**`\inputsymbol`{=latex} Inputs**

- **Booleans_0** (Number: Boolean)
- **Add Port** (Number: Boolean)

**`\outputsymbol`{=latex} Output**

- **Result** (Number)

**Example Patch:** [cables.gl/op/Ops.Boolean.AndMultiPort_v2#example](https://cables.gl/op/Ops.Boolean.AndMultiPort_v2#example)

**Doc:** [cables.gl/op/Ops.Boolean.AndMultiPort_v2](https://cables.gl/op/Ops.Boolean.AndMultiPort_v2)

### BoolByTrigger
![BoolByTrigger op](images/ops/Ops_Boolean_BoolByTrigger.svg)

**Full Name:** `Ops.Boolean.BoolByTrigger`

Trigger true or false values.

**`\inputsymbol`{=latex} Inputs**

- **True** (Trigger)
- **False** (Trigger)

**`\outputsymbol`{=latex} Output**

- **Result** (Number)

**Example Patch:** [cables.gl/edit/1UEVu1](https://cables.gl/edit/1UEVu1)

**Doc:** [cables.gl/op/Ops.Boolean.BoolByTrigger](https://cables.gl/op/Ops.Boolean.BoolByTrigger)

### Boolean
![Boolean op](images/ops/Ops_Boolean_Boolean.svg)

**Full Name:** `Ops.Boolean.Boolean`

Stores a boolean value.

**`\inputsymbol`{=latex} Inputs**

- **Value** (Number: Boolean)

**`\outputsymbol`{=latex} Output**

- **Result** (booleanNumber)

**Example Patch:** [cables.gl/edit/1dAfW2](https://cables.gl/edit/1dAfW2)

**Doc:** [cables.gl/op/Ops.Boolean.Boolean](https://cables.gl/op/Ops.Boolean.Boolean)

### BoolToColor
![BoolToColor op](images/ops/Ops_Boolean_BoolToColor.svg)

**Full Name:** `Ops.Boolean.BoolToColor`

Convert boolean to RGB color.

**`\inputsymbol`{=latex} Inputs**

- **Boolean** (Number: Boolean)
- **R True** (Number)
- **G True** (Number)
- **B True** (Number)
- **A True** (Number)
- **R False** (Number)
- **G False** (Number)
- **B False** (Number)
- **A False** (Number)

**`\outputsymbol`{=latex} Output**

- **R** (Number)
- **G** (Number)
- **B** (Number)
- **A** (Number)

**Example Patch:** [cables.gl/op/Ops.Boolean.BoolToColor#example](https://cables.gl/op/Ops.Boolean.BoolToColor#example)

**Doc:** [cables.gl/op/Ops.Boolean.BoolToColor](https://cables.gl/op/Ops.Boolean.BoolToColor)

### BoolToNumber_v2
![BoolToNumber_v2 op](images/ops/Ops_Boolean_BoolToNumber_v2.svg)

**Full Name:** `Ops.Boolean.BoolToNumber_v2`

Switches two number values using a boolean.

**`\inputsymbol`{=latex} Inputs**

- **Use Value 1** (Number: Boolean)
- **Value 0** (Number)
- **Value 1** (Number)

**`\outputsymbol`{=latex} Output**

- **Out Value** (Number)

**Example Patch:** [cables.gl/op/Ops.Boolean.BoolToNumber_v2#example](https://cables.gl/op/Ops.Boolean.BoolToNumber_v2#example)

**Doc:** [cables.gl/op/Ops.Boolean.BoolToNumber_v2](https://cables.gl/op/Ops.Boolean.BoolToNumber_v2)

### BoolToString
![BoolToString op](images/ops/Ops_Boolean_BoolToString.svg)

**Full Name:** `Ops.Boolean.BoolToString`

convert boolean to string.

**`\inputsymbol`{=latex} Inputs**

- **Boolean** (Number: Boolean)
- **False** (String)
- **True** (String)

**`\outputsymbol`{=latex} Output**

- **String** (String)

**Example Patch:** [cables.gl/edit/kmXCm6](https://cables.gl/edit/kmXCm6)

**Doc:** [cables.gl/op/Ops.Boolean.BoolToString](https://cables.gl/op/Ops.Boolean.BoolToString)

### DelayBooleanSimple
![DelayBooleanSimple op](images/ops/Ops_Boolean_DelayBooleanSimple.svg)

**Full Name:** `Ops.Boolean.DelayBooleanSimple`

Delay the input/output of a boolean by x seconds.

**`\inputsymbol`{=latex} Inputs**

- **Value** (Number)
- **Delay True** (Number)
- **Delay False** (Number)

**`\outputsymbol`{=latex} Output**

- **Out Value** (Number)

**Example Patch:** [cables.gl/edit/VBa0ft](https://cables.gl/edit/VBa0ft)

**Doc:** [cables.gl/op/Ops.Boolean.DelayBooleanSimple](https://cables.gl/op/Ops.Boolean.DelayBooleanSimple)

### IfFalseThen
![IfFalseThen op](images/ops/Ops_Boolean_IfFalseThen.svg)

**Full Name:** `Ops.Boolean.IfFalseThen`

Triggers if input value is `false`.

**`\inputsymbol`{=latex} Inputs**

- **Exe** (Trigger)
- **Boolean** (Number: Boolean)

**`\outputsymbol`{=latex} Output**

- **Exe** (Trigger)
- **Boolean** (Number: Boolean)
- **Then** (Trigger)
- **Else** (Trigger)

**Example Patch:** [cables.gl/op/Ops.Boolean.IfFalseThen#example](https://cables.gl/op/Ops.Boolean.IfFalseThen#example)

**Doc:** [cables.gl/op/Ops.Boolean.IfFalseThen](https://cables.gl/op/Ops.Boolean.IfFalseThen)

### IfTrueThen_v2
![IfTrueThen_v2 op](images/ops/Ops_Boolean_IfTrueThen_v2.svg)

**Full Name:** `Ops.Boolean.IfTrueThen_v2`

Switch, trigger one or the other trigger port based on the input value.

**`\inputsymbol`{=latex} Inputs**

- **Exe** (Trigger)
- **Boolean** (Number: Boolean)

**`\outputsymbol`{=latex} Output**

- **Then** (Trigger)
- **Else** (Trigger)

**Example Patch:** [cables.gl/edit/F9tjX8](https://cables.gl/edit/F9tjX8)

**Doc:** [cables.gl/op/Ops.Boolean.IfTrueThen_v2](https://cables.gl/op/Ops.Boolean.IfTrueThen_v2)

### IsOne
![IsOne op](images/ops/Ops_Boolean_IsOne.svg)

**Full Name:** `Ops.Boolean.IsOne`

Returns `true` if input value is `1`.

**`\inputsymbol`{=latex} Inputs**

- **Value** (Number)

**`\outputsymbol`{=latex} Output**

- **Result** (Number)

**Example Patch:** [cables.gl/op/Ops.Boolean.IsOne#example](https://cables.gl/op/Ops.Boolean.IsOne#example)

**Doc:** [cables.gl/op/Ops.Boolean.IsOne](https://cables.gl/op/Ops.Boolean.IsOne)

### IsZero
![IsZero op](images/ops/Ops_Boolean_IsZero.svg)

**Full Name:** `Ops.Boolean.IsZero`

Returns `true` if input value is `0`.

**`\inputsymbol`{=latex} Inputs**

- **Value** (Number)

**`\outputsymbol`{=latex} Output**

- **Result** (Number)

**Example Patch:** [cables.gl/op/Ops.Boolean.IsZero#example](https://cables.gl/op/Ops.Boolean.IsZero#example)

**Doc:** [cables.gl/op/Ops.Boolean.IsZero](https://cables.gl/op/Ops.Boolean.IsZero)

### MonoFlop
![MonoFlop op](images/ops/Ops_Boolean_MonoFlop.svg)

**Full Name:** `Ops.Boolean.MonoFlop`

Sets output to `1` when triggered, turns back to `0` automatically after x seconds.

**`\inputsymbol`{=latex} Inputs**

- **Trigger** (Trigger)
- **Duration** (Number)
- **Value True** (Number)
- **Value False** (Number)
- **Reset** (Trigger)

**`\outputsymbol`{=latex} Output**

- **Activated** (Trigger)
- **Ended** (Trigger)
- **Result** (Number)

**Example Patch:** [cables.gl/edit/F3r9L5](https://cables.gl/edit/F3r9L5)

**Doc:** [cables.gl/op/Ops.Boolean.MonoFlop](https://cables.gl/op/Ops.Boolean.MonoFlop)

### Not
![Not op](images/ops/Ops_Boolean_Not.svg)

**Full Name:** `Ops.Boolean.Not`

result is false if input is true and vice versa (negate/toggle/switch/!=).

**`\inputsymbol`{=latex} Inputs**

- **Boolean** (Number: Boolean)

**`\outputsymbol`{=latex} Output**

- **Result** (Number)

**Example Patch:** [cables.gl/edit/1dAfW2](https://cables.gl/edit/1dAfW2)

**Doc:** [cables.gl/op/Ops.Boolean.Not](https://cables.gl/op/Ops.Boolean.Not)

### Or
![Or op](images/ops/Ops_Boolean_Or.svg)

**Full Name:** `Ops.Boolean.Or`

Returns `true` if one or more of the input booleans are `true`.

**`\inputsymbol`{=latex} Inputs**

- **Bool 1** (Number: Boolean)
- **Bool 2** (Number: Boolean)
- **Bool 3** (Number: Boolean)
- **Bool 4** (Number: Boolean)
- **Bool 5** (Number: Boolean)
- **Bool 6** (Number: Boolean)
- **Bool 7** (Number: Boolean)
- **Bool 8** (Number: Boolean)
- **Bool 9** (Number: Boolean)
- **Bool 10** (Number: Boolean)

**`\outputsymbol`{=latex} Output**

- **Result** (booleanNumber)

**Example Patch:** [cables.gl/edit/1dAfW2](https://cables.gl/edit/1dAfW2)

**Doc:** [cables.gl/op/Ops.Boolean.Or](https://cables.gl/op/Ops.Boolean.Or)

### OrNumber_v2
![OrNumber_v2 op](images/ops/Ops_Boolean_OrNumber_v2.svg)

**Full Name:** `Ops.Boolean.OrNumber_v2`

Output another number if input number is zero.

**`\inputsymbol`{=latex} Inputs**

- **Number** (Number)
- **Number 2** (Number)
- **Number 3** (Number)
- **Number 4** (Number)
- **Number 5** (Number)
- **Number 6** (Number)
- **Number 7** (Number)
- **Number 8** (Number)

**`\outputsymbol`{=latex} Output**

- **Result** (Number)

**Example Patch:** [cables.gl/edit/J4cYet](https://cables.gl/edit/J4cYet)

**Doc:** [cables.gl/op/Ops.Boolean.OrNumber_v2](https://cables.gl/op/Ops.Boolean.OrNumber_v2)

### ParseBoolean_v2
![ParseBoolean_v2 op](images/ops/Ops_Boolean_ParseBoolean_v2.svg)

**Full Name:** `Ops.Boolean.ParseBoolean_v2`

parse boolean from string/number.

**`\inputsymbol`{=latex} Inputs**

- **String** (String)

**`\outputsymbol`{=latex} Output**

- **Result** (booleanNumber)

**Example Patch:** [cables.gl/edit/2nXYet](https://cables.gl/edit/2nXYet)

**Doc:** [cables.gl/op/Ops.Boolean.ParseBoolean_v2](https://cables.gl/op/Ops.Boolean.ParseBoolean_v2)

### RouteBoolean
![RouteBoolean op](images/ops/Ops_Boolean_RouteBoolean.svg)

**Full Name:** `Ops.Boolean.RouteBoolean`

Route a boolean to an output port.

**`\inputsymbol`{=latex} Inputs**

- **Index** (Number: Integer)
- **Boolean In** (Number: Boolean)
- **Default Boolean** (Number: Boolean)

**`\outputsymbol`{=latex} Output**

- **Index 0 Boolean** (booleanNumber)
- **Index 1 Boolean** (booleanNumber)
- **Index 2 Boolean** (booleanNumber)
- **Index 3 Boolean** (booleanNumber)
- **Index 4 Boolean** (booleanNumber)
- **Index 5 Boolean** (booleanNumber)
- **Index 6 Boolean** (booleanNumber)
- **Index 7 Boolean** (booleanNumber)
- **Index 8 Boolean** (booleanNumber)
- **Index 9 Boolean** (booleanNumber)

**Example Patch:** [cables.gl/edit/mS8CX8](https://cables.gl/edit/mS8CX8)

**Doc:** [cables.gl/op/Ops.Boolean.RouteBoolean](https://cables.gl/op/Ops.Boolean.RouteBoolean)

### ToggleBool_v2
![ToggleBool_v2 op](images/ops/Ops_Boolean_ToggleBool_v2.svg)

**Full Name:** `Ops.Boolean.ToggleBool_v2`

Toggle a boolean value by triggering.

**`\inputsymbol`{=latex} Inputs**

- **Trigger** (Trigger)
- **Reset** (Trigger)
- **Default** (Number: Boolean)

**`\outputsymbol`{=latex} Output**

- **Next** (Trigger)
- **Result** (booleanNumber)

**Example Patch:** [cables.gl/edit/UxJNHj](https://cables.gl/edit/UxJNHj)

**Doc:** [cables.gl/op/Ops.Boolean.ToggleBool_v2](https://cables.gl/op/Ops.Boolean.ToggleBool_v2)

### TriggerChangedFalse
![TriggerChangedFalse op](images/ops/Ops_Boolean_TriggerChangedFalse.svg)

**Full Name:** `Ops.Boolean.TriggerChangedFalse`

Triggers next only after value has changed to `false`.

**`\inputsymbol`{=latex} Inputs**

- **Value** (Number: Boolean)

**`\outputsymbol`{=latex} Output**

- **Next** (Trigger)

**Example Patch:** [cables.gl/edit/UWCvS8](https://cables.gl/edit/UWCvS8)

**Doc:** [cables.gl/op/Ops.Boolean.TriggerChangedFalse](https://cables.gl/op/Ops.Boolean.TriggerChangedFalse)

### TriggerChangedTrue
![TriggerChangedTrue op](images/ops/Ops_Boolean_TriggerChangedTrue.svg)

**Full Name:** `Ops.Boolean.TriggerChangedTrue`

Triggers next only after value has changed to `true`.

**`\inputsymbol`{=latex} Inputs**

- **Value** (Number: Boolean)

**`\outputsymbol`{=latex} Output**

- **Next** (Trigger)

**Example Patch:** [cables.gl/edit/UWCvS8](https://cables.gl/edit/UWCvS8)

**Doc:** [cables.gl/op/Ops.Boolean.TriggerChangedTrue](https://cables.gl/op/Ops.Boolean.TriggerChangedTrue)

### TriggerOnChangeBoolean_v2
![TriggerOnChangeBoolean_v2 op](images/ops/Ops_Boolean_TriggerOnChangeBoolean_v2.svg)

**Full Name:** `Ops.Boolean.TriggerOnChangeBoolean_v2`

Triggers when boolean value has changed.

**`\inputsymbol`{=latex} Inputs**

- **Value** (Number: Boolean)

**`\outputsymbol`{=latex} Output**

- **True** (Trigger)
- **False** (Trigger)

**Example Patch:** [cables.gl/edit/UWCvS8](https://cables.gl/edit/UWCvS8)

**Doc:** [cables.gl/op/Ops.Boolean.TriggerOnChangeBoolean_v2](https://cables.gl/op/Ops.Boolean.TriggerOnChangeBoolean_v2)


