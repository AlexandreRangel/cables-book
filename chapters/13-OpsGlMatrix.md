# Ops.Gl.Matrix

*Part of the [All Operators Reference](13-_AllOps.md)*

---

## Ops.Gl.Matrix

### AnimMatrix
![AnimMatrix op](images/ops/Ops_Gl_Matrix_AnimMatrix.svg)

**Full Name:** `Ops.Gl.Matrix.AnimMatrix`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Gl.Matrix.AnimMatrix) for details*

**> Input Ports:**
- **Update** (Trigger)
- **Next Matrix** (Array)
- **Duration** (Number)
- **Easing Index** (Number: Integer)

**< Output Ports:**
- **Next** (Trigger)
- **Matrix** (Array)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Gl.Matrix.AnimMatrix#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "AnimMatrix"*
**Docs:** [https://cables.gl/op/Ops.Gl.Matrix.AnimMatrix](https://cables.gl/op/Ops.Gl.Matrix.AnimMatrix)

---

### ArrayPathFollow
![ArrayPathFollow op](images/ops/Ops_Gl_Matrix_ArrayPathFollow.svg)

**Full Name:** `Ops.Gl.Matrix.ArrayPathFollow`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Gl.Matrix.ArrayPathFollow) for details*

**> Input Ports:**
- **Exe** (Trigger)
- **Array** (Array)
- **Time** (Number)
- **Duration** (Number)
- **Offset** (Number)
- **Look Ahead** (Number)

**< Output Ports:**
- **Trigger** (Trigger)
- **Transform Lookat** (Trigger)
- **Index** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Gl.Matrix.ArrayPathFollow#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ArrayPathFollow"*
**Docs:** [https://cables.gl/op/Ops.Gl.Matrix.ArrayPathFollow](https://cables.gl/op/Ops.Gl.Matrix.ArrayPathFollow)

---

### ArrayPathFollowParticles_v2
![ArrayPathFollowParticles_v2 op](images/ops/Ops_Gl_Matrix_ArrayPathFollowParticles_v2.svg)

**Full Name:** `Ops.Gl.Matrix.ArrayPathFollowParticles_v2`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Gl.Matrix.ArrayPathFollowParticles_v2) for details*

**> Input Ports:**
- **Exec** (Trigger)
- **Points** (Array)
- **Num Particles** (Number)
- **Length** (Number)
- **Spread** (Number)
- **Offset** (Number)
- **Max Distance** (Number)
- **RandomSpeed** (Number: Boolean)

**< Output Ports:**
- **Next** (Trigger)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Gl.Matrix.ArrayPathFollowParticles_v2#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ArrayPathFollowParticles_v2"*
**Docs:** [https://cables.gl/op/Ops.Gl.Matrix.ArrayPathFollowParticles_v2](https://cables.gl/op/Ops.Gl.Matrix.ArrayPathFollowParticles_v2)

---

### Billboard
![Billboard op](images/ops/Ops_Gl_Matrix_Billboard.svg)

**Full Name:** `Ops.Gl.Matrix.Billboard`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Gl.Matrix.Billboard) for details*

**> Input Ports:**
- **Exec** (Trigger)

**< Output Ports:**
- **Next** (Trigger)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Gl.Matrix.Billboard#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "Billboard"*
**Docs:** [https://cables.gl/op/Ops.Gl.Matrix.Billboard](https://cables.gl/op/Ops.Gl.Matrix.Billboard)

---

### Camera_v2
![Camera_v2 op](images/ops/Ops_Gl_Matrix_Camera_v2.svg)

**Full Name:** `Ops.Gl.Matrix.Camera_v2`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Gl.Matrix.Camera_v2) for details*

**> Input Ports:**
- **Render** (Trigger)
- **Identity** (Number: Boolean)
- **Projection Mode Index** (Number: Integer)
- **Frustum Near** (Number)
- **Frustum Far** (Number)
- **Fov** (Number)
- **Auto Aspect Ratio** (Number: Boolean)
- **Aspect Ratio** (Number)
- **Eye X** (Number)
- **Eye Y** (Number)
- **Eye Z** (Number)
- **Center X** (Number)
- **Center Y** (Number)
- **Center Z** (Number)
- **Truck** (Number)
- **Move sideways** (in local x axis)
- **Boom** (Number)
- **Dolly** (Number)
- **Tilt** (Number)
- **Pan** (Number)
- **Roll** (Number)

