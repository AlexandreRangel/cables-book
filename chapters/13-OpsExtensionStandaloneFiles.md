# Ops.Extension.Standalone.Files

*Part of the [All Operators Reference](13-_AllOps.md)*

---

## Ops.Extension.Standalone.Files

### CreateFile
![CreateFile op](images/ops/Ops_Extension_Standalone_Files_CreateFile.svg)

**Full Name:** `Ops.Extension.Standalone.Files.CreateFile`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Extension.Standalone.Files.CreateFile) for details*

**> Input Ports:**
- **Default Path** (String)
- **Create File** (Trigger)

**< Output Ports:**
- **Path** (String)
- **Next** (Trigger)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Extension.Standalone.Files.CreateFile#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "CreateFile"*
**Docs:** [https://cables.gl/op/Ops.Extension.Standalone.Files.CreateFile](https://cables.gl/op/Ops.Extension.Standalone.Files.CreateFile)

---

### Exist
![Exist op](images/ops/Ops_Extension_Standalone_Files_Exist.svg)

**Full Name:** `Ops.Extension.Standalone.Files.Exist`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Extension.Standalone.Files.Exist) for details*

**> Input Ports:**
- **Path** (String)
- **Execute** (Trigger)

**< Output Ports:**
- **Exists** (booleanNumber)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Extension.Standalone.Files.Exist#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "Exist"*
**Docs:** [https://cables.gl/op/Ops.Extension.Standalone.Files.Exist](https://cables.gl/op/Ops.Extension.Standalone.Files.Exist)

---

### FileUrlToPath
![FileUrlToPath op](images/ops/Ops_Extension_Standalone_Files_FileUrlToPath.svg)

**Full Name:** `Ops.Extension.Standalone.Files.FileUrlToPath`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Extension.Standalone.Files.FileUrlToPath) for details*

**> Input Ports:**
- **FileUrl** (String)

**< Output Ports:**
- **Path** (String)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Extension.Standalone.Files.FileUrlToPath#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "FileUrlToPath"*
**Docs:** [https://cables.gl/op/Ops.Extension.Standalone.Files.FileUrlToPath](https://cables.gl/op/Ops.Extension.Standalone.Files.FileUrlToPath)

---

### Makedir
![Makedir op](images/ops/Ops_Extension_Standalone_Files_Makedir.svg)

**Full Name:** `Ops.Extension.Standalone.Files.Makedir`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Extension.Standalone.Files.Makedir) for details*

**> Input Ports:**
- **Path** (String)
- **Create** (Trigger)

**< Output Ports:**
- **Next** (Trigger)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Extension.Standalone.Files.Makedir#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "Makedir"*
**Docs:** [https://cables.gl/op/Ops.Extension.Standalone.Files.Makedir](https://cables.gl/op/Ops.Extension.Standalone.Files.Makedir)

---

### OpenFileManager
![OpenFileManager op](images/ops/Ops_Extension_Standalone_Files_OpenFileManager.svg)

**Full Name:** `Ops.Extension.Standalone.Files.OpenFileManager`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Extension.Standalone.Files.OpenFileManager) for details*

**> Input Ports:**
- **Path** (String)
- **Open File Manager** (Trigger)

