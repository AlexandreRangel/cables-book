# Ops.Website

*Part of the [All Operators Reference](13-_AllOps.md)*

---

## Ops.Website

### Cookie
![Cookie op](images/ops/Ops_Website_Cookie.svg)

**Full Name:** `Ops.Website.Cookie`
**Description:** cookie of the current website as object

**> Input Ports:**
- *Visit [Ops.Website.Cookie documentation](https://cables.gl/op/Ops.Website.Cookie) for input port details*

**< Output Ports:**
- **Cookie** (Object): *See documentation*
- **Cookie String** (String): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/oNMzci)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "Cookie"*
**Docs:** [https://cables.gl/op/Ops.Website.Cookie](https://cables.gl/op/Ops.Website.Cookie)

---

### FilenameInfo
![FilenameInfo op](images/ops/Ops_Website_FilenameInfo.svg)

**Full Name:** `Ops.Website.FilenameInfo`
**Description:** information about a filename, like url protocol, suffix etc

**> Input Ports:**
- **URL** (String): *See documentation*

**< Output Ports:**
- **Protocol** (String): *See documentation*
- **Host** (String): *See documentation*
- **Full Path** (String): *See documentation*
- **Filename** (String): *See documentation*
- **Basename** (String): *See documentation*
- **Suffix** (String): *See documentation*
- **Is URL** (String): *See documentation*
- **QueryParams** (String): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/RyrLMg)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "FilenameInfo"*
**Docs:** [https://cables.gl/op/Ops.Website.FilenameInfo](https://cables.gl/op/Ops.Website.FilenameInfo)

---

### ForceHttps
![ForceHttps op](images/ops/Ops_Website_ForceHttps.svg)

**Full Name:** `Ops.Website.ForceHttps`
**Description:** will redirect to same URL using https protocol

**> Input Ports:**
- *Visit [Ops.Website.ForceHttps documentation](https://cables.gl/op/Ops.Website.ForceHttps) for input port details*

**< Output Ports:**
- *Visit [Ops.Website.ForceHttps documentation](https://cables.gl/op/Ops.Website.ForceHttps) for output port details*

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Website.ForceHttps#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ForceHttps"*
**Docs:** [https://cables.gl/op/Ops.Website.ForceHttps](https://cables.gl/op/Ops.Website.ForceHttps)

---

### InfoURL
![InfoURL op](images/ops/Ops_Website_InfoURL.svg)

**Full Name:** `Ops.Website.InfoURL`
**Description:** Information about the current URL

**> Input Ports:**
- *Visit [Ops.Website.InfoURL documentation](https://cables.gl/op/Ops.Website.InfoURL) for input port details*

**< Output Ports:**
- **URL** (String): *See documentation*
- **Host** (String): *See documentation*
- **Hash** (String): *See documentation*
- **Pathname** (String): *See documentation*
- **Protocol** (String): *See documentation*
- **Port** (String): *See documentation*
- **Hash Changed** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/9UM2YG)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "InfoURL"*
**Docs:** [https://cables.gl/op/Ops.Website.InfoURL](https://cables.gl/op/Ops.Website.InfoURL)

---

### InIframe
![InIframe op](images/ops/Ops_Website_InIframe.svg)

**Full Name:** `Ops.Website.InIframe`
**Description:** Outputs true if the patch is inside of an iframe

**> Input Ports:**
- *Visit [Ops.Website.InIframe documentation](https://cables.gl/op/Ops.Website.InIframe) for input port details*

**< Output Ports:**
- **In Iframe** (booleanNumber): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/qWDDci)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "InIframe"*
**Docs:** [https://cables.gl/op/Ops.Website.InIframe](https://cables.gl/op/Ops.Website.InIframe)

---

### LocalStorageNumber
![LocalStorageNumber op](images/ops/Ops_Website_LocalStorageNumber.svg)

**Full Name:** `Ops.Website.LocalStorageNumber`
**Description:** Store and retreive a number in browser localstorage

**> Input Ports:**
- **Key** (String): *See documentation*
- **Number** (Number): *See documentation*
- **Store** (Trigger): *See documentation*

**< Output Ports:**
- **Stored Number** (Number): *See documentation*
- **Storage Support** (Number): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/9di48i)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "LocalStorageNumber"*
**Docs:** [https://cables.gl/op/Ops.Website.LocalStorageNumber](https://cables.gl/op/Ops.Website.LocalStorageNumber)

---

### LocalStorageString
![LocalStorageString op](images/ops/Ops_Website_LocalStorageString.svg)

**Full Name:** `Ops.Website.LocalStorageString`
**Description:** Store and retreive a string in browser localstorage

**> Input Ports:**
- **Key** (String): *See documentation*
- **String** (String): *See documentation*
- **Store** (Trigger): *See documentation*

**< Output Ports:**
- **Stored String** (String): *See documentation*
- **Storage Support** (booleanNumber): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/QKe58i)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "LocalStorageString"*
**Docs:** [https://cables.gl/op/Ops.Website.LocalStorageString](https://cables.gl/op/Ops.Website.LocalStorageString)

---

### LocationHashRoute
![LocationHashRoute op](images/ops/Ops_Website_LocationHashRoute.svg)

**Full Name:** `Ops.Website.LocationHashRoute`
**Description:** gives updated information about window.location.hash

**> Input Ports:**
- **Route** (String): *See documentation*
- **pattern for url and variables** (i.e. /scene/:id): *See documentation*

**< Output Ports:**
- **Values** (Object): *See documentation*
- **Changed** (Trigger): *See documentation*
- **Matching** (booleanNumber): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/EfiWpG)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "LocationHashRoute"*
**Docs:** [https://cables.gl/op/Ops.Website.LocationHashRoute](https://cables.gl/op/Ops.Website.LocationHashRoute)

---

### SetLocationHash
![SetLocationHash op](images/ops/Ops_Website_SetLocationHash.svg)

**Full Name:** `Ops.Website.SetLocationHash`
**Description:** sets window.location.hash to the specified value(s)

**> Input Ports:**
- **Hash** (String): *See documentation*
- **Update** (Trigger): *See documentation*
- **Active** (Number: Boolean): *See documentation*
- **Silent** (Number: Boolean): *See documentation*
- **Allow Empty** (Number: Boolean): *See documentation*

**< Output Ports:**
- *Visit [Ops.Website.SetLocationHash documentation](https://cables.gl/op/Ops.Website.SetLocationHash) for output port details*

**Example Patch:** [Open in Editor](https://cables.gl/edit/EfiWpG)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "SetLocationHash"*
**Docs:** [https://cables.gl/op/Ops.Website.SetLocationHash](https://cables.gl/op/Ops.Website.SetLocationHash)

---

### UrlQueryParams_v2
![UrlQueryParams_v2 op](images/ops/Ops_Website_UrlQueryParams_v2.svg)

**Full Name:** `Ops.Website.UrlQueryParams_v2`
**Description:** Returns a URL query parameter

**> Input Ports:**
- **Parameter** (String): *See documentation*
- **Default** (String): *See documentation*

**< Output Ports:**
- **Result** (String): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/2SE58i)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "UrlQueryParams_v2"*
**Docs:** [https://cables.gl/op/Ops.Website.UrlQueryParams_v2](https://cables.gl/op/Ops.Website.UrlQueryParams_v2)

---