**< Output Ports:**
- **Trigger** (Trigger)
- **Aspect** (Number)
- **Look At Array** (Array)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Gl.Matrix.Camera_v2#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "Camera_v2"*
**Docs:** [https://cables.gl/op/Ops.Gl.Matrix.Camera_v2](https://cables.gl/op/Ops.Gl.Matrix.Camera_v2)

---

### CameraInfo
![CameraInfo op](images/ops/Ops_Gl_Matrix_CameraInfo.svg)

**Full Name:** `Ops.Gl.Matrix.CameraInfo`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Gl.Matrix.CameraInfo) for details*

**> Input Ports:**
- **Render** (Trigger)
- **Camera Type Index** (Number: Integer)

**< Output Ports:**
- **Trigger** (Trigger)
- **X** (Number)
- **Y** (Number)
- **Z** (Number)
- **Right X** (Number)
- **Right Y** (Number)
- **Right Z** (Number)
- **Up X** (Number)
- **Up Y** (Number)
- **Up Z** (Number)
- **Forward X** (Number)
- **Forward Y** (Number)
- **Forward Z** (Number)
- **Near Frustum** (Number)
- **Far Frustum** (Number)
- **Bottom Frustum** (Number)
- **Top Frustum** (Number)
- **Left Frustum** (Number)
- **Right Frustum** (Number)
- **FOV** (Number)
- **Aspect Ratio** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Gl.Matrix.CameraInfo#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "CameraInfo"*
**Docs:** [https://cables.gl/op/Ops.Gl.Matrix.CameraInfo](https://cables.gl/op/Ops.Gl.Matrix.CameraInfo)

---

### CameraPosition
![CameraPosition op](images/ops/Ops_Gl_Matrix_CameraPosition.svg)

**Full Name:** `Ops.Gl.Matrix.CameraPosition`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Gl.Matrix.CameraPosition) for details*

**> Input Ports:**
- **Render** (Trigger)

**< Output Ports:**
- **Trigger** (Trigger)
- **X** (Number)
- **Y** (Number)
- **Z** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Gl.Matrix.CameraPosition#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "CameraPosition"*
**Docs:** [https://cables.gl/op/Ops.Gl.Matrix.CameraPosition](https://cables.gl/op/Ops.Gl.Matrix.CameraPosition)

---

### Coordinates
![Coordinates op](images/ops/Ops_Gl_Matrix_Coordinates.svg)

**Full Name:** `Ops.Gl.Matrix.Coordinates`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Gl.Matrix.Coordinates) for details*

**> Input Ports:**
- **Render** (Trigger)

**< Output Ports:**
- **Trigger** (Trigger)
- **X** (Number)
- **Y** (Number)
- **Z** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Gl.Matrix.Coordinates#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "Coordinates"*
**Docs:** [https://cables.gl/op/Ops.Gl.Matrix.Coordinates](https://cables.gl/op/Ops.Gl.Matrix.Coordinates)

---

### DeviceOrientationCamera
![DeviceOrientationCamera op](images/ops/Ops_Gl_Matrix_DeviceOrientationCamera.svg)

**Full Name:** `Ops.Gl.Matrix.DeviceOrientationCamera`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Gl.Matrix.DeviceOrientationCamera) for details*

**> Input Ports:**
- **Render** (Trigger)

**< Output Ports:**
- **Next** (Trigger)
- **Window Orientation** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Gl.Matrix.DeviceOrientationCamera#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "DeviceOrientationCamera"*
**Docs:** [https://cables.gl/op/Ops.Gl.Matrix.DeviceOrientationCamera](https://cables.gl/op/Ops.Gl.Matrix.DeviceOrientationCamera)

---

### GetMatrixScaling
![GetMatrixScaling op](images/ops/Ops_Gl_Matrix_GetMatrixScaling.svg)

**Full Name:** `Ops.Gl.Matrix.GetMatrixScaling`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Gl.Matrix.GetMatrixScaling) for details*