**< Output Ports:**
- *Visit [Ops.Extension.Standalone.Files.OpenFileManager documentation](https://cables.gl/op/Ops.Extension.Standalone.Files.OpenFileManager) for output port details*

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Extension.Standalone.Files.OpenFileManager#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "OpenFileManager"*
**Docs:** [https://cables.gl/op/Ops.Extension.Standalone.Files.OpenFileManager](https://cables.gl/op/Ops.Extension.Standalone.Files.OpenFileManager)

---

### PathToFileUrl
![PathToFileUrl op](images/ops/Ops_Extension_Standalone_Files_PathToFileUrl.svg)

**Full Name:** `Ops.Extension.Standalone.Files.PathToFileUrl`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Extension.Standalone.Files.PathToFileUrl) for details*

**> Input Ports:**
- **Path** (String)

**< Output Ports:**
- **FileUrl** (String)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Extension.Standalone.Files.PathToFileUrl#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "PathToFileUrl"*
**Docs:** [https://cables.gl/op/Ops.Extension.Standalone.Files.PathToFileUrl](https://cables.gl/op/Ops.Extension.Standalone.Files.PathToFileUrl)

---

### ReadDir
![ReadDir op](images/ops/Ops_Extension_Standalone_Files_ReadDir.svg)

**Full Name:** `Ops.Extension.Standalone.Files.ReadDir`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Extension.Standalone.Files.ReadDir) for details*

**> Input Ports:**
- **Path** (String)
- **Reload** (Trigger)

**< Output Ports:**
- **Entries** (Array)
- **Has Error** (booleanNumber)
- **Error** (String)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Extension.Standalone.Files.ReadDir#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ReadDir"*
**Docs:** [https://cables.gl/op/Ops.Extension.Standalone.Files.ReadDir](https://cables.gl/op/Ops.Extension.Standalone.Files.ReadDir)

---

### ResolvePath
![ResolvePath op](images/ops/Ops_Extension_Standalone_Files_ResolvePath.svg)

**Full Name:** `Ops.Extension.Standalone.Files.ResolvePath`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Extension.Standalone.Files.ResolvePath) for details*

**> Input Ports:**
- **Path** (String)

**< Output Ports:**
- **Result** (String)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Extension.Standalone.Files.ResolvePath#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ResolvePath"*
**Docs:** [https://cables.gl/op/Ops.Extension.Standalone.Files.ResolvePath](https://cables.gl/op/Ops.Extension.Standalone.Files.ResolvePath)

---

### SelectDir
![SelectDir op](images/ops/Ops_Extension_Standalone_Files_SelectDir.svg)

**Full Name:** `Ops.Extension.Standalone.Files.SelectDir`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Extension.Standalone.Files.SelectDir) for details*

**> Input Ports:**
- **Default Path** (String)
- **Select Directory** (Trigger)

**< Output Ports:**
- **Path** (String)
- **Next** (Trigger)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Extension.Standalone.Files.SelectDir#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "SelectDir"*
**Docs:** [https://cables.gl/op/Ops.Extension.Standalone.Files.SelectDir](https://cables.gl/op/Ops.Extension.Standalone.Files.SelectDir)

---

### SelectFile
![SelectFile op](images/ops/Ops_Extension_Standalone_Files_SelectFile.svg)

**Full Name:** `Ops.Extension.Standalone.Files.SelectFile`

**Description:** *Visit [documentation](https://cables.gl/op/Ops.Extension.Standalone.Files.SelectFile) for details*

**> Input Ports:**
- **Default Path** (String)
- **Select File** (Trigger)

**< Output Ports:**
- **Path** (String)
- **Next** (Trigger)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Extension.Standalone.Files.SelectFile#example)

**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "SelectFile"*

**Docs:** [https://cables.gl/op/Ops.Extension.Standalone.Files.SelectFile](https://cables.gl/op/Ops.Extension.Standalone.Files.SelectFile)

---

### Stat
![Stat op](images/ops/Ops_Extension_Standalone_Files_Stat.svg)

**Full Name:** `Ops.Extension.Standalone.Files.Stat`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Extension.Standalone.Files.Stat) for details*

**> Input Ports:**
- **Path** (String)

**< Output Ports:**
- **Stats** (Object)
- **Is Directory** (booleanNumber)
- **Is File** (booleanNumber)
- **Has Error** (booleanNumber)
- **Error** (String)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Extension.Standalone.Files.Stat#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "Stat"*
**Docs:** [https://cables.gl/op/Ops.Extension.Standalone.Files.Stat](https://cables.gl/op/Ops.Extension.Standalone.Files.Stat)

---

### SystemDirs
![SystemDirs op](images/ops/Ops_Extension_Standalone_Files_SystemDirs.svg)

**Full Name:** `Ops.Extension.Standalone.Files.SystemDirs`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Extension.Standalone.Files.SystemDirs) for details*

**> Input Ports:**
- *Visit [Ops.Extension.Standalone.Files.SystemDirs documentation](https://cables.gl/op/Ops.Extension.Standalone.Files.SystemDirs) for input port details*

**< Output Ports:**
- **Home** (String)
- **Downloads** (String)
- **Documents** (String)
- **Desktop** (String)
- **Exe** (String)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Extension.Standalone.Files.SystemDirs#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "SystemDirs"*
**Docs:** [https://cables.gl/op/Ops.Extension.Standalone.Files.SystemDirs](https://cables.gl/op/Ops.Extension.Standalone.Files.SystemDirs)

---

### Watch
![Watch op](images/ops/Ops_Extension_Standalone_Files_Watch.svg)

**Full Name:** `Ops.Extension.Standalone.Files.Watch`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Extension.Standalone.Files.Watch) for details*

**> Input Ports:**
- **Path** (String)
- **Read** (Trigger)

**< Output Ports:**
- **Event Type** (String)
- **Event Filename** (String)
- **Event Happened** (Trigger)
- **Content** (String)
- **Has Error** (booleanNumber)
- **Error** (String)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Extension.Standalone.Files.Watch#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "Watch"*
**Docs:** [https://cables.gl/op/Ops.Extension.Standalone.Files.Watch](https://cables.gl/op/Ops.Extension.Standalone.Files.Watch)

---

### WriteBinaryFileFromBase64
![WriteBinaryFileFromBase64 op](images/ops/Ops_Extension_Standalone_Files_WriteBinaryFileFromBase64.svg)

**Full Name:** `Ops.Extension.Standalone.Files.WriteBinaryFileFromBase64`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Extension.Standalone.Files.WriteBinaryFileFromBase64) for details*

**> Input Ports:**
- **Trigger** (Trigger)
- **Base64** (String)
- **Filename** (String)

**< Output Ports:**
- *Visit [Ops.Extension.Standalone.Files.WriteBinaryFileFromBase64 documentation](https://cables.gl/op/Ops.Extension.Standalone.Files.WriteBinaryFileFromBase64) for output port details*

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Extension.Standalone.Files.WriteBinaryFileFromBase64#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "WriteBinaryFileFromBase64"*
**Docs:** [https://cables.gl/op/Ops.Extension.Standalone.Files.WriteBinaryFileFromBase64](https://cables.gl/op/Ops.Extension.Standalone.Files.WriteBinaryFileFromBase64)

---

### WriteTextFile
![WriteTextFile op](images/ops/Ops_Extension_Standalone_Files_WriteTextFile.svg)

**Full Name:** `Ops.Extension.Standalone.Files.WriteTextFile`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Extension.Standalone.Files.WriteTextFile) for details*

**> Input Ports:**
- **Filename** (String)
- **Content** (String)
- **Write** (Trigger)

**< Output Ports:**
- **Next** (Trigger)
- **Has Error** (booleanNumber)
- **Error** (String)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Extension.Standalone.Files.WriteTextFile#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "WriteTextFile"*
**Docs:** [https://cables.gl/op/Ops.Extension.Standalone.Files.WriteTextFile](https://cables.gl/op/Ops.Extension.Standalone.Files.WriteTextFile)

---

