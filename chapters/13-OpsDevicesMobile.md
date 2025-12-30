# Ops.Devices.Mobile

*Part of the [All Operators Reference](13-_AllOps.md)*

---

## Ops.Devices.Mobile

### DeviceVibrate
![DeviceVibrate op](images/ops/Ops_Devices_Mobile_DeviceVibrate.svg)

**Full Name:** `Ops.Devices.Mobile.DeviceVibrate`
**Description:** vibrating a mobile device

**> Input Ports:**
- **Vibrate** (Trigger): *See documentation*

**< Output Ports:**
- **Supported** (Number): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/H4NGFU)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "DeviceVibrate"*
**Docs:** [https://cables.gl/op/Ops.Devices.Mobile.DeviceVibrate](https://cables.gl/op/Ops.Devices.Mobile.DeviceVibrate)

---

### GeoLocation
![GeoLocation op](images/ops/Ops_Devices_Mobile_GeoLocation.svg)

**Full Name:** `Ops.Devices.Mobile.GeoLocation`
**Description:** tries to get the geo coordinates from the mobile device/browser

**> Input Ports:**
- *Visit [Ops.Devices.Mobile.GeoLocation documentation](https://cables.gl/op/Ops.Devices.Mobile.GeoLocation) for input port details*

**< Output Ports:**
- **Browser Support** (booleanNumber): *See documentation*
- **Latitude** (Number): *See documentation*
- **Longitude** (Number): *See documentation*
- **Data** (Object): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/kIZ3Ms)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "GeoLocation"*
**Docs:** [https://cables.gl/op/Ops.Devices.Mobile.GeoLocation](https://cables.gl/op/Ops.Devices.Mobile.GeoLocation)

---

### LockOrientation
![LockOrientation op](images/ops/Ops_Devices_Mobile_LockOrientation.svg)

**Full Name:** `Ops.Devices.Mobile.LockOrientation`
**Description:** locks orientation to landscape or portrait mode

**> Input Ports:**
- **Portrait** (Number: Boolean): *See documentation*
- **Landscape** (Number: Boolean): *See documentation*

**< Output Ports:**
- **Supported** (Number): *See documentation*
- **Locked** (Number): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Devices.Mobile.LockOrientation#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "LockOrientation"*
**Docs:** [https://cables.gl/op/Ops.Devices.Mobile.LockOrientation](https://cables.gl/op/Ops.Devices.Mobile.LockOrientation)

---

### MotionSensor_v2
![MotionSensor_v2 op](images/ops/Ops_Devices_Mobile_MotionSensor_v2.svg)

**Full Name:** `Ops.Devices.Mobile.MotionSensor_v2`
**Description:** get values from the device motion sensor mobile

**> Input Ports:**
- **Mul Orientation** (Number): *See documentation*
- **Request Permissions** (Trigger): *See documentation*

**< Output Ports:**
- **Orientation Alpha** (Number): *See documentation*
- **Orientation Beta** (Number): *See documentation*
- **Orientation Gamma** (Number): *See documentation*
- **Acceleration X** (Number): *See documentation*
- **Acceleration Y** (Number): *See documentation*
- **Acceleration Z** (Number): *See documentation*
- **Acceleration X No Gravity** (Number): *See documentation*
- **Acceleration Y No Gravity** (Number): *See documentation*
- **Acceleration Z No Gravity** (Number): *See documentation*
- **Rotation Rate Alpha** (Number): *See documentation*
- **Rotation Rate Beta** (Number): *See documentation*
- **Rotation Rate Gamma** (Number): *See documentation*
- **Permissions** (String): *See documentation*
- **Object** (Object): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/dZ8wQ0)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "MotionSensor_v2"*
**Docs:** [https://cables.gl/op/Ops.Devices.Mobile.MotionSensor_v2](https://cables.gl/op/Ops.Devices.Mobile.MotionSensor_v2)

---

### Pinch
![Pinch op](images/ops/Ops_Devices_Mobile_Pinch.svg)

**Full Name:** `Ops.Devices.Mobile.Pinch`
**Description:** detect two finger pinch gestures on touchscreens

**> Input Ports:**
- **Enabled** (Number: Boolean): *See documentation*
- **Min Scale** (Number): *See documentation*
- **Max Scale** (Number): *See documentation*
- **Reset Scale** (Trigger): *See documentation*
- **Limit** (Number: Boolean): *See documentation*

**< Output Ports:**
- **Scale** (Number): *See documentation*
- **Event Details** (Object): *See documentation*
- **Delta** (Number): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Devices.Mobile.Pinch#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "Pinch"*
**Docs:** [https://cables.gl/op/Ops.Devices.Mobile.Pinch](https://cables.gl/op/Ops.Devices.Mobile.Pinch)

---

### ScreenOrientation_v2
![ScreenOrientation_v2 op](images/ops/Ops_Devices_Mobile_ScreenOrientation_v2.svg)

**Full Name:** `Ops.Devices.Mobile.ScreenOrientation_v2`
**Description:** get orientation of the physical screen

**> Input Ports:**
- *Visit [Ops.Devices.Mobile.ScreenOrientation_v2 documentation](https://cables.gl/op/Ops.Devices.Mobile.ScreenOrientation_v2) for input port details*

**< Output Ports:**
- **Angle** (Number): *See documentation*
- **Type** (String): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/Zc398i)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ScreenOrientation_v2"*
**Docs:** [https://cables.gl/op/Ops.Devices.Mobile.ScreenOrientation_v2](https://cables.gl/op/Ops.Devices.Mobile.ScreenOrientation_v2)

---

### ShakeGesture
![ShakeGesture op](images/ops/Ops_Devices_Mobile_ShakeGesture.svg)

**Full Name:** `Ops.Devices.Mobile.ShakeGesture`
**Description:** Reads the accelerometer data from a mobile device

**> Input Ports:**
- *Visit [Ops.Devices.Mobile.ShakeGesture documentation](https://cables.gl/op/Ops.Devices.Mobile.ShakeGesture) for input port details*

**< Output Ports:**
- **Acceleration X** (Number): *See documentation*
- **Acceleration Y** (Number): *See documentation*
- **Acceleration Z** (Number): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Devices.Mobile.ShakeGesture#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ShakeGesture"*
**Docs:** [https://cables.gl/op/Ops.Devices.Mobile.ShakeGesture](https://cables.gl/op/Ops.Devices.Mobile.ShakeGesture)

---