**> Input Ports:**
- **Render** (Trigger)
- **Matrix** (Array)

**< Output Ports:**
- **Trigger** (Trigger)
- **Scaling** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Gl.Matrix.GetMatrixScaling#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "GetMatrixScaling"*
**Docs:** [https://cables.gl/op/Ops.Gl.Matrix.GetMatrixScaling](https://cables.gl/op/Ops.Gl.Matrix.GetMatrixScaling)

---

### GetModelMatrix
![GetModelMatrix op](images/ops/Ops_Gl_Matrix_GetModelMatrix.svg)

**Full Name:** `Ops.Gl.Matrix.GetModelMatrix`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Gl.Matrix.GetModelMatrix) for details*

**> Input Ports:**
- **Render** (Trigger)

**< Output Ports:**
- **Trigger** (Trigger)
- **Matrix** (Array)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Gl.Matrix.GetModelMatrix#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "GetModelMatrix"*
**Docs:** [https://cables.gl/op/Ops.Gl.Matrix.GetModelMatrix](https://cables.gl/op/Ops.Gl.Matrix.GetModelMatrix)

---

### GetProjectionMatrix
![GetProjectionMatrix op](images/ops/Ops_Gl_Matrix_GetProjectionMatrix.svg)

**Full Name:** `Ops.Gl.Matrix.GetProjectionMatrix`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Gl.Matrix.GetProjectionMatrix) for details*

**> Input Ports:**
- **Render** (Trigger)

**< Output Ports:**
- **Trigger** (Trigger)
- **Matrix** (Array)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Gl.Matrix.GetProjectionMatrix#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "GetProjectionMatrix"*
**Docs:** [https://cables.gl/op/Ops.Gl.Matrix.GetProjectionMatrix](https://cables.gl/op/Ops.Gl.Matrix.GetProjectionMatrix)

---

### GetViewMatrix
![GetViewMatrix op](images/ops/Ops_Gl_Matrix_GetViewMatrix.svg)

**Full Name:** `Ops.Gl.Matrix.GetViewMatrix`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Gl.Matrix.GetViewMatrix) for details*

**> Input Ports:**
- **Render** (Trigger)

**< Output Ports:**
- **Trigger** (Trigger)
- **Matrix** (Array)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Gl.Matrix.GetViewMatrix#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "GetViewMatrix"*
**Docs:** [https://cables.gl/op/Ops.Gl.Matrix.GetViewMatrix](https://cables.gl/op/Ops.Gl.Matrix.GetViewMatrix)

---

### InterpolateMatrix
![InterpolateMatrix op](images/ops/Ops_Gl_Matrix_InterpolateMatrix.svg)

**Full Name:** `Ops.Gl.Matrix.InterpolateMatrix`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Gl.Matrix.InterpolateMatrix) for details*

**> Input Ports:**
- **Exe** (Trigger)
- **Array 1** (Array)
- **Array 2** (Array)
- **Perc** (Number)

**< Output Ports:**
- **Next** (Trigger)
- **Result** (Array)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Gl.Matrix.InterpolateMatrix#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "InterpolateMatrix"*
**Docs:** [https://cables.gl/op/Ops.Gl.Matrix.InterpolateMatrix](https://cables.gl/op/Ops.Gl.Matrix.InterpolateMatrix)

---

### InvertMatrix
![InvertMatrix op](images/ops/Ops_Gl_Matrix_InvertMatrix.svg)

**Full Name:** `Ops.Gl.Matrix.InvertMatrix`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Gl.Matrix.InvertMatrix) for details*

**> Input Ports:**
- **Matrix** (Array)

