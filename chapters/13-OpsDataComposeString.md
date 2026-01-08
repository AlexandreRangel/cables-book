# Ops.Data.Compose.String


```{=latex}
\OpsSubsubNoSubsectionNumbering\setcounter{subsubsection}{0}
```
### CompString
![CompString op](images/ops/Ops_Data_Compose_String_CompString.svg)

**Full Name:** `Ops.Data.Compose.String.CompString`

Compose a string.

**`\inputsymbol`{=latex} Inputs**

- **Update** (Trigger)
- **Clear** (Number: Boolean)
- **Reset** (Trigger)

**`\outputsymbol`{=latex} Output**

- **Next** (Trigger)
- **Result** (String)

**Example Patch:** [cables.gl/edit/GUpzJB](https://cables.gl/edit/GUpzJB)

**Doc:** [cables.gl/op/Ops.Data.Compose.String.CompString](https://cables.gl/op/Ops.Data.Compose.String.CompString)

### CompStringAppend
![CompStringAppend op](images/ops/Ops_Data_Compose_String_CompStringAppend.svg)

**Full Name:** `Ops.Data.Compose.String.CompStringAppend`

Append a string to a string.

**`\inputsymbol`{=latex} Inputs**

- **Update** (Trigger)
- **String** (String)
- **Add Break** (Number: Boolean)

**`\outputsymbol`{=latex} Output**

- **Next** (Trigger)

**Example Patch:** [cables.gl/edit/Yqj7eG](https://cables.gl/edit/Yqj7eG)

**Doc:** [cables.gl/op/Ops.Data.Compose.String.CompStringAppend](https://cables.gl/op/Ops.Data.Compose.String.CompStringAppend)

### CompStringShorten
![CompStringShorten op](images/ops/Ops_Data_Compose_String_CompStringShorten.svg)

**Full Name:** `Ops.Data.Compose.String.CompStringShorten`

Remove characters from the beginning or end of a string.

**`\inputsymbol`{=latex} Inputs**

- **Update** (Trigger)
- **Direction Index** (Number: Integer)
- **Num Chars** (Number: Integer)

**`\outputsymbol`{=latex} Output**

- **Next** (Trigger)

**Example Patch:** [cables.gl/edit/Yqj7eG](https://cables.gl/edit/Yqj7eG)

**Doc:** [cables.gl/op/Ops.Data.Compose.String.CompStringShorten](https://cables.gl/op/Ops.Data.Compose.String.CompStringShorten)


