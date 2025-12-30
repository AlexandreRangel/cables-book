# Ops.Extension.SocketCluster

*Part of the [All Operators Reference](13-_AllOps.md)*

---

## Ops.Extension.SocketCluster

### SocketClusterClient_v2
![SocketClusterClient_v2 op](images/ops/Ops_Extension_SocketCluster_SocketClusterClient_v2.svg)

**Full Name:** `Ops.Extension.SocketCluster.SocketClusterClient_v2`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Extension.SocketCluster.SocketClusterClient_v2) for details*

**> Input Ports:**
- **Channel** (String)
- **Server Hostname** (String)
- **Server Port** (Number)
- **Use SSL** (Number: Boolean)
- **enable encryption** (needs to be supported by server)
- **Server Path** (String)
- **Allow Send** (Number: Boolean)
- **Allow Multiple Senders** (Number: Boolean)
- **Additional Serverdata** (Object)
- **additional data send with every message** (can be used for auth-token)
- **Active** (Number: Boolean)

**< Output Ports:**
- **Ready** (booleanNumber)
- **Socket** (Object)
- **Own Client Id** (String)
- **Can Send** (booleanNumber)
- **Error** (String)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Extension.SocketCluster.SocketClusterClient_v2#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "SocketClusterClient_v2"*
**Docs:** [https://cables.gl/op/Ops.Extension.SocketCluster.SocketClusterClient_v2](https://cables.gl/op/Ops.Extension.SocketCluster.SocketClusterClient_v2)

---

### SocketClusterReceiveObject
![SocketClusterReceiveObject op](images/ops/Ops_Extension_SocketCluster_SocketClusterReceiveObject.svg)

**Full Name:** `Ops.Extension.SocketCluster.SocketClusterReceiveObject`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Extension.SocketCluster.SocketClusterReceiveObject) for details*

**> Input Ports:**
- **Socket** (Object:Socketcluster)
- **Topic** (String)
- **Receive Own Data** (Number: Boolean)

**< Output Ports:**
- **Client Id** (String)
- **Data** (Object)
- **Received** (Trigger)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Extension.SocketCluster.SocketClusterReceiveObject#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "SocketClusterReceiveObject"*
**Docs:** [https://cables.gl/op/Ops.Extension.SocketCluster.SocketClusterReceiveObject](https://cables.gl/op/Ops.Extension.SocketCluster.SocketClusterReceiveObject)

---

### SocketClusterReceiveTrigger
![SocketClusterReceiveTrigger op](images/ops/Ops_Extension_SocketCluster_SocketClusterReceiveTrigger.svg)

**Full Name:** `Ops.Extension.SocketCluster.SocketClusterReceiveTrigger`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Extension.SocketCluster.SocketClusterReceiveTrigger) for details*

**> Input Ports:**
- **Socket** (Object:Socketcluster)
- **Topic** (String)
- **Receive Own Data** (Number: Boolean)
- **Use Named Trigger** (Number: Boolean)

**< Output Ports:**
- **Client Id** (String)
- **Trigger Name** (String)
- **Received** (Trigger)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Extension.SocketCluster.SocketClusterReceiveTrigger#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "SocketClusterReceiveTrigger"*
**Docs:** [https://cables.gl/op/Ops.Extension.SocketCluster.SocketClusterReceiveTrigger](https://cables.gl/op/Ops.Extension.SocketCluster.SocketClusterReceiveTrigger)

---

### SocketClusterSendObject
![SocketClusterSendObject op](images/ops/Ops_Extension_SocketCluster_SocketClusterSendObject.svg)

**Full Name:** `Ops.Extension.SocketCluster.SocketClusterSendObject`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Extension.SocketCluster.SocketClusterSendObject) for details*

**> Input Ports:**
- **Socket** (Object:Socketcluster)
- **Topic** (String)
- **Data** (Object)
- **Send** (Trigger)

**< Output Ports:**
- **Sent Data** (Trigger)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Extension.SocketCluster.SocketClusterSendObject#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "SocketClusterSendObject"*
**Docs:** [https://cables.gl/op/Ops.Extension.SocketCluster.SocketClusterSendObject](https://cables.gl/op/Ops.Extension.SocketCluster.SocketClusterSendObject)

---

### SocketClusterSendTrigger
![SocketClusterSendTrigger op](images/ops/Ops_Extension_SocketCluster_SocketClusterSendTrigger.svg)

**Full Name:** `Ops.Extension.SocketCluster.SocketClusterSendTrigger`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Extension.SocketCluster.SocketClusterSendTrigger) for details*

**> Input Ports:**
- **Data** (Trigger)
- **Socket** (Object:Socketcluster)
- **Topic** (String)
- **Trigger Name** (String)
- **the name of the trigger** (created with TriggerSend)

**< Output Ports:**
- *Visit [Ops.Extension.SocketCluster.SocketClusterSendTrigger documentation](https://cables.gl/op/Ops.Extension.SocketCluster.SocketClusterSendTrigger) for output port details*

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Extension.SocketCluster.SocketClusterSendTrigger#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "SocketClusterSendTrigger"*
**Docs:** [https://cables.gl/op/Ops.Extension.SocketCluster.SocketClusterSendTrigger](https://cables.gl/op/Ops.Extension.SocketCluster.SocketClusterSendTrigger)

---

### SocketClusterTopicInfo_v2
![SocketClusterTopicInfo_v2 op](images/ops/Ops_Extension_SocketCluster_SocketClusterTopicInfo_v2.svg)

**Full Name:** `Ops.Extension.SocketCluster.SocketClusterTopicInfo_v2`
**Description:** *Visit [documentation](https://cables.gl/op/Ops.Extension.SocketCluster.SocketClusterTopicInfo_v2) for details*

**> Input Ports:**
- **Socket** (Object:Socketcluster)
- **Topic** (String)
- **Timeout Seconds** (Number: Integer)
- **Soft Timeout Seconds** (Number: Integer)
- **Retain Messages** (Number: Integer)
- **Update** (Trigger)
- **Receive My Data** (Number: Boolean)

**< Output Ports:**
- **Active Clients** (Array)
- **Will Time Out** (Object)
- **Timed Out Clients** (Array)
- **Messages** (Object)
- **Updated** (Trigger)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.Extension.SocketCluster.SocketClusterTopicInfo_v2#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "SocketClusterTopicInfo_v2"*
**Docs:** [https://cables.gl/op/Ops.Extension.SocketCluster.SocketClusterTopicInfo_v2](https://cables.gl/op/Ops.Extension.SocketCluster.SocketClusterTopicInfo_v2)

---

