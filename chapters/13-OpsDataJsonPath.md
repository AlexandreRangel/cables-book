# Ops.Data.JsonPath

*Part of the [All Operators Reference](13-_AllOps.md)*

---

## Ops.Data.JsonPath

### ArrayGetArrayByPath
![ArrayGetArrayByPath op](images/ops/Ops_Data_JsonPath_ArrayGetArrayByPath.svg)

**Full Name:** `Ops.Data.JsonPath.ArrayGetArrayByPath`
**Description:** returns the array at the position defined by a path

**> Input Ports:**

- **Array** (Array)
- **Path** (String)
- **path to array** (i.e. data.numbers)

**< Output Ports:**

- **Found** (booleanNumber)

**Example Patch:** [Open in Editor](https://cables.gl/edit/uqXSWr)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ArrayGetArrayByPath"*
**Docs:** [https://cables.gl/op/Ops.Data.JsonPath.ArrayGetArrayByPath](https://cables.gl/op/Ops.Data.JsonPath.ArrayGetArrayByPath)

---

### ArrayGetArrayValuesByPath
![ArrayGetArrayValuesByPath op](images/ops/Ops_Data_JsonPath_ArrayGetArrayValuesByPath.svg)

**Full Name:** `Ops.Data.JsonPath.ArrayGetArrayValuesByPath`
**Description:** Outputs all the values of the properties of an array of objects given a path

**> Input Ports:**

- **Array** (Array)
- **Path** (String)
- **path to first array field** (i.e. "data.0.firstName")

**< Output Ports:**

- **Found** (booleanNumber)

**Example Patch:** [Open in Editor](https://cables.gl/edit/Y3pXWr)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ArrayGetArrayValuesByPath"*
**Docs:** [https://cables.gl/op/Ops.Data.JsonPath.ArrayGetArrayValuesByPath](https://cables.gl/op/Ops.Data.JsonPath.ArrayGetArrayValuesByPath)

---

### ArrayGetNumberByPath
![ArrayGetNumberByPath op](images/ops/Ops_Data_JsonPath_ArrayGetNumberByPath.svg)

**Full Name:** `Ops.Data.JsonPath.ArrayGetNumberByPath`
**Description:** finds a number at a position in an array defined by path

**> Input Ports:**

- **Array** (Array)
- **Path** (String)
- **the past** (i.e. person.age)

**< Output Ports:**

- **Found** (booleanNumber)

**Example Patch:** [Open in Editor](https://cables.gl/edit/7kSVWr)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ArrayGetNumberByPath"*
**Docs:** [https://cables.gl/op/Ops.Data.JsonPath.ArrayGetNumberByPath](https://cables.gl/op/Ops.Data.JsonPath.ArrayGetNumberByPath)

---

### ArrayGetObjectByPath
![ArrayGetObjectByPath op](images/ops/Ops_Data_JsonPath_ArrayGetObjectByPath.svg)

**Full Name:** `Ops.Data.JsonPath.ArrayGetObjectByPath`
**Description:** Returns the object at the position defined by a path

**> Input Ports:**

- **Array** (Array)
- **Path** (String)

**< Output Ports:**

- **Found** (booleanNumber)

**Example Patch:** [Open in Editor](https://cables.gl/edit/AapUWr)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ArrayGetObjectByPath"*
**Docs:** [https://cables.gl/op/Ops.Data.JsonPath.ArrayGetObjectByPath](https://cables.gl/op/Ops.Data.JsonPath.ArrayGetObjectByPath)

---

### ArrayGetStringByPath_v2
![ArrayGetStringByPath_v2 op](images/ops/Ops_Data_JsonPath_ArrayGetStringByPath_v2.svg)

**Full Name:** `Ops.Data.JsonPath.ArrayGetStringByPath_v2`
**Description:** Finds a string at a position in an array defined by path

**> Input Ports:**

- **Array** (Array)
- **Path** (String)
- **the path** (i.e. data.names)
- **Return Path If Missing** (Number: Boolean)

**< Output Ports:**

- **Found** (booleanNumber)

**Example Patch:** [Open in Editor](https://cables.gl/edit/rs0XWr)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ArrayGetStringByPath_v2"*
**Docs:** [https://cables.gl/op/Ops.Data.JsonPath.ArrayGetStringByPath_v2](https://cables.gl/op/Ops.Data.JsonPath.ArrayGetStringByPath_v2)

---

### ObjectGetArrayByPath
![ObjectGetArrayByPath op](images/ops/Ops_Data_JsonPath_ObjectGetArrayByPath.svg)

**Full Name:** `Ops.Data.JsonPath.ObjectGetArrayByPath`
**Description:** returns the array at the position defined by a path

**> Input Ports:**

- **Object** (Object)
- **Path** (String)
- **path to array** (i.e. data.numbers)

**< Output Ports:**

- **Found** (booleanNumber)

**Example Patch:** [Open in Editor](https://cables.gl/edit/oghmln)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ObjectGetArrayByPath"*
**Docs:** [https://cables.gl/op/Ops.Data.JsonPath.ObjectGetArrayByPath](https://cables.gl/op/Ops.Data.JsonPath.ObjectGetArrayByPath)

---

### ObjectGetArrayValuesByPath
![ObjectGetArrayValuesByPath op](images/ops/Ops_Data_JsonPath_ObjectGetArrayValuesByPath.svg)

**Full Name:** `Ops.Data.JsonPath.ObjectGetArrayValuesByPath`
**Description:** Outputs all the values of the properties of an array of objects given a path

**> Input Ports:**

- **Object** (Object)
- **Path** (String)
- **path to first array field** (i.e. "data.0.firstName")

**< Output Ports:**

- **Found** (booleanNumber)

**Example Patch:** [Open in Editor](https://cables.gl/edit/fBcgln)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ObjectGetArrayValuesByPath"*
**Docs:** [https://cables.gl/op/Ops.Data.JsonPath.ObjectGetArrayValuesByPath](https://cables.gl/op/Ops.Data.JsonPath.ObjectGetArrayValuesByPath)

---

### ObjectGetNumberByPath
![ObjectGetNumberByPath op](images/ops/Ops_Data_JsonPath_ObjectGetNumberByPath.svg)

**Full Name:** `Ops.Data.JsonPath.ObjectGetNumberByPath`
**Description:** finds a number at a position in an object defined by path

**> Input Ports:**

- **Object** (Object)
- **Path** (String)
- **the past** (i.e. person.age)

**< Output Ports:**

- **Found** (booleanNumber)

**Example Patch:** [Open in Editor](https://cables.gl/edit/RrYnln)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ObjectGetNumberByPath"*
**Docs:** [https://cables.gl/op/Ops.Data.JsonPath.ObjectGetNumberByPath](https://cables.gl/op/Ops.Data.JsonPath.ObjectGetNumberByPath)

---

### ObjectGetObjectByPath
![ObjectGetObjectByPath op](images/ops/Ops_Data_JsonPath_ObjectGetObjectByPath.svg)

**Full Name:** `Ops.Data.JsonPath.ObjectGetObjectByPath`
**Description:** Returns the object at the position defined by a path

**> Input Ports:**

- **Object** (Object)
- **Path** (String)

**< Output Ports:**

- **Found** (booleanNumber)

**Example Patch:** [Open in Editor](https://cables.gl/edit/-Zlrln)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ObjectGetObjectByPath"*
**Docs:** [https://cables.gl/op/Ops.Data.JsonPath.ObjectGetObjectByPath](https://cables.gl/op/Ops.Data.JsonPath.ObjectGetObjectByPath)

---

### ObjectGetStringByPath_v2
![ObjectGetStringByPath_v2 op](images/ops/Ops_Data_JsonPath_ObjectGetStringByPath_v2.svg)

**Full Name:** `Ops.Data.JsonPath.ObjectGetStringByPath_v2`
**Description:** Finds a string at a position in an object defined by path

**> Input Ports:**

- **Object** (Object)
- **Path** (String)
- **the path** (i.e. data.names)
- **Output Path If Missing** (Number: Boolean)

**< Output Ports:**

- **Found** (booleanNumber)

**Example Patch:** [Open in Editor](https://cables.gl/edit/eJIqln)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ObjectGetStringByPath_v2"*
**Docs:** [https://cables.gl/op/Ops.Data.JsonPath.ObjectGetStringByPath_v2](https://cables.gl/op/Ops.Data.JsonPath.ObjectGetStringByPath_v2)

---

