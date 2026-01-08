# Ops.Extension.Osc2Ws


```{=latex}
\OpsSubsubNoSubsectionNumbering\setcounter{subsubsection}{0}
```
### Osc2WsArray
![Osc2WsArray op](images/ops/Ops_Extension_Osc2Ws_Osc2WsArray.svg)

**Full Name:** `Ops.Extension.Osc2Ws.Osc2WsArray`

Outputs an array of data from a user defined OSC address.

**`\inputsymbol`{=latex} Inputs**

- **Message** (Object)
- **Address** (String)
- **Learn** (Trigger)

**`\outputsymbol`{=latex} Output**

- **Result Message** (Object)
- **Array Out** (Array)
- **Array Length** (Number)
- **Received** (Trigger)

**Example Patch:** [cables.gl/edit/F77YvQ](https://cables.gl/edit/F77YvQ)

**Doc:** [cables.gl/op/Ops.Extension.Osc2Ws.Osc2WsArray](https://cables.gl/op/Ops.Extension.Osc2Ws.Osc2WsArray)

### Osc2WsMessage
![Osc2WsMessage op](images/ops/Ops_Extension_Osc2Ws_Osc2WsMessage.svg)

**Full Name:** `Ops.Extension.Osc2Ws.Osc2WsMessage`

Shows the current active address of an incoming OSC message.

**`\inputsymbol`{=latex} Inputs**

- **Message** (Object)

**`\outputsymbol`{=latex} Output**

- **Adress** (String)
- **Arguments** (Array)
- **Total Arguments** (Number)

**Example Patch:** [cables.gl/edit/F77YvQ](https://cables.gl/edit/F77YvQ)

**Doc:** [cables.gl/op/Ops.Extension.Osc2Ws.Osc2WsMessage](https://cables.gl/op/Ops.Extension.Osc2Ws.Osc2WsMessage)

### Osc2WsNumber
![Osc2WsNumber op](images/ops/Ops_Extension_Osc2Ws_Osc2WsNumber.svg)

**Full Name:** `Ops.Extension.Osc2Ws.Osc2WsNumber`

Outputs a single number from a user defined OSC address.

**`\inputsymbol`{=latex} Inputs**

- **Message** (Object)
- **Address** (String)
- **Learn** (Trigger)

**`\outputsymbol`{=latex} Output**

- **Result Message** (Object)
- **Value** (Number)
- **Received** (Trigger)

**Example Patch:** [cables.gl/edit/F77YvQ](https://cables.gl/edit/F77YvQ)

**Doc:** [cables.gl/op/Ops.Extension.Osc2Ws.Osc2WsNumber](https://cables.gl/op/Ops.Extension.Osc2Ws.Osc2WsNumber)

### Osc2WsNumbers
![Osc2WsNumbers op](images/ops/Ops_Extension_Osc2Ws_Osc2WsNumbers.svg)

**Full Name:** `Ops.Extension.Osc2Ws.Osc2WsNumbers`

Outputs up to 4 numbers from a user defined OSC address.

**`\inputsymbol`{=latex} Inputs**

- **Message In** (Object)
- **Osc Address** (String)
- **Learn** (Trigger)

**`\outputsymbol`{=latex} Output**

- **Message Through** (Object)
- **Received** (Trigger)
- **Number 0** (Number)
- **Number 1** (Number)
- **Number 2** (Number)
- **Number 3** (Number)

**Example Patch:** [cables.gl/edit/F77YvQ](https://cables.gl/edit/F77YvQ)

**Doc:** [cables.gl/op/Ops.Extension.Osc2Ws.Osc2WsNumbers](https://cables.gl/op/Ops.Extension.Osc2Ws.Osc2WsNumbers)


