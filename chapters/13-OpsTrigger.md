# Ops.Trigger

*Part of the [All Operators Reference](13-_AllOps.md)*

---

## Ops.Trigger

### DelayedTrigger
![DelayedTrigger op](images/ops/Ops_Trigger_DelayedTrigger.svg)

**Full Name:** `Ops.Trigger.DelayedTrigger`
**Description:** delay triggering next port by x seconds

**> Input Ports:**
- **Exe** (Trigger): *See documentation*
- **Delay** (Number): *See documentation*
- **Cancel** (Trigger): *See documentation*

**< Output Ports:**
- **Next** (Trigger): *See documentation*
- **Delaying** (booleanNumber): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/VgtMji)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "DelayedTrigger"*
**Docs:** [https://cables.gl/op/Ops.Trigger.DelayedTrigger](https://cables.gl/op/Ops.Trigger.DelayedTrigger)

---

### GateTrigger
![GateTrigger op](images/ops/Ops_Trigger_GateTrigger.svg)

**Full Name:** `Ops.Trigger.GateTrigger`
**Description:** Allows a trigger to pass only if the gate is open

**> Input Ports:**
- **Execute** (Trigger): *See documentation*
- **Pass Through** (Number: Boolean): *See documentation*

**< Output Ports:**
- **Trigger Out** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/xotJAH)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "GateTrigger"*
**Docs:** [https://cables.gl/op/Ops.Trigger.GateTrigger](https://cables.gl/op/Ops.Trigger.GateTrigger)

---

### Interval
![Interval op](images/ops/Ops_Trigger_Interval.svg)

**Full Name:** `Ops.Trigger.Interval`
**Description:** Timed Trigger every x ms

**> Input Ports:**
- **Interval** (Number): *See documentation*
- **Active** (Number: Boolean): *See documentation*

**< Output Ports:**
- **Trigger** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/ZdvX7i)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "Interval"*
**Docs:** [https://cables.gl/op/Ops.Trigger.Interval](https://cables.gl/op/Ops.Trigger.Interval)

---

### IsTriggered
![IsTriggered op](images/ops/Ops_Trigger_IsTriggered.svg)

**Full Name:** `Ops.Trigger.IsTriggered`
**Description:** outputs true if being triggered last frame

**> Input Ports:**
- **Trigger** (Trigger): *See documentation*

**< Output Ports:**
- **Next** (Trigger): *See documentation*
- **Was Triggered** (Number): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/kmXCm6)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "IsTriggered"*
**Docs:** [https://cables.gl/op/Ops.Trigger.IsTriggered](https://cables.gl/op/Ops.Trigger.IsTriggered)

---

### NthTrigger_v2
![NthTrigger_v2 op](images/ops/Ops_Trigger_NthTrigger_v2.svg)

**Full Name:** `Ops.Trigger.NthTrigger_v2`
**Description:** Lets a trigger through every nth time (trigger limiter)

**> Input Ports:**
- **Execute** (Trigger): *See documentation*
- **Nth** (Number): *See documentation*

**< Output Ports:**
- **Next** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/cnVqii)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "NthTrigger_v2"*
**Docs:** [https://cables.gl/op/Ops.Trigger.NthTrigger_v2](https://cables.gl/op/Ops.Trigger.NthTrigger_v2)

---

### NumberByTrigger
![NumberByTrigger op](images/ops/Ops_Trigger_NumberByTrigger.svg)

**Full Name:** `Ops.Trigger.NumberByTrigger`
**Description:** Outputs the last number of the input port which was triggered

**> Input Ports:**
- *Visit [Ops.Trigger.NumberByTrigger documentation](https://cables.gl/op/Ops.Trigger.NumberByTrigger) for input port details*

**< Output Ports:**
- **Number** (Number): *See documentation*
- **Triggered** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/kzTxsh)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "NumberByTrigger"*
**Docs:** [https://cables.gl/op/Ops.Trigger.NumberByTrigger](https://cables.gl/op/Ops.Trigger.NumberByTrigger)

---

### NumberByTriggerMultiPort_v2
![NumberByTriggerMultiPort_v2 op](images/ops/Ops_Trigger_NumberByTriggerMultiPort_v2.svg)

**Full Name:** `Ops.Trigger.NumberByTriggerMultiPort_v2`
**Description:** output a number by triggering an index port

**> Input Ports:**
- **Trigger_0** (Trigger): *See documentation*
- **Add Port** (Trigger): *See documentation*

**< Output Ports:**
- **Next** (Trigger): *See documentation*
- **Number Triggered** (Number): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/ubuysh)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "NumberByTriggerMultiPort_v2"*
**Docs:** [https://cables.gl/op/Ops.Trigger.NumberByTriggerMultiPort_v2](https://cables.gl/op/Ops.Trigger.NumberByTriggerMultiPort_v2)

---

### ProbabilityTrigger
![ProbabilityTrigger op](images/ops/Ops_Trigger_ProbabilityTrigger.svg)

**Full Name:** `Ops.Trigger.ProbabilityTrigger`
**Description:** trigger by chance

**> Input Ports:**
- **Trigger In** (Trigger): *See documentation*
- **Probability** (Number): *See documentation*

**< Output Ports:**
- **Trigger Output** (Trigger): *See documentation*
- **Inverse Trigger Output** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/I61CCu)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ProbabilityTrigger"*
**Docs:** [https://cables.gl/op/Ops.Trigger.ProbabilityTrigger](https://cables.gl/op/Ops.Trigger.ProbabilityTrigger)

---

### RandomTrigger
![RandomTrigger op](images/ops/Ops_Trigger_RandomTrigger.svg)

**Full Name:** `Ops.Trigger.RandomTrigger`
**Description:** randomly trigger

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Num Times** (Number): *See documentation*
- **Seed** (Number): *See documentation*
- **Only Once** (Number: Boolean): *See documentation*

**< Output Ports:**
- **Render** (Trigger): *See documentation*
- **Num Times** (Number): *See documentation*
- **Seed** (Number): *See documentation*
- **Only Once** (Number: Boolean): *See documentation*
- **Index** (Number): *See documentation*
- **Trigger 0** (Trigger): *See documentation*
- **Trigger 1** (Trigger): *See documentation*
- **Trigger 2** (Trigger): *See documentation*
- **Trigger 3** (Trigger): *See documentation*
- **Trigger 4** (Trigger): *See documentation*
- **Trigger 5** (Trigger): *See documentation*
- **Trigger 6** (Trigger): *See documentation*
- **Trigger 7** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/3P54t7)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "RandomTrigger"*
**Docs:** [https://cables.gl/op/Ops.Trigger.RandomTrigger](https://cables.gl/op/Ops.Trigger.RandomTrigger)

---

### Repeat2d
![Repeat2d op](images/ops/Ops_Trigger_Repeat2d.svg)

**Full Name:** `Ops.Trigger.Repeat2d`
**Description:** Triggers all ops underneath Num X * Num Y times

**> Input Ports:**
- **Exe** (Trigger): *See documentation*
- **Num X** (Number: Integer): *See documentation*
- **Num Y** (Number: Integer): *See documentation*
- **Mul** (Number): *See documentation*
- **Center** (Number: Boolean): *See documentation*
- **Centers X and Y around the origin** (0/0): *See documentation*

**< Output Ports:**
- **Trigger** (Trigger): *See documentation*
- **X** (Number): *See documentation*
- **Y** (Number): *See documentation*
- **Index** (Number): *See documentation*
- **Total Iterations** (Number): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/lPZfgg)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "Repeat2d"*
**Docs:** [https://cables.gl/op/Ops.Trigger.Repeat2d](https://cables.gl/op/Ops.Trigger.Repeat2d)

---

### Repeat_v2
![Repeat_v2 op](images/ops/Ops_Trigger_Repeat_v2.svg)

**Full Name:** `Ops.Trigger.Repeat_v2`
**Description:** Triggers all ops below x times (for loop / while)

**> Input Ports:**
- **Execute** (Trigger): *See documentation*
- **Repeats** (Number: Integer): *See documentation*

**< Output Ports:**
- **Next** (Trigger): *See documentation*
- **Index** (Number): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/VFAfgg)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "Repeat_v2"*
**Docs:** [https://cables.gl/op/Ops.Trigger.Repeat_v2](https://cables.gl/op/Ops.Trigger.Repeat_v2)

---

### RouteTrigger
![RouteTrigger op](images/ops/Ops_Trigger_RouteTrigger.svg)

**Full Name:** `Ops.Trigger.RouteTrigger`
**Description:** Triggers one of the out ports - value index switch case (was SwitchTrigger)

**> Input Ports:**
- **Execute** (Trigger): *See documentation*
- **Switch Value** (Number: Integer): *See documentation*

**< Output Ports:**
- **Next Trigger** (Trigger): *See documentation*
- **Switched Value** (Number): *See documentation*
- **Trigger 0** (Trigger): *See documentation*
- **Trigger 1** (Trigger): *See documentation*
- **Trigger 2** (Trigger): *See documentation*
- **Trigger 3** (Trigger): *See documentation*
- **Trigger 4** (Trigger): *See documentation*
- **Trigger 5** (Trigger): *See documentation*
- **Trigger 6** (Trigger): *See documentation*
- **Trigger 7** (Trigger): *See documentation*
- **Trigger 8** (Trigger): *See documentation*
- **Trigger 9** (Trigger): *See documentation*
- **Trigger 10** (Trigger): *See documentation*
- **Trigger 11** (Trigger): *See documentation*
- **Trigger 12** (Trigger): *See documentation*
- **Trigger 13** (Trigger): *See documentation*
- **Trigger 14** (Trigger): *See documentation*
- **Trigger 15** (Trigger): *See documentation*
- **Trigger 16** (Trigger): *See documentation*
- **Trigger 17** (Trigger): *See documentation*
- **Trigger 18** (Trigger): *See documentation*
- **Trigger 19** (Trigger): *See documentation*
- **Trigger 20** (Trigger): *See documentation*
- **Trigger 21** (Trigger): *See documentation*
- **Trigger 22** (Trigger): *See documentation*
- **Trigger 23** (Trigger): *See documentation*
- **Default Trigger** (Trigger): *See documentation*
- **Highest Index** (Number): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/DzH9S5)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "RouteTrigger"*
**Docs:** [https://cables.gl/op/Ops.Trigger.RouteTrigger](https://cables.gl/op/Ops.Trigger.RouteTrigger)

---

### RouteTriggerAnimated
![RouteTriggerAnimated op](images/ops/Ops_Trigger_RouteTriggerAnimated.svg)

**Full Name:** `Ops.Trigger.RouteTriggerAnimated`
**Description:** animated switching between things

**> Input Ports:**
- **Index** (Number: Integer): *See documentation*
- **Exe** (Trigger): *See documentation*
- **Duration** (Number): *See documentation*

**< Output Ports:**
- **Qutsn94pc** (Trigger): *See documentation*
- **Hvyzlh9o8** (Trigger): *See documentation*
- **T8dvyjuoq** (Trigger): *See documentation*
- **A0w7orgi8** (Trigger): *See documentation*
- **R8h4qx4z8** (Trigger): *See documentation*
- **Cr80a86xi** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/pUtH15)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "RouteTriggerAnimated"*
**Docs:** [https://cables.gl/op/Ops.Trigger.RouteTriggerAnimated](https://cables.gl/op/Ops.Trigger.RouteTriggerAnimated)

---

### RouteTriggerMultiPort_v2
![RouteTriggerMultiPort_v2 op](images/ops/Ops_Trigger_RouteTriggerMultiPort_v2.svg)

**Full Name:** `Ops.Trigger.RouteTriggerMultiPort_v2`
**Description:** Triggers one of the - value index switch case

**> Input Ports:**
- **Execute** (Trigger): *See documentation*
- **Switch Value** (Number: Integer): *See documentation*

**< Output Ports:**
- **Execute** (Trigger): *See documentation*
- **Switch Value** (Number: Integer): *See documentation*
- **Total Connections** (Number): *See documentation*
- **Connected Op Names** (Array): *See documentation*
- **Trigger_0** (Trigger): *See documentation*
- **Trigger_1** (Trigger): *See documentation*
- **Trigger_2** (Trigger): *See documentation*
- **Trigger_3** (Trigger): *See documentation*
- **Trigger_4** (Trigger): *See documentation*
- **Trigger_5** (Trigger): *See documentation*
- **Trigger_6** (Trigger): *See documentation*
- **Trigger_7** (Trigger): *See documentation*
- **Trigger_8** (Trigger): *See documentation*
- **Trigger_9** (Trigger): *See documentation*
- **Trigger_10** (Trigger): *See documentation*
- **Trigger_11** (Trigger): *See documentation*
- **Trigger_12** (Trigger): *See documentation*
- **Trigger_13** (Trigger): *See documentation*
- **Trigger_14** (Trigger): *See documentation*
- **Trigger_15** (Trigger): *See documentation*
- **Trigger_16** (Trigger): *See documentation*
- **Trigger_17** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/NxGysh)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "RouteTriggerMultiPort_v2"*
**Docs:** [https://cables.gl/op/Ops.Trigger.RouteTriggerMultiPort_v2](https://cables.gl/op/Ops.Trigger.RouteTriggerMultiPort_v2)

---

### RouteTriggerString_v2
![RouteTriggerString_v2 op](images/ops/Ops_Trigger_RouteTriggerString_v2.svg)

**Full Name:** `Ops.Trigger.RouteTriggerString_v2`
**Description:** route trigger output by string

**> Input Ports:**
- **Execute** (Trigger): *See documentation*
- **Switch Value** (String): *See documentation*
- **String 0** (String): *See documentation*
- **String 1** (String): *See documentation*
- **String 2** (String): *See documentation*
- **String 3** (String): *See documentation*
- **String 4** (String): *See documentation*
- **String 5** (String): *See documentation*
- **String 6** (String): *See documentation*
- **String 7** (String): *See documentation*
- **String 8** (String): *See documentation*
- **String 9** (String): *See documentation*
- **String 10** (String): *See documentation*
- **String 11** (String): *See documentation*
- **String 12** (String): *See documentation*
- **String 13** (String): *See documentation*
- **String 14** (String): *See documentation*
- **String 15** (String): *See documentation*
- **String 16** (String): *See documentation*
- **String 17** (String): *See documentation*
- **String 18** (String): *See documentation*
- **String 19** (String): *See documentation*
- **String 20** (String): *See documentation*
- **String 21** (String): *See documentation*
- **String 22** (String): *See documentation*
- **String 23** (String): *See documentation*

**< Output Ports:**
- **Next Trigger** (Trigger): *See documentation*
- **Switched Index** (Number): *See documentation*
- **Trigger 0** (Trigger): *See documentation*
- **Trigger 1** (Trigger): *See documentation*
- **Trigger 2** (Trigger): *See documentation*
- **Trigger 3** (Trigger): *See documentation*
- **Trigger 4** (Trigger): *See documentation*
- **Trigger 5** (Trigger): *See documentation*
- **Trigger 6** (Trigger): *See documentation*
- **Trigger 7** (Trigger): *See documentation*
- **Trigger 8** (Trigger): *See documentation*
- **Trigger 9** (Trigger): *See documentation*
- **Trigger 10** (Trigger): *See documentation*
- **Trigger 11** (Trigger): *See documentation*
- **Trigger 12** (Trigger): *See documentation*
- **Trigger 13** (Trigger): *See documentation*
- **Trigger 14** (Trigger): *See documentation*
- **Trigger 15** (Trigger): *See documentation*
- **Trigger 16** (Trigger): *See documentation*
- **Trigger 17** (Trigger): *See documentation*
- **Trigger 18** (Trigger): *See documentation*
- **Trigger 19** (Trigger): *See documentation*
- **Trigger 20** (Trigger): *See documentation*
- **Trigger 21** (Trigger): *See documentation*
- **Trigger 22** (Trigger): *See documentation*
- **Trigger 23** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/8uTjhI)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "RouteTriggerString_v2"*
**Docs:** [https://cables.gl/op/Ops.Trigger.RouteTriggerString_v2](https://cables.gl/op/Ops.Trigger.RouteTriggerString_v2)

---

### Sequence
![Sequence op](images/ops/Ops_Trigger_Sequence.svg)

**Full Name:** `Ops.Trigger.Sequence`
**Description:** control the order of execution/triggering

**> Input Ports:**
- **Exe** (Trigger): *See documentation*
- **Exe 0** (Trigger): *See documentation*
- **Exe 1** (Trigger): *See documentation*
- **Exe 2** (Trigger): *See documentation*
- **Exe 3** (Trigger): *See documentation*
- **Exe 4** (Trigger): *See documentation*
- **Exe 5** (Trigger): *See documentation*
- **Exe 6** (Trigger): *See documentation*
- **Exe 7** (Trigger): *See documentation*
- **Exe 8** (Trigger): *See documentation*
- **Exe 9** (Trigger): *See documentation*
- **Exe 10** (Trigger): *See documentation*
- **Exe 11** (Trigger): *See documentation*
- **Exe 12** (Trigger): *See documentation*
- **Exe 13** (Trigger): *See documentation*
- **Exe 14** (Trigger): *See documentation*

**< Output Ports:**
- **Trigger 0** (Trigger): *See documentation*
- **Trigger 1** (Trigger): *See documentation*
- **Trigger 2** (Trigger): *See documentation*
- **Trigger 3** (Trigger): *See documentation*
- **Trigger 4** (Trigger): *See documentation*
- **Trigger 5** (Trigger): *See documentation*
- **Trigger 6** (Trigger): *See documentation*
- **Trigger 7** (Trigger): *See documentation*
- **Trigger 8** (Trigger): *See documentation*
- **Trigger 9** (Trigger): *See documentation*
- **Trigger 10** (Trigger): *See documentation*
- **Trigger 11** (Trigger): *See documentation*
- **Trigger 12** (Trigger): *See documentation*
- **Trigger 13** (Trigger): *See documentation*
- **Trigger 14** (Trigger): *See documentation*
- **Trigger 15** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/0bQrii)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "Sequence"*
**Docs:** [https://cables.gl/op/Ops.Trigger.Sequence](https://cables.gl/op/Ops.Trigger.Sequence)

---

### SequenceMultiPort_v2
![SequenceMultiPort_v2 op](images/ops/Ops_Trigger_SequenceMultiPort_v2.svg)

**Full Name:** `Ops.Trigger.SequenceMultiPort_v2`
**Description:** sequence trigger

**> Input Ports:**
- **Input_0** (Trigger): *See documentation*
- **Add Port** (Trigger): *See documentation*

**< Output Ports:**
- **Output_0** (Trigger): *See documentation*
- **Output_1** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/F5L0sh)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "SequenceMultiPort_v2"*
**Docs:** [https://cables.gl/op/Ops.Trigger.SequenceMultiPort_v2](https://cables.gl/op/Ops.Trigger.SequenceMultiPort_v2)

---

### SwitchTrigger
![SwitchTrigger op](images/ops/Ops_Trigger_SwitchTrigger.svg)

**Full Name:** `Ops.Trigger.SwitchTrigger`
**Description:** route input triggers by index to one output

**> Input Ports:**
- **Trigger Index** (Number: Integer): *See documentation*
- **Trigger In 0** (Trigger): *See documentation*
- **Trigger In 1** (Trigger): *See documentation*
- **Trigger In 2** (Trigger): *See documentation*
- **Trigger In 3** (Trigger): *See documentation*
- **Trigger In 4** (Trigger): *See documentation*
- **Trigger In 5** (Trigger): *See documentation*
- **Trigger In 6** (Trigger): *See documentation*
- **Trigger In 7** (Trigger): *See documentation*
- **Trigger In 8** (Trigger): *See documentation*
- **Trigger In 9** (Trigger): *See documentation*
- **Trigger In 10** (Trigger): *See documentation*
- **Trigger In 11** (Trigger): *See documentation*
- **Trigger In 12** (Trigger): *See documentation*
- **Trigger In 13** (Trigger): *See documentation*
- **Trigger In 14** (Trigger): *See documentation*
- **Trigger In 15** (Trigger): *See documentation*

**< Output Ports:**
- **Trigger Out** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/upF4rn)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "SwitchTrigger"*
**Docs:** [https://cables.gl/op/Ops.Trigger.SwitchTrigger](https://cables.gl/op/Ops.Trigger.SwitchTrigger)

---

### Threshold
![Threshold op](images/ops/Ops_Trigger_Threshold.svg)

**Full Name:** `Ops.Trigger.Threshold`
**Description:** Triggers only once when threshold is crossed

**> Input Ports:**
- **Threshold** (Number): *See documentation*

**< Output Ports:**
- *Visit [Ops.Trigger.Threshold documentation](https://cables.gl/op/Ops.Trigger.Threshold) for output port details*

**Example Patch:** [Open in Editor](https://cables.gl/edit/pG-Mwq)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "Threshold"*
**Docs:** [https://cables.gl/op/Ops.Trigger.Threshold](https://cables.gl/op/Ops.Trigger.Threshold)

---

### TimedSequence
![TimedSequence op](images/ops/Ops_Trigger_TimedSequence.svg)

**Full Name:** `Ops.Trigger.TimedSequence`
**Description:** timed switching of trigger

**> Input Ports:**
- **Exe** (Trigger): *See documentation*
- **Current** (Number: Integer): *See documentation*
- **OverwriteTime** (Number: Boolean): *See documentation*
- **IgnoreInSubPatch** (Number: Boolean): *See documentation*

**< Output Ports:**
- **TriggerAlways** (Trigger): *See documentation*
- **Names** (Array): *See documentation*
- **CurrentKeyTime** (Number): *See documentation*
- **Current** (Number): *See documentation*
- **Trigger 0** (Trigger): *See documentation*
- **Trigger 1** (Trigger): *See documentation*
- **Trigger 2** (Trigger): *See documentation*
- **Trigger 3** (Trigger): *See documentation*
- **Trigger 4** (Trigger): *See documentation*
- **Trigger 5** (Trigger): *See documentation*
- **Trigger 6** (Trigger): *See documentation*
- **Trigger 7** (Trigger): *See documentation*
- **Trigger 8** (Trigger): *See documentation*
- **Trigger 9** (Trigger): *See documentation*
- **Trigger 10** (Trigger): *See documentation*
- **Trigger 11** (Trigger): *See documentation*
- **Trigger 12** (Trigger): *See documentation*
- **Trigger 13** (Trigger): *See documentation*
- **Trigger 14** (Trigger): *See documentation*
- **Trigger 15** (Trigger): *See documentation*
- **Trigger 16** (Trigger): *See documentation*
- **Trigger 17** (Trigger): *See documentation*
- **Trigger 18** (Trigger): *See documentation*
- **Trigger 19** (Trigger): *See documentation*
- **Trigger 20** (Trigger): *See documentation*
- **Trigger 21** (Trigger): *See documentation*
- **Trigger 22** (Trigger): *See documentation*
- **Trigger 23** (Trigger): *See documentation*
- **Trigger 24** (Trigger): *See documentation*
- **Trigger 25** (Trigger): *See documentation*
- **Trigger 26** (Trigger): *See documentation*
- **Trigger 27** (Trigger): *See documentation*
- **Trigger 28** (Trigger): *See documentation*
- **Trigger 29** (Trigger): *See documentation*
- **Trigger 30** (Trigger): *See documentation*
- **Trigger 31** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/GbEqL-)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "TimedSequence"*
**Docs:** [https://cables.gl/op/Ops.Trigger.TimedSequence](https://cables.gl/op/Ops.Trigger.TimedSequence)

---

### TimeSinceTrigger
![TimeSinceTrigger op](images/ops/Ops_Trigger_TimeSinceTrigger.svg)

**Full Name:** `Ops.Trigger.TimeSinceTrigger`
**Description:** Get the time since last trigger

**> Input Ports:**
- **Exe** (Trigger): *See documentation*
- **Trigger** (Trigger): *See documentation*
- **Reset** (Trigger): *See documentation*

**< Output Ports:**
- **Next** (Trigger): *See documentation*
- **Time** (Number): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/fCN_98)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "TimeSinceTrigger"*
**Docs:** [https://cables.gl/op/Ops.Trigger.TimeSinceTrigger](https://cables.gl/op/Ops.Trigger.TimeSinceTrigger)

---

### TriggerButton
![TriggerButton op](images/ops/Ops_Trigger_TriggerButton.svg)

**Full Name:** `Ops.Trigger.TriggerButton`
**Description:** simple button to trigger manually

**> Input Ports:**
- **Trigger** (Trigger): *See documentation*

**< Output Ports:**
- **Next** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/05Arii)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "TriggerButton"*
**Docs:** [https://cables.gl/op/Ops.Trigger.TriggerButton](https://cables.gl/op/Ops.Trigger.TriggerButton)

---

### TriggerCounter
![TriggerCounter op](images/ops/Ops_Trigger_TriggerCounter.svg)

**Full Name:** `Ops.Trigger.TriggerCounter`
**Description:** Counts how often the port was triggered

**> Input Ports:**
- **Exe** (Trigger): *See documentation*
- **Reset** (Trigger): *See documentation*

**< Output Ports:**
- **Trigger** (Trigger): *See documentation*
- **TimesTriggered** (Number): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/WNh8pc)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "TriggerCounter"*
**Docs:** [https://cables.gl/op/Ops.Trigger.TriggerCounter](https://cables.gl/op/Ops.Trigger.TriggerCounter)

---

### TriggerCounterLoop
![TriggerCounterLoop op](images/ops/Ops_Trigger_TriggerCounterLoop.svg)

**Full Name:** `Ops.Trigger.TriggerCounterLoop`
**Description:** Increments with each trigger and loops depending on min and max loop values.

**> Input Ports:**
- **Trigger In** (Trigger): *See documentation*
- **Reset** (Trigger): *See documentation*
- **Loop Min** (Number: Integer): *See documentation*
- **Loop Max** (Number: Integer): *See documentation*

**< Output Ports:**
- **Trigger Out** (Trigger): *See documentation*
- **Current Count** (Number): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/V8TekF)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "TriggerCounterLoop"*
**Docs:** [https://cables.gl/op/Ops.Trigger.TriggerCounterLoop](https://cables.gl/op/Ops.Trigger.TriggerCounterLoop)

---

### TriggerDistributeByValue
![TriggerDistributeByValue op](images/ops/Ops_Trigger_TriggerDistributeByValue.svg)

**Full Name:** `Ops.Trigger.TriggerDistributeByValue`
**Description:** triggers evenly distributed by value

**> Input Ports:**
- **Exe** (Trigger): *See documentation*
- **Number** (Number): *See documentation*
- **Max** (Number): *See documentation*
- **Num Outputs** (Number): *See documentation*

**< Output Ports:**
- **Num** (Number): *See documentation*
- **Trigger 0** (Trigger): *See documentation*
- **Trigger 1** (Trigger): *See documentation*
- **Trigger 2** (Trigger): *See documentation*
- **Trigger 3** (Trigger): *See documentation*
- **Trigger 4** (Trigger): *See documentation*
- **Trigger 5** (Trigger): *See documentation*
- **Trigger 6** (Trigger): *See documentation*
- **Trigger 7** (Trigger): *See documentation*
- **Trigger 8** (Trigger): *See documentation*
- **Trigger 9** (Trigger): *See documentation*
- **Trigger 10** (Trigger): *See documentation*
- **Trigger 11** (Trigger): *See documentation*
- **Trigger 12** (Trigger): *See documentation*
- **Trigger 13** (Trigger): *See documentation*
- **Trigger 14** (Trigger): *See documentation*
- **Trigger 15** (Trigger): *See documentation*
- **Trigger 16** (Trigger): *See documentation*
- **Trigger 17** (Trigger): *See documentation*
- **Trigger 18** (Trigger): *See documentation*
- **Trigger 19** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/FsZFVB)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "TriggerDistributeByValue"*
**Docs:** [https://cables.gl/op/Ops.Trigger.TriggerDistributeByValue](https://cables.gl/op/Ops.Trigger.TriggerDistributeByValue)

---

### TriggerExtender
![TriggerExtender op](images/ops/Ops_Trigger_TriggerExtender.svg)

**Full Name:** `Ops.Trigger.TriggerExtender`
**Description:** Extends a trigger (useful in big patches for better overview)

**> Input Ports:**
- **Execute** (Trigger): *See documentation*

**< Output Ports:**
- **Next** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/mDiCq6)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "TriggerExtender"*
**Docs:** [https://cables.gl/op/Ops.Trigger.TriggerExtender](https://cables.gl/op/Ops.Trigger.TriggerExtender)

---

### TriggerIfDecreased
![TriggerIfDecreased op](images/ops/Ops_Trigger_TriggerIfDecreased.svg)

**Full Name:** `Ops.Trigger.TriggerIfDecreased`
**Description:** trigger if a value decreases / gets smaller

**> Input Ports:**
- **Value** (Number): *See documentation*

**< Output Ports:**
- **Trigger** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/AFiCfe)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "TriggerIfDecreased"*
**Docs:** [https://cables.gl/op/Ops.Trigger.TriggerIfDecreased](https://cables.gl/op/Ops.Trigger.TriggerIfDecreased)

---

### TriggerIfIncreased
![TriggerIfIncreased op](images/ops/Ops_Trigger_TriggerIfIncreased.svg)

**Full Name:** `Ops.Trigger.TriggerIfIncreased`
**Description:** Outputs a trigger if the value of a number increases

**> Input Ports:**
- **Value** (Number): *See documentation*

**< Output Ports:**
- **Trigger** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/AFiCfe)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "TriggerIfIncreased"*
**Docs:** [https://cables.gl/op/Ops.Trigger.TriggerIfIncreased](https://cables.gl/op/Ops.Trigger.TriggerIfIncreased)

---

### TriggerLimiter
![TriggerLimiter op](images/ops/Ops_Trigger_TriggerLimiter.svg)

**Full Name:** `Ops.Trigger.TriggerLimiter`
**Description:** Limits how often a trigger goes through to x ms

**> Input Ports:**
- **In Trigger** (Trigger): *See documentation*
- **Milliseconds** (Number): *See documentation*

**< Output Ports:**
- **Out Trigger** (Trigger): *See documentation*
- **Progress** (Number): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/dS8EQm)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "TriggerLimiter"*
**Docs:** [https://cables.gl/op/Ops.Trigger.TriggerLimiter](https://cables.gl/op/Ops.Trigger.TriggerLimiter)

---

### TriggerNumber
![TriggerNumber op](images/ops/Ops_Trigger_TriggerNumber.svg)

**Full Name:** `Ops.Trigger.TriggerNumber`
**Description:** Outputs a number when triggered

**> Input Ports:**
- **Set** (Trigger): *See documentation*
- **Number** (Number): *See documentation*

**< Output Ports:**
- **Next** (Trigger): *See documentation*
- **Out Value** (Number): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/Qq3Y7i)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "TriggerNumber"*
**Docs:** [https://cables.gl/op/Ops.Trigger.TriggerNumber](https://cables.gl/op/Ops.Trigger.TriggerNumber)

---

### TriggerOnce
![TriggerOnce op](images/ops/Ops_Trigger_TriggerOnce.svg)

**Full Name:** `Ops.Trigger.TriggerOnce`
**Description:** Trigger the following children once

**> Input Ports:**
- **Exec** (Trigger): *See documentation*
- **Reset** (Trigger): *See documentation*

**< Output Ports:**
- **Next** (Trigger): *See documentation*
- **Was Triggered** (Number): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/9Eiyci)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "TriggerOnce"*
**Docs:** [https://cables.gl/op/Ops.Trigger.TriggerOnce](https://cables.gl/op/Ops.Trigger.TriggerOnce)

---

### TriggerOnChangeArray_v2
![TriggerOnChangeArray_v2 op](images/ops/Ops_Trigger_TriggerOnChangeArray_v2.svg)

**Full Name:** `Ops.Trigger.TriggerOnChangeArray_v2`
**Description:** triggers when array has changed

**> Input Ports:**
- **Array** (Array): *See documentation*

**< Output Ports:**
- **Changed** (Trigger): *See documentation*
- **Result** (Array): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Trigger.TriggerOnChangeArray_v2#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "TriggerOnChangeArray_v2"*
**Docs:** [https://cables.gl/op/Ops.Trigger.TriggerOnChangeArray_v2](https://cables.gl/op/Ops.Trigger.TriggerOnChangeArray_v2)

---

### TriggerOnChangeObject_v2
![TriggerOnChangeObject_v2 op](images/ops/Ops_Trigger_TriggerOnChangeObject_v2.svg)

**Full Name:** `Ops.Trigger.TriggerOnChangeObject_v2`
**Description:** triggers when Object has changed

**> Input Ports:**
- **Object** (Object): *See documentation*

**< Output Ports:**
- **Changed** (Trigger): *See documentation*
- **Result** (Object): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Trigger.TriggerOnChangeObject_v2#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "TriggerOnChangeObject_v2"*
**Docs:** [https://cables.gl/op/Ops.Trigger.TriggerOnChangeObject_v2](https://cables.gl/op/Ops.Trigger.TriggerOnChangeObject_v2)

---

### TriggerOnChangeString_v2
![TriggerOnChangeString_v2 op](images/ops/Ops_Trigger_TriggerOnChangeString_v2.svg)

**Full Name:** `Ops.Trigger.TriggerOnChangeString_v2`
**Description:** triggers when string has changed

**> Input Ports:**
- **String** (String): *See documentation*

**< Output Ports:**
- **Changed** (Trigger): *See documentation*
- **Result** (String): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/ohxBci)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "TriggerOnChangeString_v2"*
**Docs:** [https://cables.gl/op/Ops.Trigger.TriggerOnChangeString_v2](https://cables.gl/op/Ops.Trigger.TriggerOnChangeString_v2)

---

### TriggerOnChangeTexture
![TriggerOnChangeTexture op](images/ops/Ops_Trigger_TriggerOnChangeTexture.svg)

**Full Name:** `Ops.Trigger.TriggerOnChangeTexture`
**Description:** triggers when texture has changed

**> Input Ports:**
- **Texture** (Object:Texture): *See documentation*

**< Output Ports:**
- **Changed** (Trigger): *See documentation*
- **Result** (Object): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/QGqQ7f)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "TriggerOnChangeTexture"*
**Docs:** [https://cables.gl/op/Ops.Trigger.TriggerOnChangeTexture](https://cables.gl/op/Ops.Trigger.TriggerOnChangeTexture)

---

### TriggerReceive
![TriggerReceive op](images/ops/Ops_Trigger_TriggerReceive.svg)

**Full Name:** `Ops.Trigger.TriggerReceive`
**Description:** Receives triggers from a TriggerSend op with the same variable name

**> Input Ports:**
- *Visit [Ops.Trigger.TriggerReceive documentation](https://cables.gl/op/Ops.Trigger.TriggerReceive) for input port details*

**< Output Ports:**
- **Triggered** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/hrXVpH)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "TriggerReceive"*
**Docs:** [https://cables.gl/op/Ops.Trigger.TriggerReceive](https://cables.gl/op/Ops.Trigger.TriggerReceive)

---

### TriggerReceiveFilter
![TriggerReceiveFilter op](images/ops/Ops_Trigger_TriggerReceiveFilter.svg)

**Full Name:** `Ops.Trigger.TriggerReceiveFilter`
**Description:** receives all named trigges and relays them, optionally using a filter-prefix on the name

**> Input Ports:**
- **Prefix** (String): *See documentation*

**< Output Ports:**
- **Trigger Out** (Trigger): *See documentation*
- **Trigger Name** (String): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/niHmJt)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "TriggerReceiveFilter"*
**Docs:** [https://cables.gl/op/Ops.Trigger.TriggerReceiveFilter](https://cables.gl/op/Ops.Trigger.TriggerReceiveFilter)

---

### TriggerSend
![TriggerSend op](images/ops/Ops_Trigger_TriggerSend.svg)

**Full Name:** `Ops.Trigger.TriggerSend`
**Description:** Allows triggers to be sent to a TriggerReceive op with the same variable name

**> Input Ports:**
- **Trigger** (Trigger): *See documentation*

**< Output Ports:**
- **Next** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/hrXVpH)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "TriggerSend"*
**Docs:** [https://cables.gl/op/Ops.Trigger.TriggerSend](https://cables.gl/op/Ops.Trigger.TriggerSend)

---

### TriggerSendNamed
![TriggerSendNamed op](images/ops/Ops_Trigger_TriggerSendNamed.svg)

**Full Name:** `Ops.Trigger.TriggerSendNamed`
**Description:** Allows triggers to be sent to a TriggerReceive op with the same variable name

**> Input Ports:**
- **Trigger** (Trigger): *See documentation*
- **Named Trigger** (String): *See documentation*

**< Output Ports:**
- *Visit [Ops.Trigger.TriggerSendNamed documentation](https://cables.gl/op/Ops.Trigger.TriggerSendNamed) for output port details*

**Example Patch:** [Open in Editor](https://cables.gl/edit/Tc3pcI)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "TriggerSendNamed"*
**Docs:** [https://cables.gl/op/Ops.Trigger.TriggerSendNamed](https://cables.gl/op/Ops.Trigger.TriggerSendNamed)

---

### TriggersPerSecond
![TriggersPerSecond op](images/ops/Ops_Trigger_TriggersPerSecond.svg)

**Full Name:** `Ops.Trigger.TriggersPerSecond`
**Description:** Counts how often the port is triggered per second

**> Input Ports:**
- **Exe** (Trigger): *See documentation*

**< Output Ports:**
- **Cps** (Number): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/JCkpVJ)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "TriggersPerSecond"*
**Docs:** [https://cables.gl/op/Ops.Trigger.TriggersPerSecond](https://cables.gl/op/Ops.Trigger.TriggersPerSecond)

---

### TriggerString
![TriggerString op](images/ops/Ops_Trigger_TriggerString.svg)

**Full Name:** `Ops.Trigger.TriggerString`
**Description:** trigger a string

**> Input Ports:**
- **Trigger** (Trigger): *See documentation*
- **String** (String): *See documentation*

**< Output Ports:**
- **Next** (Trigger): *See documentation*
- **Result** (String): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/VHsHue)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "TriggerString"*
**Docs:** [https://cables.gl/op/Ops.Trigger.TriggerString](https://cables.gl/op/Ops.Trigger.TriggerString)

---

### ValueBecameZeroTrigger
![ValueBecameZeroTrigger op](images/ops/Ops_Trigger_ValueBecameZeroTrigger.svg)

**Full Name:** `Ops.Trigger.ValueBecameZeroTrigger`
**Description:** Triggers when the input value became zero

**> Input Ports:**
- **Value** (Number): *See documentation*

**< Output Ports:**
- **Became Zero Trigger** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Trigger.ValueBecameZeroTrigger#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ValueBecameZeroTrigger"*
**Docs:** [https://cables.gl/op/Ops.Trigger.ValueBecameZeroTrigger](https://cables.gl/op/Ops.Trigger.ValueBecameZeroTrigger)

---

