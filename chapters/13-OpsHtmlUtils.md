# Ops.Html.Utils

*Part of the [All Operators Reference](13-_AllOps.md)*

---

## Ops.Html.Utils

### CablesLink
![CablesLink op](images/ops/Ops_Html_Utils_CablesLink.svg)

**Full Name:** `Ops.Html.Utils.CablesLink`
**Description:** create a cables logo which links to cables gl

**> Input Ports:**
- **Size** (Number): *See documentation*
- **Opacity** (Number): *See documentation*

**< Output Ports:**
- *Visit [Ops.Html.Utils.CablesLink documentation](https://cables.gl/op/Ops.Html.Utils.CablesLink) for output port details*

**Example Patch:** [Open in Editor](https://cables.gl/edit/ilts7O)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "CablesLink"*
**Docs:** [https://cables.gl/op/Ops.Html.Utils.CablesLink](https://cables.gl/op/Ops.Html.Utils.CablesLink)

---

### LoadingIndicator_v2
![LoadingIndicator_v2 op](images/ops/Ops_Html_Utils_LoadingIndicator_v2.svg)

**Full Name:** `Ops.Html.Utils.LoadingIndicator_v2`
**Description:** show a typical web loading/progress indicator animation

**> Input Ports:**
- **Center Position** (Number: Boolean): *See documentation*

**< Output Ports:**
- **Elment** (Object): *See documentation*
- **Requests** (Array): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/EsV74q)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "LoadingIndicator_v2"*
**Docs:** [https://cables.gl/op/Ops.Html.Utils.LoadingIndicator_v2](https://cables.gl/op/Ops.Html.Utils.LoadingIndicator_v2)

---

### Notification
![Notification op](images/ops/Ops_Html_Utils_Notification.svg)

**Full Name:** `Ops.Html.Utils.Notification`
**Description:** Trigger a simple pop up notification on the screen

**> Input Ports:**
- **Trigger Animation** (Trigger): *See documentation*
- **Text** (String): *See documentation*
- **Class** (String): *See documentation*
- **Style** (String): *See documentation*
- **Active** (Number: Boolean): *See documentation*
- **Convert Line Breaks** (Number: Boolean): *See documentation*
- **Fade In** (Number): *See documentation*
- **Hold** (Number): *See documentation*
- **Fade Out** (Number): *See documentation*
- **Mode Index** (Number: Integer): *See documentation*
- **Side Index** (Number: Integer): *See documentation*
- **Starting Position** (Number): *See documentation*
- **Ending Position** (Number): *See documentation*

**< Output Ports:**
- **Finished Trigger** (Trigger): *See documentation*
- **Finished** (booleanNumber): *See documentation*
- **DOM Element** (Object): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/2Rue0j)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "Notification"*
**Docs:** [https://cables.gl/op/Ops.Html.Utils.Notification](https://cables.gl/op/Ops.Html.Utils.Notification)

---

### PlayButton
![PlayButton op](images/ops/Ops_Html_Utils_PlayButton.svg)

**Full Name:** `Ops.Html.Utils.PlayButton`
**Description:** shows a playbutton for forcing a simple user interaction

**> Input Ports:**
- **Trigger** (Trigger): *See documentation*
- **Only If Audio Suspended** (Number: Boolean): *See documentation*
- **Reset** (Trigger): *See documentation*
- **Style Outer** (String): *See documentation*
- **Style Inner** (String): *See documentation*
- **Active** (Number: Boolean): *See documentation*

**< Output Ports:**
- **Next** (Trigger): *See documentation*
- **Not Clicked** (Trigger): *See documentation*
- **Audiocontext State** (String): *See documentation*
- **Element** (Object): *See documentation*
- **Clicked** (booleanNumber): *See documentation*
- **Clicked Trigger** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/WoGy8s)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "PlayButton"*
**Docs:** [https://cables.gl/op/Ops.Html.Utils.PlayButton](https://cables.gl/op/Ops.Html.Utils.PlayButton)

---

### PlayerControlPanel_v2
![PlayerControlPanel_v2 op](images/ops/Ops_Html_Utils_PlayerControlPanel_v2.svg)

**Full Name:** `Ops.Html.Utils.PlayerControlPanel_v2`
**Description:** simple html ui for timeline/mediaplayers (was: TimeLineUI)

**> Input Ports:**
- **Length** (Number): *See documentation*
- **Current** (Number): *See documentation*
- **Clamp** (Number: Boolean): *See documentation*
- **Is Playing** (Number: Boolean): *See documentation*
- **Visible** (Number: Boolean): *See documentation*
- **Show Time** (Number: Boolean): *See documentation*
- **Show Skip Buttons** (Number: Boolean): *See documentation*

**< Output Ports:**
- **Play Clicked** (Trigger): *See documentation*
- **Pause Clicked** (Trigger): *See documentation*
- **Rewind Clicked** (Trigger): *See documentation*
- **Skip Back Clicked** (Trigger): *See documentation*
- **Skip Forward Clicked** (Trigger): *See documentation*
- **Dragged** (Trigger): *See documentation*
- **Current Value** (Number): *See documentation*
- **Dragging** (booleanNumber): *See documentation*
- **DOM Element** (Object): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/3F6DOe)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "PlayerControlPanel_v2"*
**Docs:** [https://cables.gl/op/Ops.Html.Utils.PlayerControlPanel_v2](https://cables.gl/op/Ops.Html.Utils.PlayerControlPanel_v2)

---

### QrCode
![QrCode op](images/ops/Ops_Html_Utils_QrCode.svg)

**Full Name:** `Ops.Html.Utils.QrCode`
**Description:** Generate a qr code as a texture

**> Input Ports:**
- **Text** (String): *See documentation*

**< Output Ports:**
- **Image DataUrl** (String): *See documentation*
- **Element** (Object): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/QjlEo-)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "QrCode"*
**Docs:** [https://cables.gl/op/Ops.Html.Utils.QrCode](https://cables.gl/op/Ops.Html.Utils.QrCode)

---

### YoutubePlayer
![YoutubePlayer op](images/ops/Ops_Html_Utils_YoutubePlayer.svg)

**Full Name:** `Ops.Html.Utils.YoutubePlayer`
**Description:** play a youtube video in a HTML element

**> Input Ports:**
- **Video Id** (String): *See documentation*
- **Active** (Number: Boolean): *See documentation*
- **Style** (String): *See documentation*
- **ElementID** (String): *See documentation*
- **Autoplay** (Number: Boolean): *See documentation*
- **Display Captions** (Number: Boolean): *See documentation*
- **Loop** (Number: Boolean): *See documentation*
- **Allow Fullscreen** (Number: Boolean): *See documentation*
- **Hide Controls** (Number: Boolean): *See documentation*
- **Start At Second** (Number: Integer): *See documentation*

**< Output Ports:**
- **Element** (Object): *See documentation*
- **Direct Link** (String): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/aMkD16)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "YoutubePlayer"*
**Docs:** [https://cables.gl/op/Ops.Html.Utils.YoutubePlayer](https://cables.gl/op/Ops.Html.Utils.YoutubePlayer)

---

