# Ops.Extension.TeachableMachines

*Part of the [All Operators Reference](13-_AllOps.md)*

---

## Ops.Extension.TeachableMachines

### AudioClassifier
![AudioClassifier op](images/ops/Ops_Extension_TeachableMachines_AudioClassifier.svg)

**Full Name:** `Ops.Extension.TeachableMachines.AudioClassifier`
**Description:** Use the Teachable Machines audio classifier for your microphone. Insert the uploaded model URL.

**> Input Ports:**

- **Trigger In** (Trigger)
- **Initialize** (Trigger)
- **Model URL** (String)

**< Output Ports:**

- **Trigger** (Trigger)
- **Initialized** (Trigger)
- **Classifier** (Array)

**Example Patch:** [Open in Editor](https://cables.gl/edit/-kzrrn)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "AudioClassifier"*
**Docs:** [https://cables.gl/op/Ops.Extension.TeachableMachines.AudioClassifier](https://cables.gl/op/Ops.Extension.TeachableMachines.AudioClassifier)

---

### ImageClassifier_v2
![ImageClassifier_v2 op](images/ops/Ops_Extension_TeachableMachines_ImageClassifier_v2.svg)

**Full Name:** `Ops.Extension.TeachableMachines.ImageClassifier_v2`
**Description:** Use the Teachable Machines image classifier. Insert the uploaded model URL.

**> Input Ports:**

- **Trigger In** (Trigger)
- **Initialize** (Trigger)
- **Model URL** (String)
- **Webcam Element** (Object)

**< Output Ports:**

- **Trigger** (Trigger)
- **Initialized** (Trigger)
- **Classifier** (Array)

**Example Patch:** [Open in Editor](https://cables.gl/edit/raewrn)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ImageClassifier_v2"*
**Docs:** [https://cables.gl/op/Ops.Extension.TeachableMachines.ImageClassifier_v2](https://cables.gl/op/Ops.Extension.TeachableMachines.ImageClassifier_v2)

---

### PoseDetection_v2
![PoseDetection_v2 op](images/ops/Ops_Extension_TeachableMachines_PoseDetection_v2.svg)

**Full Name:** `Ops.Extension.TeachableMachines.PoseDetection_v2`
**Description:** Use the Teachable Machines pose detection with your webcam. Insert the uploaded model URL.

**> Input Ports:**

- **Render** (Trigger)
- **Initialize** (Trigger)
- **Model URL** (String)
- **Webcam Element** (Object)
- **Flip Image** (Number: Boolean)

**< Output Ports:**

- **Trigger** (Trigger)
- **Initialized** (Trigger)
- **Classifier** (Array)
- **Pose Positions** (Array)
- **Image Flipped** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/edit/xOStrn)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "PoseDetection_v2"*
**Docs:** [https://cables.gl/op/Ops.Extension.TeachableMachines.PoseDetection_v2](https://cables.gl/op/Ops.Extension.TeachableMachines.PoseDetection_v2)

---

