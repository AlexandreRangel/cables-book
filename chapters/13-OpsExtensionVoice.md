# Ops.Extension.Voice

*Part of the [All Operators Reference](13-_AllOps.md)*

---

## Ops.Extension.Voice

### MeSpeak
![MeSpeak op](images/ops/Ops_Extension_Voice_MeSpeak.svg)

**Full Name:** `Ops.Extension.Voice.MeSpeak`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Extension.Voice.MeSpeak) for details*

**> Input Ports:**
- **Text** (String)
- **Say** (Trigger)
- **Amplitude** (Number)
- **Pitch** (Number)
- **Voice Index** (Number: Integer)
- **Word Gap** (Number: Integer)
- **Variants Index** (Number: Integer)
- **Line-Break Length** (Number: Integer)
- **Capitals** (Number: Integer)
- **Punctuation** (String)
- **No Stop** (Number: Boolean)
- **UTF16** (Number: Boolean)
- **SSML** (Number: Boolean)
- **Log Console** (Number: Boolean)
- **Pan** (Number)

**< Output Ports:**
- **Audio Out** (Object)
- **Speaking** (booleanNumber)
- **Voice Loaded** (booleanNumber)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Extension.Voice.MeSpeak#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "MeSpeak"*
**Docs:** [https://cables.gl/op/Ops.Extension.Voice.MeSpeak](https://cables.gl/op/Ops.Extension.Voice.MeSpeak)

---

### Say_v2
![Say_v2 op](images/ops/Ops_Extension_Voice_Say_v2.svg)

**Full Name:** `Ops.Extension.Voice.Say_v2`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Extension.Voice.Say_v2) for details*

**> Input Ports:**
- **Update State** (Trigger)
- **Text** (String)
- **Say** (Trigger)
- **Voice** (Number: Select Box)
- **Pitch** (Number)
- **Rate** (Number)
- **Volume** (Number)
- **Say On Text Change** (Number: Boolean)
- **Pause** (Trigger)
- **Resume** (Trigger)
- **Cancel** (Trigger)

**< Output Ports:**
- **Next** (Trigger)
- **Speaking** (Number)
- **Pending** (Number)
- **Paused** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Extension.Voice.Say_v2#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "Say_v2"*
**Docs:** [https://cables.gl/op/Ops.Extension.Voice.Say_v2](https://cables.gl/op/Ops.Extension.Voice.Say_v2)

---

### SpeechRecognition
![SpeechRecognition op](images/ops/Ops_Extension_Voice_SpeechRecognition.svg)

**Full Name:** `Ops.Extension.Voice.SpeechRecognition`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Extension.Voice.SpeechRecognition) for details*

**> Input Ports:**
- **Language** (String)
- **Active** (Number: Boolean)
- **Start** (Trigger)

**< Output Ports:**
- **Result** (String)
- **Confidence** (Number)
- **Supported** (booleanNumber)
- **New Result** (Trigger)
- **Started** (booleanNumber)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Extension.Voice.SpeechRecognition#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "SpeechRecognition"*
**Docs:** [https://cables.gl/op/Ops.Extension.Voice.SpeechRecognition](https://cables.gl/op/Ops.Extension.Voice.SpeechRecognition)

---