**< Output Ports:**
- **Result** (Array)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Gl.Matrix.InvertMatrix#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "InvertMatrix"*
**Docs:** [https://cables.gl/op/Ops.Gl.Matrix.InvertMatrix](https://cables.gl/op/Ops.Gl.Matrix.InvertMatrix)

---

### LookatCamera
![LookatCamera op](images/ops/Ops_Gl_Matrix_LookatCamera.svg)

**Full Name:** `Ops.Gl.Matrix.LookatCamera`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Gl.Matrix.LookatCamera) for details*

**> Input Ports:**
- **Render** (Trigger)
- **EyeX** (Number)
- **EyeY** (Number)
- **EyeZ** (Number)
- **CenterX** (Number)
- **CenterY** (Number)
- **CenterZ** (Number)
- **UpX** (Number)
- **UpY** (Number)
- **UpZ** (Number)

**< Output Ports:**
- **Trigger** (Trigger)
- **Array** (Array)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Gl.Matrix.LookatCamera#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "LookatCamera"*
**Docs:** [https://cables.gl/op/Ops.Gl.Matrix.LookatCamera](https://cables.gl/op/Ops.Gl.Matrix.LookatCamera)

---

### MatrixTranslation
![MatrixTranslation op](images/ops/Ops_Gl_Matrix_MatrixTranslation.svg)

**Full Name:** `Ops.Gl.Matrix.MatrixTranslation`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Gl.Matrix.MatrixTranslation) for details*

**> Input Ports:**
- **Render** (Trigger)
- **Matrix** (Array)

**< Output Ports:**
- **Trigger** (Trigger)
- **X** (Number)
- **Y** (Number)
- **Z** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Gl.Matrix.MatrixTranslation#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "MatrixTranslation"*
**Docs:** [https://cables.gl/op/Ops.Gl.Matrix.MatrixTranslation](https://cables.gl/op/Ops.Gl.Matrix.MatrixTranslation)

---

### MultiplyModelMatrix
![MultiplyModelMatrix op](images/ops/Ops_Gl_Matrix_MultiplyModelMatrix.svg)

**Full Name:** `Ops.Gl.Matrix.MultiplyModelMatrix`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Gl.Matrix.MultiplyModelMatrix) for details*

**> Input Ports:**
- **Render** (Trigger)
- **Identity** (Number: Boolean)
- **Matrix** (Array)

**< Output Ports:**
- **Trigger** (Trigger)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Gl.Matrix.MultiplyModelMatrix#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "MultiplyModelMatrix"*
**Docs:** [https://cables.gl/op/Ops.Gl.Matrix.MultiplyModelMatrix](https://cables.gl/op/Ops.Gl.Matrix.MultiplyModelMatrix)

---

### MulViewMatrix
![MulViewMatrix op](images/ops/Ops_Gl_Matrix_MulViewMatrix.svg)

**Full Name:** `Ops.Gl.Matrix.MulViewMatrix`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Gl.Matrix.MulViewMatrix) for details*

**> Input Ports:**
- **Render** (Trigger)
- **Matrix** (Array)
- **Identity** (Number: Boolean)

**< Output Ports:**
- **Trigger** (Trigger)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Gl.Matrix.MulViewMatrix#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "MulViewMatrix"*
**Docs:** [https://cables.gl/op/Ops.Gl.Matrix.MulViewMatrix](https://cables.gl/op/Ops.Gl.Matrix.MulViewMatrix)

---

### Quaternion
![Quaternion op](images/ops/Ops_Gl_Matrix_Quaternion.svg)

**Full Name:** `Ops.Gl.Matrix.Quaternion`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Gl.Matrix.Quaternion) for details*

**> Input Ports:**
- **Render** (Trigger)
- **X** (Number)
- **Y** (Number)
- **Z** (Number)
- **W** (Number)

**< Output Ports:**
- **Trigger** (Trigger)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Gl.Matrix.Quaternion#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "Quaternion"*
**Docs:** [https://cables.gl/op/Ops.Gl.Matrix.Quaternion](https://cables.gl/op/Ops.Gl.Matrix.Quaternion)

---

### QuaternionCamera
![QuaternionCamera op](images/ops/Ops_Gl_Matrix_QuaternionCamera.svg)

**Full Name:** `Ops.Gl.Matrix.QuaternionCamera`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Gl.Matrix.QuaternionCamera) for details*

