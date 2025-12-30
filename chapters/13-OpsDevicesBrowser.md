# Ops.Devices.Browser

*Part of the [All Operators Reference](13-_AllOps.md)*

---

## Ops.Devices.Browser

### BrowserInfo_v3
![BrowserInfo_v3 op](images/ops/Ops_Devices_Browser_BrowserInfo_v3.svg)

**Full Name:** `Ops.Devices.Browser.BrowserInfo_v3`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Devices.Browser.BrowserInfo_v3) for details*

**> Input Ports:**
- *Visit [Ops.Devices.Browser.BrowserInfo_v3 documentation](https://cables.gl/op/Ops.Devices.Browser.BrowserInfo_v3) for input port details*

**< Output Ports:**
- **Is Mobile** (booleanNumber)
- **Is Touchscreen** (booleanNumber)
- **Is IE** (booleanNumber)
- **Is Edge** (booleanNumber)
- **Is Chrome** (booleanNumber)
- **Is Firefox** (booleanNumber)
- **Is Opera** (booleanNumber)
- **Is Safari** (booleanNumber)
- **True if the browser is Safari** (iOS & macOS & OS X)
- **Is Windows** (booleanNumber)
- **Is Linux** (booleanNumber)
- **Is Mac** (booleanNumber)
- **Is IOS** (booleanNumber)
- **Is Android** (booleanNumber)
- **Is Electron** (booleanNumber)
- **Operating System** (String)
- **Browser Name** (String)
- **Browser Version** (String)
- **OS Version** (String)
- **Language** (String)
- **User Agent** (String)
- **Platform Object** (Object)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Devices.Browser.BrowserInfo_v3#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "BrowserInfo_v3"*
**Docs:** [https://cables.gl/op/Ops.Devices.Browser.BrowserInfo_v3](https://cables.gl/op/Ops.Devices.Browser.BrowserInfo_v3)

---

### ColorScheme
![ColorScheme op](images/ops/Ops_Devices_Browser_ColorScheme.svg)

**Full Name:** `Ops.Devices.Browser.ColorScheme`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Devices.Browser.ColorScheme) for details*

**> Input Ports:**
- *Visit [Ops.Devices.Browser.ColorScheme documentation](https://cables.gl/op/Ops.Devices.Browser.ColorScheme) for input port details*

**< Output Ports:**
- **Color Scheme** (String)
- **Dark Mode** (booleanNumber)
- **Light Mode** (booleanNumber)
- **Supported** (booleanNumber)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Devices.Browser.ColorScheme#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ColorScheme"*
**Docs:** [https://cables.gl/op/Ops.Devices.Browser.ColorScheme](https://cables.gl/op/Ops.Devices.Browser.ColorScheme)

---

### History
![History op](images/ops/Ops_Devices_Browser_History.svg)

**Full Name:** `Ops.Devices.Browser.History`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Devices.Browser.History) for details*

**> Input Ports:**
- **Back** (Trigger)
- **Forward** (Trigger)

**< Output Ports:**
- *Visit [Ops.Devices.Browser.History documentation](https://cables.gl/op/Ops.Devices.Browser.History) for output port details*

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Devices.Browser.History#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "History"*
**Docs:** [https://cables.gl/op/Ops.Devices.Browser.History](https://cables.gl/op/Ops.Devices.Browser.History)

---

### JsExpression
![JsExpression op](images/ops/Ops_Devices_Browser_JsExpression.svg)

**Full Name:** `Ops.Devices.Browser.JsExpression`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Devices.Browser.JsExpression) for details*

**> Input Ports:**
- **JS Expression** (String)

**< Output Ports:**
- **Result String** (String)
- **Result Number** (Number)
- **Result Array** (Array)
- **Result Object** (Object)
- **Error** (booleanNumber)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Devices.Browser.JsExpression#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "JsExpression"*
**Docs:** [https://cables.gl/op/Ops.Devices.Browser.JsExpression](https://cables.gl/op/Ops.Devices.Browser.JsExpression)

---

### JsMemory
![JsMemory op](images/ops/Ops_Devices_Browser_JsMemory.svg)

**Full Name:** `Ops.Devices.Browser.JsMemory`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Devices.Browser.JsMemory) for details*

**> Input Ports:**
- **Update** (Trigger)

**< Output Ports:**
- **Used Heap Size** (Number)
- **Total Heap Size** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Devices.Browser.JsMemory#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "JsMemory"*
**Docs:** [https://cables.gl/op/Ops.Devices.Browser.JsMemory](https://cables.gl/op/Ops.Devices.Browser.JsMemory)

---

### UserActivation
![UserActivation op](images/ops/Ops_Devices_Browser_UserActivation.svg)

**Full Name:** `Ops.Devices.Browser.UserActivation`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Devices.Browser.UserActivation) for details*

**> Input Ports:**
- **Update** (Trigger)

**< Output Ports:**
- **Next** (Trigger)
- **User Is Or Was Active** (booleanNumber)
- **User Has Been Active** (booleanNumber)
- **User Is Active** (booleanNumber)
- **Supported** (booleanNumber)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Devices.Browser.UserActivation#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "UserActivation"*
**Docs:** [https://cables.gl/op/Ops.Devices.Browser.UserActivation](https://cables.gl/op/Ops.Devices.Browser.UserActivation)

---

### WebShare
![WebShare op](images/ops/Ops_Devices_Browser_WebShare.svg)

**Full Name:** `Ops.Devices.Browser.WebShare`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Devices.Browser.WebShare) for details*

**> Input Ports:**
- **Text** (String)
- **URL** (String)
- **Base64 File** (String)
- **Data URL** (String)
- **Filetype** (String)
- **Filename** (String)
- **Share** (Trigger)

**< Output Ports:**
- **Status** (String)
- **Supported** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Devices.Browser.WebShare#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "WebShare"*
**Docs:** [https://cables.gl/op/Ops.Devices.Browser.WebShare](https://cables.gl/op/Ops.Devices.Browser.WebShare)

---

