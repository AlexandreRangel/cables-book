# Ops.WebAudio

---

## Ops.WebAudio

### AnalyzerTexture_v2
![AnalyzerTexture_v2 op](images/ops/Ops_WebAudio_AnalyzerTexture_v2.svg)

**Full Name:** `Ops.WebAudio.AnalyzerTexture_v2`

**Description:** Creates a spectrogram texture from an audio FFT array

**`\inputsymbol`{=latex} Input Ports:**

- **Refresh** (Trigger)
- **FFT Array** (Array)
- **Mirror Active** (Number: Boolean)
- **Mirror Width** (Number)
- **Texture Size Index** (Number: Integer)

**`\outputsymbol`{=latex} Output Ports:**

- **Texture Out** (Object)
- **Position** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/edit/T_-vCp)

**Docs:** [https://cables.gl/op/Ops.WebAudio.AnalyzerTexture_v2](https://cables.gl/op/Ops.WebAudio.AnalyzerTexture_v2)

### AudioAnalyzer_v2
![AudioAnalyzer_v2 op](images/ops/Ops_WebAudio_AudioAnalyzer_v2.svg)

**Full Name:** `Ops.WebAudio.AudioAnalyzer_v2`

**Description:** Extracts FFT, RMS & Waveform data from an incoming audio signal

**`\inputsymbol`{=latex} Input Ports:**

- **Trigger In** (Trigger)
- **Audio In** (Object:AudioNode)
- **FFT Size Index** (Number: Integer)
- **Smoothing** (Number)
- **Range** (in dBFS)
- **Min** (Number)
- **Max** (Number)

**`\outputsymbol`{=latex} Output Ports:**

- **Trigger Out** (Trigger)
- **Audio Out** (Object)
- **FFT Array** (Array)
- **Waveform Array** (Array)
- **Frequencies By Index Array** (Array)
- **Array Length** (Number)
- **Average Volume** (Number)
- **Average Volume Time-Domain** (Number)
- **RMS Volume** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/edit/h2eBh-)