**> Input Ports:**
- **Render** (Trigger)
- **EyeX** (Number)
- **EyeY** (Number)
- **EyeZ** (Number)
- **QuatX** (Number)
- **QuatY** (Number)
- **QuatZ** (Number)
- **QuatW** (Number)
- **UpX** (Number)
- **UpY** (Number)
- **UpZ** (Number)

**< Output Ports:**
- **Trigger** (Trigger)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Gl.Matrix.QuaternionCamera#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "QuaternionCamera"*
**Docs:** [https://cables.gl/op/Ops.Gl.Matrix.QuaternionCamera](https://cables.gl/op/Ops.Gl.Matrix.QuaternionCamera)

---

### RandomGridPlacement
![RandomGridPlacement op](images/ops/Ops_Gl_Matrix_RandomGridPlacement.svg)

**Full Name:** `Ops.Gl.Matrix.RandomGridPlacement`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Gl.Matrix.RandomGridPlacement) for details*

**> Input Ports:**
- **Exe** (Trigger)
- **Max Depth** (Number)
- **Possibility** (Number)
- **Seed** (Number)
- **Scale** (Number)
- **Width** (Number)
- **Height** (Number)

**< Output Ports:**
- **Next** (Trigger)
- **Index** (Number)
- **Depth** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Gl.Matrix.RandomGridPlacement#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "RandomGridPlacement"*
**Docs:** [https://cables.gl/op/Ops.Gl.Matrix.RandomGridPlacement](https://cables.gl/op/Ops.Gl.Matrix.RandomGridPlacement)

---

### RandomGridPlacementArrays
![RandomGridPlacementArrays op](images/ops/Ops_Gl_Matrix_RandomGridPlacementArrays.svg)

**Full Name:** `Ops.Gl.Matrix.RandomGridPlacementArrays`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Gl.Matrix.RandomGridPlacementArrays) for details*

**> Input Ports:**
- **Exe** (Trigger)
- **Max Depth** (Number)
- **Possibility** (Number)
- **Seed** (Number)
- **Scale** (Number)
- **Width** (Number)
- **Height** (Number)

**< Output Ports:**
- **Positions** (Array)
- **Scalings** (Array)
- **Array Length** (Number)
- **Total Points** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Gl.Matrix.RandomGridPlacementArrays#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "RandomGridPlacementArrays"*
**Docs:** [https://cables.gl/op/Ops.Gl.Matrix.RandomGridPlacementArrays](https://cables.gl/op/Ops.Gl.Matrix.RandomGridPlacementArrays)

---

### Scale
![Scale op](images/ops/Ops_Gl_Matrix_Scale.svg)

**Full Name:** `Ops.Gl.Matrix.Scale`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Gl.Matrix.Scale) for details*

**> Input Ports:**
- **Render** (Trigger)
- **Scale** (Number)
- **X** (Number)
- **Y** (Number)
- **Z** (Number)

**< Output Ports:**
- **Trigger** (Trigger)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Gl.Matrix.Scale#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "Scale"*
**Docs:** [https://cables.gl/op/Ops.Gl.Matrix.Scale](https://cables.gl/op/Ops.Gl.Matrix.Scale)

---

### ScaleXYZViewMatrix
![ScaleXYZViewMatrix op](images/ops/Ops_Gl_Matrix_ScaleXYZViewMatrix.svg)

**Full Name:** `Ops.Gl.Matrix.ScaleXYZViewMatrix`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Gl.Matrix.ScaleXYZViewMatrix) for details*

**> Input Ports:**
- **Render** (Trigger)
- **X** (Number)
- **Y** (Number)
- **Z** (Number)

**< Output Ports:**
- **Trigger** (Trigger)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Gl.Matrix.ScaleXYZViewMatrix#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ScaleXYZViewMatrix"*
**Docs:** [https://cables.gl/op/Ops.Gl.Matrix.ScaleXYZViewMatrix](https://cables.gl/op/Ops.Gl.Matrix.ScaleXYZViewMatrix)

---

### ScreenCoordinates_v2
![ScreenCoordinates_v2 op](images/ops/Ops_Gl_Matrix_ScreenCoordinates_v2.svg)

**Full Name:** `Ops.Gl.Matrix.ScreenCoordinates_v2`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Gl.Matrix.ScreenCoordinates_v2) for details*

