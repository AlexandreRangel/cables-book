# Ops.String.Base64


```{=latex}
\OpsSubsubNoSubsectionNumbering\setcounter{subsubsection}{0}
```
### Base64Decode_v2
![Base64Decode_v2 op](images/ops/Ops_String_Base64_Base64Decode_v2.svg)

**Full Name:** `Ops.String.Base64.Base64Decode_v2`

decode a string to base64.

**`\inputsymbol`{=latex} Inputs**

- **String** (String)

**`\outputsymbol`{=latex} Output**

- **Result** (String)

**Example Patch:** [cables.gl/op/Ops.String.Base64.Base64Decode_v2#example](https://cables.gl/op/Ops.String.Base64.Base64Decode_v2#example)

**Doc:** [cables.gl/op/Ops.String.Base64.Base64Decode_v2](https://cables.gl/op/Ops.String.Base64.Base64Decode_v2)

### Base64Encode_v3
![Base64Encode_v3 op](images/ops/Ops_String_Base64_Base64Encode_v3.svg)

**Full Name:** `Ops.String.Base64.Base64Encode_v3`

encode a string to base64.

**`\inputsymbol`{=latex} Inputs**

- **String** (String)
- **MimeType** (String)

**`\outputsymbol`{=latex} Output**

- **Result** (String)

**Example Patch:** [cables.gl/op/Ops.String.Base64.Base64Encode_v3#example](https://cables.gl/op/Ops.String.Base64.Base64Encode_v3#example)

**Doc:** [cables.gl/op/Ops.String.Base64.Base64Encode_v3](https://cables.gl/op/Ops.String.Base64.Base64Encode_v3)

### DownloadBase64File
![DownloadBase64File op](images/ops/Ops_String_Base64_DownloadBase64File.svg)

**Full Name:** `Ops.String.Base64.DownloadBase64File`

trigger a download of a base64 binary file.

**`\inputsymbol`{=latex} Inputs**

- **Data URL** (String)
- **Filename** (String)
- **Download** (Trigger)

**`\outputsymbol`{=latex} Output**

- **Next** (Trigger)

**Example Patch:** [cables.gl/edit/jE9zO8](https://cables.gl/edit/jE9zO8)

**Doc:** [cables.gl/op/Ops.String.Base64.DownloadBase64File](https://cables.gl/op/Ops.String.Base64.DownloadBase64File)


