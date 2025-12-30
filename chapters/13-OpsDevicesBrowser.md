# Ops.Devices.Browser

*Part of the [All Operators Reference](13-_AllOps.md)*

---

## Ops.Devices.Browser

### BrowserInfo_v3
![BrowserInfo_v3 op](images/ops/Ops_Devices_Browser_BrowserInfo_v3.svg)

**Full Name:** `Ops.Devices.Browser.BrowserInfo_v3`
**Description:** Reports the browser being used

**> Input Ports:**
- *Visit [Ops.Devices.Browser.BrowserInfo_v3 documentation](https://cables.gl/op/Ops.Devices.Browser.BrowserInfo_v3) for input port details*

**< Output Ports:**
- **Is Mobile** (booleanNumber): *See documentation*
- **Is Touchscreen** (booleanNumber): *See documentation*
- **Is IE** (booleanNumber): *See documentation*
- **Is Edge** (booleanNumber): *See documentation*
- **Is Chrome** (booleanNumber): *See documentation*
- **Is Firefox** (booleanNumber): *See documentation*
- **Is Opera** (booleanNumber): *See documentation*
- **Is Safari** (booleanNumber): *See documentation*
- **True if the browser is Safari** (iOS & macOS & OS X): *See documentation*
- **Is Windows** (booleanNumber): *See documentation*
- **Is Linux** (booleanNumber): *See documentation*
- **Is Mac** (booleanNumber): *See documentation*
- **Is IOS** (booleanNumber): *See documentation*
- **Is Android** (booleanNumber): *See documentation*
- **Is Electron** (booleanNumber): *See documentation*
- **Operating System** (String): *See documentation*
- **Browser Name** (String): *See documentation*
- **Browser Version** (String): *See documentation*
- **OS Version** (String): *See documentation*
- **Language** (String): *See documentation*
- **User Agent** (String): *See documentation*
- **Platform Object** (Object): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/YOJiIk)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "BrowserInfo_v3"*
**Docs:** [https://cables.gl/op/Ops.Devices.Browser.BrowserInfo_v3](https://cables.gl/op/Ops.Devices.Browser.BrowserInfo_v3)

---

### ColorScheme
![ColorScheme op](images/ops/Ops_Devices_Browser_ColorScheme.svg)

**Full Name:** `Ops.Devices.Browser.ColorScheme`
**Description:** Get light/dark color scheme preference of the browser

**> Input Ports:**
- *Visit [Ops.Devices.Browser.ColorScheme documentation](https://cables.gl/op/Ops.Devices.Browser.ColorScheme) for input port details*

**< Output Ports:**
- **Color Scheme** (String): *See documentation*
- **Dark Mode** (booleanNumber): *See documentation*
- **Light Mode** (booleanNumber): *See documentation*
- **Supported** (booleanNumber): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/An48HJ)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ColorScheme"*
**Docs:** [https://cables.gl/op/Ops.Devices.Browser.ColorScheme](https://cables.gl/op/Ops.Devices.Browser.ColorScheme)

---

### History
![History op](images/ops/Ops_Devices_Browser_History.svg)

**Full Name:** `Ops.Devices.Browser.History`
**Description:** Move back or forward in the browser navigation history

**> Input Ports:**
- **Back** (Trigger): *See documentation*
- **Forward** (Trigger): *See documentation*

**< Output Ports:**
- *Visit [Ops.Devices.Browser.History documentation](https://cables.gl/op/Ops.Devices.Browser.History) for output port details*

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Devices.Browser.History#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "History"*
**Docs:** [https://cables.gl/op/Ops.Devices.Browser.History](https://cables.gl/op/Ops.Devices.Browser.History)

---

### JsExpression
![JsExpression op](images/ops/Ops_Devices_Browser_JsExpression.svg)

**Full Name:** `Ops.Devices.Browser.JsExpression`
**Description:** evaluate a javascript expression

**> Input Ports:**
- **JS Expression** (String): *See documentation*

**< Output Ports:**
- **Result String** (String): *See documentation*
- **Result Number** (Number): *See documentation*
- **Result Array** (Array): *See documentation*
- **Result Object** (Object): *See documentation*
- **Error** (booleanNumber): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/gpp4O8)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "JsExpression"*
**Docs:** [https://cables.gl/op/Ops.Devices.Browser.JsExpression](https://cables.gl/op/Ops.Devices.Browser.JsExpression)

---

### JsMemory
![JsMemory op](images/ops/Ops_Devices_Browser_JsMemory.svg)

**Full Name:** `Ops.Devices.Browser.JsMemory`
**Description:** browser js memory consumption

**> Input Ports:**
- **Update** (Trigger): *See documentation*

**< Output Ports:**
- **Used Heap Size** (Number): *See documentation*
- **Total Heap Size** (Number): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/_UyS0f)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "JsMemory"*
**Docs:** [https://cables.gl/op/Ops.Devices.Browser.JsMemory](https://cables.gl/op/Ops.Devices.Browser.JsMemory)

---

### UserActivation
![UserActivation op](images/ops/Ops_Devices_Browser_UserActivation.svg)

**Full Name:** `Ops.Devices.Browser.UserActivation`
**Description:** detect if the user interacted with or activated the page

**> Input Ports:**
- **Update** (Trigger): *See documentation*

**< Output Ports:**
- **Next** (Trigger): *See documentation*
- **User Is Or Was Active** (booleanNumber): *See documentation*
- **User Has Been Active** (booleanNumber): *See documentation*
- **User Is Active** (booleanNumber): *See documentation*
- **Supported** (booleanNumber): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/3S26Qc)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "UserActivation"*
**Docs:** [https://cables.gl/op/Ops.Devices.Browser.UserActivation](https://cables.gl/op/Ops.Devices.Browser.UserActivation)

---

### WebShare
![WebShare op](images/ops/Ops_Devices_Browser_WebShare.svg)

**Full Name:** `Ops.Devices.Browser.WebShare`
**Description:** Opens a sharing dialog to share text and images

**> Input Ports:**
- **Text** (String): *See documentation*
- **URL** (String): *See documentation*
- **Base64 File** (String): *See documentation*
- **Data URL** (String): *See documentation*
- **Filetype** (String): *See documentation*
- **Filename** (String): *See documentation*
- **Share** (Trigger): *See documentation*

**< Output Ports:**
- **Status** (String): *See documentation*
- **Supported** (Number): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/pQ49m4)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "WebShare"*
**Docs:** [https://cables.gl/op/Ops.Devices.Browser.WebShare](https://cables.gl/op/Ops.Devices.Browser.WebShare)

---