**Docs:** [https://cables.gl/op/Ops.WebAudio.AudioAnalyzer_v2](https://cables.gl/op/Ops.WebAudio.AudioAnalyzer_v2)

### AudioBuffer_v3
![AudioBuffer_v3 op](images/ops/Ops_WebAudio_AudioBuffer_v3.svg)

**Full Name:** `Ops.WebAudio.AudioBuffer_v3`

**Description:** Holds an audio file / sample in a buffer

**`\inputsymbol`{=latex} Input Ports:**

- **URL** (String)
- **Create Loading Task** (Number: Boolean)
- **Active** (Number: Boolean)

**`\outputsymbol`{=latex} Output Ports:**

- **Audio Buffer** (Object)
- **Finished Loading** (booleanNumber)
- **Sample Rate** (Number)
- **Length** (Number)
- **Duration** (Number)
- **Number Of Channels** (Number)
- **IsLoading** (booleanNumber)

**Example Patch:** [Open in Editor](https://cables.gl/edit/xEL0rn)

**Docs:** [https://cables.gl/op/Ops.WebAudio.AudioBuffer_v3](https://cables.gl/op/Ops.WebAudio.AudioBuffer_v3)

### AudioBufferChannelRouter
![AudioBufferChannelRouter op](images/ops/Ops_WebAudio_AudioBufferChannelRouter.svg)

**Full Name:** `Ops.WebAudio.AudioBufferChannelRouter`

**Description:** Route audio from one input channel to any output channel

**`\inputsymbol`{=latex} Input Ports:**

- **Audio Buffer** (Object:AudioBuffer)
- **Channel In** (Number: Integer)
- **Channel Out** (Number: Integer)
- **Clear Others** (Number: Boolean)
- **Channel Offset** (Number: Boolean)

**`\outputsymbol`{=latex} Output Ports:**

- **Audio Buffer Out** (Object)
- **Output Channels** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/edit/KlCyYN)

**Docs:** [https://cables.gl/op/Ops.WebAudio.AudioBufferChannelRouter](https://cables.gl/op/Ops.WebAudio.AudioBufferChannelRouter)

### AudioBufferPlayer_v2
![AudioBufferPlayer_v2 op](images/ops/Ops_WebAudio_AudioBufferPlayer_v2.svg)

**Full Name:** `Ops.WebAudio.AudioBufferPlayer_v2`

**Description:** Play back audio data stored in an AudioBuffer

**`\inputsymbol`{=latex} Input Ports:**

- **Audio Buffer** (Object:AudioBuffer)
- **Loop** (Number: Boolean)
- **Restart** (Trigger)
- **Offset** (Number)
- **Playback Rate** (Number)
- **Detune** (Number)

**`\outputsymbol`{=latex} Output Ports:**

- **Audio Out** (Object)
- **Is Playing** (booleanNumber)
- **Loading** (booleanNumber)

**Example Patch:** [Open in Editor](https://cables.gl/edit/5PFIfu)

**Docs:** [https://cables.gl/op/Ops.WebAudio.AudioBufferPlayer_v2](https://cables.gl/op/Ops.WebAudio.AudioBufferPlayer_v2)

### AudioBufferToSplineArray
![AudioBufferToSplineArray op](images/ops/Ops_WebAudio_AudioBufferToSplineArray.svg)

**Full Name:** `Ops.WebAudio.AudioBufferToSplineArray`

**Description:** Outputs the waveform of an audio file as a spline array

**`\inputsymbol`{=latex} Input Ports:**

- **Render** (Trigger)
- **Audio Buffer** (Object:AudioBuffer)
- **Width** (Number)
- **Height** (Number)
- **Samples Per Pixel** (Number: Integer)

**`\outputsymbol`{=latex} Output Ports:**

- **Next** (Trigger)
- **Array Out** (Array)

**Example Patch:** [Open in Editor](https://cables.gl/edit/OcOVBp)

**Docs:** [https://cables.gl/op/Ops.WebAudio.AudioBufferToSplineArray](https://cables.gl/op/Ops.WebAudio.AudioBufferToSplineArray)

### AudioPanner
![AudioPanner op](images/ops/Ops_WebAudio_AudioPanner.svg)

**Full Name:** `Ops.WebAudio.AudioPanner`

**Description:** stereo pan an audio signal from left to right

**`\inputsymbol`{=latex} Input Ports:**

- **Audio In** (Object:AudioNode)
- **Pan** (Number)

**`\outputsymbol`{=latex} Output Ports:**

- **Audio Out** (Object)

**Example Patch:** [Open in Editor](https://cables.gl/edit/iNue_j)

**Docs:** [https://cables.gl/op/Ops.WebAudio.AudioPanner](https://cables.gl/op/Ops.WebAudio.AudioPanner)

### AudioRecorder
![AudioRecorder op](images/ops/Ops_WebAudio_AudioRecorder.svg)

**Full Name:** `Ops.WebAudio.AudioRecorder`

**Description:** record, playback and download audio

**`\inputsymbol`{=latex} Input Ports:**

- **Audio In** (Object:AudioNode)
- **Start Recording** (Trigger)
- **Stop Recording** (Trigger)
- **Input Gain** (Number)
- **Start Playback** (Trigger)
- **Stop Playback** (Trigger)
- **Clear Buffer** (Trigger)
- **Playback Gain** (Number)
- **Loop Playback** (Number: Boolean)

**`\outputsymbol`{=latex} Output Ports:**

- **Audio Out** (Object)
- **Recorded Audio Out** (Object)
- **Is Recording** (booleanNumber)
- **Is Playing Back** (booleanNumber)
- **State** (String)
- **AudioBuffer Out** (Object)
- **Data URL** (String)

**Example Patch:** [Open in Editor](https://cables.gl/edit/nEKhbI)

**Docs:** [https://cables.gl/op/Ops.WebAudio.AudioRecorder](https://cables.gl/op/Ops.WebAudio.AudioRecorder)

### BiquadFilter_v2
![BiquadFilter_v2 op](images/ops/Ops_WebAudio_BiquadFilter_v2.svg)

**Full Name:** `Ops.WebAudio.BiquadFilter_v2`

**Description:** Different kinds of audio filters

**`\inputsymbol`{=latex} Input Ports:**

- **Audio In** (Object:AudioNode)
- **Type Index** (Number: Integer)
- **Frequency** (Number)
- **Q** (Number)
- **Gain** (Number)
- **Detune** (in cents)
- **Frequency Array** (Array)

**`\outputsymbol`{=latex} Output Ports:**

- **Audio Out** (Object)
- **Magnitude Response Array** (Array)
- **Phase Response Array** (Array)
- **Response Arrays Length** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/edit/nhyACp)

**Docs:** [https://cables.gl/op/Ops.WebAudio.BiquadFilter_v2](https://cables.gl/op/Ops.WebAudio.BiquadFilter_v2)

### ClockSequencer
![ClockSequencer op](images/ops/Ops_WebAudio_ClockSequencer.svg)

**Full Name:** `Ops.WebAudio.ClockSequencer`

**Description:** send bpm based triggers like a clocked trigger sequencer / clock divider

**`\inputsymbol`{=latex} Input Ports:**

- **BPM** (Number: Integer)
- **beats per minute** (tempo)
- **Start** (Trigger)
- **Stop** (Trigger)
- **Reset** (Trigger)

**`\outputsymbol`{=latex} Output Ports:**

- **Sequencer Running** (booleanNumber)
- **BPM Out** (Number)
- **Start Out** (Trigger)
- **Stop Out** (Trigger)
- **Reset Out** (Trigger)

**Example Patch:** [Open in Editor](https://cables.gl/edit/J8Uccu)

**Docs:** [https://cables.gl/op/Ops.WebAudio.ClockSequencer](https://cables.gl/op/Ops.WebAudio.ClockSequencer)

### ClockSequencerPattern
![ClockSequencerPattern op](images/ops/Ops_WebAudio_ClockSequencerPattern.svg)

**Full Name:** `Ops.WebAudio.ClockSequencerPattern`

**Description:** sequence triggers by defining a pattern (like a drum machine)

**`\inputsymbol`{=latex} Input Ports:**

- **Clock Trigger Input** (Trigger)
- **Sequence Array** (Array)
- **Steps Index** (Number: Integer)
- **Steps** (Number: String)
- **Reset** (Trigger)

**`\outputsymbol`{=latex} Output Ports:**

- **Sequence Trigger Output** (Trigger)
- **Sequenced Value** (Number)
- **Current Step** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/edit/KM0Dgu)

**Docs:** [https://cables.gl/op/Ops.WebAudio.ClockSequencerPattern](https://cables.gl/op/Ops.WebAudio.ClockSequencerPattern)

### Convolver_v2
![Convolver_v2 op](images/ops/Ops_WebAudio_Convolver_v2.svg)

**Full Name:** `Ops.WebAudio.Convolver_v2`

**Description:** Audio reverb using an impulse response (sample)

**`\inputsymbol`{=latex} Input Ports:**

- **Audio In** (Object:AudioNode)
- **Impulse Response** (String)
- **Normalize** (Number: Boolean)
- **IR Gain** (Number)
- **Output Gain** (Number)

**`\outputsymbol`{=latex} Output Ports:**

- **Audio Out** (Object)
- **Wet Out** (Object)

**Example Patch:** [Open in Editor](https://cables.gl/edit/WlLDwp)

**Docs:** [https://cables.gl/op/Ops.WebAudio.Convolver_v2](https://cables.gl/op/Ops.WebAudio.Convolver_v2)

### CutFilter
![CutFilter op](images/ops/Ops_WebAudio_CutFilter.svg)

**Full Name:** `Ops.WebAudio.CutFilter`

**Description:** dj style filter (lowpass and highpass)

**`\inputsymbol`{=latex} Input Ports:**

- **Audio In** (Object:AudioNode)
- **Highpass Active** (Number: Boolean)
- **Low Frequency** (Number)
- **Low Q** (Number)
- **Lowpass Active** (Number: Boolean)
- **High Frequency** (Number)
- **High Q** (Number)

**`\outputsymbol`{=latex} Output Ports:**

- **Audio Out** (Object)

**Example Patch:** [Open in Editor](https://cables.gl/edit/6SsZxp)

**Docs:** [https://cables.gl/op/Ops.WebAudio.CutFilter](https://cables.gl/op/Ops.WebAudio.CutFilter)

### Delay
![Delay op](images/ops/Ops_WebAudio_Delay.svg)

**Full Name:** `Ops.WebAudio.Delay`

**Description:** add a delay effect to an audio stream

**`\inputsymbol`{=latex} Input Ports:**

- **Audio In** (Object:AudioNode)
- **Feedback** (Number)
- **BPM Based Delay Time** (Number: Boolean)
- **BPM** (Number)
- **Highpass Frequency** (Number)
- **Highpass Q** (Number)
- **Lowpass Frequency** (Number)
- **Lowpass Q** (Number)
- **LFO Intensity** (Number)
- **LFO Waveform Index** (Number: Integer)

**`\outputsymbol`{=latex} Output Ports:**

- **Mix Out** (Object)
- **Wet Out** (Object)

**Example Patch:** [Open in Editor](https://cables.gl/edit/IUjXgu)

**Docs:** [https://cables.gl/op/Ops.WebAudio.Delay](https://cables.gl/op/Ops.WebAudio.Delay)

### FFTAreaAverage_v3
![FFTAreaAverage_v3 op](images/ops/Ops_WebAudio_FFTAreaAverage_v3.svg)

**Full Name:** `Ops.WebAudio.FFTAreaAverage_v3`

**Description:** get average value in an area of a fft audio analysis buffer

**`\inputsymbol`{=latex} Input Ports:**

- **Refresh** (Trigger)
- **FFT Array** (Array)
- **X Position** (Number)
- **Y Position** (Number)
- **Width** (Number)
- **Height** (Number)
- **Create Texture** (Number: Boolean)

**`\outputsymbol`{=latex} Output Ports:**

- **Texture Out** (Object)
- **Area Average Volume** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/edit/F6Fhyp)

**Docs:** [https://cables.gl/op/Ops.WebAudio.FFTAreaAverage_v3](https://cables.gl/op/Ops.WebAudio.FFTAreaAverage_v3)

### Gain
![Gain op](images/ops/Ops_WebAudio_Gain.svg)

**Full Name:** `Ops.WebAudio.Gain`

**Description:** Changes the gain / volume

**`\inputsymbol`{=latex} Input Ports:**

- **Audio In** (Object:AudioNode)
- **Gain** (Number)
- **Mute** (Number: Boolean)

**`\outputsymbol`{=latex} Output Ports:**

- **Audio Out** (Object)

**Example Patch:** [Open in Editor](https://cables.gl/edit/JeKgDp)

**Docs:** [https://cables.gl/op/Ops.WebAudio.Gain](https://cables.gl/op/Ops.WebAudio.Gain)

### KeyPiano
![KeyPiano op](images/ops/Ops_WebAudio_KeyPiano.svg)

**Full Name:** `Ops.WebAudio.KeyPiano`

**Description:** Generates notes based on key presses

**`\inputsymbol`{=latex} Input Ports:**

- **C Note On** (Trigger)
- **C Note Off** (Trigger)
- **Cis Note On** (Trigger)
- **Cis Note Off** (Trigger)
- **D Note On** (Trigger)
- **D Note Off** (Trigger)
- **Dis Note On** (Trigger)
- **Dis Note Off** (Trigger)
- **E Note On** (Trigger)
- **E Note Off** (Trigger)
- **F Note On** (Trigger)
- **F Note Off** (Trigger)
- **Fis Note On** (Trigger)
- **Fis Note Off** (Trigger)
- **G Note On** (Trigger)
- **G Note Off** (Trigger)
- **Gis Note Ons** (Trigger)
- **Gis Note Off** (Trigger)
- **A Note On** (Trigger)
- **A Note Off** (Trigger)
- **Ais Note On** (Trigger)
- **Ais Note Off** (Trigger)
- **B Note On** (Trigger)
- **B Note Off** (Trigger)
- **Octave** (Number)

**`\outputsymbol`{=latex} Output Ports:**

- **Frequency** (Number)
- **Is Pressed** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.WebAudio.KeyPiano#example)

**Docs:** [https://cables.gl/op/Ops.WebAudio.KeyPiano](https://cables.gl/op/Ops.WebAudio.KeyPiano)

### MicrophoneIn_v2
![MicrophoneIn_v2 op](images/ops/Ops_WebAudio_MicrophoneIn_v2.svg)

**Full Name:** `Ops.WebAudio.MicrophoneIn_v2`

**Description:** Access to the microphone and/or audio input devices

**`\inputsymbol`{=latex} Input Ports:**

- **Audio Input Index** (Number: Integer)
- **Volume** (Number)
- **Mute** (Number: Boolean)
- **Start** (Trigger)

**`\outputsymbol`{=latex} Output Ports:**

- **Audio Out** (Object)
- **Listening** (booleanNumber)
- **List Of Input Devices** (Array)

**Example Patch:** [Open in Editor](https://cables.gl/edit/xjHACp)

**Docs:** [https://cables.gl/op/Ops.WebAudio.MicrophoneIn_v2](https://cables.gl/op/Ops.WebAudio.MicrophoneIn_v2)

### MidiValueToFrequency
![MidiValueToFrequency op](images/ops/Ops_WebAudio_MidiValueToFrequency.svg)

**Full Name:** `Ops.WebAudio.MidiValueToFrequency`

**Description:** Converts a midi value to a frequency

**`\inputsymbol`{=latex} Input Ports:**

- **MIDI Value** (Number)
- **Tuning** (Number)

**`\outputsymbol`{=latex} Output Ports:**

- **Frequency** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.WebAudio.MidiValueToFrequency#example)

**Docs:** [https://cables.gl/op/Ops.WebAudio.MidiValueToFrequency](https://cables.gl/op/Ops.WebAudio.MidiValueToFrequency)

### Mixer
![Mixer op](images/ops/Ops_WebAudio_Mixer.svg)

**Full Name:** `Ops.WebAudio.Mixer`

**Description:** Mix audio signals together

**`\inputsymbol`{=latex} Input Ports:**

- **Audio In 0** (Object:AudioNode)
- **Audio In 1** (Object:AudioNode)
- **Audio In 2** (Object:AudioNode)
- **Audio In 3** (Object:AudioNode)
- **Audio In 4** (Object:AudioNode)
- **Audio In 5** (Object:AudioNode)
- **Audio In 6** (Object:AudioNode)
- **Audio In 7** (Object:AudioNode)
- **In 0 Gain** (Number)
- **In 1 Gain** (Number)
- **In 2 Gain** (Number)
- **In 3 Gain** (Number)
- **In 4 Gain** (Number)
- **In 5 Gain** (Number)
- **In 6 Gain** (Number)
- **In 7 Gain** (Number)
- **In 0 Pan** (Number)
- **In 1 Pan** (Number)
- **In 2 Pan** (Number)
- **In 3 Pan** (Number)
- **In 4 Pan** (Number)
- **In 5 Pan** (Number)
- **In 6 Pan** (Number)
- **In 7 Pan** (Number)
- **Output Gain** (Number)

**`\outputsymbol`{=latex} Output Ports:**

- **Audio Out** (Object)

**Example Patch:** [Open in Editor](https://cables.gl/edit/J7YdCp)

**Docs:** [https://cables.gl/op/Ops.WebAudio.Mixer](https://cables.gl/op/Ops.WebAudio.Mixer)

### MusicalScales
![MusicalScales op](images/ops/Ops_WebAudio_MusicalScales.svg)

**Full Name:** `Ops.WebAudio.MusicalScales`

**Description:** Outputs a musical scale array (major, minor, ...) as strings, steps and midi notes

**`\inputsymbol`{=latex} Input Ports:**

- **Root Note Index** (Number: Integer)
- **Root Note** (Number: String)
- **Scale Type Index** (Number: Integer)
- **Scale Type** (Number: String)
- **Include Upper Root Note** (Number: Boolean)
- **Octave** (Number: Integer)
- **the octave of the scale** (only for string & midi note outputs)
- **Append Octave To Names** (Number: Boolean)

**`\outputsymbol`{=latex} Output Ports:**

- **Note Names Array** (Array)
- **Note Step Number Array** (Array)
- **Midi Note Array** (Array)
- **Current Scale** (String)

**Example Patch:** [Open in Editor](https://cables.gl/edit/8Ekchu)

**Docs:** [https://cables.gl/op/Ops.WebAudio.MusicalScales](https://cables.gl/op/Ops.WebAudio.MusicalScales)

### Output_v2
![Output_v2 op](images/ops/Ops_WebAudio_Output_v2.svg)

**Full Name:** `Ops.WebAudio.Output_v2`

**Description:** Sends an audio signal to your speakers

**`\inputsymbol`{=latex} Input Ports:**

- **Audio In** (Object:AudioNode)
- **Volume** (Number)
- **Mute** (Number: Boolean)
- **Show Audio Suspended Button** (Number: Boolean)

**`\outputsymbol`{=latex} Output Ports:**

- **Current Volume** (Number)
- **Number Of Channels** (Number)
- **Context State** (String)

**Example Patch:** [Open in Editor](https://cables.gl/edit/teZhCp)

**Docs:** [https://cables.gl/op/Ops.WebAudio.Output_v2](https://cables.gl/op/Ops.WebAudio.Output_v2)

### ThreeBandEqualizer
![ThreeBandEqualizer op](images/ops/Ops_WebAudio_ThreeBandEqualizer.svg)

**Full Name:** `Ops.WebAudio.ThreeBandEqualizer`

**Description:** 3 filters in one - an eq to quickly process an audio signal

**`\inputsymbol`{=latex} Input Ports:**

- **Audio In** (Object:AudioNode)
- **Low Filter Type Index** (Number: Integer)
- **Low Filter Type** (Number: String)
- **Low Frequency** (Number)
- **Low Q** (Number)
- **Low Gain** (Number)
- **Mid Filter Type Index** (Number: Integer)
- **Mid Filter Type** (Number: String)
- **Mid Frequency** (Number)
- **Mid Q** (Number)
- **Mid Gain** (Number)
- **High Filter Type Index** (Number: Integer)
- **High Filter Type** (Number: String)
- **High Frequency** (Number)
- **High Q** (Number)
- **High Gain** (Number)

**`\outputsymbol`{=latex} Output Ports:**

- **Audio Out** (Object)

**Example Patch:** [Open in Editor](https://cables.gl/edit/tD2Vxp)

**Docs:** [https://cables.gl/op/Ops.WebAudio.ThreeBandEqualizer](https://cables.gl/op/Ops.WebAudio.ThreeBandEqualizer)

### WaveformMesh
![WaveformMesh op](images/ops/Ops_WebAudio_WaveformMesh.svg)

**Full Name:** `Ops.WebAudio.WaveformMesh`

**Description:** Outputs the waveform of an audio file as a geometry

**`\inputsymbol`{=latex} Input Ports:**

- **Render** (Trigger)
- **Audio Buffer** (Object:AudioBuffer)
- **Render Active** (Number: Boolean)
- **Show Bottom Half** (Number: Boolean)
- **Center Origin** (Number: Boolean)
- **Width** (Number)
- **Samples Per Pixel** (Number: Integer)
- **Calculate Tex Coords** (Number: Boolean)

**`\outputsymbol`{=latex} Output Ports:**

- **Spline Points** (Array)
- **Next** (Trigger)
- **Geometry** (Object)

**Example Patch:** [Open in Editor](https://cables.gl/edit/VqDkCp)

**Docs:** [https://cables.gl/op/Ops.WebAudio.WaveformMesh](https://cables.gl/op/Ops.WebAudio.WaveformMesh)

### Waveshaper
![Waveshaper op](images/ops/Ops_WebAudio_Waveshaper.svg)

**Full Name:** `Ops.WebAudio.Waveshaper`

**Description:** add waveshaping (distortion, overdrive, fuzz) to an audio stream

**`\inputsymbol`{=latex} Input Ports:**

- **Audio In** (Object:AudioNode)
- **Oversampling Index** (Number: Integer)
- **Distortion Amount** (Number: Integer)
- **Waveshape Array In** (Array)
- **array input for the waveshaper** (custom distortion transfer function)
- **Output Gain** (Number)

**`\outputsymbol`{=latex} Output Ports:**

- **Audio Out** (Object)
- **Curve Out** (Array)
- **distortion curve array output** (one-dimensional)
- **Curve Length** (Number)

**Example Patch:** [Open in Editor](https://cables.gl/edit/6Vl87I)

**Docs:** [https://cables.gl/op/Ops.WebAudio.Waveshaper](https://cables.gl/op/Ops.WebAudio.Waveshaper)


