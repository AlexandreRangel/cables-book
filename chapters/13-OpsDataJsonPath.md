# Ops.Data.JsonPath


```{=latex}
\OpsSubsubNoSubsectionNumbering\setcounter{subsubsection}{0}
```
### ArrayGetArrayByPath
![ArrayGetArrayByPath op](images/ops/Ops_Data_JsonPath_ArrayGetArrayByPath.svg)

**Full Name:** `Ops.Data.JsonPath.ArrayGetArrayByPath`

returns the array at the position defined by a path.

**`\inputsymbol`{=latex} Inputs**

- **Array** (Array)
- **Path** (String)
- **path to array** (i.e. data.numbers)

**`\outputsymbol`{=latex} Output**

- **Found** (booleanNumber)

**Example:** [cables.gl/edit/uqXSWr](https://cables.gl/edit/uqXSWr)

**Doc:** [cables.gl/op/Ops.Data.JsonPath.ArrayGetArrayByPath](https://cables.gl/op/Ops.Data.JsonPath.ArrayGetArrayByPath)

### ArrayGetArrayValuesByPath
![ArrayGetArrayValuesByPath op](images/ops/Ops_Data_JsonPath_ArrayGetArrayValuesByPath.svg)

**Full Name:** `Ops.Data.JsonPath.ArrayGetArrayValuesByPath`

Outputs all the values of the properties of an array of objects given a path.

**`\inputsymbol`{=latex} Inputs**

- **Array** (Array)
- **Path** (String)
- **path to first array field** (i.e. "data.0.firstName")

**`\outputsymbol`{=latex} Output**

- **Found** (booleanNumber)

**Example:** [cables.gl/edit/Y3pXWr](https://cables.gl/edit/Y3pXWr)

**Doc:** [cables.gl/op/Ops.Data.JsonPath.ArrayGetArrayValuesByPath](https://cables.gl/op/Ops.Data.JsonPath.ArrayGetArrayValuesByPath)

### ArrayGetNumberByPath
![ArrayGetNumberByPath op](images/ops/Ops_Data_JsonPath_ArrayGetNumberByPath.svg)

**Full Name:** `Ops.Data.JsonPath.ArrayGetNumberByPath`

finds a number at a position in an array defined by path.

**`\inputsymbol`{=latex} Inputs**

- **Array** (Array)
- **Path** (String)
- **the past** (i.e. person.age)

**`\outputsymbol`{=latex} Output**

- **Found** (booleanNumber)

**Example:** [cables.gl/edit/7kSVWr](https://cables.gl/edit/7kSVWr)

**Doc:** [cables.gl/op/Ops.Data.JsonPath.ArrayGetNumberByPath](https://cables.gl/op/Ops.Data.JsonPath.ArrayGetNumberByPath)

### ArrayGetObjectByPath
![ArrayGetObjectByPath op](images/ops/Ops_Data_JsonPath_ArrayGetObjectByPath.svg)

**Full Name:** `Ops.Data.JsonPath.ArrayGetObjectByPath`

Returns the object at the position defined by a path.

**`\inputsymbol`{=latex} Inputs**

- **Array** (Array)
- **Path** (String)

**`\outputsymbol`{=latex} Output**

- **Found** (booleanNumber)

**Example:** [cables.gl/edit/AapUWr](https://cables.gl/edit/AapUWr)

**Doc:** [cables.gl/op/Ops.Data.JsonPath.ArrayGetObjectByPath](https://cables.gl/op/Ops.Data.JsonPath.ArrayGetObjectByPath)

### ArrayGetStringByPath_v2
![ArrayGetStringByPath_v2 op](images/ops/Ops_Data_JsonPath_ArrayGetStringByPath_v2.svg)

**Full Name:** `Ops.Data.JsonPath.ArrayGetStringByPath_v2`

Finds a string at a position in an array defined by path.

**`\inputsymbol`{=latex} Inputs**

- **Array** (Array)
- **Path** (String)
- **the path** (i.e. data.names)
- **Return Path If Missing** (Number: Boolean)

**`\outputsymbol`{=latex} Output**

- **Found** (booleanNumber)

**Example:** [cables.gl/edit/rs0XWr](https://cables.gl/edit/rs0XWr)

**Doc:** [cables.gl/op/Ops.Data.JsonPath.ArrayGetStringByPath_v2](https://cables.gl/op/Ops.Data.JsonPath.ArrayGetStringByPath_v2)

### ObjectGetArrayByPath
![ObjectGetArrayByPath op](images/ops/Ops_Data_JsonPath_ObjectGetArrayByPath.svg)

**Full Name:** `Ops.Data.JsonPath.ObjectGetArrayByPath`

returns the array at the position defined by a path.

**`\inputsymbol`{=latex} Inputs**

- **Object** (Object)
- **Path** (String)
- **path to array** (i.e. data.numbers)

**`\outputsymbol`{=latex} Output**

- **Found** (booleanNumber)

**Example:** [cables.gl/edit/oghmln](https://cables.gl/edit/oghmln)

**Doc:** [cables.gl/op/Ops.Data.JsonPath.ObjectGetArrayByPath](https://cables.gl/op/Ops.Data.JsonPath.ObjectGetArrayByPath)

### ObjectGetArrayValuesByPath
![ObjectGetArrayValuesByPath op](images/ops/Ops_Data_JsonPath_ObjectGetArrayValuesByPath.svg)

**Full Name:** `Ops.Data.JsonPath.ObjectGetArrayValuesByPath`

Outputs all the values of the properties of an array of objects given a path.

**`\inputsymbol`{=latex} Inputs**

- **Object** (Object)
- **Path** (String)
- **path to first array field** (i.e. "data.0.firstName")

**`\outputsymbol`{=latex} Output**

- **Found** (booleanNumber)

**Example:** [cables.gl/edit/fBcgln](https://cables.gl/edit/fBcgln)

**Doc:** [cables.gl/op/Ops.Data.JsonPath.ObjectGetArrayValuesByPath](https://cables.gl/op/Ops.Data.JsonPath.ObjectGetArrayValuesByPath)

### ObjectGetNumberByPath
![ObjectGetNumberByPath op](images/ops/Ops_Data_JsonPath_ObjectGetNumberByPath.svg)

**Full Name:** `Ops.Data.JsonPath.ObjectGetNumberByPath`

finds a number at a position in an object defined by path.

**`\inputsymbol`{=latex} Inputs**

- **Object** (Object)
- **Path** (String)
- **the past** (i.e. person.age)

**`\outputsymbol`{=latex} Output**

- **Found** (booleanNumber)

**Example:** [cables.gl/edit/RrYnln](https://cables.gl/edit/RrYnln)

**Doc:** [cables.gl/op/Ops.Data.JsonPath.ObjectGetNumberByPath](https://cables.gl/op/Ops.Data.JsonPath.ObjectGetNumberByPath)

### ObjectGetObjectByPath
![ObjectGetObjectByPath op](images/ops/Ops_Data_JsonPath_ObjectGetObjectByPath.svg)

**Full Name:** `Ops.Data.JsonPath.ObjectGetObjectByPath`

Returns the object at the position defined by a path.

**`\inputsymbol`{=latex} Inputs**

- **Object** (Object)
- **Path** (String)

**`\outputsymbol`{=latex} Output**

- **Found** (booleanNumber)

**Example:** [cables.gl/edit/-Zlrln](https://cables.gl/edit/-Zlrln)

**Doc:** [cables.gl/op/Ops.Data.JsonPath.ObjectGetObjectByPath](https://cables.gl/op/Ops.Data.JsonPath.ObjectGetObjectByPath)

### ObjectGetStringByPath_v2
![ObjectGetStringByPath_v2 op](images/ops/Ops_Data_JsonPath_ObjectGetStringByPath_v2.svg)

**Full Name:** `Ops.Data.JsonPath.ObjectGetStringByPath_v2`

Finds a string at a position in an object defined by path.

**`\inputsymbol`{=latex} Inputs**

- **Object** (Object)
- **Path** (String)
- **the path** (i.e. data.names)
- **Output Path If Missing** (Number: Boolean)

**`\outputsymbol`{=latex} Output**

- **Found** (booleanNumber)

**Example:** [cables.gl/edit/eJIqln](https://cables.gl/edit/eJIqln)

**Doc:** [cables.gl/op/Ops.Data.JsonPath.ObjectGetStringByPath_v2](https://cables.gl/op/Ops.Data.JsonPath.ObjectGetStringByPath_v2)


