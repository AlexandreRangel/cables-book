# Ops.Devices.WebXr.Vr

*Part of the [All Operators Reference](13-_AllOps.md)*

---

## Ops.Devices.WebXr.Vr

### Vr
![Vr op](images/ops/Ops_Devices_WebXr_Vr_Vr.svg)

**Full Name:** `Ops.Devices.WebXr.Vr.Vr`
**Description:** rendering on webxr virtual reality immersive devices

**> Input Ports:**
- **Mainloop** (Trigger)
- **Stop** (Trigger)
- **Show Button** (Number: Boolean)
- **Button Style** (String)
- **Render To Texture** (Number: Boolean)
- **Shader** (Object:Shader)

**< Output Ports:**
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
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "Vr"*
**Docs:** [https://cables.gl/op/Ops.Devices.WebXr.Vr.Vr](https://cables.gl/op/Ops.Devices.WebXr.Vr.Vr)

---

### VrController
![VrController op](images/ops/Ops_Devices_WebXr_Vr_VrController.svg)

**Full Name:** `Ops.Devices.WebXr.Vr.VrController`
**Description:** tracking of vr hand controller

**> Input Ports:**
- **Update** (Trigger)
- **Handedness Index** (Number: Integer)

**< Output Ports:**
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
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "VrController"*
**Docs:** [https://cables.gl/op/Ops.Devices.WebXr.Vr.VrController](https://cables.gl/op/Ops.Devices.WebXr.Vr.VrController)

---

