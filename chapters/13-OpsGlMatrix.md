# Ops.Gl.Matrix


```{=latex}
\OpsSubsubNoSubsectionNumbering\setcounter{subsubsection}{0}
```
### AnimMatrix
![AnimMatrix op](images/ops/Ops_Gl_Matrix_AnimMatrix.svg)

**Full Name:** `Ops.Gl.Matrix.AnimMatrix`

animate values in a matrix to a new matrix.

**`\inputsymbol`{=latex} Inputs**

- **Update** (Trigger)
- **Next Matrix** (Array)
- **Duration** (Number)
- **Easing Index** (Number: Integer)

**`\outputsymbol`{=latex} Output**

- **Next** (Trigger)
- **Matrix** (Array)

**Example:** [cables.gl/edit/99cg1x](https://cables.gl/edit/99cg1x)

**Doc:** [cables.gl/op/Ops.Gl.Matrix.AnimMatrix](https://cables.gl/op/Ops.Gl.Matrix.AnimMatrix)

### ArrayPathFollow
![ArrayPathFollow op](images/ops/Ops_Gl_Matrix_ArrayPathFollow.svg)

**Full Name:** `Ops.Gl.Matrix.ArrayPathFollow`

interpolate position on a spline/array3x.

**`\inputsymbol`{=latex} Inputs**

- **Exe** (Trigger)
- **Array** (Array)
- **Time** (Number)
- **Duration** (Number)
- **Offset** (Number)
- **Look Ahead** (Number)

**`\outputsymbol`{=latex} Output**

- **Trigger** (Trigger)
- **Transform Lookat** (Trigger)
- **Index** (Number)

**Example:** [cables.gl/edit/lL9_EF](https://cables.gl/edit/lL9_EF)

**Doc:** [cables.gl/op/Ops.Gl.Matrix.ArrayPathFollow](https://cables.gl/op/Ops.Gl.Matrix.ArrayPathFollow)

### ArrayPathFollowParticles_v2
![ArrayPathFollowParticles_v2 op](images/ops/Ops_Gl_Matrix_ArrayPathFollowParticles_v2.svg)

**Full Name:** `Ops.Gl.Matrix.ArrayPathFollowParticles_v2`

render lots of particles following a path/spline/array3x.

**`\inputsymbol`{=latex} Inputs**

- **Exec** (Trigger)
- **Points** (Array)
- **Num Particles** (Number)
- **Length** (Number)
- **Spread** (Number)
- **Offset** (Number)
- **Max Distance** (Number)
- **RandomSpeed** (Number: Boolean)

**`\outputsymbol`{=latex} Output**

- **Next** (Trigger)

**Example:** [cables.gl/edit/4wT0J6](https://cables.gl/edit/4wT0J6)

**Doc:** [cables.gl/op/Ops.Gl.Matrix.ArrayPathFollowParticles_v2](https://cables.gl/op/Ops.Gl.Matrix.ArrayPathFollowParticles_v2)

### Billboard
![Billboard op](images/ops/Ops_Gl_Matrix_Billboard.svg)

**Full Name:** `Ops.Gl.Matrix.Billboard`

rotate an object to always face the camera.

**`\inputsymbol`{=latex} Inputs**

- **Exec** (Trigger)

**`\outputsymbol`{=latex} Output**

- **Next** (Trigger)

**Example:** [cables.gl/edit/GVpkrq](https://cables.gl/edit/GVpkrq)

**Doc:** [cables.gl/op/Ops.Gl.Matrix.Billboard](https://cables.gl/op/Ops.Gl.Matrix.Billboard)

### Camera_v2
![Camera_v2 op](images/ops/Ops_Gl_Matrix_Camera_v2.svg)

**Full Name:** `Ops.Gl.Matrix.Camera_v2`

Transforms and projects the scene from the point of view of the camera.

**`\inputsymbol`{=latex} Inputs**

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

**`\outputsymbol`{=latex} Output**

- **Trigger** (Trigger)
- **Aspect** (Number)
- **Look At Array** (Array)

**Example:** [cables.gl/edit/PSw73e](https://cables.gl/edit/PSw73e)

**Doc:** [cables.gl/op/Ops.Gl.Matrix.Camera_v2](https://cables.gl/op/Ops.Gl.Matrix.Camera_v2)

### CameraInfo
![CameraInfo op](images/ops/Ops_Gl_Matrix_CameraInfo.svg)

**Full Name:** `Ops.Gl.Matrix.CameraInfo`

get camera attributes from current camera/orbit controls.

**`\inputsymbol`{=latex} Inputs**

- **Render** (Trigger)
- **Camera Type Index** (Number: Integer)

**`\outputsymbol`{=latex} Output**

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

**Example:** [cables.gl/edit/YfJ4S-](https://cables.gl/edit/YfJ4S-)

**Doc:** [cables.gl/op/Ops.Gl.Matrix.CameraInfo](https://cables.gl/op/Ops.Gl.Matrix.CameraInfo)

### CameraPosition
![CameraPosition op](images/ops/Ops_Gl_Matrix_CameraPosition.svg)

**Full Name:** `Ops.Gl.Matrix.CameraPosition`

get the current position of viewmatrix/camera eye.

**`\inputsymbol`{=latex} Inputs**

- **Render** (Trigger)

**`\outputsymbol`{=latex} Output**

- **Trigger** (Trigger)
- **X** (Number)
- **Y** (Number)
- **Z** (Number)

**Example:** [cables.gl/edit/JwL86R](https://cables.gl/edit/JwL86R)

**Doc:** [cables.gl/op/Ops.Gl.Matrix.CameraPosition](https://cables.gl/op/Ops.Gl.Matrix.CameraPosition)

### Coordinates
![Coordinates op](images/ops/Ops_Gl_Matrix_Coordinates.svg)

**Full Name:** `Ops.Gl.Matrix.Coordinates`

current xyz coordinates (modelmatrix).

**`\inputsymbol`{=latex} Inputs**

- **Render** (Trigger)

**`\outputsymbol`{=latex} Output**

- **Trigger** (Trigger)
- **X** (Number)
- **Y** (Number)
- **Z** (Number)

**Example:** [cables.gl/edit/2AtI98](https://cables.gl/edit/2AtI98)

**Doc:** [cables.gl/op/Ops.Gl.Matrix.Coordinates](https://cables.gl/op/Ops.Gl.Matrix.Coordinates)

### DeviceOrientationCamera
![DeviceOrientationCamera op](images/ops/Ops_Gl_Matrix_DeviceOrientationCamera.svg)

**Full Name:** `Ops.Gl.Matrix.DeviceOrientationCamera`

gyroscope motionsensor camera.

**`\inputsymbol`{=latex} Inputs**

- **Render** (Trigger)

**`\outputsymbol`{=latex} Output**

- **Next** (Trigger)
- **Window Orientation** (Number)

**Example:** [cables.gl/edit/dZ8wQ0](https://cables.gl/edit/dZ8wQ0)

**Doc:** [cables.gl/op/Ops.Gl.Matrix.DeviceOrientationCamera](https://cables.gl/op/Ops.Gl.Matrix.DeviceOrientationCamera)

### GetMatrixScaling
![GetMatrixScaling op](images/ops/Ops_Gl_Matrix_GetMatrixScaling.svg)

**Full Name:** `Ops.Gl.Matrix.GetMatrixScaling`

Get the scalar scaling of a matrix.

**`\inputsymbol`{=latex} Inputs**

- **Render** (Trigger)
- **Matrix** (Array)

**`\outputsymbol`{=latex} Output**

- **Trigger** (Trigger)
- **Scaling** (Number)

**Example:** [cables.gl/op/Ops.Gl.Matrix.GetMatrixScaling#example](https://cables.gl/op/Ops.Gl.Matrix.GetMatrixScaling#example)

**Doc:** [cables.gl/op/Ops.Gl.Matrix.GetMatrixScaling](https://cables.gl/op/Ops.Gl.Matrix.GetMatrixScaling)

### GetModelMatrix
![GetModelMatrix op](images/ops/Ops_Gl_Matrix_GetModelMatrix.svg)

**Full Name:** `Ops.Gl.Matrix.GetModelMatrix`

Get current modelmatrix.

**`\inputsymbol`{=latex} Inputs**

- **Render** (Trigger)

**`\outputsymbol`{=latex} Output**

- **Trigger** (Trigger)
- **Matrix** (Array)

**Example:** [cables.gl/edit/HkYpci](https://cables.gl/edit/HkYpci)

**Doc:** [cables.gl/op/Ops.Gl.Matrix.GetModelMatrix](https://cables.gl/op/Ops.Gl.Matrix.GetModelMatrix)

### GetProjectionMatrix
![GetProjectionMatrix op](images/ops/Ops_Gl_Matrix_GetProjectionMatrix.svg)

**Full Name:** `Ops.Gl.Matrix.GetProjectionMatrix`

get current projectionmatrix.

**`\inputsymbol`{=latex} Inputs**

- **Render** (Trigger)

**`\outputsymbol`{=latex} Output**

- **Trigger** (Trigger)
- **Matrix** (Array)

**Example:** [cables.gl/edit/573_4S](https://cables.gl/edit/573_4S)

**Doc:** [cables.gl/op/Ops.Gl.Matrix.GetProjectionMatrix](https://cables.gl/op/Ops.Gl.Matrix.GetProjectionMatrix)

### GetViewMatrix
![GetViewMatrix op](images/ops/Ops_Gl_Matrix_GetViewMatrix.svg)

**Full Name:** `Ops.Gl.Matrix.GetViewMatrix`

get current viewmatrix.

**`\inputsymbol`{=latex} Inputs**

- **Render** (Trigger)

**`\outputsymbol`{=latex} Output**

- **Trigger** (Trigger)
- **Matrix** (Array)

**Example:** [cables.gl/edit/hDWuci](https://cables.gl/edit/hDWuci)

**Doc:** [cables.gl/op/Ops.Gl.Matrix.GetViewMatrix](https://cables.gl/op/Ops.Gl.Matrix.GetViewMatrix)

### InterpolateMatrix
![InterpolateMatrix op](images/ops/Ops_Gl_Matrix_InterpolateMatrix.svg)

**Full Name:** `Ops.Gl.Matrix.InterpolateMatrix`

interpolate between two matrices.

**`\inputsymbol`{=latex} Inputs**

- **Exe** (Trigger)
- **Array 1** (Array)
- **Array 2** (Array)
- **Perc** (Number)

**`\outputsymbol`{=latex} Output**

- **Next** (Trigger)
- **Result** (Array)

**Example:** [cables.gl/op/Ops.Gl.Matrix.InterpolateMatrix#example](https://cables.gl/op/Ops.Gl.Matrix.InterpolateMatrix#example)

**Doc:** [cables.gl/op/Ops.Gl.Matrix.InterpolateMatrix](https://cables.gl/op/Ops.Gl.Matrix.InterpolateMatrix)

### InvertMatrix
![InvertMatrix op](images/ops/Ops_Gl_Matrix_InvertMatrix.svg)

**Full Name:** `Ops.Gl.Matrix.InvertMatrix`

outputs an inverted matrix.

**`\inputsymbol`{=latex} Inputs**

- **Matrix** (Array)

**`\outputsymbol`{=latex} Output**

- **Result** (Array)

**Example:** [cables.gl/edit/G51FhI](https://cables.gl/edit/G51FhI)

**Doc:** [cables.gl/op/Ops.Gl.Matrix.InvertMatrix](https://cables.gl/op/Ops.Gl.Matrix.InvertMatrix)

### LookatCamera
![LookatCamera op](images/ops/Ops_Gl_Matrix_LookatCamera.svg)

**Full Name:** `Ops.Gl.Matrix.LookatCamera`

transforms view to look from eye to center.

**`\inputsymbol`{=latex} Inputs**

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

**`\outputsymbol`{=latex} Output**

- **Trigger** (Trigger)
- **Array** (Array)

**Example:** [cables.gl/edit/_JlGz6](https://cables.gl/edit/_JlGz6)

**Doc:** [cables.gl/op/Ops.Gl.Matrix.LookatCamera](https://cables.gl/op/Ops.Gl.Matrix.LookatCamera)

### MatrixTranslation
![MatrixTranslation op](images/ops/Ops_Gl_Matrix_MatrixTranslation.svg)

**Full Name:** `Ops.Gl.Matrix.MatrixTranslation`

get translation of a matrix.

**`\inputsymbol`{=latex} Inputs**

- **Render** (Trigger)
- **Matrix** (Array)

**`\outputsymbol`{=latex} Output**

- **Trigger** (Trigger)
- **X** (Number)
- **Y** (Number)
- **Z** (Number)

**Example:** [cables.gl/edit/Zz52On](https://cables.gl/edit/Zz52On)

**Doc:** [cables.gl/op/Ops.Gl.Matrix.MatrixTranslation](https://cables.gl/op/Ops.Gl.Matrix.MatrixTranslation)

### MultiplyModelMatrix
![MultiplyModelMatrix op](images/ops/Ops_Gl_Matrix_MultiplyModelMatrix.svg)

**Full Name:** `Ops.Gl.Matrix.MultiplyModelMatrix`

multiply model matrix.

**`\inputsymbol`{=latex} Inputs**

- **Render** (Trigger)
- **Identity** (Number: Boolean)
- **Matrix** (Array)

**`\outputsymbol`{=latex} Output**

- **Trigger** (Trigger)

**Example:** [cables.gl/edit/HkYpci](https://cables.gl/edit/HkYpci)

**Doc:** [cables.gl/op/Ops.Gl.Matrix.MultiplyModelMatrix](https://cables.gl/op/Ops.Gl.Matrix.MultiplyModelMatrix)

### MulViewMatrix
![MulViewMatrix op](images/ops/Ops_Gl_Matrix_MulViewMatrix.svg)

**Full Name:** `Ops.Gl.Matrix.MulViewMatrix`

multiply view matrix.

**`\inputsymbol`{=latex} Inputs**

- **Render** (Trigger)
- **Matrix** (Array)
- **Identity** (Number: Boolean)

**`\outputsymbol`{=latex} Output**

- **Trigger** (Trigger)

**Example:** [cables.gl/edit/hDWuci](https://cables.gl/edit/hDWuci)

**Doc:** [cables.gl/op/Ops.Gl.Matrix.MulViewMatrix](https://cables.gl/op/Ops.Gl.Matrix.MulViewMatrix)

### Quaternion
![Quaternion op](images/ops/Ops_Gl_Matrix_Quaternion.svg)

**Full Name:** `Ops.Gl.Matrix.Quaternion`

multiplies current modelmatrix with a quaternion.

**`\inputsymbol`{=latex} Inputs**

- **Render** (Trigger)
- **X** (Number)
- **Y** (Number)
- **Z** (Number)
- **W** (Number)

**`\outputsymbol`{=latex} Output**

- **Trigger** (Trigger)

**Example:** [cables.gl/op/Ops.Gl.Matrix.Quaternion#example](https://cables.gl/op/Ops.Gl.Matrix.Quaternion#example)

**Doc:** [cables.gl/op/Ops.Gl.Matrix.Quaternion](https://cables.gl/op/Ops.Gl.Matrix.Quaternion)

### QuaternionCamera
![QuaternionCamera op](images/ops/Ops_Gl_Matrix_QuaternionCamera.svg)

**Full Name:** `Ops.Gl.Matrix.QuaternionCamera`

Set up a camera, rotated by a quaternion.

**`\inputsymbol`{=latex} Inputs**

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

**`\outputsymbol`{=latex} Output**

- **Trigger** (Trigger)

**Example:** [cables.gl/op/Ops.Gl.Matrix.QuaternionCamera#example](https://cables.gl/op/Ops.Gl.Matrix.QuaternionCamera#example)

**Doc:** [cables.gl/op/Ops.Gl.Matrix.QuaternionCamera](https://cables.gl/op/Ops.Gl.Matrix.QuaternionCamera)

### RandomGridPlacement
![RandomGridPlacement op](images/ops/Ops_Gl_Matrix_RandomGridPlacement.svg)

**Full Name:** `Ops.Gl.Matrix.RandomGridPlacement`

place random objects on a grid.

**`\inputsymbol`{=latex} Inputs**

- **Exe** (Trigger)
- **Max Depth** (Number)
- **Possibility** (Number)
- **Seed** (Number)
- **Scale** (Number)
- **Width** (Number)
- **Height** (Number)

**`\outputsymbol`{=latex} Output**

- **Next** (Trigger)
- **Index** (Number)
- **Depth** (Number)

**Example:** [cables.gl/edit/FsZFVB](https://cables.gl/edit/FsZFVB)

**Doc:** [cables.gl/op/Ops.Gl.Matrix.RandomGridPlacement](https://cables.gl/op/Ops.Gl.Matrix.RandomGridPlacement)

### RandomGridPlacementArrays
![RandomGridPlacementArrays op](images/ops/Ops_Gl_Matrix_RandomGridPlacementArrays.svg)

**Full Name:** `Ops.Gl.Matrix.RandomGridPlacementArrays`

Place random objects on a grid.

**`\inputsymbol`{=latex} Inputs**

- **Exe** (Trigger)
- **Max Depth** (Number)
- **Possibility** (Number)
- **Seed** (Number)
- **Scale** (Number)
- **Width** (Number)
- **Height** (Number)

**`\outputsymbol`{=latex} Output**

- **Positions** (Array)
- **Scalings** (Array)
- **Array Length** (Number)
- **Total Points** (Number)

**Example:** [cables.gl/edit/PYUHNP](https://cables.gl/edit/PYUHNP)

**Doc:** [cables.gl/op/Ops.Gl.Matrix.RandomGridPlacementArrays](https://cables.gl/op/Ops.Gl.Matrix.RandomGridPlacementArrays)

### Scale
![Scale op](images/ops/Ops_Gl_Matrix_Scale.svg)

**Full Name:** `Ops.Gl.Matrix.Scale`

Scale all child objects (scaleXYZ).

**`\inputsymbol`{=latex} Inputs**

- **Render** (Trigger)
- **Scale** (Number)
- **X** (Number)
- **Y** (Number)
- **Z** (Number)

**`\outputsymbol`{=latex} Output**

- **Trigger** (Trigger)

**Example:** [cables.gl/edit/au9U7i](https://cables.gl/edit/au9U7i)

**Doc:** [cables.gl/op/Ops.Gl.Matrix.Scale](https://cables.gl/op/Ops.Gl.Matrix.Scale)

### ScaleXYZViewMatrix
![ScaleXYZViewMatrix op](images/ops/Ops_Gl_Matrix_ScaleXYZViewMatrix.svg)

**Full Name:** `Ops.Gl.Matrix.ScaleXYZViewMatrix`

scale xyz of viewmatrix.

**`\inputsymbol`{=latex} Inputs**

- **Render** (Trigger)
- **X** (Number)
- **Y** (Number)
- **Z** (Number)

**`\outputsymbol`{=latex} Output**

- **Trigger** (Trigger)

**Example:** [cables.gl/edit/aSB6On](https://cables.gl/edit/aSB6On)

**Doc:** [cables.gl/op/Ops.Gl.Matrix.ScaleXYZViewMatrix](https://cables.gl/op/Ops.Gl.Matrix.ScaleXYZViewMatrix)

### ScreenCoordinates_v2
![ScreenCoordinates_v2 op](images/ops/Ops_Gl_Matrix_ScreenCoordinates_v2.svg)

**Full Name:** `Ops.Gl.Matrix.ScreenCoordinates_v2`

screen/pixel coordinates of the current transform.

**`\inputsymbol`{=latex} Inputs**

- **Execute** (Trigger)
- **Pixel Unit Index** (Number: Integer)

**`\outputsymbol`{=latex} Output**

- **Trigger** (Trigger)
- **X** (Number)
- **Y** (Number)
- **Visible** (Number)

**Example:** [cables.gl/edit/-GNBD-](https://cables.gl/edit/-GNBD-)

**Doc:** [cables.gl/op/Ops.Gl.Matrix.ScreenCoordinates_v2](https://cables.gl/op/Ops.Gl.Matrix.ScreenCoordinates_v2)

### ScreenPosTo3d_v3
![ScreenPosTo3d_v3 op](images/ops/Ops_Gl_Matrix_ScreenPosTo3d_v3.svg)

**Full Name:** `Ops.Gl.Matrix.ScreenPosTo3d_v3`

convert screen coordinates to a 3d position.

**`\inputsymbol`{=latex} Inputs**

- **Exec** (Trigger)
- **X** (Number)
- **Y** (Number)
- **Input Type Index** (Number: Integer)

**`\outputsymbol`{=latex} Output**

- **Trigger Out** (Trigger)
- **Result X** (Number)
- **Result Y** (Number)

**Example:** [cables.gl/edit/mDiCq6](https://cables.gl/edit/mDiCq6)

**Doc:** [cables.gl/op/Ops.Gl.Matrix.ScreenPosTo3d_v3](https://cables.gl/op/Ops.Gl.Matrix.ScreenPosTo3d_v3)

### SetProjectionMatrix
![SetProjectionMatrix op](images/ops/Ops_Gl_Matrix_SetProjectionMatrix.svg)

**Full Name:** `Ops.Gl.Matrix.SetProjectionMatrix`

set a projection matrix.

**`\inputsymbol`{=latex} Inputs**

- **Exe** (Trigger)
- **Matrix** (Array)

**`\outputsymbol`{=latex} Output**

- **Next** (Trigger)

**Example:** [cables.gl/edit/573_4S](https://cables.gl/edit/573_4S)

**Doc:** [cables.gl/op/Ops.Gl.Matrix.SetProjectionMatrix](https://cables.gl/op/Ops.Gl.Matrix.SetProjectionMatrix)

### Shear
![Shear op](images/ops/Ops_Gl_Matrix_Shear.svg)

**Full Name:** `Ops.Gl.Matrix.Shear`

displaces each point of a mesh in fixed direction.

**`\inputsymbol`{=latex} Inputs**

- **Render** (Trigger)
- **ShearX** (Number)
- **ShearY** (Number)

**`\outputsymbol`{=latex} Output**

- **Trigger** (Trigger)

**Example:** [cables.gl/edit/PmTYnO](https://cables.gl/edit/PmTYnO)

**Doc:** [cables.gl/op/Ops.Gl.Matrix.Shear](https://cables.gl/op/Ops.Gl.Matrix.Shear)

### TransformMatrix
![TransformMatrix op](images/ops/Ops_Gl_Matrix_TransformMatrix.svg)

**Full Name:** `Ops.Gl.Matrix.TransformMatrix`

transform a matrix (mat4).

**`\inputsymbol`{=latex} Inputs**

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

**`\outputsymbol`{=latex} Output**

- **Next** (Trigger)
- **Result** (Array)

**Example:** [cables.gl/edit/A0W1Jx](https://cables.gl/edit/A0W1Jx)

**Doc:** [cables.gl/op/Ops.Gl.Matrix.TransformMatrix](https://cables.gl/op/Ops.Gl.Matrix.TransformMatrix)

### TransformMul
![TransformMul op](images/ops/Ops_Gl_Matrix_TransformMul.svg)

**Full Name:** `Ops.Gl.Matrix.TransformMul`

multiply current modelmatrix.

**`\inputsymbol`{=latex} Inputs**

- **Render** (Trigger)
- **Mul** (Number)

**`\outputsymbol`{=latex} Output**

- **Trigger** (Trigger)

**Example:** [cables.gl/op/Ops.Gl.Matrix.TransformMul#example](https://cables.gl/op/Ops.Gl.Matrix.TransformMul#example)

**Doc:** [cables.gl/op/Ops.Gl.Matrix.TransformMul](https://cables.gl/op/Ops.Gl.Matrix.TransformMul)

### Translate
![Translate op](images/ops/Ops_Gl_Matrix_Translate.svg)

**Full Name:** `Ops.Gl.Matrix.Translate`

Translate objects (move / position in 3D space).

**`\inputsymbol`{=latex} Inputs**

- **Render** (Trigger)
- **X** (Number)
- **Y** (Number)
- **Z** (Number)

**`\outputsymbol`{=latex} Output**

- **Trigger** (Trigger)

**Example:** [cables.gl/op/Ops.Gl.Matrix.Translate#example](https://cables.gl/op/Ops.Gl.Matrix.Translate#example)

**Doc:** [cables.gl/op/Ops.Gl.Matrix.Translate](https://cables.gl/op/Ops.Gl.Matrix.Translate)

### TranslateView
![TranslateView op](images/ops/Ops_Gl_Matrix_TranslateView.svg)

**Full Name:** `Ops.Gl.Matrix.TranslateView`

translate the view/camera matrix.

**`\inputsymbol`{=latex} Inputs**

- **Render** (Trigger)
- **X** (Number)
- **Y** (Number)
- **Z** (Number)

**`\outputsymbol`{=latex} Output**

- **Trigger** (Trigger)

**Example:** [cables.gl/op/Ops.Gl.Matrix.TranslateView#example](https://cables.gl/op/Ops.Gl.Matrix.TranslateView#example)

**Doc:** [cables.gl/op/Ops.Gl.Matrix.TranslateView](https://cables.gl/op/Ops.Gl.Matrix.TranslateView)

### VectorTranslate
![VectorTranslate op](images/ops/Ops_Gl_Matrix_VectorTranslate.svg)

**Full Name:** `Ops.Gl.Matrix.VectorTranslate`

Translate any geometry underneath it using vectors and speed.

**`\inputsymbol`{=latex} Inputs**

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

**`\outputsymbol`{=latex} Output**

- **Next** (Trigger)

**Example:** [cables.gl/op/Ops.Gl.Matrix.VectorTranslate#example](https://cables.gl/op/Ops.Gl.Matrix.VectorTranslate#example)

**Doc:** [cables.gl/op/Ops.Gl.Matrix.VectorTranslate](https://cables.gl/op/Ops.Gl.Matrix.VectorTranslate)

### WASDCamera_v2
![WASDCamera_v2 op](images/ops/Ops_Gl_Matrix_WASDCamera_v2.svg)

**Full Name:** `Ops.Gl.Matrix.WASDCamera_v2`

simple camera you control with W,A,S,D keys like in a FPS game.

**`\inputsymbol`{=latex} Inputs**

- **Render** (Trigger)
- **Enable Pointer Lock** (Number: Boolean)
- **Speed** (Number)
- **Mouse Speed** (Number)
- **Allow Flying** (Number: Boolean)
- **Active** (Number: Boolean)
- **Move X-** (Number: Boolean)
- **Move Y-** (Number: Boolean)
- **Reset** (Trigger)

**`\outputsymbol`{=latex} Output**

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

**Example:** [cables.gl/edit/oLCaao](https://cables.gl/edit/oLCaao)

**Doc:** [cables.gl/op/Ops.Gl.Matrix.WASDCamera_v2](https://cables.gl/op/Ops.Gl.Matrix.WASDCamera_v2)


