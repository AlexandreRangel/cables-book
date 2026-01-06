# Ops.Html.Elements


```{=latex}
\OpsSubsubNoSubsectionNumbering\setcounter{subsubsection}{0}
```
### AudioMediaElement
![AudioMediaElement op](images/ops/Ops_Html_Elements_AudioMediaElement.svg)

**Full Name:** `Ops.Html.Elements.AudioMediaElement`

**Description:** Simple Audio Player, using HTML5 Audio, does not need WebAudio

**`\inputsymbol`{=latex} Inputs**

- **File** (String)
- **Play** (Number: Boolean)
- **Volume** (Number)
- **Loop** (Number: Boolean)

**`\outputsymbol`{=latex} Output**

- **Playing** (Number)
- **Element** (Object)
- **Has Ended** (Trigger)

**Example Patch:** [Open in Editor](https://cables.gl/edit/ftHtx3)

**Docs:** [https://cables.gl/op/Ops.Html.Elements.AudioMediaElement](https://cables.gl/op/Ops.Html.Elements.AudioMediaElement)

### Element_v2
![Element_v2 op](images/ops/Ops_Html_Elements_Element_v2.svg)

**Full Name:** `Ops.Html.Elements.Element_v2`

**Description:** A more convinient version of div element op, that can be used for creating html without writing much css code

**`\inputsymbol`{=latex} Inputs**

- **Text** (String)
- **Set Size** (Number: Boolean)
- **Width** (Number)
- **Height** (Number)
- **Inline Style** (String)
- **CSS Class** (String)
- **Disable CSS Props** (String)
- **Display Index** (Number: Integer)
- **Tag Name** (String)
- **Opacity** (Number)
- **Propagate Click-Events** (Number: Boolean)
- **Add To DOM** (Number: Boolean)

**`\outputsymbol`{=latex} Output**

- **DOM Element** (Object)
- **Hovering** (booleanNumber)
- **Clicked** (Trigger)

**Example Patch:** [Open in Editor](https://cables.gl/edit/KmnVEm)

**Docs:** [https://cables.gl/op/Ops.Html.Elements.Element_v2](https://cables.gl/op/Ops.Html.Elements.Element_v2)

### IFrame_v3
![IFrame_v3 op](images/ops/Ops_Html_Elements_IFrame_v3.svg)

**Full Name:** `Ops.Html.Elements.IFrame_v3`

**Description:** Show another website in an iframe element

**`\inputsymbol`{=latex} Inputs**

- **URL** (String)
- **ID** (String)
- **Active** (Number: Boolean)
- **Style** (String)

**`\outputsymbol`{=latex} Output**

- **Element** (Object)

**Example Patch:** [Open in Editor](https://cables.gl/edit/SLesr2)

**Docs:** [https://cables.gl/op/Ops.Html.Elements.IFrame_v3](https://cables.gl/op/Ops.Html.Elements.IFrame_v3)

### ImageElement_v3
![ImageElement_v3 op](images/ops/Ops_Html_Elements_ImageElement_v3.svg)

**Full Name:** `Ops.Html.Elements.ImageElement_v3`

**Description:** create an image(img) html element

**`\inputsymbol`{=latex} Inputs**

- **File** (String)
- **Class** (String)
- **Style** (String)
- **Alt Text** (String)

**`\outputsymbol`{=latex} Output**

- **Image Element** (Object)
- **Width** (Number)
- **Height** (Number)
- **Loading** (booleanNumber)
- **Error** (booleanNumber)
- **Loaded** (Trigger)

**Example Patch:** [Open in Editor](https://cables.gl/edit/OZaVN8)

**Docs:** [https://cables.gl/op/Ops.Html.Elements.ImageElement_v3](https://cables.gl/op/Ops.Html.Elements.ImageElement_v3)

### InputElement
![InputElement op](images/ops/Ops_Html_Elements_InputElement.svg)

**Full Name:** `Ops.Html.Elements.InputElement`

**Description:** HTML input/textarea element to allow the user to enter text

**`\inputsymbol`{=latex} Inputs**

- **Default Value** (String)
- **Placeholder** (String)
- **Id** (String)
- **Class** (String)
- **Style** (String)
- **Autocomplete** (Number: Boolean)
- **Max Length** (Number: Integer)
- **Enter Key Prevent Default** (Number: Boolean)
- **Visible** (Number: Boolean)
- **Focus** (Trigger)
- **Blur** (Trigger)
- **Clear** (Trigger)
- **Select** (Trigger)

**`\outputsymbol`{=latex} Output**

- **DOM Element** (Object)
- **Value** (String)
- **Hover** (booleanNumber)
- **Enter Pressed** (Trigger)
- **Escape Pressed** (Trigger)

**Example Patch:** [Open in Editor](https://cables.gl/edit/L83aeG)

**Docs:** [https://cables.gl/op/Ops.Html.Elements.InputElement](https://cables.gl/op/Ops.Html.Elements.InputElement)

### VideoElement
![VideoElement op](images/ops/Ops_Html_Elements_VideoElement.svg)

**Full Name:** `Ops.Html.Elements.VideoElement`

**Description:** html video player element

**`\inputsymbol`{=latex} Inputs**

- **File** (String)
- **ID** (String)
- **Play** (Number: Boolean)
- **Autoplay** (Number: Boolean)
- **Controls** (Number: Boolean)
- **Active** (Number: Boolean)
- **Loop** (Number: Boolean)
- **Muted** (Number: Boolean)
- **Style** (String)
- **Rewind** (Trigger)

**`\outputsymbol`{=latex} Output**

- **Element** (Object)
- **Playing** (booleanNumber)
- **Can Play Through** (booleanNumber)
- **Time** (Number)
- **Ended** (Trigger)
- **Has Error** (booleanNumber)
- **Error Message** (String)
- **Video Width** (Number)
- **Video Height** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/edit/1QTBve)

**Docs:** [https://cables.gl/op/Ops.Html.Elements.VideoElement](https://cables.gl/op/Ops.Html.Elements.VideoElement)


