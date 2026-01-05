# Ops.Extension.Standalone.Files

---

```{=latex}
\OpsSubsubNoSubsectionNumbering\setcounter{subsubsection}{0}
```
### CreateFile
![CreateFile op](images/ops/Ops_Extension_Standalone_Files_CreateFile.svg)

**Full Name:** `Ops.Extension.Standalone.Files.CreateFile`

**Description:** Create a new empty file on your local harddrive

**`\inputsymbol`{=latex} Inputs**

- **Default Path** (String)
- **Create File** (Trigger)

**`\outputsymbol`{=latex} Output**

- **Path** (String)
- **Next** (Trigger)

**Example Patch:** [Open in Editor](https://cables.gl/edit/dhvNAs)

**Docs:** [https://cables.gl/op/Ops.Extension.Standalone.Files.CreateFile](https://cables.gl/op/Ops.Extension.Standalone.Files.CreateFile)

### Exist
![Exist op](images/ops/Ops_Extension_Standalone_Files_Exist.svg)

**Full Name:** `Ops.Extension.Standalone.Files.Exist`

**Description:** Check if a file exists on the local file system

**`\inputsymbol`{=latex} Inputs**

- **Path** (String)
- **Execute** (Trigger)

**`\outputsymbol`{=latex} Output**

- **Exists** (booleanNumber)

**Example Patch:** [Open in Editor](https://cables.gl/edit/XlQrun)

**Docs:** [https://cables.gl/op/Ops.Extension.Standalone.Files.Exist](https://cables.gl/op/Ops.Extension.Standalone.Files.Exist)

### FileUrlToPath
![FileUrlToPath op](images/ops/Ops_Extension_Standalone_Files_FileUrlToPath.svg)

**Full Name:** `Ops.Extension.Standalone.Files.FileUrlToPath`

**Description:** convert file-url to path

**`\inputsymbol`{=latex} Inputs**

- **FileUrl** (String)

**`\outputsymbol`{=latex} Output**

- **Path** (String)

**Example Patch:** [Open in Editor](https://cables.gl/edit/upnVAs)

**Docs:** [https://cables.gl/op/Ops.Extension.Standalone.Files.FileUrlToPath](https://cables.gl/op/Ops.Extension.Standalone.Files.FileUrlToPath)

### Makedir
![Makedir op](images/ops/Ops_Extension_Standalone_Files_Makedir.svg)

**Full Name:** `Ops.Extension.Standalone.Files.Makedir`

**Description:** Create a directory on the local file system

**`\inputsymbol`{=latex} Inputs**

- **Path** (String)
- **Create** (Trigger)

**`\outputsymbol`{=latex} Output**

- **Next** (Trigger)

**Example Patch:** [Open in Editor](https://cables.gl/edit/q5evun)

**Docs:** [https://cables.gl/op/Ops.Extension.Standalone.Files.Makedir](https://cables.gl/op/Ops.Extension.Standalone.Files.Makedir)

### OpenFileManager
![OpenFileManager op](images/ops/Ops_Extension_Standalone_Files_OpenFileManager.svg)

**Full Name:** `Ops.Extension.Standalone.Files.OpenFileManager`

**Description:** Open the native file manager application using that path

**`\inputsymbol`{=latex} Inputs**

- **Path** (String)
- **Open File Manager** (Trigger)

**`\outputsymbol`{=latex} Output**

- *Visit [Ops.Extension.Standalone.Files.OpenFileManager documentation](https://cables.gl/op/Ops.Extension.Standalone.Files.OpenFileManager) for output port details*

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Extension.Standalone.Files.OpenFileManager#example)

**Docs:** [https://cables.gl/op/Ops.Extension.Standalone.Files.OpenFileManager](https://cables.gl/op/Ops.Extension.Standalone.Files.OpenFileManager)

### PathToFileUrl
![PathToFileUrl op](images/ops/Ops_Extension_Standalone_Files_PathToFileUrl.svg)

**Full Name:** `Ops.Extension.Standalone.Files.PathToFileUrl`

**Description:** convert local path to file-url

**`\inputsymbol`{=latex} Inputs**

- **Path** (String)

**`\outputsymbol`{=latex} Output**

- **FileUrl** (String)

**Example Patch:** [Open in Editor](https://cables.gl/edit/pekPAs)

**Docs:** [https://cables.gl/op/Ops.Extension.Standalone.Files.PathToFileUrl](https://cables.gl/op/Ops.Extension.Standalone.Files.PathToFileUrl)

### ReadDir
![ReadDir op](images/ops/Ops_Extension_Standalone_Files_ReadDir.svg)

**Full Name:** `Ops.Extension.Standalone.Files.ReadDir`

**Description:** Read all entries in a directory

**`\inputsymbol`{=latex} Inputs**

- **Path** (String)
- **Reload** (Trigger)

**`\outputsymbol`{=latex} Output**

- **Entries** (Array)
- **Has Error** (booleanNumber)
- **Error** (String)

**Example Patch:** [Open in Editor](https://cables.gl/edit/I6buun)

**Docs:** [https://cables.gl/op/Ops.Extension.Standalone.Files.ReadDir](https://cables.gl/op/Ops.Extension.Standalone.Files.ReadDir)

### ResolvePath
![ResolvePath op](images/ops/Ops_Extension_Standalone_Files_ResolvePath.svg)

**Full Name:** `Ops.Extension.Standalone.Files.ResolvePath`

**Description:** Resolves a paths into an absolute path

**`\inputsymbol`{=latex} Inputs**

- **Path** (String)

**`\outputsymbol`{=latex} Output**

- **Result** (String)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Extension.Standalone.Files.ResolvePath#example)

**Docs:** [https://cables.gl/op/Ops.Extension.Standalone.Files.ResolvePath](https://cables.gl/op/Ops.Extension.Standalone.Files.ResolvePath)

### SelectDir
![SelectDir op](images/ops/Ops_Extension_Standalone_Files_SelectDir.svg)

**Full Name:** `Ops.Extension.Standalone.Files.SelectDir`

**Description:** Choose a directory on your hard drive

**`\inputsymbol`{=latex} Inputs**

- **Default Path** (String)
- **Select Directory** (Trigger)

**`\outputsymbol`{=latex} Output**

- **Path** (String)
- **Next** (Trigger)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Extension.Standalone.Files.SelectDir#example)

**Docs:** [https://cables.gl/op/Ops.Extension.Standalone.Files.SelectDir](https://cables.gl/op/Ops.Extension.Standalone.Files.SelectDir)

### SelectFile
![SelectFile op](images/ops/Ops_Extension_Standalone_Files_SelectFile.svg)

**Full Name:** `Ops.Extension.Standalone.Files.SelectFile`

**Description:** Choose a file on your hard drive

**`\inputsymbol`{=latex} Inputs**

- **Default Path** (String)
- **Select File** (Trigger)

**`\outputsymbol`{=latex} Output**

- **Path** (String)
- **Next** (Trigger)

**Example Patch:** [Open in Editor](https://cables.gl/edit/M58UAs)

**Docs:** [https://cables.gl/op/Ops.Extension.Standalone.Files.SelectFile](https://cables.gl/op/Ops.Extension.Standalone.Files.SelectFile)

### Stat
![Stat op](images/ops/Ops_Extension_Standalone_Files_Stat.svg)

**Full Name:** `Ops.Extension.Standalone.Files.Stat`

**Description:** Get statistics about a file on the local file system

**`\inputsymbol`{=latex} Inputs**

- **Path** (String)

**`\outputsymbol`{=latex} Output**

- **Stats** (Object)
- **Is Directory** (booleanNumber)
- **Is File** (booleanNumber)
- **Has Error** (booleanNumber)
- **Error** (String)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Extension.Standalone.Files.Stat#example)

**Docs:** [https://cables.gl/op/Ops.Extension.Standalone.Files.Stat](https://cables.gl/op/Ops.Extension.Standalone.Files.Stat)

### SystemDirs
![SystemDirs op](images/ops/Ops_Extension_Standalone_Files_SystemDirs.svg)

**Full Name:** `Ops.Extension.Standalone.Files.SystemDirs`

**Description:** Get Default System Directories Paths

**`\inputsymbol`{=latex} Inputs**

- *Visit [Ops.Extension.Standalone.Files.SystemDirs documentation](https://cables.gl/op/Ops.Extension.Standalone.Files.SystemDirs) for input port details*

**`\outputsymbol`{=latex} Output**

- **Home** (String)
- **Downloads** (String)
- **Documents** (String)
- **Desktop** (String)
- **Exe** (String)

**Example Patch:** [Open in Editor](https://cables.gl/edit/7hftun)

**Docs:** [https://cables.gl/op/Ops.Extension.Standalone.Files.SystemDirs](https://cables.gl/op/Ops.Extension.Standalone.Files.SystemDirs)

### Watch
![Watch op](images/ops/Ops_Extension_Standalone_Files_Watch.svg)

**Full Name:** `Ops.Extension.Standalone.Files.Watch`

**Description:** Watch a directory, get a trigger when a file changes

**`\inputsymbol`{=latex} Inputs**

- **Path** (String)
- **Read** (Trigger)

**`\outputsymbol`{=latex} Output**

- **Event Type** (String)
- **Event Filename** (String)
- **Event Happened** (Trigger)
- **Content** (String)
- **Has Error** (booleanNumber)
- **Error** (String)

**Example Patch:** [Open in Editor](https://cables.gl/edit/PT9Aun)

**Docs:** [https://cables.gl/op/Ops.Extension.Standalone.Files.Watch](https://cables.gl/op/Ops.Extension.Standalone.Files.Watch)

### WriteBinaryFileFromBase64
![WriteBinaryFileFromBase64 op](images/ops/Ops_Extension_Standalone_Files_WriteBinaryFileFromBase64.svg)

**Full Name:** `Ops.Extension.Standalone.Files.WriteBinaryFileFromBase64`

**Description:** Create a binary file on the local file system from a base64 string

**`\inputsymbol`{=latex} Inputs**

- **Trigger** (Trigger)
- **Base64** (String)
- **Filename** (String)

**`\outputsymbol`{=latex} Output**

- *Visit [Ops.Extension.Standalone.Files.WriteBinaryFileFromBase64 documentation](https://cables.gl/op/Ops.Extension.Standalone.Files.WriteBinaryFileFromBase64) for output port details*

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Extension.Standalone.Files.WriteBinaryFileFromBase64#example)

**Docs:** [https://cables.gl/op/Ops.Extension.Standalone.Files.WriteBinaryFileFromBase64](https://cables.gl/op/Ops.Extension.Standalone.Files.WriteBinaryFileFromBase64)

### WriteTextFile
![WriteTextFile op](images/ops/Ops_Extension_Standalone_Files_WriteTextFile.svg)

**Full Name:** `Ops.Extension.Standalone.Files.WriteTextFile`

**Description:** Write a string to a text file on the local file system

**`\inputsymbol`{=latex} Inputs**

- **Filename** (String)
- **Content** (String)
- **Write** (Trigger)

**`\outputsymbol`{=latex} Output**

- **Next** (Trigger)
- **Has Error** (booleanNumber)
- **Error** (String)

**Example Patch:** [Open in Editor](https://cables.gl/edit/PT9Aun)

**Docs:** [https://cables.gl/op/Ops.Extension.Standalone.Files.WriteTextFile](https://cables.gl/op/Ops.Extension.Standalone.Files.WriteTextFile)


