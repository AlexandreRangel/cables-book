# Ops.Extension.Mediapipe

*Part of the [All Operators Reference](13-_AllOps.md)*

---

## Ops.Extension.Mediapipe

### FaceMesh
![FaceMesh op](images/ops/Ops_Extension_Mediapipe_FaceMesh.svg)

**Full Name:** `Ops.Extension.Mediapipe.FaceMesh`
**Description:** Generate an animated geometry from MpFaceTracking Point Coordinates

**> Input Ports:**
- **Geom** (Object): *See documentation*
- **Points** (Array): *See documentation*

**< Output Ports:**
- **Result Geom** (Object): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/by9Tq4)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "FaceMesh"*
**Docs:** [https://cables.gl/op/Ops.Extension.Mediapipe.FaceMesh](https://cables.gl/op/Ops.Extension.Mediapipe.FaceMesh)

---

### MpFaceTracking
![MpFaceTracking op](images/ops/Ops_Extension_Mediapipe_MpFaceTracking.svg)

**Full Name:** `Ops.Extension.Mediapipe.MpFaceTracking`
**Description:** Get face mesh from webcam/video using mediapipe library

**> Input Ports:**
- **Element** (Object): *See documentation*
- **Refine LandMarks** (Number: Boolean): *See documentation*

**< Output Ports:**
- **Points** (Array): *See documentation*
- **Found** (Number): *See documentation*
- **Result** (Object): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/wznlp4)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "MpFaceTracking"*
**Docs:** [https://cables.gl/op/Ops.Extension.Mediapipe.MpFaceTracking](https://cables.gl/op/Ops.Extension.Mediapipe.MpFaceTracking)

---

### MpHand
![MpHand op](images/ops/Ops_Extension_Mediapipe_MpHand.svg)

**Full Name:** `Ops.Extension.Mediapipe.MpHand`
**Description:** Get points and lines for left/right hand from mediapipe

**> Input Ports:**
- **Hands Result** (Object): *See documentation*
- **Hand Index** (Number: Integer): *See documentation*
- **Min Score** (Number): *See documentation*

**< Output Ports:**
- **Points** (Array): *See documentation*
- **Lines** (Array): *See documentation*
- **Data** (Object): *See documentation*
- **Found Hand** (Number): *See documentation*
- **Score** (Number): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/a5xfp4)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "MpHand"*
**Docs:** [https://cables.gl/op/Ops.Extension.Mediapipe.MpHand](https://cables.gl/op/Ops.Extension.Mediapipe.MpHand)

---

### MpHandCoordinate
![MpHandCoordinate op](images/ops/Ops_Extension_Mediapipe_MpHandCoordinate.svg)

**Full Name:** `Ops.Extension.Mediapipe.MpHandCoordinate`
**Description:** Get individual coordinates of fingers or wrist from an array of mediapipe data

**> Input Ports:**
- **Hand Points** (Array): *See documentation*
- **Joint Index** (Number: Integer): *See documentation*

**< Output Ports:**
- **X** (Number): *See documentation*
- **Y** (Number): *See documentation*
- **Z** (Number): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/a5xfp4)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "MpHandCoordinate"*
**Docs:** [https://cables.gl/op/Ops.Extension.Mediapipe.MpHandCoordinate](https://cables.gl/op/Ops.Extension.Mediapipe.MpHandCoordinate)

---

### MpHandTracking
![MpHandTracking op](images/ops/Ops_Extension_Mediapipe_MpHandTracking.svg)

**Full Name:** `Ops.Extension.Mediapipe.MpHandTracking`
**Description:** Get hand data from mediapipe library, use with MpHand

**> Input Ports:**
- **Element** (Object:Element): *See documentation*
- **Min Confidence Detect** (Number): *See documentation*
- **Min Confidence Tracking** (Number): *See documentation*

**< Output Ports:**
- **Result** (Object): *See documentation*
- **Found Hands** (Number): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/a5xfp4)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "MpHandTracking"*
**Docs:** [https://cables.gl/op/Ops.Extension.Mediapipe.MpHandTracking](https://cables.gl/op/Ops.Extension.Mediapipe.MpHandTracking)

---

### MpPoseGetCoordinate
![MpPoseGetCoordinate op](images/ops/Ops_Extension_Mediapipe_MpPoseGetCoordinate.svg)

**Full Name:** `Ops.Extension.Mediapipe.MpPoseGetCoordinate`
**Description:** Get coordinates of specific body parts from mediapipe data

**> Input Ports:**
- **Landmarks** (Array): *See documentation*
- **Landmark Index** (Number: Integer): *See documentation*

**< Output Ports:**
- **X** (Number): *See documentation*
- **Y** (Number): *See documentation*
- **Z** (Number): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/uepop4)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "MpPoseGetCoordinate"*
**Docs:** [https://cables.gl/op/Ops.Extension.Mediapipe.MpPoseGetCoordinate](https://cables.gl/op/Ops.Extension.Mediapipe.MpPoseGetCoordinate)

---

### MpPoseTracking
![MpPoseTracking op](images/ops/Ops_Extension_Mediapipe_MpPoseTracking.svg)

**Full Name:** `Ops.Extension.Mediapipe.MpPoseTracking`
**Description:** Get pose-data (points/landmarks/lines) from webcam using mediapipe library

**> Input Ports:**
- **Element** (Object:Element): *See documentation*
- **Smooth Landmarks** (Number: Boolean): *See documentation*
- **Min Detection Confidence** (Number): *See documentation*
- **Min Tracking Confidence** (Number): *See documentation*
- **Enable Segmentation** (Number: Boolean): *See documentation*
- **Update Texture** (Trigger): *See documentation*
- **Smooth Segmentation** (Number: Boolean): *See documentation*
- **Flip X** (Number: Boolean): *See documentation*
- **Flip Y** (Number: Boolean): *See documentation*

**< Output Ports:**
- **Points** (Array): *See documentation*
- **Segmentation Mask** (Object): *See documentation*
- **Landmarks** (Array): *See documentation*
- **Lines** (Array): *See documentation*
- **Found** (Number): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/uepop4)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "MpPoseTracking"*
**Docs:** [https://cables.gl/op/Ops.Extension.Mediapipe.MpPoseTracking](https://cables.gl/op/Ops.Extension.Mediapipe.MpPoseTracking)

---

