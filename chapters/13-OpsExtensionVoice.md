# Ops.Extension.Voice

*Part of the [All Operators Reference](13-_AllOps.md)*

---

## Ops.Extension.Voice

### MeSpeak
![MeSpeak op](images/ops/Ops_Extension_Voice_MeSpeak.svg)

**Full Name:** `Ops.Extension.Voice.MeSpeak`
**Description:** uses mespeak.js to convert text-to-speech

**> Input Ports:**
- **Text** (String): *See documentation*
- **Say** (Trigger): *See documentation*
- **Amplitude** (Number): *See documentation*
- **Pitch** (Number): *See documentation*
- **Voice Index** (Number: Integer): *See documentation*
- **Word Gap** (Number: Integer): *See documentation*
- **Variants Index** (Number: Integer): *See documentation*
- **Line-Break Length** (Number: Integer): *See documentation*
- **Capitals** (Number: Integer): *See documentation*
- **Punctuation** (String): *See documentation*
- **No Stop** (Number: Boolean): *See documentation*
- **UTF16** (Number: Boolean): *See documentation*
- **SSML** (Number: Boolean): *See documentation*
- **Log Console** (Number: Boolean): *See documentation*
- **Pan** (Number): *See documentation*

**< Output Ports:**
- **Audio Out** (Object): *See documentation*
- **Speaking** (booleanNumber): *See documentation*
- **Voice Loaded** (booleanNumber): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Extension.Voice.MeSpeak#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "MeSpeak"*
**Docs:** [https://cables.gl/op/Ops.Extension.Voice.MeSpeak](https://cables.gl/op/Ops.Extension.Voice.MeSpeak)

---

### Say_v2
![Say_v2 op](images/ops/Ops_Extension_Voice_Say_v2.svg)

**Full Name:** `Ops.Extension.Voice.Say_v2`
**Description:** Text-to-Speech, speaks different languages (speech synthesis)

**> Input Ports:**
- **Update State** (Trigger): *See documentation*
- **Text** (String): *See documentation*
- **Say** (Trigger): *See documentation*
- **Voice** (Number: Select Box): *See documentation*
- **Pitch** (Number): *See documentation*
- **Rate** (Number): *See documentation*
- **Volume** (Number): *See documentation*
- **Say On Text Change** (Number: Boolean): *See documentation*
- **Pause** (Trigger): *See documentation*
- **Resume** (Trigger): *See documentation*
- **Cancel** (Trigger): *See documentation*

**< Output Ports:**
- **Next** (Trigger): *See documentation*
- **Speaking** (Number): *See documentation*
- **Pending** (Number): *See documentation*
- **Paused** (Number): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/WubOWc)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "Say_v2"*
**Docs:** [https://cables.gl/op/Ops.Extension.Voice.Say_v2](https://cables.gl/op/Ops.Extension.Voice.Say_v2)

---

### SpeechRecognition
![SpeechRecognition op](images/ops/Ops_Extension_Voice_SpeechRecognition.svg)

**Full Name:** `Ops.Extension.Voice.SpeechRecognition`
**Description:** speech to text recognition

**> Input Ports:**
- **Language** (String): *See documentation*
- **Active** (Number: Boolean): *See documentation*
- **Start** (Trigger): *See documentation*

**< Output Ports:**
- **Result** (String): *See documentation*
- **Confidence** (Number): *See documentation*
- **Supported** (booleanNumber): *See documentation*
- **New Result** (Trigger): *See documentation*
- **Started** (booleanNumber): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/9p7kw4)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "SpeechRecognition"*
**Docs:** [https://cables.gl/op/Ops.Extension.Voice.SpeechRecognition](https://cables.gl/op/Ops.Extension.Voice.SpeechRecognition)

---

