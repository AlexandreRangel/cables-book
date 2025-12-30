# Ops.Cables

*Part of the [All Operators Reference](13-_AllOps.md)*

---

## Ops.Cables

### AssetPathURL
![AssetPathURL op](images/ops/Ops_Cables_AssetPathURL.svg)

**Full Name:** `Ops.Cables.AssetPathURL`
**Description:** outputs the path to the assets

**> Input Ports:**
- **Filename** (String): *See documentation*

**< Output Ports:**
- **Path** (String): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/mwhthf)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "AssetPathURL"*
**Docs:** [https://cables.gl/op/Ops.Cables.AssetPathURL](https://cables.gl/op/Ops.Cables.AssetPathURL)

---

### CablesInfo
![CablesInfo op](images/ops/Ops_Cables_CablesInfo.svg)

**Full Name:** `Ops.Cables.CablesInfo`
**Description:** Output the cables URL of the current editor environment

**> Input Ports:**
- *Visit [Ops.Cables.CablesInfo documentation](https://cables.gl/op/Ops.Cables.CablesInfo) for input port details*

**< Output Ports:**
- **URL** (String): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/vaK7iO)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "CablesInfo"*
**Docs:** [https://cables.gl/op/Ops.Cables.CablesInfo](https://cables.gl/op/Ops.Cables.CablesInfo)

---

### CallBack_v2
![CallBack_v2 op](images/ops/Ops_Cables_CallBack_v2.svg)

**Full Name:** `Ops.Cables.CallBack_v2`
**Description:** Useful when a cables patch is embedded into a website. All parameters (`Value 1`, `Value 2`, `Value 3` will be send as a parameter array. So e.g. if `Callback Name` is `foo` cables would call: ``` CABLES.patch.config.foo([Value 1, Value 2, Value 3]) ```

**> Input Ports:**
- **Exe** (Trigger): *See documentation*
- **Callback Name** (String): *See documentation*
- **Parameter 1** (String): *See documentation*
- **Parameter 2** (String): *See documentation*
- **Parameter 3** (String): *See documentation*
- **Public** (7): LANDINGPORTAFOLIO
- **LOGICX BED** (PUBLIC): wirmachenbunt - Published Sep 30, 2021 at 12:25

**< Output Ports:**
- *Visit [Ops.Cables.CallBack_v2 documentation](https://cables.gl/op/Ops.Cables.CallBack_v2) for output port details*

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Cables.CallBack_v2#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "CallBack_v2"*
**Docs:** [https://cables.gl/op/Ops.Cables.CallBack_v2](https://cables.gl/op/Ops.Cables.CallBack_v2)

---

### FPS_v2
![FPS_v2 op](images/ops/Ops_Cables_FPS_v2.svg)

**Full Name:** `Ops.Cables.FPS_v2`
**Description:** output current frames per second

**> Input Ports:**
- *Visit [Ops.Cables.FPS_v2 documentation](https://cables.gl/op/Ops.Cables.FPS_v2) for input port details*

**< Output Ports:**
- **FPS** (Number): *See documentation*
- **MS** (Number): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/KhFA8i)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "FPS_v2"*
**Docs:** [https://cables.gl/op/Ops.Cables.FPS_v2](https://cables.gl/op/Ops.Cables.FPS_v2)

---

### Function_v2
![Function_v2 op](images/ops/Ops_Cables_Function_v2.svg)

**Full Name:** `Ops.Cables.Function_v2`
**Description:** trigger from external function when embedded into a website

**> Input Ports:**
- **Function Name** (String): *See documentation*
- **Trigger** (Trigger): *See documentation*
- **Default Parameter 1** (String): *See documentation*
- **Default Parameter 2** (String): *See documentation*
- **Default Parameter 3** (String): *See documentation*

**< Output Ports:**
- **Next** (Trigger): *See documentation*
- **Parameter 1** (String): *See documentation*
- **Parameter 2** (String): *See documentation*
- **Parameter 3** (String): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Cables.Function_v2#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "Function_v2"*
**Docs:** [https://cables.gl/op/Ops.Cables.Function_v2](https://cables.gl/op/Ops.Cables.Function_v2)

---

### GetOpName
![GetOpName op](images/ops/Ops_Cables_GetOpName.svg)

**Full Name:** `Ops.Cables.GetOpName`
**Description:** Get op name by id

**> Input Ports:**
- **OpId** (String): *See documentation*

**< Output Ports:**
- **Found** (booleanNumber): *See documentation*
- **Name** (String): *See documentation*
- **Shortname** (String): *See documentation*
- **Version** (Number): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/Hmk7iO)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "GetOpName"*
**Docs:** [https://cables.gl/op/Ops.Cables.GetOpName](https://cables.gl/op/Ops.Cables.GetOpName)

---

### GetSubPatchName
![GetSubPatchName op](images/ops/Ops_Cables_GetSubPatchName.svg)

**Full Name:** `Ops.Cables.GetSubPatchName`
**Description:** Outputs the current subpatch op name

**> Input Ports:**
- *Visit [Ops.Cables.GetSubPatchName documentation](https://cables.gl/op/Ops.Cables.GetSubPatchName) for input port details*

**< Output Ports:**
- **Name** (String): *See documentation*
- **ShortName** (String): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/20tMrh)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "GetSubPatchName"*
**Docs:** [https://cables.gl/op/Ops.Cables.GetSubPatchName](https://cables.gl/op/Ops.Cables.GetSubPatchName)

---

### LoadingJob
![LoadingJob op](images/ops/Ops_Cables_LoadingJob.svg)

**Full Name:** `Ops.Cables.LoadingJob`
**Description:** Create a loading job while input is true

**> Input Ports:**
- **Loading Active** (Number: Boolean): *See documentation*

**< Output Ports:**
- *Visit [Ops.Cables.LoadingJob documentation](https://cables.gl/op/Ops.Cables.LoadingJob) for output port details*

**Example Patch:** [Open in Editor](https://cables.gl/edit/bzn9z1)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "LoadingJob"*
**Docs:** [https://cables.gl/op/Ops.Cables.LoadingJob](https://cables.gl/op/Ops.Cables.LoadingJob)

---

### LoadingStatus_v2
![LoadingStatus_v2 op](images/ops/Ops_Cables_LoadingStatus_v2.svg)

**Full Name:** `Ops.Cables.LoadingStatus_v2`
**Description:** trigger events / get information about asset-loading status

**> Input Ports:**
- **Exe** (Trigger): *See documentation*
- **Play Timeline** (Number: Boolean): *See documentation*

**< Output Ports:**
- **Next** (Trigger): *See documentation*
- **Finished Initial Loading** (booleanNumber): *See documentation*
- **Loading** (booleanNumber): *See documentation*
- **Progress** (Number): *See documentation*
- **Jobs** (Array): *See documentation*
- **Trigger Loading Finished** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/5FQ08W)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "LoadingStatus_v2"*
**Docs:** [https://cables.gl/op/Ops.Cables.LoadingStatus_v2](https://cables.gl/op/Ops.Cables.LoadingStatus_v2)

---

### PatchInfo_v2
![PatchInfo_v2 op](images/ops/Ops_Cables_PatchInfo_v2.svg)

**Full Name:** `Ops.Cables.PatchInfo_v2`
**Description:** read patch config when embedding on another page

**> Input Ports:**
- *Visit [Ops.Cables.PatchInfo_v2 documentation](https://cables.gl/op/Ops.Cables.PatchInfo_v2) for input port details*

**< Output Ports:**
- **Config** (Object): *See documentation*
- **Name** (String): *See documentation*
- **Patch Id** (String): *See documentation*
- **Namespace** (String): *See documentation*
- **Last Saved** (Number): *See documentation*
- **Last Exported** (Number): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/3hkdqX)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "PatchInfo_v2"*
**Docs:** [https://cables.gl/op/Ops.Cables.PatchInfo_v2](https://cables.gl/op/Ops.Cables.PatchInfo_v2)

---

### UIMode
![UIMode op](images/ops/Ops_Cables_UIMode.svg)

**Full Name:** `Ops.Cables.UIMode`
**Description:** Outputs `true` if patch is executed in the cables editor (UI)

**> Input Ports:**
- *Visit [Ops.Cables.UIMode documentation](https://cables.gl/op/Ops.Cables.UIMode) for input port details*

**< Output Ports:**
- **UI** (booleanNumber): *See documentation*
- **Overlay Mode** (booleanNumber): *See documentation*
- **Remote Viewer** (booleanNumber): *See documentation*
- **Is Standalone** (booleanNumber): *See documentation*
- **Canvas Mode** (Number): *See documentation*
- **Patch Field Visible** (booleanNumber): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/vyqgR3)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "UIMode"*
**Docs:** [https://cables.gl/op/Ops.Cables.UIMode](https://cables.gl/op/Ops.Cables.UIMode)

---

### UploadAsset
![UploadAsset op](images/ops/Ops_Cables_UploadAsset.svg)

**Full Name:** `Ops.Cables.UploadAsset`
**Description:** Upload a file into the cables patch assets using a base64 string

**> Input Ports:**
- **Filename** (String): *See documentation*
- **Base64 String** (String): *See documentation*
- **Upload** (Trigger): *See documentation*

**< Output Ports:**
- **Result** (String): *See documentation*
- **Error** (booleanNumber): *See documentation*
- **Finished** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/6vDCsh)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "UploadAsset"*
**Docs:** [https://cables.gl/op/Ops.Cables.UploadAsset](https://cables.gl/op/Ops.Cables.UploadAsset)

---

### UploadScreenshot
![UploadScreenshot op](images/ops/Ops_Cables_UploadScreenshot.svg)

**Full Name:** `Ops.Cables.UploadScreenshot`
**Description:** Upload an image as screentshot in cables

**> Input Ports:**
- **Trigger** (Trigger): *See documentation*
- **DataUrl** (String): *See documentation*

**< Output Ports:**
- **Result** (Number): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Cables.UploadScreenshot#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "UploadScreenshot"*
**Docs:** [https://cables.gl/op/Ops.Cables.UploadScreenshot](https://cables.gl/op/Ops.Cables.UploadScreenshot)

---

