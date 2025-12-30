# Ops.Html.Elements

*Part of the [All Operators Reference](13-_AllOps.md)*

---

## Ops.Html.Elements

### AudioMediaElement
![AudioMediaElement op](images/ops/Ops_Html_Elements_AudioMediaElement.svg)

**Full Name:** `Ops.Html.Elements.AudioMediaElement`
**Description:** Simple Audio Player, using HTML5 Audio, does not need WebAudio

**> Input Ports:**
- **File** (String): *See documentation*
- **Play** (Number: Boolean): *See documentation*
- **Volume** (Number): *See documentation*
- **Loop** (Number: Boolean): *See documentation*

**< Output Ports:**
- **Playing** (Number): *See documentation*
- **Element** (Object): *See documentation*
- **Has Ended** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/ftHtx3)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "AudioMediaElement"*
**Docs:** [https://cables.gl/op/Ops.Html.Elements.AudioMediaElement](https://cables.gl/op/Ops.Html.Elements.AudioMediaElement)

---

### Element_v2
![Element_v2 op](images/ops/Ops_Html_Elements_Element_v2.svg)

**Full Name:** `Ops.Html.Elements.Element_v2`
**Description:** A more convinient version of div element op, that can be used for creating html without writing much css code

**> Input Ports:**
- **Text** (String): *See documentation*
- **Set Size** (Number: Boolean): *See documentation*
- **Width** (Number): *See documentation*
- **Height** (Number): *See documentation*
- **Inline Style** (String): *See documentation*
- **CSS Class** (String): *See documentation*
- **Disable CSS Props** (String): *See documentation*
- **Display Index** (Number: Integer): *See documentation*
- **Tag Name** (String): *See documentation*
- **Opacity** (Number): *See documentation*
- **Propagate Click-Events** (Number: Boolean): *See documentation*
- **Add To DOM** (Number: Boolean): *See documentation*

**< Output Ports:**
- **DOM Element** (Object): *See documentation*
- **Hovering** (booleanNumber): *See documentation*
- **Clicked** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/KmnVEm)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "Element_v2"*
**Docs:** [https://cables.gl/op/Ops.Html.Elements.Element_v2](https://cables.gl/op/Ops.Html.Elements.Element_v2)

---

### IFrame_v3
![IFrame_v3 op](images/ops/Ops_Html_Elements_IFrame_v3.svg)

**Full Name:** `Ops.Html.Elements.IFrame_v3`
**Description:** Show another website in an iframe element

**> Input Ports:**
- **URL** (String): *See documentation*
- **ID** (String): *See documentation*
- **Active** (Number: Boolean): *See documentation*
- **Style** (String): *See documentation*

**< Output Ports:**
- **Element** (Object): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/SLesr2)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "IFrame_v3"*
**Docs:** [https://cables.gl/op/Ops.Html.Elements.IFrame_v3](https://cables.gl/op/Ops.Html.Elements.IFrame_v3)

---

### ImageElement_v3
![ImageElement_v3 op](images/ops/Ops_Html_Elements_ImageElement_v3.svg)

**Full Name:** `Ops.Html.Elements.ImageElement_v3`
**Description:** create an image(img) html element

**> Input Ports:**
- **File** (String): *See documentation*
- **Class** (String): *See documentation*
- **Style** (String): *See documentation*
- **Alt Text** (String): *See documentation*

**< Output Ports:**
- **Image Element** (Object): *See documentation*
- **Width** (Number): *See documentation*
- **Height** (Number): *See documentation*
- **Loading** (booleanNumber): *See documentation*
- **Error** (booleanNumber): *See documentation*
- **Loaded** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/OZaVN8)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ImageElement_v3"*
**Docs:** [https://cables.gl/op/Ops.Html.Elements.ImageElement_v3](https://cables.gl/op/Ops.Html.Elements.ImageElement_v3)

---

### InputElement
![InputElement op](images/ops/Ops_Html_Elements_InputElement.svg)

**Full Name:** `Ops.Html.Elements.InputElement`
**Description:** HTML input/textarea element to allow the user to enter text

**> Input Ports:**
- **Default Value** (String): *See documentation*
- **Placeholder** (String): *See documentation*
- **Id** (String): *See documentation*
- **Class** (String): *See documentation*
- **Style** (String): *See documentation*
- **Autocomplete** (Number: Boolean): *See documentation*
- **Max Length** (Number: Integer): *See documentation*
- **Enter Key Prevent Default** (Number: Boolean): *See documentation*
- **Visible** (Number: Boolean): *See documentation*
- **Focus** (Trigger): *See documentation*
- **Blur** (Trigger): *See documentation*
- **Clear** (Trigger): *See documentation*
- **Select** (Trigger): *See documentation*

**< Output Ports:**
- **DOM Element** (Object): *See documentation*
- **Value** (String): *See documentation*
- **Hover** (booleanNumber): *See documentation*
- **Enter Pressed** (Trigger): *See documentation*
- **Escape Pressed** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/L83aeG)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "InputElement"*
**Docs:** [https://cables.gl/op/Ops.Html.Elements.InputElement](https://cables.gl/op/Ops.Html.Elements.InputElement)

---

### VideoElement
![VideoElement op](images/ops/Ops_Html_Elements_VideoElement.svg)

**Full Name:** `Ops.Html.Elements.VideoElement`
**Description:** html video player element

**> Input Ports:**
- **File** (String): *See documentation*
- **ID** (String): *See documentation*
- **Play** (Number: Boolean): *See documentation*
- **Autoplay** (Number: Boolean): *See documentation*
- **Controls** (Number: Boolean): *See documentation*
- **Active** (Number: Boolean): *See documentation*
- **Loop** (Number: Boolean): *See documentation*
- **Muted** (Number: Boolean): *See documentation*
- **Style** (String): *See documentation*
- **Rewind** (Trigger): *See documentation*

**< Output Ports:**
- **Element** (Object): *See documentation*
- **Playing** (booleanNumber): *See documentation*
- **Can Play Through** (booleanNumber): *See documentation*
- **Time** (Number): *See documentation*
- **Ended** (Trigger): *See documentation*
- **Has Error** (booleanNumber): *See documentation*
- **Error Message** (String): *See documentation*
- **Video Width** (Number): *See documentation*
- **Video Height** (Number): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/1QTBve)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "VideoElement"*
**Docs:** [https://cables.gl/op/Ops.Html.Elements.VideoElement](https://cables.gl/op/Ops.Html.Elements.VideoElement)

---

