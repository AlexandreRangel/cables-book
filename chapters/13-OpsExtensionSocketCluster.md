# Ops.Extension.SocketCluster

*Part of the [All Operators Reference](13-_AllOps.md)*

---

## Ops.Extension.SocketCluster

### SocketClusterClient_v2
![SocketClusterClient_v2 op](images/ops/Ops_Extension_SocketCluster_SocketClusterClient_v2.svg)

**Full Name:** `Ops.Extension.SocketCluster.SocketClusterClient_v2`
**Description:** connect to a socketcluster server and manage the connection

**> Input Ports:**
- **Channel** (String): *See documentation*
- **Server Hostname** (String): *See documentation*
- **Server Port** (Number): *See documentation*
- **Use SSL** (Number: Boolean): *See documentation*
- **enable encryption** (needs to be supported by server): *See documentation*
- **Server Path** (String): *See documentation*
- **Allow Send** (Number: Boolean): *See documentation*
- **Allow Multiple Senders** (Number: Boolean): *See documentation*
- **Additional Serverdata** (Object): *See documentation*
- **additional data send with every message** (can be used for auth-token): *See documentation*
- **Active** (Number: Boolean): *See documentation*

**< Output Ports:**
- **Ready** (booleanNumber): *See documentation*
- **Socket** (Object): *See documentation*
- **Own Client Id** (String): *See documentation*
- **Can Send** (booleanNumber): *See documentation*
- **Error** (String): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/EJvr0a)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "SocketClusterClient_v2"*
**Docs:** [https://cables.gl/op/Ops.Extension.SocketCluster.SocketClusterClient_v2](https://cables.gl/op/Ops.Extension.SocketCluster.SocketClusterClient_v2)

---

### SocketClusterReceiveObject
![SocketClusterReceiveObject op](images/ops/Ops_Extension_SocketCluster_SocketClusterReceiveObject.svg)

**Full Name:** `Ops.Extension.SocketCluster.SocketClusterReceiveObject`
**Description:** Receives object from the socketcluster socket/topic

**> Input Ports:**
- **Socket** (Object:Socketcluster): *See documentation*
- **Topic** (String): *See documentation*
- **Receive Own Data** (Number: Boolean): *See documentation*

**< Output Ports:**
- **Client Id** (String): *See documentation*
- **Data** (Object): *See documentation*
- **Received** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/EJvr0a)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "SocketClusterReceiveObject"*
**Docs:** [https://cables.gl/op/Ops.Extension.SocketCluster.SocketClusterReceiveObject](https://cables.gl/op/Ops.Extension.SocketCluster.SocketClusterReceiveObject)

---

### SocketClusterReceiveTrigger
![SocketClusterReceiveTrigger op](images/ops/Ops_Extension_SocketCluster_SocketClusterReceiveTrigger.svg)

**Full Name:** `Ops.Extension.SocketCluster.SocketClusterReceiveTrigger`
**Description:** Receives trigger from the socketcluster socket/topic

**> Input Ports:**
- **Socket** (Object:Socketcluster): *See documentation*
- **Topic** (String): *See documentation*
- **Receive Own Data** (Number: Boolean): *See documentation*
- **Use Named Trigger** (Number: Boolean): *See documentation*

**< Output Ports:**
- **Client Id** (String): *See documentation*
- **Trigger Name** (String): *See documentation*
- **Received** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/mecjP3)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "SocketClusterReceiveTrigger"*
**Docs:** [https://cables.gl/op/Ops.Extension.SocketCluster.SocketClusterReceiveTrigger](https://cables.gl/op/Ops.Extension.SocketCluster.SocketClusterReceiveTrigger)

---

### SocketClusterSendObject
![SocketClusterSendObject op](images/ops/Ops_Extension_SocketCluster_SocketClusterSendObject.svg)

**Full Name:** `Ops.Extension.SocketCluster.SocketClusterSendObject`
**Description:** sends an object via socketcluster/websocket

**> Input Ports:**
- **Socket** (Object:Socketcluster): *See documentation*
- **Topic** (String): *See documentation*
- **Data** (Object): *See documentation*
- **Send** (Trigger): *See documentation*

**< Output Ports:**
- **Sent Data** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/EJvr0a)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "SocketClusterSendObject"*
**Docs:** [https://cables.gl/op/Ops.Extension.SocketCluster.SocketClusterSendObject](https://cables.gl/op/Ops.Extension.SocketCluster.SocketClusterSendObject)

---

### SocketClusterSendTrigger
![SocketClusterSendTrigger op](images/ops/Ops_Extension_SocketCluster_SocketClusterSendTrigger.svg)

**Full Name:** `Ops.Extension.SocketCluster.SocketClusterSendTrigger`
**Description:** sends a trigger via socketcluster/websocket

**> Input Ports:**
- **Data** (Trigger): *See documentation*
- **Socket** (Object:Socketcluster): *See documentation*
- **Topic** (String): *See documentation*
- **Trigger Name** (String): *See documentation*
- **the name of the trigger** (created with TriggerSend): *See documentation*

**< Output Ports:**
- *Visit [Ops.Extension.SocketCluster.SocketClusterSendTrigger documentation](https://cables.gl/op/Ops.Extension.SocketCluster.SocketClusterSendTrigger) for output port details*

**Example Patch:** [Open in Editor](https://cables.gl/edit/mecjP3)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "SocketClusterSendTrigger"*
**Docs:** [https://cables.gl/op/Ops.Extension.SocketCluster.SocketClusterSendTrigger](https://cables.gl/op/Ops.Extension.SocketCluster.SocketClusterSendTrigger)

---

### SocketClusterTopicInfo_v2
![SocketClusterTopicInfo_v2 op](images/ops/Ops_Extension_SocketCluster_SocketClusterTopicInfo_v2.svg)

**Full Name:** `Ops.Extension.SocketCluster.SocketClusterTopicInfo_v2`
**Description:** get info for clients listening on a socketcluster topic

**> Input Ports:**
- **Socket** (Object:Socketcluster): *See documentation*
- **Topic** (String): *See documentation*
- **Timeout Seconds** (Number: Integer): *See documentation*
- **Soft Timeout Seconds** (Number: Integer): *See documentation*
- **Retain Messages** (Number: Integer): *See documentation*
- **Update** (Trigger): *See documentation*
- **Receive My Data** (Number: Boolean): *See documentation*

**< Output Ports:**
- **Active Clients** (Array): *See documentation*
- **Will Time Out** (Object): *See documentation*
- **Timed Out Clients** (Array): *See documentation*
- **Messages** (Object): *See documentation*
- **Updated** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/EJvr0a)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "SocketClusterTopicInfo_v2"*
**Docs:** [https://cables.gl/op/Ops.Extension.SocketCluster.SocketClusterTopicInfo_v2](https://cables.gl/op/Ops.Extension.SocketCluster.SocketClusterTopicInfo_v2)

---

