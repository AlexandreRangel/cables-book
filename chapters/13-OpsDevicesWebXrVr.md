# Ops.Devices.WebXr.Vr

---

## Ops.Devices.WebXr.Vr

### Vr
![Vr op](images/ops/Ops_Devices_WebXr_Vr_Vr.svg)

**Full Name:** `Ops.Devices.WebXr.Vr.Vr`

**Description:** rendering on webxr virtual reality immersive devices

**`\inputsymbol`{=latex} Inputs**

- **Mainloop** (Trigger)
- **Stop** (Trigger)
- **Show Button** (Number: Boolean)
- **Button Style** (String)
- **Render To Texture** (Number: Boolean)
- **Shader** (Object:Shader)

**`\outputsymbol`{=latex} Output**

- **Next** (Trigger)
- **Render After Eyes** (Trigger)
- **Viewer Pose** (Object)
- **Eye Index** (Number)
- **VR Support** (booleanNumber)
- **Matrix** (Array)
- **DOM Overlay Ele** (Object)
- **In Session** (booleanNumber)
- **Ms Per Eye** (Array)
- **Texture** (Object)
- **Texture Depth** (Object)

**Example Patch:** [Open in Editor](https://cables.gl/edit/IzKYx5)

**Docs:** [https://cables.gl/op/Ops.Devices.WebXr.Vr.Vr](https://cables.gl/op/Ops.Devices.WebXr.Vr.Vr)

### VrController
![VrController op](images/ops/Ops_Devices_WebXr_Vr_VrController.svg)

**Full Name:** `Ops.Devices.WebXr.Vr.VrController`

**Description:** tracking of vr hand controller

**`\inputsymbol`{=latex} Inputs**

- **Update** (Trigger)
- **Handedness Index** (Number: Integer)

**`\outputsymbol`{=latex} Output**

- **Next** (Trigger)
- **Axis 1** (Number)
- **Axis 2** (Number)
- **Axis 3** (Number)
- **Axis 4** (Number)
- **Button 1 Pressed** (Number)
- **Button 2 Pressed** (Number)
- **Button 3 Pressed** (Number)
- **Button 4 Pressed** (Number)
- **Button 5 Pressed** (Number)
- **Button 6 Pressed** (Number)
- **Button 7 Pressed** (Number)
- **Button 1 Touched** (Number)
- **Button 2 Touched** (Number)
- **Button 3 Touched** (Number)
- **Button 4 Touched** (Number)
- **Button 5 Touched** (Number)
- **Button 6 Touched** (Number)
- **Button 7 Touched** (Number)
- **Position X** (Number)
- **Position Y** (Number)
- **Position Z** (Number)
- **Gamepad Values** (Object)
- **Transformed Position** (Trigger)
- **Found** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/edit/IzKYx5)

**Docs:** [https://cables.gl/op/Ops.Devices.WebXr.Vr.VrController](https://cables.gl/op/Ops.Devices.WebXr.Vr.VrController)


