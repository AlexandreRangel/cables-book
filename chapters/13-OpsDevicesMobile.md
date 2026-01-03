# Ops.Devices.Mobile

---

## Ops.Devices.Mobile

### DeviceVibrate
![DeviceVibrate op](images/ops/Ops_Devices_Mobile_DeviceVibrate.svg)

**Full Name:** `Ops.Devices.Mobile.DeviceVibrate`

**Description:** vibrating a mobile device

**> Input Ports:**

- **Vibrate** (Trigger)

**< Output Ports:**

- **Supported** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/edit/H4NGFU)

**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "DeviceVibrate"*

**Docs:** [https://cables.gl/op/Ops.Devices.Mobile.DeviceVibrate](https://cables.gl/op/Ops.Devices.Mobile.DeviceVibrate)


### GeoLocation
![GeoLocation op](images/ops/Ops_Devices_Mobile_GeoLocation.svg)

**Full Name:** `Ops.Devices.Mobile.GeoLocation`

**Description:** tries to get the geo coordinates from the mobile device/browser

**> Input Ports:**

- *Visit [Ops.Devices.Mobile.GeoLocation documentation](https://cables.gl/op/Ops.Devices.Mobile.GeoLocation) for input port details*

**< Output Ports:**

- **Browser Support** (booleanNumber)
- **Latitude** (Number)
- **Longitude** (Number)
- **Data** (Object)

**Example Patch:** [Open in Editor](https://cables.gl/edit/kIZ3Ms)

**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "GeoLocation"*

**Docs:** [https://cables.gl/op/Ops.Devices.Mobile.GeoLocation](https://cables.gl/op/Ops.Devices.Mobile.GeoLocation)


### LockOrientation
![LockOrientation op](images/ops/Ops_Devices_Mobile_LockOrientation.svg)

**Full Name:** `Ops.Devices.Mobile.LockOrientation`

**Description:** locks orientation to landscape or portrait mode

**> Input Ports:**

- **Portrait** (Number: Boolean)
- **Landscape** (Number: Boolean)

**< Output Ports:**

- **Supported** (Number)
- **Locked** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Devices.Mobile.LockOrientation#example)

**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "LockOrientation"*

**Docs:** [https://cables.gl/op/Ops.Devices.Mobile.LockOrientation](https://cables.gl/op/Ops.Devices.Mobile.LockOrientation)


### MotionSensor_v2
![MotionSensor_v2 op](images/ops/Ops_Devices_Mobile_MotionSensor_v2.svg)

**Full Name:** `Ops.Devices.Mobile.MotionSensor_v2`

**Description:** get values from the device motion sensor mobile

**> Input Ports:**

- **Mul Orientation** (Number)
- **Request Permissions** (Trigger)

**< Output Ports:**

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

**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "MotionSensor_v2"*

**Docs:** [https://cables.gl/op/Ops.Devices.Mobile.MotionSensor_v2](https://cables.gl/op/Ops.Devices.Mobile.MotionSensor_v2)


### Pinch
![Pinch op](images/ops/Ops_Devices_Mobile_Pinch.svg)

**Full Name:** `Ops.Devices.Mobile.Pinch`

**Description:** detect two finger pinch gestures on touchscreens

**> Input Ports:**

- **Enabled** (Number: Boolean)
- **Min Scale** (Number)
- **Max Scale** (Number)
- **Reset Scale** (Trigger)
- **Limit** (Number: Boolean)

**< Output Ports:**

- **Scale** (Number)
- **Event Details** (Object)
- **Delta** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Devices.Mobile.Pinch#example)

**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "Pinch"*

**Docs:** [https://cables.gl/op/Ops.Devices.Mobile.Pinch](https://cables.gl/op/Ops.Devices.Mobile.Pinch)


### ScreenOrientation_v2
![ScreenOrientation_v2 op](images/ops/Ops_Devices_Mobile_ScreenOrientation_v2.svg)

**Full Name:** `Ops.Devices.Mobile.ScreenOrientation_v2`

**Description:** get orientation of the physical screen

**> Input Ports:**

- *Visit [Ops.Devices.Mobile.ScreenOrientation_v2 documentation](https://cables.gl/op/Ops.Devices.Mobile.ScreenOrientation_v2) for input port details*

**< Output Ports:**

- **Angle** (Number)
- **Type** (String)

**Example Patch:** [Open in Editor](https://cables.gl/edit/Zc398i)

**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ScreenOrientation_v2"*

**Docs:** [https://cables.gl/op/Ops.Devices.Mobile.ScreenOrientation_v2](https://cables.gl/op/Ops.Devices.Mobile.ScreenOrientation_v2)


### ShakeGesture
![ShakeGesture op](images/ops/Ops_Devices_Mobile_ShakeGesture.svg)

**Full Name:** `Ops.Devices.Mobile.ShakeGesture`

**Description:** Reads the accelerometer data from a mobile device

**> Input Ports:**

- *Visit [Ops.Devices.Mobile.ShakeGesture documentation](https://cables.gl/op/Ops.Devices.Mobile.ShakeGesture) for input port details*

**< Output Ports:**

- **Acceleration X** (Number)
- **Acceleration Y** (Number)
- **Acceleration Z** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Devices.Mobile.ShakeGesture#example)

**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ShakeGesture"*

**Docs:** [https://cables.gl/op/Ops.Devices.Mobile.ShakeGesture](https://cables.gl/op/Ops.Devices.Mobile.ShakeGesture)