**> Input Ports:**
- **Execute** (Trigger)
- **Pixel Unit Index** (Number: Integer)

**< Output Ports:**
- **Trigger** (Trigger)
- **X** (Number)
- **Y** (Number)
- **Visible** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Gl.Matrix.ScreenCoordinates_v2#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ScreenCoordinates_v2"*
**Docs:** [https://cables.gl/op/Ops.Gl.Matrix.ScreenCoordinates_v2](https://cables.gl/op/Ops.Gl.Matrix.ScreenCoordinates_v2)

---

### ScreenPosTo3d_v3
![ScreenPosTo3d_v3 op](images/ops/Ops_Gl_Matrix_ScreenPosTo3d_v3.svg)

**Full Name:** `Ops.Gl.Matrix.ScreenPosTo3d_v3`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Gl.Matrix.ScreenPosTo3d_v3) for details*

**> Input Ports:**
- **Exec** (Trigger)
- **X** (Number)
- **Y** (Number)
- **Input Type Index** (Number: Integer)

**< Output Ports:**
- **Trigger Out** (Trigger)
- **Result X** (Number)
- **Result Y** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Gl.Matrix.ScreenPosTo3d_v3#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ScreenPosTo3d_v3"*
**Docs:** [https://cables.gl/op/Ops.Gl.Matrix.ScreenPosTo3d_v3](https://cables.gl/op/Ops.Gl.Matrix.ScreenPosTo3d_v3)

---

### SetProjectionMatrix
![SetProjectionMatrix op](images/ops/Ops_Gl_Matrix_SetProjectionMatrix.svg)

**Full Name:** `Ops.Gl.Matrix.SetProjectionMatrix`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Gl.Matrix.SetProjectionMatrix) for details*

**> Input Ports:**
- **Exe** (Trigger)
- **Matrix** (Array)

**< Output Ports:**
- **Next** (Trigger)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Gl.Matrix.SetProjectionMatrix#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "SetProjectionMatrix"*
**Docs:** [https://cables.gl/op/Ops.Gl.Matrix.SetProjectionMatrix](https://cables.gl/op/Ops.Gl.Matrix.SetProjectionMatrix)

---

### Shear
![Shear op](images/ops/Ops_Gl_Matrix_Shear.svg)

**Full Name:** `Ops.Gl.Matrix.Shear`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Gl.Matrix.Shear) for details*

**> Input Ports:**
- **Render** (Trigger)
- **ShearX** (Number)
- **ShearY** (Number)

**< Output Ports:**
- **Trigger** (Trigger)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Gl.Matrix.Shear#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "Shear"*
**Docs:** [https://cables.gl/op/Ops.Gl.Matrix.Shear](https://cables.gl/op/Ops.Gl.Matrix.Shear)

---

### TransformMatrix
![TransformMatrix op](images/ops/Ops_Gl_Matrix_TransformMatrix.svg)

**Full Name:** `Ops.Gl.Matrix.TransformMatrix`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Gl.Matrix.TransformMatrix) for details*

**> Input Ports:**
- **Transform** (Trigger)
- **Matrix** (Array)
- **Translate X** (Number)
- **Translate Y** (Number)
- **Translate Z** (Number)
- **Scale X** (Number)
- **Scale Y** (Number)
- **Scale Z** (Number)
- **Rotation X** (Number)
- **Rotation Y** (Number)
- **Rotation Z** (Number)

**< Output Ports:**
- **Next** (Trigger)
- **Result** (Array)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Gl.Matrix.TransformMatrix#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "TransformMatrix"*
**Docs:** [https://cables.gl/op/Ops.Gl.Matrix.TransformMatrix](https://cables.gl/op/Ops.Gl.Matrix.TransformMatrix)

---

### TransformMul
![TransformMul op](images/ops/Ops_Gl_Matrix_TransformMul.svg)

**Full Name:** `Ops.Gl.Matrix.TransformMul`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Gl.Matrix.TransformMul) for details*

