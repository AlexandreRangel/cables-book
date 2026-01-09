# Ops.Extension.Standalone.Files


```{=latex}
\OpsSubsubNoSubsectionNumbering\setcounter{subsubsection}{0}
```
### CreateFile
![CreateFile op](images/ops/Ops_Extension_Standalone_Files_CreateFile.svg)

**Full Name:** `Ops.Extension.Standalone.Files.CreateFile`

Create a new empty file on your local harddrive.

**`\inputsymbol`{=latex} Inputs**

- **Default Path** (String)
- **Create File** (Trigger)

**`\outputsymbol`{=latex} Output**

- **Path** (String)
- **Next** (Trigger)

**Example Patch:** [cables.gl/edit/dhvNAs](https://cables.gl/edit/dhvNAs)

**Doc:** [cables.gl/op/Ops.Extension.Standalone.Files.CreateFile](https://cables.gl/op/Ops.Extension.Standalone.Files.CreateFile)

### Exist
![Exist op](images/ops/Ops_Extension_Standalone_Files_Exist.svg)

**Full Name:** `Ops.Extension.Standalone.Files.Exist`

Check if a file exists on the local file system.

**`\inputsymbol`{=latex} Inputs**

- **Path** (String)
- **Execute** (Trigger)

**`\outputsymbol`{=latex} Output**

- **Exists** (booleanNumber)

**Example Patch:** [cables.gl/edit/XlQrun](https://cables.gl/edit/XlQrun)

**Doc:** [cables.gl/op/Ops.Extension.Standalone.Files.Exist](https://cables.gl/op/Ops.Extension.Standalone.Files.Exist)

### FileUrlToPath
![FileUrlToPath op](images/ops/Ops_Extension_Standalone_Files_FileUrlToPath.svg)

**Full Name:** `Ops.Extension.Standalone.Files.FileUrlToPath`

convert file-url to path.

**`\inputsymbol`{=latex} Inputs**

- **FileUrl** (String)

**`\outputsymbol`{=latex} Output**

- **Path** (String)

**Example Patch:** [cables.gl/edit/upnVAs](https://cables.gl/edit/upnVAs)

**Doc:** [cables.gl/op/Ops.Extension.Standalone.Files.FileUrlToPath](https://cables.gl/op/Ops.Extension.Standalone.Files.FileUrlToPath)

### Makedir
![Makedir op](images/ops/Ops_Extension_Standalone_Files_Makedir.svg)

**Full Name:** `Ops.Extension.Standalone.Files.Makedir`

Create a directory on the local file system.

**`\inputsymbol`{=latex} Inputs**

- **Path** (String)
- **Create** (Trigger)

**`\outputsymbol`{=latex} Output**

- **Next** (Trigger)

**Example Patch:** [cables.gl/edit/q5evun](https://cables.gl/edit/q5evun)

**Doc:** [cables.gl/op/Ops.Extension.Standalone.Files.Makedir](https://cables.gl/op/Ops.Extension.Standalone.Files.Makedir)

### OpenFileManager
![OpenFileManager op](images/ops/Ops_Extension_Standalone_Files_OpenFileManager.svg)

**Full Name:** `Ops.Extension.Standalone.Files.OpenFileManager`

Open the native file manager application using that path.

**`\inputsymbol`{=latex} Inputs**

- **Path** (String)
- **Open File Manager** (Trigger)

**Example Patch:** [cables.gl/op/Ops.Extension.Standalone.Files.OpenFileManager#example](https://cables.gl/op/Ops.Extension.Standalone.Files.OpenFileManager#example)

**Doc:** [cables.gl/op/Ops.Extension.Standalone.Files.OpenFileManager](https://cables.gl/op/Ops.Extension.Standalone.Files.OpenFileManager)

### PathToFileUrl
![PathToFileUrl op](images/ops/Ops_Extension_Standalone_Files_PathToFileUrl.svg)

**Full Name:** `Ops.Extension.Standalone.Files.PathToFileUrl`

convert local path to file-url.

**`\inputsymbol`{=latex} Inputs**

- **Path** (String)

**`\outputsymbol`{=latex} Output**

- **FileUrl** (String)

**Example Patch:** [cables.gl/edit/pekPAs](https://cables.gl/edit/pekPAs)

**Doc:** [cables.gl/op/Ops.Extension.Standalone.Files.PathToFileUrl](https://cables.gl/op/Ops.Extension.Standalone.Files.PathToFileUrl)

### ReadDir
![ReadDir op](images/ops/Ops_Extension_Standalone_Files_ReadDir.svg)

**Full Name:** `Ops.Extension.Standalone.Files.ReadDir`

Read all entries in a directory.

**`\inputsymbol`{=latex} Inputs**

- **Path** (String)
- **Reload** (Trigger)

**`\outputsymbol`{=latex} Output**

- **Entries** (Array)
- **Has Error** (booleanNumber)
- **Error** (String)

**Example Patch:** [cables.gl/edit/I6buun](https://cables.gl/edit/I6buun)

**Doc:** [cables.gl/op/Ops.Extension.Standalone.Files.ReadDir](https://cables.gl/op/Ops.Extension.Standalone.Files.ReadDir)

### ResolvePath
![ResolvePath op](images/ops/Ops_Extension_Standalone_Files_ResolvePath.svg)

**Full Name:** `Ops.Extension.Standalone.Files.ResolvePath`

Resolves a paths into an absolute path.

**`\inputsymbol`{=latex} Inputs**

- **Path** (String)

**`\outputsymbol`{=latex} Output**

- **Result** (String)

**Example Patch:** [cables.gl/op/Ops.Extension.Standalone.Files.ResolvePath#example](https://cables.gl/op/Ops.Extension.Standalone.Files.ResolvePath#example)

**Doc:** [cables.gl/op/Ops.Extension.Standalone.Files.ResolvePath](https://cables.gl/op/Ops.Extension.Standalone.Files.ResolvePath)

### SelectDir
![SelectDir op](images/ops/Ops_Extension_Standalone_Files_SelectDir.svg)

**Full Name:** `Ops.Extension.Standalone.Files.SelectDir`

Choose a directory on your hard drive.

**`\inputsymbol`{=latex} Inputs**

- **Default Path** (String)
- **Select Directory** (Trigger)

**`\outputsymbol`{=latex} Output**

- **Path** (String)
- **Next** (Trigger)

**Example Patch:** [cables.gl/op/Ops.Extension.Standalone.Files.SelectDir#example](https://cables.gl/op/Ops.Extension.Standalone.Files.SelectDir#example)

**Doc:** [cables.gl/op/Ops.Extension.Standalone.Files.SelectDir](https://cables.gl/op/Ops.Extension.Standalone.Files.SelectDir)

### SelectFile
![SelectFile op](images/ops/Ops_Extension_Standalone_Files_SelectFile.svg)

**Full Name:** `Ops.Extension.Standalone.Files.SelectFile`

Choose a file on your hard drive.

**`\inputsymbol`{=latex} Inputs**

- **Default Path** (String)
- **Select File** (Trigger)

**`\outputsymbol`{=latex} Output**

- **Path** (String)
- **Next** (Trigger)

**Example Patch:** [cables.gl/edit/M58UAs](https://cables.gl/edit/M58UAs)

**Doc:** [cables.gl/op/Ops.Extension.Standalone.Files.SelectFile](https://cables.gl/op/Ops.Extension.Standalone.Files.SelectFile)

### Stat
![Stat op](images/ops/Ops_Extension_Standalone_Files_Stat.svg)

**Full Name:** `Ops.Extension.Standalone.Files.Stat`

Get statistics about a file on the local file system.

**`\inputsymbol`{=latex} Inputs**

- **Path** (String)

**`\outputsymbol`{=latex} Output**

- **Stats** (Object)
- **Is Directory** (booleanNumber)
- **Is File** (booleanNumber)
- **Has Error** (booleanNumber)
- **Error** (String)

**Example Patch:** [cables.gl/op/Ops.Extension.Standalone.Files.Stat#example](https://cables.gl/op/Ops.Extension.Standalone.Files.Stat#example)

**Doc:** [cables.gl/op/Ops.Extension.Standalone.Files.Stat](https://cables.gl/op/Ops.Extension.Standalone.Files.Stat)

### SystemDirs
![SystemDirs op](images/ops/Ops_Extension_Standalone_Files_SystemDirs.svg)

**Full Name:** `Ops.Extension.Standalone.Files.SystemDirs`

Get Default System Directories Paths.

**`\outputsymbol`{=latex} Output**

- **Home** (String)
- **Downloads** (String)
- **Documents** (String)
- **Desktop** (String)
- **Exe** (String)

**Example Patch:** [cables.gl/edit/7hftun](https://cables.gl/edit/7hftun)

**Doc:** [cables.gl/op/Ops.Extension.Standalone.Files.SystemDirs](https://cables.gl/op/Ops.Extension.Standalone.Files.SystemDirs)

### Watch
![Watch op](images/ops/Ops_Extension_Standalone_Files_Watch.svg)

**Full Name:** `Ops.Extension.Standalone.Files.Watch`

Watch a directory, get a trigger when a file changes.

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

**Example Patch:** [cables.gl/edit/PT9Aun](https://cables.gl/edit/PT9Aun)

**Doc:** [cables.gl/op/Ops.Extension.Standalone.Files.Watch](https://cables.gl/op/Ops.Extension.Standalone.Files.Watch)

### WriteBinaryFileFromBase64
![WriteBinaryFileFromBase64 op](images/ops/Ops_Extension_Standalone_Files_WriteBinaryFileFromBase64.svg)

**Full Name:** `Ops.Extension.Standalone.Files.WriteBinaryFileFromBase64`

Create a binary file on the local file system from a base64 string.

**`\inputsymbol`{=latex} Inputs**

- **Trigger** (Trigger)
- **Base64** (String)
- **Filename** (String)

**Example Patch:** [cables.gl/op/Ops.Extension.Standalone.Files.WriteBinaryFileFromBase64#example](https://cables.gl/op/Ops.Extension.Standalone.Files.WriteBinaryFileFromBase64#example)

**Doc:** [cables.gl/op/Ops.Extension.Standalone.Files.WriteBinaryFileFromBase64](https://cables.gl/op/Ops.Extension.Standalone.Files.WriteBinaryFileFromBase64)

### WriteTextFile
![WriteTextFile op](images/ops/Ops_Extension_Standalone_Files_WriteTextFile.svg)

**Full Name:** `Ops.Extension.Standalone.Files.WriteTextFile`

Write a string to a text file on the local file system.

**`\inputsymbol`{=latex} Inputs**

- **Filename** (String)
- **Content** (String)
- **Write** (Trigger)

**`\outputsymbol`{=latex} Output**

- **Next** (Trigger)
- **Has Error** (booleanNumber)
- **Error** (String)

**Example Patch:** [cables.gl/edit/PT9Aun](https://cables.gl/edit/PT9Aun)

**Doc:** [cables.gl/op/Ops.Extension.Standalone.Files.WriteTextFile](https://cables.gl/op/Ops.Extension.Standalone.Files.WriteTextFile)


