# Ops.Sidebar

*Part of the [All Operators Reference](13-_AllOps.md)*

---

## Ops.Sidebar

### Button_v2
![Button_v2 op](images/ops/Ops_Sidebar_Button_v2.svg)

**Full Name:** `Ops.Sidebar.Button_v2`
**Description:** sidebar push button/trigger element

**> Input Ports:**
- **Link** (Object): *See documentation*
- **Text** (String): *See documentation*
- **Grey Out** (Number: Boolean): *See documentation*
- **Visible** (Number: Boolean): *See documentation*

**< Output Ports:**
- **Childs** (Object): *See documentation*
- **Pressed Trigger** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/aDgYX5)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "Button_v2"*
**Docs:** [https://cables.gl/op/Ops.Sidebar.Button_v2](https://cables.gl/op/Ops.Sidebar.Button_v2)

---

### ColorPicker_v3
![ColorPicker_v3 op](images/ops/Ops_Sidebar_ColorPicker_v3.svg)

**Full Name:** `Ops.Sidebar.ColorPicker_v3`
**Description:** Shows a color-picker in the sidebar

**> Input Ports:**
- **Link** (Object): *See documentation*
- **Text** (String): *See documentation*
- **Input Red** (Number): *See documentation*
- **Input Green** (Number): *See documentation*
- **Input Blue** (Number): *See documentation*
- **Input Opacity** (Number): *See documentation*
- **Set Default** (Trigger): *See documentation*
- **Show Opacity** (Number: Boolean): *See documentation*

**< Output Ports:**
- **Children** (Object): *See documentation*
- **Red** (Number): *See documentation*
- **Green** (Number): *See documentation*
- **Blue** (Number): *See documentation*
- **Opacity** (Number): *See documentation*
- **Hex** (String): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/8-XQ5d)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ColorPicker_v3"*
**Docs:** [https://cables.gl/op/Ops.Sidebar.ColorPicker_v3](https://cables.gl/op/Ops.Sidebar.ColorPicker_v3)

---

### DisplayValue_v2
![DisplayValue_v2 op](images/ops/Ops_Sidebar_DisplayValue_v2.svg)

**Full Name:** `Ops.Sidebar.DisplayValue_v2`
**Description:** display a value or string

**> Input Ports:**
- **Link** (Object): *See documentation*
- **Text** (String): *See documentation*
- **Value** (String): *See documentation*

**< Output Ports:**
- **Childs** (Object): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/aDgYX5)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "DisplayValue_v2"*
**Docs:** [https://cables.gl/op/Ops.Sidebar.DisplayValue_v2](https://cables.gl/op/Ops.Sidebar.DisplayValue_v2)

---

### DropDown_v2
![DropDown_v2 op](images/ops/Ops_Sidebar_DropDown_v2.svg)

**Full Name:** `Ops.Sidebar.DropDown_v2`
**Description:** Shows a drop-down (select) element in the sidebar

**> Input Ports:**
- **Link** (Object): *See documentation*
- **Text** (String): *See documentation*
- **Values** (Array): *See documentation*
- **Grey Out** (Number: Boolean): *See documentation*
- **Visible** (Number: Boolean): *See documentation*
- **Multiple Selection** (Number: Boolean): *See documentation*
- **Lines** (Number: Integer): *See documentation*
- **Set Default** (Trigger): *See documentation*

**< Output Ports:**
- **Children** (Object): *See documentation*
- **Result** (String): *See documentation*
- **Index** (Number): *See documentation*
- **Selected Values** (Array): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/0wKJ5d)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "DropDown_v2"*
**Docs:** [https://cables.gl/op/Ops.Sidebar.DropDown_v2](https://cables.gl/op/Ops.Sidebar.DropDown_v2)

---

### Group
![Group op](images/ops/Ops_Sidebar_Group.svg)

**Full Name:** `Ops.Sidebar.Group`
**Description:** organize sidebar elements into groups

**> Input Ports:**
- **Link** (Object): *See documentation*
- **Text** (String): *See documentation*
- **Show Title** (Number: Boolean): *See documentation*
- **Default Minimized** (Number: Boolean): *See documentation*
- **Visible** (Number: Boolean): *See documentation*

**< Output Ports:**
- **Next** (Object): *See documentation*
- **Childs** (Object): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Sidebar.Group#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "Group"*
**Docs:** [https://cables.gl/op/Ops.Sidebar.Group](https://cables.gl/op/Ops.Sidebar.Group)

---

### Incrementor_v3
![Incrementor_v3 op](images/ops/Ops_Sidebar_Incrementor_v3.svg)

**Full Name:** `Ops.Sidebar.Incrementor_v3`
**Description:** steps through numerical or array values one by one

**> Input Ports:**
- **Link** (Object): *See documentation*
- **Label** (String): *See documentation*
- **Min** (Number): *See documentation*
- **Max** (Number): *See documentation*
- **Stepsize** (Number): *See documentation*
- **Default** (Number): *See documentation*
- **Grey Out** (Number: Boolean): *See documentation*
- **Increment** (Trigger): *See documentation*
- **Decrement** (Trigger): *See documentation*
- **Set Default** (Trigger): *See documentation*
- **Reset** (Trigger): *See documentation*

**< Output Ports:**
- **Childs** (Object): *See documentation*
- **Value** (Number): *See documentation*
- **Changed** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/DLV0n6)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "Incrementor_v3"*
**Docs:** [https://cables.gl/op/Ops.Sidebar.Incrementor_v3](https://cables.gl/op/Ops.Sidebar.Incrementor_v3)

---

### LocalFileToDataUrl
![LocalFileToDataUrl op](images/ops/Ops_Sidebar_LocalFileToDataUrl.svg)

**Full Name:** `Ops.Sidebar.LocalFileToDataUrl`
**Description:** load a local file and output as data url

**> Input Ports:**
- **Link** (Object): *See documentation*
- **Text** (String): *See documentation*
- **Button Text** (String): *See documentation*
- **Accept Files** (String): *See documentation*
- **Allow Multiple Files** (Number: Boolean): *See documentation*
- **Id** (Number: String): *See documentation*
- **Visible** (Number: Boolean): *See documentation*
- **Grey Out** (Number: Boolean): *See documentation*
- **Show Dialog** (Trigger): *See documentation*
- **Reset** (Trigger): *See documentation*

**< Output Ports:**
- **Childs** (Object): *See documentation*
- **Data URL** (String): *See documentation*
- **Filename** (String): *See documentation*
- **File Object** (Object): *See documentation*
- **Num Files** (Number): *See documentation*
- **Data URLs** (Array): *See documentation*
- **Filenames** (Array): *See documentation*
- **File Changed** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/a0V6xn)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "LocalFileToDataUrl"*
**Docs:** [https://cables.gl/op/Ops.Sidebar.LocalFileToDataUrl](https://cables.gl/op/Ops.Sidebar.LocalFileToDataUrl)

---

### NumberInput_v2
![NumberInput_v2 op](images/ops/Ops_Sidebar_NumberInput_v2.svg)

**Full Name:** `Ops.Sidebar.NumberInput_v2`
**Description:** Enter a number in the sidebar

**> Input Ports:**
- **Link** (Object): *See documentation*
- **Text** (String): *See documentation*
- **Set Default** (Trigger): *See documentation*

**< Output Ports:**
- **Children** (Object): *See documentation*
- **Result** (Number): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/aDgYX5)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "NumberInput_v2"*
**Docs:** [https://cables.gl/op/Ops.Sidebar.NumberInput_v2](https://cables.gl/op/Ops.Sidebar.NumberInput_v2)

---

### Presets_v2
![Presets_v2 op](images/ops/Ops_Sidebar_Presets_v2.svg)

**Full Name:** `Ops.Sidebar.Presets_v2`
**Description:** manage sidebar presets

**> Input Ports:**
- **Link** (Object): *See documentation*
- **Text** (String): *See documentation*
- **Add Preset** (Trigger): *See documentation*
- **Update Current Preset** (Trigger): *See documentation*
- **Preset Title 0** (String): *See documentation*
- **Preset 0** (Object): *See documentation*
- **Preset Title 1** (String): *See documentation*
- **Preset 1** (Object): *See documentation*
- **Preset Title 2** (String): *See documentation*
- **Preset 2** (Object): *See documentation*
- **Preset Title 3** (String): *See documentation*
- **Preset 3** (Object): *See documentation*
- **Preset Title 4** (String): *See documentation*
- **Preset 4** (Object): *See documentation*
- **Preset Title 5** (String): *See documentation*
- **Preset 5** (Object): *See documentation*
- **Preset Title 6** (String): *See documentation*
- **Preset 6** (Object): *See documentation*
- **Preset Title 7** (String): *See documentation*
- **Preset 7** (Object): *See documentation*

**< Output Ports:**
- **Children** (Object): *See documentation*
- **Index** (Number): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/KKabBN)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "Presets_v2"*
**Docs:** [https://cables.gl/op/Ops.Sidebar.Presets_v2](https://cables.gl/op/Ops.Sidebar.Presets_v2)

---

### Sidebar
![Sidebar op](images/ops/Ops_Sidebar_Sidebar.svg)

**Full Name:** `Ops.Sidebar.Sidebar`
**Description:** Sidebar overlay to control values

**> Input Ports:**
- **Visible** (Number: Boolean): *See documentation*
- **Opacity** (Number): *See documentation*
- **Default Minimized** (Number: Boolean): *See documentation*
- **Minimized Opacity** (Number): *See documentation*
- **Show Undo Button** (Number: Boolean): *See documentation*
- **Show Minimize** (Number: Boolean): *See documentation*
- **Title** (String): *See documentation*
- **Side** (Number: Boolean): *See documentation*
- **Default CSS** (Number: Boolean): *See documentation*

**< Output Ports:**
- **Childs** (Object): *See documentation*
- **Opfened** (booleanNumber): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/aDgYX5)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "Sidebar"*
**Docs:** [https://cables.gl/op/Ops.Sidebar.Sidebar](https://cables.gl/op/Ops.Sidebar.Sidebar)

---

### SidebarDateTime
![SidebarDateTime op](images/ops/Ops_Sidebar_SidebarDateTime.svg)

**Full Name:** `Ops.Sidebar.SidebarDateTime`
**Description:** date or datetime picker in the sidebar

**> Input Ports:**
- **Link** (Object): *See documentation*
- **Text** (String): *See documentation*
- **Default** (String): *See documentation*
- **Min** (String): *See documentation*
- **Max** (String): *See documentation*
- **Type Index** (Number: Integer): *See documentation*
- **Grey Out** (Number: Boolean): *See documentation*
- **Visible** (Number: Boolean): *See documentation*

**< Output Ports:**
- **Children** (Object): *See documentation*
- **Result** (String): *See documentation*
- **Focus** (booleanNumber): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/Bkzmci)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "SidebarDateTime"*
**Docs:** [https://cables.gl/op/Ops.Sidebar.SidebarDateTime](https://cables.gl/op/Ops.Sidebar.SidebarDateTime)

---

### SidebarElement
![SidebarElement op](images/ops/Ops_Sidebar_SidebarElement.svg)

**Full Name:** `Ops.Sidebar.SidebarElement`
**Description:** Add custom HTML Elements into the sidebar

**> Input Ports:**
- **Link** (Object): *See documentation*
- **Child Element** (Object): *See documentation*
- **Border** (Number: Boolean): *See documentation*
- **Visible** (Number: Boolean): *See documentation*

**< Output Ports:**
- **Childs** (Object): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/CQrFox)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "SidebarElement"*
**Docs:** [https://cables.gl/op/Ops.Sidebar.SidebarElement](https://cables.gl/op/Ops.Sidebar.SidebarElement)

---

### SideBarImage
![SideBarImage op](images/ops/Ops_Sidebar_SideBarImage.svg)

**Full Name:** `Ops.Sidebar.SideBarImage`
**Description:** Display an image in the sidebar

**> Input Ports:**
- **Link** (Object): *See documentation*
- **File** (String): *See documentation*

**< Output Ports:**
- **Childs** (Object): *See documentation*
- **Image Element** (Object): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/nLvdby)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "SideBarImage"*
**Docs:** [https://cables.gl/op/Ops.Sidebar.SideBarImage](https://cables.gl/op/Ops.Sidebar.SideBarImage)

---

### SideBarStyle
![SideBarStyle op](images/ops/Ops_Sidebar_SideBarStyle.svg)

**Full Name:** `Ops.Sidebar.SideBarStyle`
**Description:** adjust appearance of sidebar

**> Input Ports:**
- **Link** (Object): *See documentation*
- **Width** (Number: Integer): *See documentation*
- **Round Corners** (Number): *See documentation*
- **Special Color** (String): *See documentation*

**< Output Ports:**
- **Childs** (Object): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/o1fXgI)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "SideBarStyle"*
**Docs:** [https://cables.gl/op/Ops.Sidebar.SideBarStyle](https://cables.gl/op/Ops.Sidebar.SideBarStyle)

---

### SideBarSwitch
![SideBarSwitch op](images/ops/Ops_Sidebar_SideBarSwitch.svg)

**Full Name:** `Ops.Sidebar.SideBarSwitch`
**Description:** add tabs or switchbar to a sidebar

**> Input Ports:**
- **Link** (Object): *See documentation*
- **Names** (Array): *See documentation*
- **Text** (String): *See documentation*
- **Set Default** (Trigger): *See documentation*
- **Grey Out** (Number: Boolean): *See documentation*
- **Default** (Number): *See documentation*

**< Output Ports:**
- **Childs** (Object): *See documentation*
- **Index** (Number): *See documentation*
- **String** (String): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/7uuz6D)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "SideBarSwitch"*
**Docs:** [https://cables.gl/op/Ops.Sidebar.SideBarSwitch](https://cables.gl/op/Ops.Sidebar.SideBarSwitch)

---

### SidebarText_v3
![SidebarText_v3 op](images/ops/Ops_Sidebar_SidebarText_v3.svg)

**Full Name:** `Ops.Sidebar.SidebarText_v3`
**Description:** Display text in the sidebar

**> Input Ports:**
- **Link** (Object): *See documentation*
- **Text** (String): *See documentation*
- **Id** (String): *See documentation*
- **Visible** (Number: Boolean): *See documentation*

**< Output Ports:**
- **Childs** (Object): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/Ut4y8i)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "SidebarText_v3"*
**Docs:** [https://cables.gl/op/Ops.Sidebar.SidebarText_v3](https://cables.gl/op/Ops.Sidebar.SidebarText_v3)

---

### SidebarVariables
![SidebarVariables op](images/ops/Ops_Sidebar_SidebarVariables.svg)

**Full Name:** `Ops.Sidebar.SidebarVariables`
**Description:** show values of all variables in a sidebar

**> Input Ports:**
- **Link** (Object): *See documentation*
- **Id** (Number: String): *See documentation*
- **Update** (Trigger): *See documentation*

**< Output Ports:**
- **Childs** (Object): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/H2kYgL)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "SidebarVariables"*
**Docs:** [https://cables.gl/op/Ops.Sidebar.SidebarVariables](https://cables.gl/op/Ops.Sidebar.SidebarVariables)

---

### Slider_v3
![Slider_v3 op](images/ops/Ops_Sidebar_Slider_v3.svg)

**Full Name:** `Ops.Sidebar.Slider_v3`
**Description:** Sidebar slider element (range)

**> Input Ports:**
- **Link** (Object): *See documentation*
- **Text** (String): *See documentation*
- **Min** (Number): *See documentation*
- **Max** (Number): *See documentation*
- **Step** (Number): *See documentation*
- **Suffix** (String): *See documentation*
- **Grey Out** (Number: Boolean): *See documentation*
- **Visible** (Number: Boolean): *See documentation*
- **Set Default** (Trigger): *See documentation*
- **Reset** (Trigger): *See documentation*

**< Output Ports:**
- **Childs** (Object): *See documentation*
- **Result** (Number): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/aDgYX5)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "Slider_v3"*
**Docs:** [https://cables.gl/op/Ops.Sidebar.Slider_v3](https://cables.gl/op/Ops.Sidebar.Slider_v3)

---

### TextInput_v2
![TextInput_v2 op](images/ops/Ops_Sidebar_TextInput_v2.svg)

**Full Name:** `Ops.Sidebar.TextInput_v2`
**Description:** Get a string from an sidebar input field

**> Input Ports:**
- **Link** (Object): *See documentation*
- **Where to attach the sidebar item to** (Sidebar / Sidebar Group): *See documentation*
- **Text** (String): *See documentation*
- **Default** (String): *See documentation*
- **Placeholder** (String): *See documentation*
- **TextArea** (Number: Boolean): *See documentation*
- **Grey Out** (Number: Boolean): *See documentation*
- **Visible** (Number: Boolean): *See documentation*
- **Spellcheck** (Number: Boolean): *See documentation*
- **Enter Key Prevent Default** (Number: Boolean): *See documentation*
- **Clear** (Trigger): *See documentation*
- **Focus Input** (Trigger): *See documentation*

**< Output Ports:**
- **Children** (Object): *See documentation*
- **Result** (String): *See documentation*
- **Focus** (booleanNumber): *See documentation*
- **Keypress Enter** (Trigger): *See documentation*
- **Keypress ESC** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/wa-KH-)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "TextInput_v2"*
**Docs:** [https://cables.gl/op/Ops.Sidebar.TextInput_v2](https://cables.gl/op/Ops.Sidebar.TextInput_v2)

---

### Toggle_v4
![Toggle_v4 op](images/ops/Ops_Sidebar_Toggle_v4.svg)

**Full Name:** `Ops.Sidebar.Toggle_v4`
**Description:** sidebar boolean toggle/switch element

**> Input Ports:**
- **Link** (Object): *See documentation*
- **Text** (String): *See documentation*
- **Set Default** (Trigger): *See documentation*
- **Grey Out** (Number: Boolean): *See documentation*
- **Visible** (Number: Boolean): *See documentation*

**< Output Ports:**
- **Childs** (Object): *See documentation*
- **Value** (booleanNumber): *See documentation*
- **Toggled** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/aDgYX5)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "Toggle_v4"*
**Docs:** [https://cables.gl/op/Ops.Sidebar.Toggle_v4](https://cables.gl/op/Ops.Sidebar.Toggle_v4)

---

### XYPad
![XYPad op](images/ops/Ops_Sidebar_XYPad.svg)

**Full Name:** `Ops.Sidebar.XYPad`
**Description:** 2d coordinate input element

**> Input Ports:**
- **Link** (Object): *See documentation*
- **Text** (String): *See documentation*
- **Input X** (Number): *See documentation*
- **Input Y** (Number): *See documentation*
- **Flip X** (Number: Boolean): *See documentation*
- **Flip Y** (Number: Boolean): *See documentation*
- **Set Default** (Trigger): *See documentation*
- **Visible** (Number: Boolean): *See documentation*

**< Output Ports:**
- **Children** (Object): *See documentation*
- **X** (Number): *See documentation*
- **Y** (Number): *See documentation*
- **HTML Element** (Object): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/0NF2FL)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "XYPad"*
**Docs:** [https://cables.gl/op/Ops.Sidebar.XYPad](https://cables.gl/op/Ops.Sidebar.XYPad)

---

