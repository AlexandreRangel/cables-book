# Ops.WebAudio

*Part of the [All Operators Reference](13-_AllOps.md)*

---

## Ops.WebAudio

### AnalyzerTexture_v2
![AnalyzerTexture_v2 op](images/ops/Ops_WebAudio_AnalyzerTexture_v2.svg)

**Full Name:** `Ops.WebAudio.AnalyzerTexture_v2`
**Description:** Creates a spectrogram texture from an audio FFT array

**> Input Ports:**
- **Refresh** (Trigger): *See documentation*
- **FFT Array** (Array): *See documentation*
- **Mirror Active** (Number: Boolean): *See documentation*
- **Mirror Width** (Number): *See documentation*
- **Texture Size Index** (Number: Integer): *See documentation*

**< Output Ports:**
- **Texture Out** (Object): *See documentation*
- **Position** (Number): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/T_-vCp)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "AnalyzerTexture_v2"*
**Docs:** [https://cables.gl/op/Ops.WebAudio.AnalyzerTexture_v2](https://cables.gl/op/Ops.WebAudio.AnalyzerTexture_v2)

---

### AudioAnalyzer_v2
![AudioAnalyzer_v2 op](images/ops/Ops_WebAudio_AudioAnalyzer_v2.svg)

**Full Name:** `Ops.WebAudio.AudioAnalyzer_v2`
**Description:** Extracts FFT, RMS & Waveform data from an incoming audio signal

**> Input Ports:**
- **Trigger In** (Trigger): *See documentation*
- **Audio In** (Object:AudioNode): *See documentation*
- **FFT Size Index** (Number: Integer): *See documentation*
- **Smoothing** (Number): *See documentation*
- **Range** (in dBFS): *See documentation*
- **Min** (Number): *See documentation*
- **Max** (Number): *See documentation*

**< Output Ports:**
- **Trigger Out** (Trigger): *See documentation*
- **Audio Out** (Object): *See documentation*
- **FFT Array** (Array): *See documentation*
- **Waveform Array** (Array): *See documentation*
- **Frequencies By Index Array** (Array): *See documentation*
- **Array Length** (Number): *See documentation*
- **Average Volume** (Number): *See documentation*
- **Average Volume Time-Domain** (Number): *See documentation*
- **RMS Volume** (Number): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/h2eBh-)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "AudioAnalyzer_v2"*
**Docs:** [https://cables.gl/op/Ops.WebAudio.AudioAnalyzer_v2](https://cables.gl/op/Ops.WebAudio.AudioAnalyzer_v2)

---

### AudioBuffer_v3
![AudioBuffer_v3 op](images/ops/Ops_WebAudio_AudioBuffer_v3.svg)

**Full Name:** `Ops.WebAudio.AudioBuffer_v3`
**Description:** Holds an audio file / sample in a buffer

**> Input Ports:**
- **URL** (String): *See documentation*
- **Create Loading Task** (Number: Boolean): *See documentation*
- **Active** (Number: Boolean): *See documentation*

**< Output Ports:**
- **Audio Buffer** (Object): *See documentation*
- **Finished Loading** (booleanNumber): *See documentation*
- **Sample Rate** (Number): *See documentation*
- **Length** (Number): *See documentation*
- **Duration** (Number): *See documentation*
- **Number Of Channels** (Number): *See documentation*
- **IsLoading** (booleanNumber): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/xEL0rn)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "AudioBuffer_v3"*
**Docs:** [https://cables.gl/op/Ops.WebAudio.AudioBuffer_v3](https://cables.gl/op/Ops.WebAudio.AudioBuffer_v3)

---

### AudioBufferChannelRouter
![AudioBufferChannelRouter op](images/ops/Ops_WebAudio_AudioBufferChannelRouter.svg)

**Full Name:** `Ops.WebAudio.AudioBufferChannelRouter`
**Description:** Route audio from one input channel to any output channel

**> Input Ports:**
- **Audio Buffer** (Object:AudioBuffer): *See documentation*
- **Channel In** (Number: Integer): *See documentation*
- **Channel Out** (Number: Integer): *See documentation*
- **Clear Others** (Number: Boolean): *See documentation*
- **Channel Offset** (Number: Boolean): *See documentation*

**< Output Ports:**
- **Audio Buffer Out** (Object): *See documentation*
- **Output Channels** (Number): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/KlCyYN)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "AudioBufferChannelRouter"*
**Docs:** [https://cables.gl/op/Ops.WebAudio.AudioBufferChannelRouter](https://cables.gl/op/Ops.WebAudio.AudioBufferChannelRouter)

---

### AudioBufferPlayer_v2
![AudioBufferPlayer_v2 op](images/ops/Ops_WebAudio_AudioBufferPlayer_v2.svg)

**Full Name:** `Ops.WebAudio.AudioBufferPlayer_v2`
**Description:** Play back audio data stored in an AudioBuffer

**> Input Ports:**
- **Audio Buffer** (Object:AudioBuffer): *See documentation*
- **Loop** (Number: Boolean): *See documentation*
- **Restart** (Trigger): *See documentation*
- **Offset** (Number): *See documentation*
- **Playback Rate** (Number): *See documentation*
- **Detune** (Number): *See documentation*

**< Output Ports:**
- **Audio Out** (Object): *See documentation*
- **Is Playing** (booleanNumber): *See documentation*
- **Loading** (booleanNumber): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/5PFIfu)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "AudioBufferPlayer_v2"*
**Docs:** [https://cables.gl/op/Ops.WebAudio.AudioBufferPlayer_v2](https://cables.gl/op/Ops.WebAudio.AudioBufferPlayer_v2)

---

### AudioBufferToSplineArray
![AudioBufferToSplineArray op](images/ops/Ops_WebAudio_AudioBufferToSplineArray.svg)

**Full Name:** `Ops.WebAudio.AudioBufferToSplineArray`
**Description:** Outputs the waveform of an audio file as a spline array

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Audio Buffer** (Object:AudioBuffer): *See documentation*
- **Width** (Number): *See documentation*
- **Height** (Number): *See documentation*
- **Samples Per Pixel** (Number: Integer): *See documentation*

**< Output Ports:**
- **Next** (Trigger): *See documentation*
- **Array Out** (Array): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/OcOVBp)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "AudioBufferToSplineArray"*
**Docs:** [https://cables.gl/op/Ops.WebAudio.AudioBufferToSplineArray](https://cables.gl/op/Ops.WebAudio.AudioBufferToSplineArray)

---

### AudioPanner
![AudioPanner op](images/ops/Ops_WebAudio_AudioPanner.svg)

**Full Name:** `Ops.WebAudio.AudioPanner`
**Description:** stereo pan an audio signal from left to right

**> Input Ports:**
- **Audio In** (Object:AudioNode): *See documentation*
- **Pan** (Number): *See documentation*

**< Output Ports:**
- **Audio Out** (Object): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/iNue_j)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "AudioPanner"*
**Docs:** [https://cables.gl/op/Ops.WebAudio.AudioPanner](https://cables.gl/op/Ops.WebAudio.AudioPanner)

---

### AudioRecorder
![AudioRecorder op](images/ops/Ops_WebAudio_AudioRecorder.svg)

**Full Name:** `Ops.WebAudio.AudioRecorder`
**Description:** record, playback and download audio

**> Input Ports:**
- **Audio In** (Object:AudioNode): *See documentation*
- **Start Recording** (Trigger): *See documentation*
- **Stop Recording** (Trigger): *See documentation*
- **Input Gain** (Number): *See documentation*
- **Start Playback** (Trigger): *See documentation*
- **Stop Playback** (Trigger): *See documentation*
- **Clear Buffer** (Trigger): *See documentation*
- **Playback Gain** (Number): *See documentation*
- **Loop Playback** (Number: Boolean): *See documentation*

**< Output Ports:**
- **Audio Out** (Object): *See documentation*
- **Recorded Audio Out** (Object): *See documentation*
- **Is Recording** (booleanNumber): *See documentation*
- **Is Playing Back** (booleanNumber): *See documentation*
- **State** (String): *See documentation*
- **AudioBuffer Out** (Object): *See documentation*
- **Data URL** (String): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/nEKhbI)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "AudioRecorder"*
**Docs:** [https://cables.gl/op/Ops.WebAudio.AudioRecorder](https://cables.gl/op/Ops.WebAudio.AudioRecorder)

---

### BiquadFilter_v2
![BiquadFilter_v2 op](images/ops/Ops_WebAudio_BiquadFilter_v2.svg)

**Full Name:** `Ops.WebAudio.BiquadFilter_v2`
**Description:** Different kinds of audio filters

**> Input Ports:**
- **Audio In** (Object:AudioNode): *See documentation*
- **Type Index** (Number: Integer): *See documentation*
- **Frequency** (Number): *See documentation*
- **Q** (Number): *See documentation*
- **Gain** (Number): *See documentation*
- **Detune** (in cents): *See documentation*
- **Frequency Array** (Array): *See documentation*

**< Output Ports:**
- **Audio Out** (Object): *See documentation*
- **Magnitude Response Array** (Array): *See documentation*
- **Phase Response Array** (Array): *See documentation*
- **Response Arrays Length** (Number): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/nhyACp)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "BiquadFilter_v2"*
**Docs:** [https://cables.gl/op/Ops.WebAudio.BiquadFilter_v2](https://cables.gl/op/Ops.WebAudio.BiquadFilter_v2)

---

### ClockSequencer
![ClockSequencer op](images/ops/Ops_WebAudio_ClockSequencer.svg)

**Full Name:** `Ops.WebAudio.ClockSequencer`
**Description:** send bpm based triggers like a clocked trigger sequencer / clock divider

**> Input Ports:**
- **BPM** (Number: Integer): *See documentation*
- **beats per minute** (tempo): *See documentation*
- **Start** (Trigger): *See documentation*
- **Stop** (Trigger): *See documentation*
- **Reset** (Trigger): *See documentation*

**< Output Ports:**
- **Sequencer Running** (booleanNumber): *See documentation*
- **BPM Out** (Number): *See documentation*
- **Start Out** (Trigger): *See documentation*
- **Stop Out** (Trigger): *See documentation*
- **Reset Out** (Trigger): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/J8Uccu)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ClockSequencer"*
**Docs:** [https://cables.gl/op/Ops.WebAudio.ClockSequencer](https://cables.gl/op/Ops.WebAudio.ClockSequencer)

---

### ClockSequencerPattern
![ClockSequencerPattern op](images/ops/Ops_WebAudio_ClockSequencerPattern.svg)

**Full Name:** `Ops.WebAudio.ClockSequencerPattern`
**Description:** sequence triggers by defining a pattern (like a drum machine)

**> Input Ports:**
- **Clock Trigger Input** (Trigger): *See documentation*
- **Sequence Array** (Array): *See documentation*
- **Steps Index** (Number: Integer): *See documentation*
- **Steps** (Number: String): *See documentation*
- **Reset** (Trigger): *See documentation*

**< Output Ports:**
- **Sequence Trigger Output** (Trigger): *See documentation*
- **Sequenced Value** (Number): *See documentation*
- **Current Step** (Number): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/KM0Dgu)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ClockSequencerPattern"*
**Docs:** [https://cables.gl/op/Ops.WebAudio.ClockSequencerPattern](https://cables.gl/op/Ops.WebAudio.ClockSequencerPattern)

---

### Convolver_v2
![Convolver_v2 op](images/ops/Ops_WebAudio_Convolver_v2.svg)

**Full Name:** `Ops.WebAudio.Convolver_v2`
**Description:** Audio reverb using an impulse response (sample)

**> Input Ports:**
- **Audio In** (Object:AudioNode): *See documentation*
- **Impulse Response** (String): *See documentation*
- **Normalize** (Number: Boolean): *See documentation*
- **IR Gain** (Number): *See documentation*
- **Output Gain** (Number): *See documentation*

**< Output Ports:**
- **Audio Out** (Object): *See documentation*
- **Wet Out** (Object): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/WlLDwp)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "Convolver_v2"*
**Docs:** [https://cables.gl/op/Ops.WebAudio.Convolver_v2](https://cables.gl/op/Ops.WebAudio.Convolver_v2)

---

### CutFilter
![CutFilter op](images/ops/Ops_WebAudio_CutFilter.svg)

**Full Name:** `Ops.WebAudio.CutFilter`
**Description:** dj style filter (lowpass and highpass)

**> Input Ports:**
- **Audio In** (Object:AudioNode): *See documentation*
- **Highpass Active** (Number: Boolean): *See documentation*
- **Low Frequency** (Number): *See documentation*
- **Low Q** (Number): *See documentation*
- **Lowpass Active** (Number: Boolean): *See documentation*
- **High Frequency** (Number): *See documentation*
- **High Q** (Number): *See documentation*

**< Output Ports:**
- **Audio Out** (Object): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/6SsZxp)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "CutFilter"*
**Docs:** [https://cables.gl/op/Ops.WebAudio.CutFilter](https://cables.gl/op/Ops.WebAudio.CutFilter)

---

### Delay
![Delay op](images/ops/Ops_WebAudio_Delay.svg)

**Full Name:** `Ops.WebAudio.Delay`
**Description:** add a delay effect to an audio stream

**> Input Ports:**
- **Audio In** (Object:AudioNode): *See documentation*
- **Feedback** (Number): *See documentation*
- **BPM Based Delay Time** (Number: Boolean): *See documentation*
- **BPM** (Number): *See documentation*
- **Highpass Frequency** (Number): *See documentation*
- **Highpass Q** (Number): *See documentation*
- **Lowpass Frequency** (Number): *See documentation*
- **Lowpass Q** (Number): *See documentation*
- **LFO Intensity** (Number): *See documentation*
- **LFO Waveform Index** (Number: Integer): *See documentation*

**< Output Ports:**
- **Mix Out** (Object): *See documentation*
- **Wet Out** (Object): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/IUjXgu)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "Delay"*
**Docs:** [https://cables.gl/op/Ops.WebAudio.Delay](https://cables.gl/op/Ops.WebAudio.Delay)

---

### FFTAreaAverage_v3
![FFTAreaAverage_v3 op](images/ops/Ops_WebAudio_FFTAreaAverage_v3.svg)

**Full Name:** `Ops.WebAudio.FFTAreaAverage_v3`
**Description:** get average value in an area of a fft audio analysis buffer

**> Input Ports:**
- **Refresh** (Trigger): *See documentation*
- **FFT Array** (Array): *See documentation*
- **X Position** (Number): *See documentation*
- **Y Position** (Number): *See documentation*
- **Width** (Number): *See documentation*
- **Height** (Number): *See documentation*
- **Create Texture** (Number: Boolean): *See documentation*

**< Output Ports:**
- **Texture Out** (Object): *See documentation*
- **Area Average Volume** (Number): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/F6Fhyp)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "FFTAreaAverage_v3"*
**Docs:** [https://cables.gl/op/Ops.WebAudio.FFTAreaAverage_v3](https://cables.gl/op/Ops.WebAudio.FFTAreaAverage_v3)

---

### Gain
![Gain op](images/ops/Ops_WebAudio_Gain.svg)

**Full Name:** `Ops.WebAudio.Gain`
**Description:** Changes the gain / volume

**> Input Ports:**
- **Audio In** (Object:AudioNode): *See documentation*
- **Gain** (Number): *See documentation*
- **Mute** (Number: Boolean): *See documentation*

**< Output Ports:**
- **Audio Out** (Object): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/JeKgDp)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "Gain"*
**Docs:** [https://cables.gl/op/Ops.WebAudio.Gain](https://cables.gl/op/Ops.WebAudio.Gain)

---

### KeyPiano
![KeyPiano op](images/ops/Ops_WebAudio_KeyPiano.svg)

**Full Name:** `Ops.WebAudio.KeyPiano`
**Description:** Generates notes based on key presses

**> Input Ports:**
- **C Note On** (Trigger): *See documentation*
- **C Note Off** (Trigger): *See documentation*
- **Cis Note On** (Trigger): *See documentation*
- **Cis Note Off** (Trigger): *See documentation*
- **D Note On** (Trigger): *See documentation*
- **D Note Off** (Trigger): *See documentation*
- **Dis Note On** (Trigger): *See documentation*
- **Dis Note Off** (Trigger): *See documentation*
- **E Note On** (Trigger): *See documentation*
- **E Note Off** (Trigger): *See documentation*
- **F Note On** (Trigger): *See documentation*
- **F Note Off** (Trigger): *See documentation*
- **Fis Note On** (Trigger): *See documentation*
- **Fis Note Off** (Trigger): *See documentation*
- **G Note On** (Trigger): *See documentation*
- **G Note Off** (Trigger): *See documentation*
- **Gis Note Ons** (Trigger): *See documentation*
- **Gis Note Off** (Trigger): *See documentation*
- **A Note On** (Trigger): *See documentation*
- **A Note Off** (Trigger): *See documentation*
- **Ais Note On** (Trigger): *See documentation*
- **Ais Note Off** (Trigger): *See documentation*
- **B Note On** (Trigger): *See documentation*
- **B Note Off** (Trigger): *See documentation*
- **Octave** (Number): *See documentation*

**< Output Ports:**
- **Frequency** (Number): *See documentation*
- **Is Pressed** (Number): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.WebAudio.KeyPiano#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "KeyPiano"*
**Docs:** [https://cables.gl/op/Ops.WebAudio.KeyPiano](https://cables.gl/op/Ops.WebAudio.KeyPiano)

---

### MicrophoneIn_v2
![MicrophoneIn_v2 op](images/ops/Ops_WebAudio_MicrophoneIn_v2.svg)

**Full Name:** `Ops.WebAudio.MicrophoneIn_v2`
**Description:** Access to the microphone and/or audio input devices

**> Input Ports:**
- **Audio Input Index** (Number: Integer): *See documentation*
- **Volume** (Number): *See documentation*
- **Mute** (Number: Boolean): *See documentation*
- **Start** (Trigger): *See documentation*

**< Output Ports:**
- **Audio Out** (Object): *See documentation*
- **Listening** (booleanNumber): *See documentation*
- **List Of Input Devices** (Array): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/xjHACp)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "MicrophoneIn_v2"*
**Docs:** [https://cables.gl/op/Ops.WebAudio.MicrophoneIn_v2](https://cables.gl/op/Ops.WebAudio.MicrophoneIn_v2)

---

### MidiValueToFrequency
![MidiValueToFrequency op](images/ops/Ops_WebAudio_MidiValueToFrequency.svg)

**Full Name:** `Ops.WebAudio.MidiValueToFrequency`
**Description:** Converts a midi value to a frequency

**> Input Ports:**
- **MIDI Value** (Number): *See documentation*
- **Tuning** (Number): *See documentation*

**< Output Ports:**
- **Frequency** (Number): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/op/Ops.WebAudio.MidiValueToFrequency#example)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "MidiValueToFrequency"*
**Docs:** [https://cables.gl/op/Ops.WebAudio.MidiValueToFrequency](https://cables.gl/op/Ops.WebAudio.MidiValueToFrequency)

---

### Mixer
![Mixer op](images/ops/Ops_WebAudio_Mixer.svg)

**Full Name:** `Ops.WebAudio.Mixer`
**Description:** Mix audio signals together

**> Input Ports:**
- **Audio In 0** (Object:AudioNode): *See documentation*
- **Audio In 1** (Object:AudioNode): *See documentation*
- **Audio In 2** (Object:AudioNode): *See documentation*
- **Audio In 3** (Object:AudioNode): *See documentation*
- **Audio In 4** (Object:AudioNode): *See documentation*
- **Audio In 5** (Object:AudioNode): *See documentation*
- **Audio In 6** (Object:AudioNode): *See documentation*
- **Audio In 7** (Object:AudioNode): *See documentation*
- **In 0 Gain** (Number): *See documentation*
- **In 1 Gain** (Number): *See documentation*
- **In 2 Gain** (Number): *See documentation*
- **In 3 Gain** (Number): *See documentation*
- **In 4 Gain** (Number): *See documentation*
- **In 5 Gain** (Number): *See documentation*
- **In 6 Gain** (Number): *See documentation*
- **In 7 Gain** (Number): *See documentation*
- **In 0 Pan** (Number): *See documentation*
- **In 1 Pan** (Number): *See documentation*
- **In 2 Pan** (Number): *See documentation*
- **In 3 Pan** (Number): *See documentation*
- **In 4 Pan** (Number): *See documentation*
- **In 5 Pan** (Number): *See documentation*
- **In 6 Pan** (Number): *See documentation*
- **In 7 Pan** (Number): *See documentation*
- **Output Gain** (Number): *See documentation*

**< Output Ports:**
- **Audio Out** (Object): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/J7YdCp)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "Mixer"*
**Docs:** [https://cables.gl/op/Ops.WebAudio.Mixer](https://cables.gl/op/Ops.WebAudio.Mixer)

---

### MusicalScales
![MusicalScales op](images/ops/Ops_WebAudio_MusicalScales.svg)

**Full Name:** `Ops.WebAudio.MusicalScales`
**Description:** Outputs a musical scale array (major, minor, ...) as strings, steps and midi notes

**> Input Ports:**
- **Root Note Index** (Number: Integer): *See documentation*
- **Root Note** (Number: String): *See documentation*
- **Scale Type Index** (Number: Integer): *See documentation*
- **Scale Type** (Number: String): *See documentation*
- **Include Upper Root Note** (Number: Boolean): *See documentation*
- **Octave** (Number: Integer): *See documentation*
- **the octave of the scale** (only for string & midi note outputs): *See documentation*
- **Append Octave To Names** (Number: Boolean): *See documentation*

**< Output Ports:**
- **Note Names Array** (Array): *See documentation*
- **Note Step Number Array** (Array): *See documentation*
- **Midi Note Array** (Array): *See documentation*
- **Current Scale** (String): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/8Ekchu)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "MusicalScales"*
**Docs:** [https://cables.gl/op/Ops.WebAudio.MusicalScales](https://cables.gl/op/Ops.WebAudio.MusicalScales)

---

### Output_v2
![Output_v2 op](images/ops/Ops_WebAudio_Output_v2.svg)

**Full Name:** `Ops.WebAudio.Output_v2`
**Description:** Sends an audio signal to your speakers

**> Input Ports:**
- **Audio In** (Object:AudioNode): *See documentation*
- **Volume** (Number): *See documentation*
- **Mute** (Number: Boolean): *See documentation*
- **Show Audio Suspended Button** (Number: Boolean): *See documentation*

**< Output Ports:**
- **Current Volume** (Number): *See documentation*
- **Number Of Channels** (Number): *See documentation*
- **Context State** (String): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/teZhCp)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "Output_v2"*
**Docs:** [https://cables.gl/op/Ops.WebAudio.Output_v2](https://cables.gl/op/Ops.WebAudio.Output_v2)

---

### ThreeBandEqualizer
![ThreeBandEqualizer op](images/ops/Ops_WebAudio_ThreeBandEqualizer.svg)

**Full Name:** `Ops.WebAudio.ThreeBandEqualizer`
**Description:** 3 filters in one - an eq to quickly process an audio signal

**> Input Ports:**
- **Audio In** (Object:AudioNode): *See documentation*
- **Low Filter Type Index** (Number: Integer): *See documentation*
- **Low Filter Type** (Number: String): *See documentation*
- **Low Frequency** (Number): *See documentation*
- **Low Q** (Number): *See documentation*
- **Low Gain** (Number): *See documentation*
- **Mid Filter Type Index** (Number: Integer): *See documentation*
- **Mid Filter Type** (Number: String): *See documentation*
- **Mid Frequency** (Number): *See documentation*
- **Mid Q** (Number): *See documentation*
- **Mid Gain** (Number): *See documentation*
- **High Filter Type Index** (Number: Integer): *See documentation*
- **High Filter Type** (Number: String): *See documentation*
- **High Frequency** (Number): *See documentation*
- **High Q** (Number): *See documentation*
- **High Gain** (Number): *See documentation*

**< Output Ports:**
- **Audio Out** (Object): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/tD2Vxp)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "ThreeBandEqualizer"*
**Docs:** [https://cables.gl/op/Ops.WebAudio.ThreeBandEqualizer](https://cables.gl/op/Ops.WebAudio.ThreeBandEqualizer)

---

### WaveformMesh
![WaveformMesh op](images/ops/Ops_WebAudio_WaveformMesh.svg)

**Full Name:** `Ops.WebAudio.WaveformMesh`
**Description:** Outputs the waveform of an audio file as a geometry

**> Input Ports:**
- **Render** (Trigger): *See documentation*
- **Audio Buffer** (Object:AudioBuffer): *See documentation*
- **Render Active** (Number: Boolean): *See documentation*
- **Show Bottom Half** (Number: Boolean): *See documentation*
- **Center Origin** (Number: Boolean): *See documentation*
- **Width** (Number): *See documentation*
- **Samples Per Pixel** (Number: Integer): *See documentation*
- **Calculate Tex Coords** (Number: Boolean): *See documentation*

**< Output Ports:**
- **Spline Points** (Array): *See documentation*
- **Next** (Trigger): *See documentation*
- **Geometry** (Object): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/VqDkCp)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "WaveformMesh"*
**Docs:** [https://cables.gl/op/Ops.WebAudio.WaveformMesh](https://cables.gl/op/Ops.WebAudio.WaveformMesh)

---

### Waveshaper
![Waveshaper op](images/ops/Ops_WebAudio_Waveshaper.svg)

**Full Name:** `Ops.WebAudio.Waveshaper`
**Description:** add waveshaping (distortion, overdrive, fuzz) to an audio stream

**> Input Ports:**
- **Audio In** (Object:AudioNode): *See documentation*
- **Oversampling Index** (Number: Integer): *See documentation*
- **Distortion Amount** (Number: Integer): *See documentation*
- **Waveshape Array In** (Array): *See documentation*
- **array input for the waveshaper** (custom distortion transfer function): *See documentation*
- **Output Gain** (Number): *See documentation*

**< Output Ports:**
- **Audio Out** (Object): *See documentation*
- **Curve Out** (Array): *See documentation*
- **distortion curve array output** (one-dimensional): *See documentation*
- **Curve Length** (Number): *See documentation*

**Example Patch:** [Open in Editor](https://cables.gl/edit/6Vl87I)
**Patches Using This Op:** *Search [cables.gl patches](https://cables.gl/patches) for "Waveshaper"*
**Docs:** [https://cables.gl/op/Ops.WebAudio.Waveshaper](https://cables.gl/op/Ops.WebAudio.Waveshaper)

---

