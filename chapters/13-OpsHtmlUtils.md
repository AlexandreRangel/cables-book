# Ops.Html.Utils

*Part of the [All Operators Reference](13-_AllOps.md)*

---

## Ops.Html.Utils

### CablesLink
![CablesLink op](images/ops/Ops_Html_Utils_CablesLink.svg)

**Full Name:** `Ops.Html.Utils.CablesLink`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Html.Utils.CablesLink) for details*

**> Input Ports:**
- **Size** (Number)
- **Opacity** (Number)

**< Output Ports:**
- *Visit [Ops.Html.Utils.CablesLink documentation](https://cables.gl/op/Ops.Html.Utils.CablesLink) for output port details*

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Html.Utils.CablesLink#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "CablesLink"*
**Docs:** [https://cables.gl/op/Ops.Html.Utils.CablesLink](https://cables.gl/op/Ops.Html.Utils.CablesLink)

---

### LoadingIndicator_v2
![LoadingIndicator_v2 op](images/ops/Ops_Html_Utils_LoadingIndicator_v2.svg)

**Full Name:** `Ops.Html.Utils.LoadingIndicator_v2`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Html.Utils.LoadingIndicator_v2) for details*

**> Input Ports:**
- **Center Position** (Number: Boolean)

**< Output Ports:**
- **Elment** (Object)
- **Requests** (Array)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Html.Utils.LoadingIndicator_v2#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "LoadingIndicator_v2"*
**Docs:** [https://cables.gl/op/Ops.Html.Utils.LoadingIndicator_v2](https://cables.gl/op/Ops.Html.Utils.LoadingIndicator_v2)

---

### Notification
![Notification op](images/ops/Ops_Html_Utils_Notification.svg)

**Full Name:** `Ops.Html.Utils.Notification`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Html.Utils.Notification) for details*

**> Input Ports:**
- **Trigger Animation** (Trigger)
- **Text** (String)
- **Class** (String)
- **Style** (String)
- **Active** (Number: Boolean)
- **Convert Line Breaks** (Number: Boolean)
- **Fade In** (Number)
- **Hold** (Number)
- **Fade Out** (Number)
- **Mode Index** (Number: Integer)
- **Side Index** (Number: Integer)
- **Starting Position** (Number)
- **Ending Position** (Number)

**< Output Ports:**
- **Finished Trigger** (Trigger)
- **Finished** (booleanNumber)
- **DOM Element** (Object)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Html.Utils.Notification#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "Notification"*
**Docs:** [https://cables.gl/op/Ops.Html.Utils.Notification](https://cables.gl/op/Ops.Html.Utils.Notification)

---

### PlayButton
![PlayButton op](images/ops/Ops_Html_Utils_PlayButton.svg)

**Full Name:** `Ops.Html.Utils.PlayButton`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Html.Utils.PlayButton) for details*

**> Input Ports:**
- **Trigger** (Trigger)
- **Only If Audio Suspended** (Number: Boolean)
- **Reset** (Trigger)
- **Style Outer** (String)
- **Style Inner** (String)
- **Active** (Number: Boolean)

**< Output Ports:**
- **Next** (Trigger)
- **Not Clicked** (Trigger)
- **Audiocontext State** (String)
- **Element** (Object)
- **Clicked** (booleanNumber)
- **Clicked Trigger** (Trigger)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Html.Utils.PlayButton#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "PlayButton"*
**Docs:** [https://cables.gl/op/Ops.Html.Utils.PlayButton](https://cables.gl/op/Ops.Html.Utils.PlayButton)

---

### PlayerControlPanel_v2
![PlayerControlPanel_v2 op](images/ops/Ops_Html_Utils_PlayerControlPanel_v2.svg)

**Full Name:** `Ops.Html.Utils.PlayerControlPanel_v2`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Html.Utils.PlayerControlPanel_v2) for details*

**> Input Ports:**
- **Length** (Number)
- **Current** (Number)
- **Clamp** (Number: Boolean)
- **Is Playing** (Number: Boolean)
- **Visible** (Number: Boolean)
- **Show Time** (Number: Boolean)
- **Show Skip Buttons** (Number: Boolean)

**< Output Ports:**
- **Play Clicked** (Trigger)
- **Pause Clicked** (Trigger)
- **Rewind Clicked** (Trigger)
- **Skip Back Clicked** (Trigger)
- **Skip Forward Clicked** (Trigger)
- **Dragged** (Trigger)
- **Current Value** (Number)
- **Dragging** (booleanNumber)
- **DOM Element** (Object)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Html.Utils.PlayerControlPanel_v2#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "PlayerControlPanel_v2"*
**Docs:** [https://cables.gl/op/Ops.Html.Utils.PlayerControlPanel_v2](https://cables.gl/op/Ops.Html.Utils.PlayerControlPanel_v2)

---

### QrCode
![QrCode op](images/ops/Ops_Html_Utils_QrCode.svg)

**Full Name:** `Ops.Html.Utils.QrCode`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Html.Utils.QrCode) for details*

**> Input Ports:**
- **Text** (String)

**< Output Ports:**
- **Image DataUrl** (String)
- **Element** (Object)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Html.Utils.QrCode#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "QrCode"*
**Docs:** [https://cables.gl/op/Ops.Html.Utils.QrCode](https://cables.gl/op/Ops.Html.Utils.QrCode)

---

### YoutubePlayer
![YoutubePlayer op](images/ops/Ops_Html_Utils_YoutubePlayer.svg)

**Full Name:** `Ops.Html.Utils.YoutubePlayer`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Html.Utils.YoutubePlayer) for details*

**> Input Ports:**
- **Video Id** (String)
- **Active** (Number: Boolean)
- **Style** (String)
- **ElementID** (String)
- **Autoplay** (Number: Boolean)
- **Display Captions** (Number: Boolean)
- **Loop** (Number: Boolean)
- **Allow Fullscreen** (Number: Boolean)
- **Hide Controls** (Number: Boolean)
- **Start At Second** (Number: Integer)

**< Output Ports:**
- **Element** (Object)
- **Direct Link** (String)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Html.Utils.YoutubePlayer#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "YoutubePlayer"*
**Docs:** [https://cables.gl/op/Ops.Html.Utils.YoutubePlayer](https://cables.gl/op/Ops.Html.Utils.YoutubePlayer)

---

