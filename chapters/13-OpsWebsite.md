# Ops.Website


```{=latex}
\OpsSubsubNoSubsectionNumbering\setcounter{subsubsection}{0}
```
### Cookie
![Cookie op](images/ops/Ops_Website_Cookie.svg)

**Full Name:** `Ops.Website.Cookie`

cookie of the current website as object.

**`\outputsymbol`{=latex} Output**

- **Cookie** (Object)
- **Cookie String** (String)

**Example:** [cables.gl/edit/oNMzci](https://cables.gl/edit/oNMzci)

**Doc:** [cables.gl/op/Ops.Website.Cookie](https://cables.gl/op/Ops.Website.Cookie)

### FilenameInfo
![FilenameInfo op](images/ops/Ops_Website_FilenameInfo.svg)

**Full Name:** `Ops.Website.FilenameInfo`

information about a filename, like url protocol, suffix etc.

**`\inputsymbol`{=latex} Inputs**

- **URL** (String)

**`\outputsymbol`{=latex} Output**

- **Protocol** (String)
- **Host** (String)
- **Full Path** (String)
- **Filename** (String)
- **Basename** (String)
- **Suffix** (String)
- **Is URL** (String)
- **QueryParams** (String)

**Example:** [cables.gl/edit/RyrLMg](https://cables.gl/edit/RyrLMg)

**Doc:** [cables.gl/op/Ops.Website.FilenameInfo](https://cables.gl/op/Ops.Website.FilenameInfo)

### ForceHttps
![ForceHttps op](images/ops/Ops_Website_ForceHttps.svg)

**Full Name:** `Ops.Website.ForceHttps`

will redirect to same URL using https protocol.

**Example:** [cables.gl/op/Ops.Website.ForceHttps#example](https://cables.gl/op/Ops.Website.ForceHttps#example)

**Doc:** [cables.gl/op/Ops.Website.ForceHttps](https://cables.gl/op/Ops.Website.ForceHttps)

### InfoURL
![InfoURL op](images/ops/Ops_Website_InfoURL.svg)

**Full Name:** `Ops.Website.InfoURL`

Information about the current URL.

**`\outputsymbol`{=latex} Output**

- **URL** (String)
- **Host** (String)
- **Hash** (String)
- **Pathname** (String)
- **Protocol** (String)
- **Port** (String)
- **Hash Changed** (Trigger)

**Example:** [cables.gl/edit/9UM2YG](https://cables.gl/edit/9UM2YG)

**Doc:** [cables.gl/op/Ops.Website.InfoURL](https://cables.gl/op/Ops.Website.InfoURL)

### InIframe
![InIframe op](images/ops/Ops_Website_InIframe.svg)

**Full Name:** `Ops.Website.InIframe`

Outputs true if the patch is inside of an iframe.

**`\outputsymbol`{=latex} Output**

- **In Iframe** (booleanNumber)

**Example:** [cables.gl/edit/qWDDci](https://cables.gl/edit/qWDDci)

**Doc:** [cables.gl/op/Ops.Website.InIframe](https://cables.gl/op/Ops.Website.InIframe)

### LocalStorageNumber
![LocalStorageNumber op](images/ops/Ops_Website_LocalStorageNumber.svg)

**Full Name:** `Ops.Website.LocalStorageNumber`

Store and retreive a number in browser localstorage.

**`\inputsymbol`{=latex} Inputs**

- **Key** (String)
- **Number** (Number)
- **Store** (Trigger)

**`\outputsymbol`{=latex} Output**

- **Stored Number** (Number)
- **Storage Support** (Number)

**Example:** [cables.gl/edit/9di48i](https://cables.gl/edit/9di48i)

**Doc:** [cables.gl/op/Ops.Website.LocalStorageNumber](https://cables.gl/op/Ops.Website.LocalStorageNumber)

### LocalStorageString
![LocalStorageString op](images/ops/Ops_Website_LocalStorageString.svg)

**Full Name:** `Ops.Website.LocalStorageString`

Store and retreive a string in browser localstorage.

**`\inputsymbol`{=latex} Inputs**

- **Key** (String)
- **String** (String)
- **Store** (Trigger)

**`\outputsymbol`{=latex} Output**

- **Stored String** (String)
- **Storage Support** (booleanNumber)

**Example:** [cables.gl/edit/QKe58i](https://cables.gl/edit/QKe58i)

**Doc:** [cables.gl/op/Ops.Website.LocalStorageString](https://cables.gl/op/Ops.Website.LocalStorageString)

### LocationHashRoute
![LocationHashRoute op](images/ops/Ops_Website_LocationHashRoute.svg)

**Full Name:** `Ops.Website.LocationHashRoute`

gives updated information about window.location.hash.

**`\inputsymbol`{=latex} Inputs**

- **Route** (String)
- **pattern for url and variables** (i.e. /scene/:id)

**`\outputsymbol`{=latex} Output**

- **Values** (Object)
- **Changed** (Trigger)
- **Matching** (booleanNumber)

**Example:** [cables.gl/edit/EfiWpG](https://cables.gl/edit/EfiWpG)

**Doc:** [cables.gl/op/Ops.Website.LocationHashRoute](https://cables.gl/op/Ops.Website.LocationHashRoute)

### SetLocationHash
![SetLocationHash op](images/ops/Ops_Website_SetLocationHash.svg)

**Full Name:** `Ops.Website.SetLocationHash`

sets window.location.hash to the specified value(s).

**`\inputsymbol`{=latex} Inputs**

- **Hash** (String)
- **Update** (Trigger)
- **Active** (Number: Boolean)
- **Silent** (Number: Boolean)
- **Allow Empty** (Number: Boolean)

**Example:** [cables.gl/edit/EfiWpG](https://cables.gl/edit/EfiWpG)

**Doc:** [cables.gl/op/Ops.Website.SetLocationHash](https://cables.gl/op/Ops.Website.SetLocationHash)

### UrlQueryParams_v2
![UrlQueryParams_v2 op](images/ops/Ops_Website_UrlQueryParams_v2.svg)

**Full Name:** `Ops.Website.UrlQueryParams_v2`

Returns a URL query parameter.

**`\inputsymbol`{=latex} Inputs**

- **Parameter** (String)
- **Default** (String)

**`\outputsymbol`{=latex} Output**

- **Result** (String)

**Example:** [cables.gl/edit/2SE58i](https://cables.gl/edit/2SE58i)

**Doc:** [cables.gl/op/Ops.Website.UrlQueryParams_v2](https://cables.gl/op/Ops.Website.UrlQueryParams_v2)


