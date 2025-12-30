# Ops.Gl.Matrix

*Part of the [All Operators Reference](13-_AllOps.md)*

---

## Ops.Gl.Matrix

### AnimMatrix
![AnimMatrix op](images/ops/Ops_Gl_Matrix_AnimMatrix.svg)

**Full Name:** `Ops.Gl.Matrix.AnimMatrix`
**Description:** animate values in a matrix to a new matrix

**> Input Ports:**
- **Update** (Trigger): *See documentation*
- **Next Matrix** (Array): *See documentation*
- **Duration** (Number): *See documentation*
- **Easing Index** (Number: Integer): *See documentation*

**< Output Ports:**
- **Next** (Trigger): *See documentation*
- **Matrix** (Array): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/99cg1x)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "AnimMatrix"*
**Docs:** [https://cables.gl/op/Ops.Gl.Matrix.AnimMatrix](https://cables.gl/op/Ops.Gl.Matrix.AnimMatrix)

---

### ArrayPathFollow
![ArrayPathFollow op](images/ops/Ops_Gl_Matrix_ArrayPathFollow.svg)

**Full Name:** `Ops.Gl.Matrix.ArrayPathFollow`
**Description:** interpolate position on a spline/array3x

**> Input Ports:**
- **Exe** (Trigger): *See documentation*
- **Array** (Array): *See documentation*
- **Time** (Number): *See documentation*
- **Duration** (Number): *See documentation*
- **Offset** (Number): *See documentation*
- **Look Ahead** (Number): *See documentation*

**< Output Ports:**
- **Trigger** (Trigger): *See documentation*
- **Transform Lookat** (Trigger): *See documentation*
- **Index** (Number): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/lL9_EF)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ArrayPathFollow"*
**Docs:** [https://cables.gl/op/Ops.Gl.Matrix.ArrayPathFollow](https://cables.gl/op/Ops.Gl.Matrix.ArrayPathFollow)

---

### ArrayPathFollowParticles_v2
![ArrayPathFollowParticles_v2 op](images/ops/Ops_Gl_Matrix_ArrayPathFollowParticles_v2.svg)

**Full Name:** `Ops.Gl.Matrix.ArrayPathFollowParticles_v2`
**Description:** render lots of particles following a path/spline/array3x

**> Input Ports:**
- **Exec** (Trigger): *See documentation*
- **Points** (Array): *See documentation*
- **Num Particles** (Number): *See documentation*
- **Length** (Number): *See documentation*
- **Spread** (Number): *See documentation*
- **Offset** (Number): *See documentation*
- **Max Distance** (Number): *See documentation*
- **RandomSpeed** (Number: Boolean): *See documentation*

**< Output Ports:**
- **Next** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/4wT0J6)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ArrayPathFollowParticles_v2"*
**Docs:** [https://cables.gl/op/Ops.Gl.Matrix.ArrayPathFollowParticles_v2](https://cables.gl/op/Ops.Gl.Matrix.ArrayPathFollowParticles_v2)

---

### Billboard
![Billboard op](images/ops/Ops_Gl_Matrix_Billboard.svg)

**Full Name:** `Ops.Gl.Matrix.Billboard`
**Description:** rotate an object to always face the camera

**> Input Ports:**
- **Exec** (Trigger): *See documentation*

**< Output Ports:**
- **Next** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/GVpkrq)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "Billboard"*
**Docs:** [https://cables.gl/op/Ops.Gl.Matrix.Billboard](https://cables.gl/op/Ops.Gl.Matrix.Billboard)

---

### Camera_v2
![Camera_v2 op](images/ops/Ops_Gl_Matrix_Camera_v2.svg)

**Full Name:** `Ops.Gl.Matrix.Camera_v2`
**Description:** Transforms and projects the scene from the point of view of the camera.

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Identity** (Number: Boolean): *See documentation*
- **Projection Mode Index** (Number: Integer): *See documentation*
- **Frustum Near** (Number): *See documentation*
- **Frustum Far** (Number): *See documentation*
- **Fov** (Number): *See documentation*
- **Auto Aspect Ratio** (Number: Boolean): *See documentation*
- **Aspect Ratio** (Number): *See documentation*
- **Eye X** (Number): *See documentation*
- **Eye Y** (Number): *See documentation*
- **Eye Z** (Number): *See documentation*
- **Center X** (Number): *See documentation*
- **Center Y** (Number): *See documentation*
- **Center Z** (Number): *See documentation*
- **Truck** (Number): *See documentation*
- **Move sideways** (in local x axis): *See documentation*
- **Boom** (Number): *See documentation*
- **Dolly** (Number): *See documentation*
- **Tilt** (Number): *See documentation*
- **Pan** (Number): *See documentation*
- **Roll** (Number): *See documentation*

**< Output Ports:**
- **Trigger** (Trigger): *See documentation*
- **Aspect** (Number): *See documentation*
- **Look At Array** (Array): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/PSw73e)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "Camera_v2"*
**Docs:** [https://cables.gl/op/Ops.Gl.Matrix.Camera_v2](https://cables.gl/op/Ops.Gl.Matrix.Camera_v2)

---

### CameraInfo
![CameraInfo op](images/ops/Ops_Gl_Matrix_CameraInfo.svg)

**Full Name:** `Ops.Gl.Matrix.CameraInfo`
**Description:** get camera attributes from current camera/orbit controls

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Camera Type Index** (Number: Integer): *See documentation*

**< Output Ports:**
- **Trigger** (Trigger): *See documentation*
- **X** (Number): *See documentation*
- **Y** (Number): *See documentation*
- **Z** (Number): *See documentation*
- **Right X** (Number): *See documentation*
- **Right Y** (Number): *See documentation*
- **Right Z** (Number): *See documentation*
- **Up X** (Number): *See documentation*
- **Up Y** (Number): *See documentation*
- **Up Z** (Number): *See documentation*
- **Forward X** (Number): *See documentation*
- **Forward Y** (Number): *See documentation*
- **Forward Z** (Number): *See documentation*
- **Near Frustum** (Number): *See documentation*
- **Far Frustum** (Number): *See documentation*
- **Bottom Frustum** (Number): *See documentation*
- **Top Frustum** (Number): *See documentation*
- **Left Frustum** (Number): *See documentation*
- **Right Frustum** (Number): *See documentation*
- **FOV** (Number): *See documentation*
- **Aspect Ratio** (Number): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/YfJ4S-)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "CameraInfo"*
**Docs:** [https://cables.gl/op/Ops.Gl.Matrix.CameraInfo](https://cables.gl/op/Ops.Gl.Matrix.CameraInfo)

---

### CameraPosition
![CameraPosition op](images/ops/Ops_Gl_Matrix_CameraPosition.svg)

**Full Name:** `Ops.Gl.Matrix.CameraPosition`
**Description:** get the current position of viewmatrix/camera eye

**> Input Ports:**
- **Render** (Trigger): *See documentation*

**< Output Ports:**
- **Trigger** (Trigger): *See documentation*
- **X** (Number): *See documentation*
- **Y** (Number): *See documentation*
- **Z** (Number): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/JwL86R)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "CameraPosition"*
**Docs:** [https://cables.gl/op/Ops.Gl.Matrix.CameraPosition](https://cables.gl/op/Ops.Gl.Matrix.CameraPosition)

---

### Coordinates
![Coordinates op](images/ops/Ops_Gl_Matrix_Coordinates.svg)

**Full Name:** `Ops.Gl.Matrix.Coordinates`
**Description:** current xyz coordinates (modelmatrix)

**> Input Ports:**
- **Render** (Trigger): *See documentation*

**< Output Ports:**
- **Trigger** (Trigger): *See documentation*
- **X** (Number): *See documentation*
- **Y** (Number): *See documentation*
- **Z** (Number): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/2AtI98)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "Coordinates"*
**Docs:** [https://cables.gl/op/Ops.Gl.Matrix.Coordinates](https://cables.gl/op/Ops.Gl.Matrix.Coordinates)

---

### DeviceOrientationCamera
![DeviceOrientationCamera op](images/ops/Ops_Gl_Matrix_DeviceOrientationCamera.svg)

**Full Name:** `Ops.Gl.Matrix.DeviceOrientationCamera`
**Description:** gyroscope motionsensor camera

**> Input Ports:**
- **Render** (Trigger): *See documentation*

**< Output Ports:**
- **Next** (Trigger): *See documentation*
- **Window Orientation** (Number): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/dZ8wQ0)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "DeviceOrientationCamera"*
**Docs:** [https://cables.gl/op/Ops.Gl.Matrix.DeviceOrientationCamera](https://cables.gl/op/Ops.Gl.Matrix.DeviceOrientationCamera)

---

### GetMatrixScaling
![GetMatrixScaling op](images/ops/Ops_Gl_Matrix_GetMatrixScaling.svg)

**Full Name:** `Ops.Gl.Matrix.GetMatrixScaling`
**Description:** Get the scalar scaling of a matrix

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Matrix** (Array): *See documentation*

**< Output Ports:**
- **Trigger** (Trigger): *See documentation*
- **Scaling** (Number): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Gl.Matrix.GetMatrixScaling#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "GetMatrixScaling"*
**Docs:** [https://cables.gl/op/Ops.Gl.Matrix.GetMatrixScaling](https://cables.gl/op/Ops.Gl.Matrix.GetMatrixScaling)

---

### GetModelMatrix
![GetModelMatrix op](images/ops/Ops_Gl_Matrix_GetModelMatrix.svg)

**Full Name:** `Ops.Gl.Matrix.GetModelMatrix`
**Description:** Get current modelmatrix

**> Input Ports:**
- **Render** (Trigger): *See documentation*

**< Output Ports:**
- **Trigger** (Trigger): *See documentation*
- **Matrix** (Array): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/HkYpci)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "GetModelMatrix"*
**Docs:** [https://cables.gl/op/Ops.Gl.Matrix.GetModelMatrix](https://cables.gl/op/Ops.Gl.Matrix.GetModelMatrix)

---

### GetProjectionMatrix
![GetProjectionMatrix op](images/ops/Ops_Gl_Matrix_GetProjectionMatrix.svg)

**Full Name:** `Ops.Gl.Matrix.GetProjectionMatrix`
**Description:** get current projectionmatrix

**> Input Ports:**
- **Render** (Trigger): *See documentation*

**< Output Ports:**
- **Trigger** (Trigger): *See documentation*
- **Matrix** (Array): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/573_4S)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "GetProjectionMatrix"*
**Docs:** [https://cables.gl/op/Ops.Gl.Matrix.GetProjectionMatrix](https://cables.gl/op/Ops.Gl.Matrix.GetProjectionMatrix)

---

### GetViewMatrix
![GetViewMatrix op](images/ops/Ops_Gl_Matrix_GetViewMatrix.svg)

**Full Name:** `Ops.Gl.Matrix.GetViewMatrix`
**Description:** get current viewmatrix

**> Input Ports:**
- **Render** (Trigger): *See documentation*

**< Output Ports:**
- **Trigger** (Trigger): *See documentation*
- **Matrix** (Array): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/hDWuci)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "GetViewMatrix"*
**Docs:** [https://cables.gl/op/Ops.Gl.Matrix.GetViewMatrix](https://cables.gl/op/Ops.Gl.Matrix.GetViewMatrix)

---

### InterpolateMatrix
![InterpolateMatrix op](images/ops/Ops_Gl_Matrix_InterpolateMatrix.svg)

**Full Name:** `Ops.Gl.Matrix.InterpolateMatrix`
**Description:** interpolate between two matrices

**> Input Ports:**
- **Exe** (Trigger): *See documentation*
- **Array 1** (Array): *See documentation*
- **Array 2** (Array): *See documentation*
- **Perc** (Number): *See documentation*

**< Output Ports:**
- **Next** (Trigger): *See documentation*
- **Result** (Array): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Gl.Matrix.InterpolateMatrix#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "InterpolateMatrix"*
**Docs:** [https://cables.gl/op/Ops.Gl.Matrix.InterpolateMatrix](https://cables.gl/op/Ops.Gl.Matrix.InterpolateMatrix)

---

### InvertMatrix
![InvertMatrix op](images/ops/Ops_Gl_Matrix_InvertMatrix.svg)

**Full Name:** `Ops.Gl.Matrix.InvertMatrix`
**Description:** outputs an inverted matrix

**> Input Ports:**
- **Matrix** (Array): *See documentation*

**< Output Ports:**
- **Result** (Array): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/G51FhI)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "InvertMatrix"*
**Docs:** [https://cables.gl/op/Ops.Gl.Matrix.InvertMatrix](https://cables.gl/op/Ops.Gl.Matrix.InvertMatrix)

---

### LookatCamera
![LookatCamera op](images/ops/Ops_Gl_Matrix_LookatCamera.svg)

**Full Name:** `Ops.Gl.Matrix.LookatCamera`
**Description:** transforms view to look from eye to center

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **EyeX** (Number): *See documentation*
- **EyeY** (Number): *See documentation*
- **EyeZ** (Number): *See documentation*
- **CenterX** (Number): *See documentation*
- **CenterY** (Number): *See documentation*
- **CenterZ** (Number): *See documentation*
- **UpX** (Number): *See documentation*
- **UpY** (Number): *See documentation*
- **UpZ** (Number): *See documentation*

**< Output Ports:**
- **Trigger** (Trigger): *See documentation*
- **Array** (Array): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/_JlGz6)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "LookatCamera"*
**Docs:** [https://cables.gl/op/Ops.Gl.Matrix.LookatCamera](https://cables.gl/op/Ops.Gl.Matrix.LookatCamera)

---

### MatrixTranslation
![MatrixTranslation op](images/ops/Ops_Gl_Matrix_MatrixTranslation.svg)

**Full Name:** `Ops.Gl.Matrix.MatrixTranslation`
**Description:** get translation of a matrix

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Matrix** (Array): *See documentation*

**< Output Ports:**
- **Trigger** (Trigger): *See documentation*
- **X** (Number): *See documentation*
- **Y** (Number): *See documentation*
- **Z** (Number): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/Zz52On)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "MatrixTranslation"*
**Docs:** [https://cables.gl/op/Ops.Gl.Matrix.MatrixTranslation](https://cables.gl/op/Ops.Gl.Matrix.MatrixTranslation)

---

### MultiplyModelMatrix
![MultiplyModelMatrix op](images/ops/Ops_Gl_Matrix_MultiplyModelMatrix.svg)

**Full Name:** `Ops.Gl.Matrix.MultiplyModelMatrix`
**Description:** multiply model matrix

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Identity** (Number: Boolean): *See documentation*
- **Matrix** (Array): *See documentation*

**< Output Ports:**
- **Trigger** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/HkYpci)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "MultiplyModelMatrix"*
**Docs:** [https://cables.gl/op/Ops.Gl.Matrix.MultiplyModelMatrix](https://cables.gl/op/Ops.Gl.Matrix.MultiplyModelMatrix)

---

### MulViewMatrix
![MulViewMatrix op](images/ops/Ops_Gl_Matrix_MulViewMatrix.svg)

**Full Name:** `Ops.Gl.Matrix.MulViewMatrix`
**Description:** multiply view matrix

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Matrix** (Array): *See documentation*
- **Identity** (Number: Boolean): *See documentation*

**< Output Ports:**
- **Trigger** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/hDWuci)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "MulViewMatrix"*
**Docs:** [https://cables.gl/op/Ops.Gl.Matrix.MulViewMatrix](https://cables.gl/op/Ops.Gl.Matrix.MulViewMatrix)

---

### Quaternion
![Quaternion op](images/ops/Ops_Gl_Matrix_Quaternion.svg)

**Full Name:** `Ops.Gl.Matrix.Quaternion`
**Description:** multiplies current modelmatrix with a quaternion

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **X** (Number): *See documentation*
- **Y** (Number): *See documentation*
- **Z** (Number): *See documentation*
- **W** (Number): *See documentation*

**< Output Ports:**
- **Trigger** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Gl.Matrix.Quaternion#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "Quaternion"*
**Docs:** [https://cables.gl/op/Ops.Gl.Matrix.Quaternion](https://cables.gl/op/Ops.Gl.Matrix.Quaternion)

---

### QuaternionCamera
![QuaternionCamera op](images/ops/Ops_Gl_Matrix_QuaternionCamera.svg)

**Full Name:** `Ops.Gl.Matrix.QuaternionCamera`
**Description:** Set up a camera, rotated by a quaternion

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **EyeX** (Number): *See documentation*
- **EyeY** (Number): *See documentation*
- **EyeZ** (Number): *See documentation*
- **QuatX** (Number): *See documentation*
- **QuatY** (Number): *See documentation*
- **QuatZ** (Number): *See documentation*
- **QuatW** (Number): *See documentation*
- **UpX** (Number): *See documentation*
- **UpY** (Number): *See documentation*
- **UpZ** (Number): *See documentation*

**< Output Ports:**
- **Trigger** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Gl.Matrix.QuaternionCamera#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "QuaternionCamera"*
**Docs:** [https://cables.gl/op/Ops.Gl.Matrix.QuaternionCamera](https://cables.gl/op/Ops.Gl.Matrix.QuaternionCamera)

---

### RandomGridPlacement
![RandomGridPlacement op](images/ops/Ops_Gl_Matrix_RandomGridPlacement.svg)

**Full Name:** `Ops.Gl.Matrix.RandomGridPlacement`
**Description:** place random objects on a grid

**> Input Ports:**
- **Exe** (Trigger): *See documentation*
- **Max Depth** (Number): *See documentation*
- **Possibility** (Number): *See documentation*
- **Seed** (Number): *See documentation*
- **Scale** (Number): *See documentation*
- **Width** (Number): *See documentation*
- **Height** (Number): *See documentation*

**< Output Ports:**
- **Next** (Trigger): *See documentation*
- **Index** (Number): *See documentation*
- **Depth** (Number): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/FsZFVB)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "RandomGridPlacement"*
**Docs:** [https://cables.gl/op/Ops.Gl.Matrix.RandomGridPlacement](https://cables.gl/op/Ops.Gl.Matrix.RandomGridPlacement)

---

### RandomGridPlacementArrays
![RandomGridPlacementArrays op](images/ops/Ops_Gl_Matrix_RandomGridPlacementArrays.svg)

**Full Name:** `Ops.Gl.Matrix.RandomGridPlacementArrays`
**Description:** Place random objects on a grid

**> Input Ports:**
- **Exe** (Trigger): *See documentation*
- **Max Depth** (Number): *See documentation*
- **Possibility** (Number): *See documentation*
- **Seed** (Number): *See documentation*
- **Scale** (Number): *See documentation*
- **Width** (Number): *See documentation*
- **Height** (Number): *See documentation*

**< Output Ports:**
- **Positions** (Array): *See documentation*
- **Scalings** (Array): *See documentation*
- **Array Length** (Number): *See documentation*
- **Total Points** (Number): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/PYUHNP)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "RandomGridPlacementArrays"*
**Docs:** [https://cables.gl/op/Ops.Gl.Matrix.RandomGridPlacementArrays](https://cables.gl/op/Ops.Gl.Matrix.RandomGridPlacementArrays)

---

### Scale
![Scale op](images/ops/Ops_Gl_Matrix_Scale.svg)

**Full Name:** `Ops.Gl.Matrix.Scale`
**Description:** Scale all child objects (scaleXYZ)

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Scale** (Number): *See documentation*
- **X** (Number): *See documentation*
- **Y** (Number): *See documentation*
- **Z** (Number): *See documentation*

**< Output Ports:**
- **Trigger** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/au9U7i)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "Scale"*
**Docs:** [https://cables.gl/op/Ops.Gl.Matrix.Scale](https://cables.gl/op/Ops.Gl.Matrix.Scale)

---

### ScaleXYZViewMatrix
![ScaleXYZViewMatrix op](images/ops/Ops_Gl_Matrix_ScaleXYZViewMatrix.svg)

**Full Name:** `Ops.Gl.Matrix.ScaleXYZViewMatrix`
**Description:** scale xyz of viewmatrix

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **X** (Number): *See documentation*
- **Y** (Number): *See documentation*
- **Z** (Number): *See documentation*

**< Output Ports:**
- **Trigger** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/aSB6On)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ScaleXYZViewMatrix"*
**Docs:** [https://cables.gl/op/Ops.Gl.Matrix.ScaleXYZViewMatrix](https://cables.gl/op/Ops.Gl.Matrix.ScaleXYZViewMatrix)

---

### ScreenCoordinates_v2
![ScreenCoordinates_v2 op](images/ops/Ops_Gl_Matrix_ScreenCoordinates_v2.svg)

**Full Name:** `Ops.Gl.Matrix.ScreenCoordinates_v2`
**Description:** screen/pixel coordinates of the current transform

**> Input Ports:**
- **Execute** (Trigger): *See documentation*
- **Pixel Unit Index** (Number: Integer): *See documentation*

**< Output Ports:**
- **Trigger** (Trigger): *See documentation*
- **X** (Number): *See documentation*
- **Y** (Number): *See documentation*
- **Visible** (Number): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/-GNBD-)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ScreenCoordinates_v2"*
**Docs:** [https://cables.gl/op/Ops.Gl.Matrix.ScreenCoordinates_v2](https://cables.gl/op/Ops.Gl.Matrix.ScreenCoordinates_v2)

---

### ScreenPosTo3d_v3
![ScreenPosTo3d_v3 op](images/ops/Ops_Gl_Matrix_ScreenPosTo3d_v3.svg)

**Full Name:** `Ops.Gl.Matrix.ScreenPosTo3d_v3`
**Description:** convert screen coordinates to a 3d position

**> Input Ports:**
- **Exec** (Trigger): *See documentation*
- **X** (Number): *See documentation*
- **Y** (Number): *See documentation*
- **Input Type Index** (Number: Integer): *See documentation*

**< Output Ports:**
- **Trigger Out** (Trigger): *See documentation*
- **Result X** (Number): *See documentation*
- **Result Y** (Number): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/mDiCq6)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ScreenPosTo3d_v3"*
**Docs:** [https://cables.gl/op/Ops.Gl.Matrix.ScreenPosTo3d_v3](https://cables.gl/op/Ops.Gl.Matrix.ScreenPosTo3d_v3)

---

### SetProjectionMatrix
![SetProjectionMatrix op](images/ops/Ops_Gl_Matrix_SetProjectionMatrix.svg)

**Full Name:** `Ops.Gl.Matrix.SetProjectionMatrix`
**Description:** set a projection matrix

**> Input Ports:**
- **Exe** (Trigger): *See documentation*
- **Matrix** (Array): *See documentation*

**< Output Ports:**
- **Next** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/573_4S)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "SetProjectionMatrix"*
**Docs:** [https://cables.gl/op/Ops.Gl.Matrix.SetProjectionMatrix](https://cables.gl/op/Ops.Gl.Matrix.SetProjectionMatrix)

---

### Shear
![Shear op](images/ops/Ops_Gl_Matrix_Shear.svg)

**Full Name:** `Ops.Gl.Matrix.Shear`
**Description:** displaces each point of a mesh in fixed direction

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **ShearX** (Number): *See documentation*
- **ShearY** (Number): *See documentation*

**< Output Ports:**
- **Trigger** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/PmTYnO)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "Shear"*
**Docs:** [https://cables.gl/op/Ops.Gl.Matrix.Shear](https://cables.gl/op/Ops.Gl.Matrix.Shear)

---

### TransformMatrix
![TransformMatrix op](images/ops/Ops_Gl_Matrix_TransformMatrix.svg)

**Full Name:** `Ops.Gl.Matrix.TransformMatrix`
**Description:** transform a matrix (mat4)

**> Input Ports:**
- **Transform** (Trigger): *See documentation*
- **Matrix** (Array): *See documentation*
- **Translate X** (Number): *See documentation*
- **Translate Y** (Number): *See documentation*
- **Translate Z** (Number): *See documentation*
- **Scale X** (Number): *See documentation*
- **Scale Y** (Number): *See documentation*
- **Scale Z** (Number): *See documentation*
- **Rotation X** (Number): *See documentation*
- **Rotation Y** (Number): *See documentation*
- **Rotation Z** (Number): *See documentation*

**< Output Ports:**
- **Next** (Trigger): *See documentation*
- **Result** (Array): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/A0W1Jx)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "TransformMatrix"*
**Docs:** [https://cables.gl/op/Ops.Gl.Matrix.TransformMatrix](https://cables.gl/op/Ops.Gl.Matrix.TransformMatrix)

---

### TransformMul
![TransformMul op](images/ops/Ops_Gl_Matrix_TransformMul.svg)

**Full Name:** `Ops.Gl.Matrix.TransformMul`
**Description:** multiply current modelmatrix

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Mul** (Number): *See documentation*

**< Output Ports:**
- **Trigger** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Gl.Matrix.TransformMul#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "TransformMul"*
**Docs:** [https://cables.gl/op/Ops.Gl.Matrix.TransformMul](https://cables.gl/op/Ops.Gl.Matrix.TransformMul)

---

### Translate
![Translate op](images/ops/Ops_Gl_Matrix_Translate.svg)

**Full Name:** `Ops.Gl.Matrix.Translate`
**Description:** Translate objects (move / position in 3D space)

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **X** (Number): *See documentation*
- **Y** (Number): *See documentation*
- **Z** (Number): *See documentation*

**< Output Ports:**
- **Trigger** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Gl.Matrix.Translate#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "Translate"*
**Docs:** [https://cables.gl/op/Ops.Gl.Matrix.Translate](https://cables.gl/op/Ops.Gl.Matrix.Translate)

---

### TranslateView
![TranslateView op](images/ops/Ops_Gl_Matrix_TranslateView.svg)

**Full Name:** `Ops.Gl.Matrix.TranslateView`
**Description:** translate the view/camera matrix

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **X** (Number): *See documentation*
- **Y** (Number): *See documentation*
- **Z** (Number): *See documentation*

**< Output Ports:**
- **Trigger** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Gl.Matrix.TranslateView#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "TranslateView"*
**Docs:** [https://cables.gl/op/Ops.Gl.Matrix.TranslateView](https://cables.gl/op/Ops.Gl.Matrix.TranslateView)

---

### VectorTranslate
![VectorTranslate op](images/ops/Ops_Gl_Matrix_VectorTranslate.svg)

**Full Name:** `Ops.Gl.Matrix.VectorTranslate`
**Description:** Translate any geometry underneath it using vectors and speed.

**> Input Ports:**
- **Exec** (Trigger): *See documentation*
- **Speed** (Number): *See documentation*
- **Vector X** (Number): *See documentation*
- **Vector Y** (Number): *See documentation*
- **Vector Z** (Number): *See documentation*
- **Reset Position X** (Number): *See documentation*
- **Reset Position Y** (Number): *See documentation*
- **Reset Position Z** (Number): *See documentation*
- **Reset** (Trigger): *See documentation*
- **Max** (Number): *See documentation*

**< Output Ports:**
- **Next** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Gl.Matrix.VectorTranslate#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "VectorTranslate"*
**Docs:** [https://cables.gl/op/Ops.Gl.Matrix.VectorTranslate](https://cables.gl/op/Ops.Gl.Matrix.VectorTranslate)

---

### WASDCamera_v2
![WASDCamera_v2 op](images/ops/Ops_Gl_Matrix_WASDCamera_v2.svg)

**Full Name:** `Ops.Gl.Matrix.WASDCamera_v2`
**Description:** simple camera you control with W,A,S,D keys like in a FPS game

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Enable Pointer Lock** (Number: Boolean): *See documentation*
- **Speed** (Number): *See documentation*
- **Mouse Speed** (Number): *See documentation*
- **Allow Flying** (Number: Boolean): *See documentation*
- **Active** (Number: Boolean): *See documentation*
- **Move X-** (Number: Boolean): *See documentation*
- **Move Y-** (Number: Boolean): *See documentation*
- **Reset** (Trigger): *See documentation*

**< Output Ports:**
- **Trigger** (Trigger): *See documentation*
- **IsLocked** (booleanNumber): *See documentation*
- **PosX** (Number): *See documentation*
- **PosY** (Number): *See documentation*
- **PosZ** (Number): *See documentation*
- **Mouse Left** (Trigger): *See documentation*
- **Mouse Right** (Trigger): *See documentation*
- **Dir X** (Number): *See documentation*
- **Dir Y** (Number): *See documentation*
- **Dir Z** (Number): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/oLCaao)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "WASDCamera_v2"*
**Docs:** [https://cables.gl/op/Ops.Gl.Matrix.WASDCamera_v2](https://cables.gl/op/Ops.Gl.Matrix.WASDCamera_v2)

---

