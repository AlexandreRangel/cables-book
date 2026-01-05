# Ops.Data.Compose.String

---

## Ops.Data.Compose.String

### CompString
![CompString op](images/ops/Ops_Data_Compose_String_CompString.svg)

**Full Name:** `Ops.Data.Compose.String.CompString`

**Description:** Compose a string

**`\inputsymbol`{=latex} Input Ports:**

- **Update** (Trigger)
- **Clear** (Number: Boolean)
- **Reset** (Trigger)

**`\outputsymbol`{=latex} Output Ports:**

- **Next** (Trigger)
- **Result** (String)

**Example Patch:** [Open in Editor](https://cables.gl/edit/GUpzJB)

**Docs:** [https://cables.gl/op/Ops.Data.Compose.String.CompString](https://cables.gl/op/Ops.Data.Compose.String.CompString)

### CompStringAppend
![CompStringAppend op](images/ops/Ops_Data_Compose_String_CompStringAppend.svg)

**Full Name:** `Ops.Data.Compose.String.CompStringAppend`

**Description:** Append a string to a string

**`\inputsymbol`{=latex} Input Ports:**

- **Update** (Trigger)
- **String** (String)
- **Add Break** (Number: Boolean)

**`\outputsymbol`{=latex} Output Ports:**

- **Next** (Trigger)

**Example Patch:** [Open in Editor](https://cables.gl/edit/Yqj7eG)

**Docs:** [https://cables.gl/op/Ops.Data.Compose.String.CompStringAppend](https://cables.gl/op/Ops.Data.Compose.String.CompStringAppend)

### CompStringShorten
![CompStringShorten op](images/ops/Ops_Data_Compose_String_CompStringShorten.svg)

**Full Name:** `Ops.Data.Compose.String.CompStringShorten`

**Description:** Remove characters from the beginning or end of a string

**`\inputsymbol`{=latex} Input Ports:**

- **Update** (Trigger)
- **Direction Index** (Number: Integer)
- **Num Chars** (Number: Integer)

**`\outputsymbol`{=latex} Output Ports:**

- **Next** (Trigger)

**Example Patch:** [Open in Editor](https://cables.gl/edit/Yqj7eG)

**Docs:** [https://cables.gl/op/Ops.Data.Compose.String.CompStringShorten](https://cables.gl/op/Ops.Data.Compose.String.CompStringShorten)


