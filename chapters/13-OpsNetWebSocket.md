# Ops.Net.WebSocket

---

```{=latex}
\stepcounter{subsection}\setcounter{subsubsection}{0}
```
### WebSocket_v2
![WebSocket_v2 op](images/ops/Ops_Net_WebSocket_WebSocket_v2.svg)

**Full Name:** `Ops.Net.WebSocket.WebSocket_v2`

**Description:** Create a websocket connection and receive data from it

**`\inputsymbol`{=latex} Inputs**

- **URL** (String)

**`\outputsymbol`{=latex} Output**

- **Result** (Object)
- **Valid JSON** (booleanNumber)
- **Connection** (Object)
- **Connected** (booleanNumber)
- **Received Data** (Trigger)
- **Raw Data** (String)

**Example Patch:** [Open in Editor](https://cables.gl/edit/gu7DBo)

**Docs:** [https://cables.gl/op/Ops.Net.WebSocket.WebSocket_v2](https://cables.gl/op/Ops.Net.WebSocket.WebSocket_v2)

### WebSocketSend
![WebSocketSend op](images/ops/Ops_Net_WebSocket_WebSocketSend.svg)

**Full Name:** `Ops.Net.WebSocket.WebSocketSend`

**Description:** send an object to a websocket connection

**`\inputsymbol`{=latex} Inputs**

- **Connection** (Object:Websocket)
- **Object** (Object)
- **Send** (Trigger)
- **Send String** (Number: Boolean)

**`\outputsymbol`{=latex} Output**

- **Sent** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/edit/gu7DBo)

**Docs:** [https://cables.gl/op/Ops.Net.WebSocket.WebSocketSend](https://cables.gl/op/Ops.Net.WebSocket.WebSocketSend)


