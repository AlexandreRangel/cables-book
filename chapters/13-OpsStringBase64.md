# Ops.String.Base64

*Part of the [All Operators Reference](13-_AllOps.md)*

---

## Ops.String.Base64

### Base64Decode_v2
![Base64Decode_v2 op](images/ops/Ops_String_Base64_Base64Decode_v2.svg)

**Full Name:** `Ops.String.Base64.Base64Decode_v2`
**Description:** decode a string to base64

**> Input Ports:**
- **String** (String)

**< Output Ports:**
- **Result** (String)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.String.Base64.Base64Decode_v2#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "Base64Decode_v2"*
**Docs:** [https://cables.gl/op/Ops.String.Base64.Base64Decode_v2](https://cables.gl/op/Ops.String.Base64.Base64Decode_v2)

---

### Base64Encode_v3
![Base64Encode_v3 op](images/ops/Ops_String_Base64_Base64Encode_v3.svg)

**Full Name:** `Ops.String.Base64.Base64Encode_v3`
**Description:** encode a string to base64

**> Input Ports:**
- **String** (String)
- **MimeType** (String)

**< Output Ports:**
- **Result** (String)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.String.Base64.Base64Encode_v3#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "Base64Encode_v3"*
**Docs:** [https://cables.gl/op/Ops.String.Base64.Base64Encode_v3](https://cables.gl/op/Ops.String.Base64.Base64Encode_v3)

---

### DownloadBase64File
![DownloadBase64File op](images/ops/Ops_String_Base64_DownloadBase64File.svg)

**Full Name:** `Ops.String.Base64.DownloadBase64File`
**Description:** trigger a download of a base64 binary file

**> Input Ports:**
- **Data URL** (String)
- **Filename** (String)
- **Download** (Trigger)

**< Output Ports:**
- **Next** (Trigger)

**Example Patch:** [Open in Editor](https://cables.gl/edit/jE9zO8)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "DownloadBase64File"*
**Docs:** [https://cables.gl/op/Ops.String.Base64.DownloadBase64File](https://cables.gl/op/Ops.String.Base64.DownloadBase64File)

---

