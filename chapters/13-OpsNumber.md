# Ops.Number

*Part of the [All Operators Reference](13-_AllOps.md)*

---

## Ops.Number

### DelayedNumber
![DelayedNumber op](images/ops/Ops_Number_DelayedNumber.svg)

**Full Name:** `Ops.Number.DelayedNumber`
**Description:** delay a value by seconds

**> Input Ports:**
- **Update** (Trigger): *See documentation*
- **Value** (Number): *See documentation*
- **Delay** (Number): *See documentation*
- **Clear On Change** (Number: Boolean): *See documentation*
- **Easing Index** (Number: Integer): *See documentation*

**< Output Ports:**
- **Result** (Number): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Number.DelayedNumber#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "DelayedNumber"*
**Docs:** [https://cables.gl/op/Ops.Number.DelayedNumber](https://cables.gl/op/Ops.Number.DelayedNumber)

---

### DelayNumberSimple
![DelayNumberSimple op](images/ops/Ops_Number_DelayNumberSimple.svg)

**Full Name:** `Ops.Number.DelayNumberSimple`
**Description:** delay the value data flow by x seconds

**> Input Ports:**
- **Value** (Number): *See documentation*
- **Delay** (Number): *See documentation*

**< Output Ports:**
- **Out Value** (Number): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Number.DelayNumberSimple#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "DelayNumberSimple"*
**Docs:** [https://cables.gl/op/Ops.Number.DelayNumberSimple](https://cables.gl/op/Ops.Number.DelayNumberSimple)

---

### FilterValidNumber
![FilterValidNumber op](images/ops/Ops_Number_FilterValidNumber.svg)

**Full Name:** `Ops.Number.FilterValidNumber`
**Description:** Filter valid numbers

**> Input Ports:**
- **Number** (Number): *See documentation*
- **Invalid When 0** (Number: Boolean): *See documentation*

**< Output Ports:**
- **Last Valid Number** (Number): *See documentation*
- **Is Valid** (booleanNumber): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Number.FilterValidNumber#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "FilterValidNumber"*
**Docs:** [https://cables.gl/op/Ops.Number.FilterValidNumber](https://cables.gl/op/Ops.Number.FilterValidNumber)

---

### FreezeNumber
![FreezeNumber op](images/ops/Ops_Number_FreezeNumber.svg)

**Full Name:** `Ops.Number.FreezeNumber`
**Description:** capture the current input and copy it to the output, even after a reload

**> Input Ports:**
- **Number** (Number): *See documentation*
- **Button** (Trigger): *See documentation*

**< Output Ports:**
- **Frozen Number** (Number): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/MuPepX)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "FreezeNumber"*
**Docs:** [https://cables.gl/op/Ops.Number.FreezeNumber](https://cables.gl/op/Ops.Number.FreezeNumber)

---

### GateNumber
![GateNumber op](images/ops/Ops_Number_GateNumber.svg)

**Full Name:** `Ops.Number.GateNumber`
**Description:** Let’s a number through only if control bool is true, like a gate

**> Input Ports:**
- **Value In** (Number): *See documentation*
- **Pass Through** (Number: Boolean): *See documentation*
- **Custom Value** (Number): *See documentation*

**< Output Ports:**
- **Value Out** (Number): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/JJSflJ)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "GateNumber"*
**Docs:** [https://cables.gl/op/Ops.Number.GateNumber](https://cables.gl/op/Ops.Number.GateNumber)

---

### Integer
![Integer op](images/ops/Ops_Number_Integer.svg)

**Full Name:** `Ops.Number.Integer`
**Description:** Number op which only outputs integers

**> Input Ports:**
- **Integer** (Number: Integer): *See documentation*

**< Output Ports:**
- **Number Out** (Number): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Number.Integer#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "Integer"*
**Docs:** [https://cables.gl/op/Ops.Number.Integer](https://cables.gl/op/Ops.Number.Integer)

---

### MaximumSafeInteger
![MaximumSafeInteger op](images/ops/Ops_Number_MaximumSafeInteger.svg)

**Full Name:** `Ops.Number.MaximumSafeInteger`
**Description:** Returns the maximum safe integer (number, constant)

**> Input Ports:**
- *Visit [Ops.Number.MaximumSafeInteger documentation](https://cables.gl/op/Ops.Number.MaximumSafeInteger) for input port details*

**< Output Ports:**
- **Max Int** (Number): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Number.MaximumSafeInteger#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "MaximumSafeInteger"*
**Docs:** [https://cables.gl/op/Ops.Number.MaximumSafeInteger](https://cables.gl/op/Ops.Number.MaximumSafeInteger)

---

### MinimumSafeInteger
![MinimumSafeInteger op](images/ops/Ops_Number_MinimumSafeInteger.svg)

**Full Name:** `Ops.Number.MinimumSafeInteger`
**Description:** Returns the minimum safe integer (number, constant)

**> Input Ports:**
- *Visit [Ops.Number.MinimumSafeInteger documentation](https://cables.gl/op/Ops.Number.MinimumSafeInteger) for input port details*

**< Output Ports:**
- **Min Int** (Number): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Number.MinimumSafeInteger#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "MinimumSafeInteger"*
**Docs:** [https://cables.gl/op/Ops.Number.MinimumSafeInteger](https://cables.gl/op/Ops.Number.MinimumSafeInteger)

---

### Number
![Number op](images/ops/Ops_Number_Number.svg)

**Full Name:** `Ops.Number.Number`
**Description:** Stores a value, use the same value in different places (was: value.value)

**> Input Ports:**
- **Value** (Number): *See documentation*

**< Output Ports:**
- **Result** (Number): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/0010r1)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "Number"*
**Docs:** [https://cables.gl/op/Ops.Number.Number](https://cables.gl/op/Ops.Number.Number)

---

### NumberSequence
![NumberSequence op](images/ops/Ops_Number_NumberSequence.svg)

**Full Name:** `Ops.Number.NumberSequence`
**Description:** Copies the input value to the (value sequence)

**> Input Ports:**
- **In Value** (Number): *See documentation*

**< Output Ports:**
- **In Value** (Number): *See documentation*
- **Value Changed** (Trigger): *See documentation*
- **Out Value 0** (Number): *See documentation*
- **Out Value 1** (Number): *See documentation*
- **Out Value 2** (Number): *See documentation*
- **Out Value 3** (Number): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/GfgpOb)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "NumberSequence"*
**Docs:** [https://cables.gl/op/Ops.Number.NumberSequence](https://cables.gl/op/Ops.Number.NumberSequence)

---

### Preset
![Preset op](images/ops/Ops_Number_Preset.svg)

**Full Name:** `Ops.Number.Preset`
**Description:** State management of all parameters connected to it - Create presets of multiple ops

**> Input Ports:**
- **Data** (String): *See documentation*
- **Sets** (String): *See documentation*
- **Presetid** (String): *See documentation*
- **Interpolation Index** (Number: Integer): *See documentation*
- **Interpolation** (String): *See documentation*
- **Preset A** (Number): *See documentation*
- **Preset B** (Number): *See documentation*
- **Fade** (Number): *See documentation*
- **Preset Index** (Number: Integer): *See documentation*
- **Preset** (Number: String): *See documentation*
- **Create New** (Trigger): *See documentation*
- **Update** (Trigger): *See documentation*
- **Move** (Trigger): *See documentation*
- **Delete** (Trigger): *See documentation*
- **Rename** (Trigger): *See documentation*

**< Output Ports:**
- **Create Variable** (Dynamic): *See documentation*
- **Num Presets** (Number): *See documentation*
- **Current Preset** (Number): *See documentation*
- **Dbg_data** (Array): *See documentation*
- **Dbg_sets** (Array): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/KI3veT)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "Preset"*
**Docs:** [https://cables.gl/op/Ops.Number.Preset](https://cables.gl/op/Ops.Number.Preset)

---

### PreviousNumberStore
![PreviousNumberStore op](images/ops/Ops_Number_PreviousNumberStore.svg)

**Full Name:** `Ops.Number.PreviousNumberStore`
**Description:** remember/store last set number

**> Input Ports:**
- **Value** (Number): *See documentation*

**< Output Ports:**
- **Current Value** (Number): *See documentation*
- **Previous Value** (Number): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/XhZWfo)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "PreviousNumberStore"*
**Docs:** [https://cables.gl/op/Ops.Number.PreviousNumberStore](https://cables.gl/op/Ops.Number.PreviousNumberStore)

---

### RouteNumber
![RouteNumber op](images/ops/Ops_Number_RouteNumber.svg)

**Full Name:** `Ops.Number.RouteNumber`
**Description:** Routes the value to one of the (based on index, relay)

**> Input Ports:**
- **Index** (Number: Integer): *See documentation*
- **Value** (Number): *See documentation*

**< Output Ports:**
- **Index** (Number: Integer): *See documentation*
- **Value** (Number): *See documentation*
- **Default VaonlyOnePortlue** (Number): *See documentation*
- **Set Inactive To Default** (Number: Boolean): *See documentation*
- **Index 0 Value** (Number): *See documentation*
- **Index 1 Value** (Number): *See documentation*
- **Index 2 Value** (Number): *See documentation*
- **Index 3 Value** (Number): *See documentation*
- **Index 4 Value** (Number): *See documentation*
- **Index 5 Value** (Number): *See documentation*
- **Index 6 Value** (Number): *See documentation*
- **Index 7 Value** (Number): *See documentation*
- **Index 8 Value** (Number): *See documentation*
- **Index 9 Value** (Number): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/qJcKT6)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "RouteNumber"*
**Docs:** [https://cables.gl/op/Ops.Number.RouteNumber](https://cables.gl/op/Ops.Number.RouteNumber)

---

### SequenceNumbers
![SequenceNumbers op](images/ops/Ops_Number_SequenceNumbers.svg)

**Full Name:** `Ops.Number.SequenceNumbers`
**Description:** control order and flow of numbers

**> Input Ports:**
- **Number 0** (Number): *See documentation*
- **Number 1** (Number): *See documentation*
- **Number 2** (Number): *See documentation*
- **Number 3** (Number): *See documentation*
- **Number 4** (Number): *See documentation*
- **Number 5** (Number): *See documentation*
- **Number 6** (Number): *See documentation*
- **Number 7** (Number): *See documentation*
- **Number 8** (Number): *See documentation*
- **Number 9** (Number): *See documentation*
- **Number 10** (Number): *See documentation*
- **Number 11** (Number): *See documentation*
- **Number 12** (Number): *See documentation*
- **Number 13** (Number): *See documentation*
- **Number 14** (Number): *See documentation*
- **Number 15** (Number): *See documentation*

**< Output Ports:**
- **Output 0** (Number): *See documentation*
- **Output 1** (Number): *See documentation*
- **Output 2** (Number): *See documentation*
- **Output 3** (Number): *See documentation*
- **Output 4** (Number): *See documentation*
- **Output 5** (Number): *See documentation*
- **Output 6** (Number): *See documentation*
- **Output 7** (Number): *See documentation*
- **Output 8** (Number): *See documentation*
- **Output 9** (Number): *See documentation*
- **Output 10** (Number): *See documentation*
- **Output 11** (Number): *See documentation*
- **Output 12** (Number): *See documentation*
- **Output 13** (Number): *See documentation*
- **Output 14** (Number): *See documentation*
- **Output 15** (Number): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Number.SequenceNumbers#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "SequenceNumbers"*
**Docs:** [https://cables.gl/op/Ops.Number.SequenceNumbers](https://cables.gl/op/Ops.Number.SequenceNumbers)

---

### SumMultiPort_v2
![SumMultiPort_v2 op](images/ops/Ops_Number_SumMultiPort_v2.svg)

**Full Name:** `Ops.Number.SumMultiPort_v2`
**Description:** Switch between multiple number inputs

**> Input Ports:**
- **Numbers_0** (Number): *See documentation*
- **Add Port** (Number): *See documentation*

**< Output Ports:**
- **Number** (Number): *See documentation*
- **Num Values** (Number): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/fUoCu1)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "SumMultiPort_v2"*
**Docs:** [https://cables.gl/op/Ops.Number.SumMultiPort_v2](https://cables.gl/op/Ops.Number.SumMultiPort_v2)

---

### SwitchNumber
![SwitchNumber op](images/ops/Ops_Number_SwitchNumber.svg)

**Full Name:** `Ops.Number.SwitchNumber`
**Description:** switch between number values by index

**> Input Ports:**
- **Index** (Number: Integer): *See documentation*
- **Value 0** (Number): *See documentation*
- **Value 1** (Number): *See documentation*
- **Value 2** (Number): *See documentation*
- **Value 3** (Number): *See documentation*
- **Value 4** (Number): *See documentation*
- **Value 5** (Number): *See documentation*
- **Value 6** (Number): *See documentation*
- **Value 7** (Number): *See documentation*
- **Value 8** (Number): *See documentation*
- **Value 9** (Number): *See documentation*
- **Value 10** (Number): *See documentation*
- **Value 11** (Number): *See documentation*
- **Value 12** (Number): *See documentation*
- **Value 13** (Number): *See documentation*
- **Value 14** (Number): *See documentation*
- **Value 15** (Number): *See documentation*

**< Output Ports:**
- **Result** (Number): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Number.SwitchNumber#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "SwitchNumber"*
**Docs:** [https://cables.gl/op/Ops.Number.SwitchNumber](https://cables.gl/op/Ops.Number.SwitchNumber)

---

### SwitchNumberMultiPort_v2
![SwitchNumberMultiPort_v2 op](images/ops/Ops_Number_SwitchNumberMultiPort_v2.svg)

**Full Name:** `Ops.Number.SwitchNumberMultiPort_v2`
**Description:** Switch between multiple number inputs

**> Input Ports:**
- **Index** (Number: Integer): *See documentation*
- **Numbers_0** (Number): *See documentation*
- **Add Port** (Number): *See documentation*

**< Output Ports:**
- **Number** (Number): *See documentation*
- **Num Values** (Number): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Number.SwitchNumberMultiPort_v2#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "SwitchNumberMultiPort_v2"*
**Docs:** [https://cables.gl/op/Ops.Number.SwitchNumberMultiPort_v2](https://cables.gl/op/Ops.Number.SwitchNumberMultiPort_v2)

---

### SwitchNumberOnTrigger
![SwitchNumberOnTrigger op](images/ops/Ops_Number_SwitchNumberOnTrigger.svg)

**Full Name:** `Ops.Number.SwitchNumberOnTrigger`
**Description:** Sets a specific output value on trigger

**> Input Ports:**
- **Trigger 0** (Trigger): *See documentation*
- **Value 0** (Number): *See documentation*
- **Trigger 1** (Trigger): *See documentation*
- **Value 1** (Number): *See documentation*
- **Trigger 2** (Trigger): *See documentation*
- **Value 2** (Number): *See documentation*
- **Trigger 3** (Trigger): *See documentation*
- **Value 3** (Number): *See documentation*
- **Trigger 4** (Trigger): *See documentation*
- **Value 4** (Number): *See documentation*
- **Trigger 5** (Trigger): *See documentation*
- **Value 5** (Number): *See documentation*
- **Trigger 6** (Trigger): *See documentation*
- **Value 6** (Number): *See documentation*
- **Trigger 7** (Trigger): *See documentation*
- **Value 7** (Number): *See documentation*
- **Default Value** (Number: String): *See documentation*

**< Output Ports:**
- **Value** (Number): *See documentation*
- **Last Value** (Number): *See documentation*
- **Triggered** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Number.SwitchNumberOnTrigger#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "SwitchNumberOnTrigger"*
**Docs:** [https://cables.gl/op/Ops.Number.SwitchNumberOnTrigger](https://cables.gl/op/Ops.Number.SwitchNumberOnTrigger)

---

### Trigger3Numbers
![Trigger3Numbers op](images/ops/Ops_Number_Trigger3Numbers.svg)

**Full Name:** `Ops.Number.Trigger3Numbers`
**Description:** Stores a 3D coordinate (was Value3)

**> Input Ports:**
- **Exe** (Trigger): *See documentation*
- **Value X** (Number): *See documentation*
- **Value Y** (Number): *See documentation*
- **Value Z** (Number): *See documentation*

**< Output Ports:**
- **Exe** (Trigger): *See documentation*
- **Value X** (Number): *See documentation*
- **Value Y** (Number): *See documentation*
- **Value Z** (Number): *See documentation*
- **Result X** (Number): *See documentation*
- **Result Y** (Number): *See documentation*
- **Result Z** (Number): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Number.Trigger3Numbers#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "Trigger3Numbers"*
**Docs:** [https://cables.gl/op/Ops.Number.Trigger3Numbers](https://cables.gl/op/Ops.Number.Trigger3Numbers)

---

### TriggerOnChangeNumber_v2
![TriggerOnChangeNumber_v2 op](images/ops/Ops_Number_TriggerOnChangeNumber_v2.svg)

**Full Name:** `Ops.Number.TriggerOnChangeNumber_v2`
**Description:** triggers every time the input value changed

**> Input Ports:**
- **Value** (Number): *See documentation*

**< Output Ports:**
- **Next** (Trigger): *See documentation*
- **Number** (Number): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/8y5hVJ)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "TriggerOnChangeNumber_v2"*
**Docs:** [https://cables.gl/op/Ops.Number.TriggerOnChangeNumber_v2](https://cables.gl/op/Ops.Number.TriggerOnChangeNumber_v2)

---