**> Input Ports:**
- **Render** (Trigger)
- **Mul** (Number)

**< Output Ports:**
- **Trigger** (Trigger)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Gl.Matrix.TransformMul#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "TransformMul"*
**Docs:** [https://cables.gl/op/Ops.Gl.Matrix.TransformMul](https://cables.gl/op/Ops.Gl.Matrix.TransformMul)

---

### Translate
![Translate op](images/ops/Ops_Gl_Matrix_Translate.svg)

**Full Name:** `Ops.Gl.Matrix.Translate`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Gl.Matrix.Translate) for details*

**> Input Ports:**
- **Render** (Trigger)
- **X** (Number)
- **Y** (Number)
- **Z** (Number)

**< Output Ports:**
- **Trigger** (Trigger)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Gl.Matrix.Translate#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "Translate"*
**Docs:** [https://cables.gl/op/Ops.Gl.Matrix.Translate](https://cables.gl/op/Ops.Gl.Matrix.Translate)

---

### TranslateView
![TranslateView op](images/ops/Ops_Gl_Matrix_TranslateView.svg)

**Full Name:** `Ops.Gl.Matrix.TranslateView`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Gl.Matrix.TranslateView) for details*

**> Input Ports:**
- **Render** (Trigger)
- **X** (Number)
- **Y** (Number)
- **Z** (Number)

**< Output Ports:**
- **Trigger** (Trigger)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Gl.Matrix.TranslateView#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "TranslateView"*
**Docs:** [https://cables.gl/op/Ops.Gl.Matrix.TranslateView](https://cables.gl/op/Ops.Gl.Matrix.TranslateView)

---

### VectorTranslate
![VectorTranslate op](images/ops/Ops_Gl_Matrix_VectorTranslate.svg)

**Full Name:** `Ops.Gl.Matrix.VectorTranslate`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Gl.Matrix.VectorTranslate) for details*

**> Input Ports:**
- **Exec** (Trigger)
- **Speed** (Number)
- **Vector X** (Number)
- **Vector Y** (Number)
- **Vector Z** (Number)
- **Reset Position X** (Number)
- **Reset Position Y** (Number)
- **Reset Position Z** (Number)
- **Reset** (Trigger)
- **Max** (Number)

**< Output Ports:**
- **Next** (Trigger)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Gl.Matrix.VectorTranslate#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "VectorTranslate"*
**Docs:** [https://cables.gl/op/Ops.Gl.Matrix.VectorTranslate](https://cables.gl/op/Ops.Gl.Matrix.VectorTranslate)

---

### WASDCamera_v2
![WASDCamera_v2 op](images/ops/Ops_Gl_Matrix_WASDCamera_v2.svg)

**Full Name:** `Ops.Gl.Matrix.WASDCamera_v2`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Gl.Matrix.WASDCamera_v2) for details*

**> Input Ports:**
- **Render** (Trigger)
- **Enable Pointer Lock** (Number: Boolean)
- **Speed** (Number)
- **Mouse Speed** (Number)
- **Allow Flying** (Number: Boolean)
- **Active** (Number: Boolean)
- **Move X-** (Number: Boolean)
- **Move Y-** (Number: Boolean)
- **Reset** (Trigger)

**< Output Ports:**
- **Trigger** (Trigger)
- **IsLocked** (booleanNumber)
- **PosX** (Number)
- **PosY** (Number)
- **PosZ** (Number)
- **Mouse Left** (Trigger)
- **Mouse Right** (Trigger)
- **Dir X** (Number)
- **Dir Y** (Number)
- **Dir Z** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Gl.Matrix.WASDCamera_v2#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "WASDCamera_v2"*
**Docs:** [https://cables.gl/op/Ops.Gl.Matrix.WASDCamera_v2](https://cables.gl/op/Ops.Gl.Matrix.WASDCamera_v2)

---

