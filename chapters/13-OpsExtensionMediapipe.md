# Ops.Extension.Mediapipe

*Part of the [All Operators Reference](13-_AllOps.md)*

---

## Ops.Extension.Mediapipe

### FaceMesh
![FaceMesh op](images/ops/Ops_Extension_Mediapipe_FaceMesh.svg)

**Full Name:** `Ops.Extension.Mediapipe.FaceMesh`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Extension.Mediapipe.FaceMesh) for details*

**> Input Ports:**
- **Geom** (Object)
- **Points** (Array)

**< Output Ports:**
- **Result Geom** (Object)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Extension.Mediapipe.FaceMesh#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "FaceMesh"*
**Docs:** [https://cables.gl/op/Ops.Extension.Mediapipe.FaceMesh](https://cables.gl/op/Ops.Extension.Mediapipe.FaceMesh)

---

### MpFaceTracking
![MpFaceTracking op](images/ops/Ops_Extension_Mediapipe_MpFaceTracking.svg)

**Full Name:** `Ops.Extension.Mediapipe.MpFaceTracking`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Extension.Mediapipe.MpFaceTracking) for details*

**> Input Ports:**
- **Element** (Object)
- **Refine LandMarks** (Number: Boolean)

**< Output Ports:**
- **Points** (Array)
- **Found** (Number)
- **Result** (Object)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Extension.Mediapipe.MpFaceTracking#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "MpFaceTracking"*
**Docs:** [https://cables.gl/op/Ops.Extension.Mediapipe.MpFaceTracking](https://cables.gl/op/Ops.Extension.Mediapipe.MpFaceTracking)

---

### MpHand
![MpHand op](images/ops/Ops_Extension_Mediapipe_MpHand.svg)

**Full Name:** `Ops.Extension.Mediapipe.MpHand`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Extension.Mediapipe.MpHand) for details*

**> Input Ports:**
- **Hands Result** (Object)
- **Hand Index** (Number: Integer)
- **Min Score** (Number)

**< Output Ports:**
- **Points** (Array)
- **Lines** (Array)
- **Data** (Object)
- **Found Hand** (Number)
- **Score** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Extension.Mediapipe.MpHand#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "MpHand"*
**Docs:** [https://cables.gl/op/Ops.Extension.Mediapipe.MpHand](https://cables.gl/op/Ops.Extension.Mediapipe.MpHand)

---

### MpHandCoordinate
![MpHandCoordinate op](images/ops/Ops_Extension_Mediapipe_MpHandCoordinate.svg)

**Full Name:** `Ops.Extension.Mediapipe.MpHandCoordinate`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Extension.Mediapipe.MpHandCoordinate) for details*

**> Input Ports:**
- **Hand Points** (Array)
- **Joint Index** (Number: Integer)

**< Output Ports:**
- **X** (Number)
- **Y** (Number)
- **Z** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Extension.Mediapipe.MpHandCoordinate#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "MpHandCoordinate"*
**Docs:** [https://cables.gl/op/Ops.Extension.Mediapipe.MpHandCoordinate](https://cables.gl/op/Ops.Extension.Mediapipe.MpHandCoordinate)

---

### MpHandTracking
![MpHandTracking op](images/ops/Ops_Extension_Mediapipe_MpHandTracking.svg)

**Full Name:** `Ops.Extension.Mediapipe.MpHandTracking`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Extension.Mediapipe.MpHandTracking) for details*

**> Input Ports:**
- **Element** (Object:Element)
- **Min Confidence Detect** (Number)
- **Min Confidence Tracking** (Number)

**< Output Ports:**
- **Result** (Object)
- **Found Hands** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Extension.Mediapipe.MpHandTracking#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "MpHandTracking"*
**Docs:** [https://cables.gl/op/Ops.Extension.Mediapipe.MpHandTracking](https://cables.gl/op/Ops.Extension.Mediapipe.MpHandTracking)

---

### MpPoseGetCoordinate
![MpPoseGetCoordinate op](images/ops/Ops_Extension_Mediapipe_MpPoseGetCoordinate.svg)

**Full Name:** `Ops.Extension.Mediapipe.MpPoseGetCoordinate`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Extension.Mediapipe.MpPoseGetCoordinate) for details*

**> Input Ports:**
- **Landmarks** (Array)
- **Landmark Index** (Number: Integer)

**< Output Ports:**
- **X** (Number)
- **Y** (Number)
- **Z** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Extension.Mediapipe.MpPoseGetCoordinate#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "MpPoseGetCoordinate"*
**Docs:** [https://cables.gl/op/Ops.Extension.Mediapipe.MpPoseGetCoordinate](https://cables.gl/op/Ops.Extension.Mediapipe.MpPoseGetCoordinate)

---

### MpPoseTracking
![MpPoseTracking op](images/ops/Ops_Extension_Mediapipe_MpPoseTracking.svg)

**Full Name:** `Ops.Extension.Mediapipe.MpPoseTracking`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Extension.Mediapipe.MpPoseTracking) for details*

**> Input Ports:**
- **Element** (Object:Element)
- **Smooth Landmarks** (Number: Boolean)
- **Min Detection Confidence** (Number)
- **Min Tracking Confidence** (Number)
- **Enable Segmentation** (Number: Boolean)
- **Update Texture** (Trigger)
- **Smooth Segmentation** (Number: Boolean)
- **Flip X** (Number: Boolean)
- **Flip Y** (Number: Boolean)

**< Output Ports:**
- **Points** (Array)
- **Segmentation Mask** (Object)
- **Landmarks** (Array)
- **Lines** (Array)
- **Found** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Extension.Mediapipe.MpPoseTracking#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "MpPoseTracking"*
**Docs:** [https://cables.gl/op/Ops.Extension.Mediapipe.MpPoseTracking](https://cables.gl/op/Ops.Extension.Mediapipe.MpPoseTracking)

---

