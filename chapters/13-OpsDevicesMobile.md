# Ops.Devices.Mobile

---

```{=latex}
\stepcounter{subsection}\setcounter{subsubsection}{0}
```
### DeviceVibrate
![DeviceVibrate op](images/ops/Ops_Devices_Mobile_DeviceVibrate.svg)

**Full Name:** `Ops.Devices.Mobile.DeviceVibrate`

**Description:** vibrating a mobile device

**`\inputsymbol`{=latex} Inputs**

- **Vibrate** (Trigger)

**`\outputsymbol`{=latex} Output**

- **Supported** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/edit/H4NGFU)

**Docs:** [https://cables.gl/op/Ops.Devices.Mobile.DeviceVibrate](https://cables.gl/op/Ops.Devices.Mobile.DeviceVibrate)

### GeoLocation
![GeoLocation op](images/ops/Ops_Devices_Mobile_GeoLocation.svg)

**Full Name:** `Ops.Devices.Mobile.GeoLocation`

**Description:** tries to get the geo coordinates from the mobile device/browser

**`\inputsymbol`{=latex} Inputs**

- *Visit [Ops.Devices.Mobile.GeoLocation documentation](https://cables.gl/op/Ops.Devices.Mobile.GeoLocation) for input port details*

**`\outputsymbol`{=latex} Output**

- **Browser Support** (booleanNumber)
- **Latitude** (Number)
- **Longitude** (Number)
- **Data** (Object)

**Example Patch:** [Open in Editor](https://cables.gl/edit/kIZ3Ms)

**Docs:** [https://cables.gl/op/Ops.Devices.Mobile.GeoLocation](https://cables.gl/op/Ops.Devices.Mobile.GeoLocation)

### LockOrientation
![LockOrientation op](images/ops/Ops_Devices_Mobile_LockOrientation.svg)

**Full Name:** `Ops.Devices.Mobile.LockOrientation`

**Description:** locks orientation to landscape or portrait mode

**`\inputsymbol`{=latex} Inputs**

- **Portrait** (Number: Boolean)
- **Landscape** (Number: Boolean)

**`\outputsymbol`{=latex} Output**

- **Supported** (Number)
- **Locked** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Devices.Mobile.LockOrientation#example)

**Docs:** [https://cables.gl/op/Ops.Devices.Mobile.LockOrientation](https://cables.gl/op/Ops.Devices.Mobile.LockOrientation)

### MotionSensor_v2
![MotionSensor_v2 op](images/ops/Ops_Devices_Mobile_MotionSensor_v2.svg)

**Full Name:** `Ops.Devices.Mobile.MotionSensor_v2`

**Description:** get values from the device motion sensor mobile

**`\inputsymbol`{=latex} Inputs**

- **Mul Orientation** (Number)
- **Request Permissions** (Trigger)

**`\outputsymbol`{=latex} Output**

- **Orientation Alpha** (Number)
- **Orientation Beta** (Number)
- **Orientation Gamma** (Number)
- **Acceleration X** (Number)
- **Acceleration Y** (Number)
- **Acceleration Z** (Number)
- **Acceleration X No Gravity** (Number)
- **Acceleration Y No Gravity** (Number)
- **Acceleration Z No Gravity** (Number)
- **Rotation Rate Alpha** (Number)
- **Rotation Rate Beta** (Number)
- **Rotation Rate Gamma** (Number)
- **Permissions** (String)
- **Object** (Object)

**Example Patch:** [Open in Editor](https://cables.gl/edit/dZ8wQ0)

**Docs:** [https://cables.gl/op/Ops.Devices.Mobile.MotionSensor_v2](https://cables.gl/op/Ops.Devices.Mobile.MotionSensor_v2)

### Pinch
![Pinch op](images/ops/Ops_Devices_Mobile_Pinch.svg)

**Full Name:** `Ops.Devices.Mobile.Pinch`

**Description:** detect two finger pinch gestures on touchscreens

**`\inputsymbol`{=latex} Inputs**

- **Enabled** (Number: Boolean)
- **Min Scale** (Number)
- **Max Scale** (Number)
- **Reset Scale** (Trigger)
- **Limit** (Number: Boolean)

**`\outputsymbol`{=latex} Output**

- **Scale** (Number)
- **Event Details** (Object)
- **Delta** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Devices.Mobile.Pinch#example)

**Docs:** [https://cables.gl/op/Ops.Devices.Mobile.Pinch](https://cables.gl/op/Ops.Devices.Mobile.Pinch)

### ScreenOrientation_v2
![ScreenOrientation_v2 op](images/ops/Ops_Devices_Mobile_ScreenOrientation_v2.svg)

**Full Name:** `Ops.Devices.Mobile.ScreenOrientation_v2`

**Description:** get orientation of the physical screen

**`\inputsymbol`{=latex} Inputs**

- *Visit [Ops.Devices.Mobile.ScreenOrientation_v2 documentation](https://cables.gl/op/Ops.Devices.Mobile.ScreenOrientation_v2) for input port details*

**`\outputsymbol`{=latex} Output**

- **Angle** (Number)
- **Type** (String)

**Example Patch:** [Open in Editor](https://cables.gl/edit/Zc398i)

**Docs:** [https://cables.gl/op/Ops.Devices.Mobile.ScreenOrientation_v2](https://cables.gl/op/Ops.Devices.Mobile.ScreenOrientation_v2)

### ShakeGesture
![ShakeGesture op](images/ops/Ops_Devices_Mobile_ShakeGesture.svg)

**Full Name:** `Ops.Devices.Mobile.ShakeGesture`

**Description:** Reads the accelerometer data from a mobile device

**`\inputsymbol`{=latex} Inputs**

- *Visit [Ops.Devices.Mobile.ShakeGesture documentation](https://cables.gl/op/Ops.Devices.Mobile.ShakeGesture) for input port details*

**`\outputsymbol`{=latex} Output**

- **Acceleration X** (Number)
- **Acceleration Y** (Number)
- **Acceleration Z** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Devices.Mobile.ShakeGesture#example)

**Docs:** [https://cables.gl/op/Ops.Devices.Mobile.ShakeGesture](https://cables.gl/op/Ops.Devices.Mobile.ShakeGesture)


