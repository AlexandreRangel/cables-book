# Ops.WebAudio


```{=latex}
\OpsSubsubNoSubsectionNumbering\setcounter{subsubsection}{0}
```
### AnalyzerTexture_v2
![AnalyzerTexture_v2 op](images/ops/Ops_WebAudio_AnalyzerTexture_v2.svg)

**Full Name:** `Ops.WebAudio.AnalyzerTexture_v2`

Creates a spectrogram texture from an audio FFT array.

**`\inputsymbol`{=latex} Inputs**

- **Refresh** (Trigger)
- **FFT Array** (Array)
- **Mirror Active** (Number: Boolean)
- **Mirror Width** (Number)
- **Texture Size Index** (Number: Integer)

**`\outputsymbol`{=latex} Output**

- **Texture Out** (Object)
- **Position** (Number)

**Example:** [cables.gl/edit/T_-vCp](https://cables.gl/edit/T_-vCp)

**Doc:** [cables.gl/op/Ops.WebAudio.AnalyzerTexture_v2](https://cables.gl/op/Ops.WebAudio.AnalyzerTexture_v2)

### AudioAnalyzer_v2
![AudioAnalyzer_v2 op](images/ops/Ops_WebAudio_AudioAnalyzer_v2.svg)

**Full Name:** `Ops.WebAudio.AudioAnalyzer_v2`

Extracts FFT, RMS & Waveform data from an incoming audio signal.

**`\inputsymbol`{=latex} Inputs**

- **Trigger In** (Trigger)
- **Audio In** (Object:AudioNode)
- **FFT Size Index** (Number: Integer)
- **Smoothing** (Number)
- **Range** (in dBFS)
- **Min** (Number)
- **Max** (Number)

**`\outputsymbol`{=latex} Output**

- **Trigger Out** (Trigger)
- **Audio Out** (Object)
- **FFT Array** (Array)
- **Waveform Array** (Array)
- **Frequencies By Index Array** (Array)
- **Array Length** (Number)
- **Average Volume** (Number)
- **Average Volume Time-Domain** (Number)
- **RMS Volume** (Number)

**Example:** [cables.gl/edit/h2eBh-](https://cables.gl/edit/h2eBh-)

**Doc:** [cables.gl/op/Ops.WebAudio.AudioAnalyzer_v2](https://cables.gl/op/Ops.WebAudio.AudioAnalyzer_v2)

### AudioBuffer_v3
![AudioBuffer_v3 op](images/ops/Ops_WebAudio_AudioBuffer_v3.svg)

**Full Name:** `Ops.WebAudio.AudioBuffer_v3`

Holds an audio file / sample in a buffer.

**`\inputsymbol`{=latex} Inputs**

- **URL** (String)
- **Create Loading Task** (Number: Boolean)
- **Active** (Number: Boolean)

**`\outputsymbol`{=latex} Output**

- **Audio Buffer** (Object)
- **Finished Loading** (booleanNumber)
- **Sample Rate** (Number)
- **Length** (Number)
- **Duration** (Number)
- **Number Of Channels** (Number)
- **IsLoading** (booleanNumber)

**Example:** [cables.gl/edit/xEL0rn](https://cables.gl/edit/xEL0rn)

**Doc:** [cables.gl/op/Ops.WebAudio.AudioBuffer_v3](https://cables.gl/op/Ops.WebAudio.AudioBuffer_v3)

### AudioBufferChannelRouter
![AudioBufferChannelRouter op](images/ops/Ops_WebAudio_AudioBufferChannelRouter.svg)

**Full Name:** `Ops.WebAudio.AudioBufferChannelRouter`

Route audio from one input channel to any output channel.

**`\inputsymbol`{=latex} Inputs**

- **Audio Buffer** (Object:AudioBuffer)
- **Channel In** (Number: Integer)
- **Channel Out** (Number: Integer)
- **Clear Others** (Number: Boolean)
- **Channel Offset** (Number: Boolean)

**`\outputsymbol`{=latex} Output**

- **Audio Buffer Out** (Object)
- **Output Channels** (Number)

**Example:** [cables.gl/edit/KlCyYN](https://cables.gl/edit/KlCyYN)

**Doc:** [cables.gl/op/Ops.WebAudio.AudioBufferChannelRouter](https://cables.gl/op/Ops.WebAudio.AudioBufferChannelRouter)

### AudioBufferPlayer_v2
![AudioBufferPlayer_v2 op](images/ops/Ops_WebAudio_AudioBufferPlayer_v2.svg)

**Full Name:** `Ops.WebAudio.AudioBufferPlayer_v2`

Play back audio data stored in an AudioBuffer.

**`\inputsymbol`{=latex} Inputs**

- **Audio Buffer** (Object:AudioBuffer)
- **Loop** (Number: Boolean)
- **Restart** (Trigger)
- **Offset** (Number)
- **Playback Rate** (Number)
- **Detune** (Number)

**`\outputsymbol`{=latex} Output**

- **Audio Out** (Object)
- **Is Playing** (booleanNumber)
- **Loading** (booleanNumber)

**Example:** [cables.gl/edit/5PFIfu](https://cables.gl/edit/5PFIfu)

**Doc:** [cables.gl/op/Ops.WebAudio.AudioBufferPlayer_v2](https://cables.gl/op/Ops.WebAudio.AudioBufferPlayer_v2)

### AudioBufferToSplineArray
![AudioBufferToSplineArray op](images/ops/Ops_WebAudio_AudioBufferToSplineArray.svg)

**Full Name:** `Ops.WebAudio.AudioBufferToSplineArray`

Outputs the waveform of an audio file as a spline array.

**`\inputsymbol`{=latex} Inputs**

- **Render** (Trigger)
- **Audio Buffer** (Object:AudioBuffer)
- **Width** (Number)
- **Height** (Number)
- **Samples Per Pixel** (Number: Integer)

**`\outputsymbol`{=latex} Output**

- **Next** (Trigger)
- **Array Out** (Array)

**Example:** [cables.gl/edit/OcOVBp](https://cables.gl/edit/OcOVBp)

**Doc:** [cables.gl/op/Ops.WebAudio.AudioBufferToSplineArray](https://cables.gl/op/Ops.WebAudio.AudioBufferToSplineArray)

### AudioPanner
![AudioPanner op](images/ops/Ops_WebAudio_AudioPanner.svg)

**Full Name:** `Ops.WebAudio.AudioPanner`

stereo pan an audio signal from left to right.

**`\inputsymbol`{=latex} Inputs**

- **Audio In** (Object:AudioNode)
- **Pan** (Number)

**`\outputsymbol`{=latex} Output**

- **Audio Out** (Object)

**Example:** [cables.gl/edit/iNue_j](https://cables.gl/edit/iNue_j)

**Doc:** [cables.gl/op/Ops.WebAudio.AudioPanner](https://cables.gl/op/Ops.WebAudio.AudioPanner)

### AudioRecorder
![AudioRecorder op](images/ops/Ops_WebAudio_AudioRecorder.svg)

**Full Name:** `Ops.WebAudio.AudioRecorder`

record, playback and download audio.

**`\inputsymbol`{=latex} Inputs**

- **Audio In** (Object:AudioNode)
- **Start Recording** (Trigger)
- **Stop Recording** (Trigger)
- **Input Gain** (Number)
- **Start Playback** (Trigger)
- **Stop Playback** (Trigger)
- **Clear Buffer** (Trigger)
- **Playback Gain** (Number)
- **Loop Playback** (Number: Boolean)

**`\outputsymbol`{=latex} Output**

- **Audio Out** (Object)
- **Recorded Audio Out** (Object)
- **Is Recording** (booleanNumber)
- **Is Playing Back** (booleanNumber)
- **State** (String)
- **AudioBuffer Out** (Object)
- **Data URL** (String)

**Example:** [cables.gl/edit/nEKhbI](https://cables.gl/edit/nEKhbI)

**Doc:** [cables.gl/op/Ops.WebAudio.AudioRecorder](https://cables.gl/op/Ops.WebAudio.AudioRecorder)

### BiquadFilter_v2
![BiquadFilter_v2 op](images/ops/Ops_WebAudio_BiquadFilter_v2.svg)

**Full Name:** `Ops.WebAudio.BiquadFilter_v2`

Different kinds of audio filters.

**`\inputsymbol`{=latex} Inputs**

- **Audio In** (Object:AudioNode)
- **Type Index** (Number: Integer)
- **Frequency** (Number)
- **Q** (Number)
- **Gain** (Number)
- **Detune** (in cents)
- **Frequency Array** (Array)

**`\outputsymbol`{=latex} Output**

- **Audio Out** (Object)
- **Magnitude Response Array** (Array)
- **Phase Response Array** (Array)
- **Response Arrays Length** (Number)

**Example:** [cables.gl/edit/nhyACp](https://cables.gl/edit/nhyACp)

**Doc:** [cables.gl/op/Ops.WebAudio.BiquadFilter_v2](https://cables.gl/op/Ops.WebAudio.BiquadFilter_v2)

### ClockSequencer
![ClockSequencer op](images/ops/Ops_WebAudio_ClockSequencer.svg)

**Full Name:** `Ops.WebAudio.ClockSequencer`

send bpm based triggers like a clocked trigger sequencer / clock divider.

**`\inputsymbol`{=latex} Inputs**

- **BPM** (Number: Integer)
- **beats per minute** (tempo)
- **Start** (Trigger)
- **Stop** (Trigger)
- **Reset** (Trigger)

**`\outputsymbol`{=latex} Output**

- **Sequencer Running** (booleanNumber)
- **BPM Out** (Number)
- **Start Out** (Trigger)
- **Stop Out** (Trigger)
- **Reset Out** (Trigger)

**Example:** [cables.gl/edit/J8Uccu](https://cables.gl/edit/J8Uccu)

**Doc:** [cables.gl/op/Ops.WebAudio.ClockSequencer](https://cables.gl/op/Ops.WebAudio.ClockSequencer)

### ClockSequencerPattern
![ClockSequencerPattern op](images/ops/Ops_WebAudio_ClockSequencerPattern.svg)

**Full Name:** `Ops.WebAudio.ClockSequencerPattern`

sequence triggers by defining a pattern (like a drum machine).

**`\inputsymbol`{=latex} Inputs**

- **Clock Trigger Input** (Trigger)
- **Sequence Array** (Array)
- **Steps Index** (Number: Integer)
- **Steps** (Number: String)
- **Reset** (Trigger)

**`\outputsymbol`{=latex} Output**

- **Sequence Trigger Output** (Trigger)
- **Sequenced Value** (Number)
- **Current Step** (Number)

**Example:** [cables.gl/edit/KM0Dgu](https://cables.gl/edit/KM0Dgu)

**Doc:** [cables.gl/op/Ops.WebAudio.ClockSequencerPattern](https://cables.gl/op/Ops.WebAudio.ClockSequencerPattern)

### Convolver_v2
![Convolver_v2 op](images/ops/Ops_WebAudio_Convolver_v2.svg)

**Full Name:** `Ops.WebAudio.Convolver_v2`

Audio reverb using an impulse response (sample).

**`\inputsymbol`{=latex} Inputs**

- **Audio In** (Object:AudioNode)
- **Impulse Response** (String)
- **Normalize** (Number: Boolean)
- **IR Gain** (Number)
- **Output Gain** (Number)

**`\outputsymbol`{=latex} Output**

- **Audio Out** (Object)
- **Wet Out** (Object)

**Example:** [cables.gl/edit/WlLDwp](https://cables.gl/edit/WlLDwp)

**Doc:** [cables.gl/op/Ops.WebAudio.Convolver_v2](https://cables.gl/op/Ops.WebAudio.Convolver_v2)

### CutFilter
![CutFilter op](images/ops/Ops_WebAudio_CutFilter.svg)

**Full Name:** `Ops.WebAudio.CutFilter`

dj style filter (lowpass and highpass).

**`\inputsymbol`{=latex} Inputs**

- **Audio In** (Object:AudioNode)
- **Highpass Active** (Number: Boolean)
- **Low Frequency** (Number)
- **Low Q** (Number)
- **Lowpass Active** (Number: Boolean)
- **High Frequency** (Number)
- **High Q** (Number)

**`\outputsymbol`{=latex} Output**

- **Audio Out** (Object)

**Example:** [cables.gl/edit/6SsZxp](https://cables.gl/edit/6SsZxp)

**Doc:** [cables.gl/op/Ops.WebAudio.CutFilter](https://cables.gl/op/Ops.WebAudio.CutFilter)

### Delay
![Delay op](images/ops/Ops_WebAudio_Delay.svg)

**Full Name:** `Ops.WebAudio.Delay`

add a delay effect to an audio stream.

**`\inputsymbol`{=latex} Inputs**

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

**`\outputsymbol`{=latex} Output**

- **Mix Out** (Object)
- **Wet Out** (Object)

**Example:** [cables.gl/edit/IUjXgu](https://cables.gl/edit/IUjXgu)

**Doc:** [cables.gl/op/Ops.WebAudio.Delay](https://cables.gl/op/Ops.WebAudio.Delay)

### FFTAreaAverage_v3
![FFTAreaAverage_v3 op](images/ops/Ops_WebAudio_FFTAreaAverage_v3.svg)

**Full Name:** `Ops.WebAudio.FFTAreaAverage_v3`

get average value in an area of a fft audio analysis buffer.

**`\inputsymbol`{=latex} Inputs**

- **Refresh** (Trigger)
- **FFT Array** (Array)
- **X Position** (Number)
- **Y Position** (Number)
- **Width** (Number)
- **Height** (Number)
- **Create Texture** (Number: Boolean)

**`\outputsymbol`{=latex} Output**

- **Texture Out** (Object)
- **Area Average Volume** (Number)

**Example:** [cables.gl/edit/F6Fhyp](https://cables.gl/edit/F6Fhyp)

**Doc:** [cables.gl/op/Ops.WebAudio.FFTAreaAverage_v3](https://cables.gl/op/Ops.WebAudio.FFTAreaAverage_v3)

### Gain
![Gain op](images/ops/Ops_WebAudio_Gain.svg)

**Full Name:** `Ops.WebAudio.Gain`

Changes the gain / volume.

**`\inputsymbol`{=latex} Inputs**

- **Audio In** (Object:AudioNode)
- **Gain** (Number)
- **Mute** (Number: Boolean)

**`\outputsymbol`{=latex} Output**

- **Audio Out** (Object)

**Example:** [cables.gl/edit/JeKgDp](https://cables.gl/edit/JeKgDp)

**Doc:** [cables.gl/op/Ops.WebAudio.Gain](https://cables.gl/op/Ops.WebAudio.Gain)

### KeyPiano
![KeyPiano op](images/ops/Ops_WebAudio_KeyPiano.svg)

**Full Name:** `Ops.WebAudio.KeyPiano`

Generates notes based on key presses.

**`\inputsymbol`{=latex} Inputs**

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

**`\outputsymbol`{=latex} Output**

- **Frequency** (Number)
- **Is Pressed** (Number)

**Example:** [cables.gl/op/Ops.WebAudio.KeyPiano#example](https://cables.gl/op/Ops.WebAudio.KeyPiano#example)

**Doc:** [cables.gl/op/Ops.WebAudio.KeyPiano](https://cables.gl/op/Ops.WebAudio.KeyPiano)

### MicrophoneIn_v2
![MicrophoneIn_v2 op](images/ops/Ops_WebAudio_MicrophoneIn_v2.svg)

**Full Name:** `Ops.WebAudio.MicrophoneIn_v2`

Access to the microphone and/or audio input devices.

**`\inputsymbol`{=latex} Inputs**

- **Audio Input Index** (Number: Integer)
- **Volume** (Number)
- **Mute** (Number: Boolean)
- **Start** (Trigger)

**`\outputsymbol`{=latex} Output**

- **Audio Out** (Object)
- **Listening** (booleanNumber)
- **List Of Input Devices** (Array)

**Example:** [cables.gl/edit/xjHACp](https://cables.gl/edit/xjHACp)

**Doc:** [cables.gl/op/Ops.WebAudio.MicrophoneIn_v2](https://cables.gl/op/Ops.WebAudio.MicrophoneIn_v2)

### MidiValueToFrequency
![MidiValueToFrequency op](images/ops/Ops_WebAudio_MidiValueToFrequency.svg)

**Full Name:** `Ops.WebAudio.MidiValueToFrequency`

Converts a midi value to a frequency.

**`\inputsymbol`{=latex} Inputs**

- **MIDI Value** (Number)
- **Tuning** (Number)

**`\outputsymbol`{=latex} Output**

- **Frequency** (Number)

**Example:** [cables.gl/op/Ops.WebAudio.MidiValueToFrequency#example](https://cables.gl/op/Ops.WebAudio.MidiValueToFrequency#example)

**Doc:** [cables.gl/op/Ops.WebAudio.MidiValueToFrequency](https://cables.gl/op/Ops.WebAudio.MidiValueToFrequency)

### Mixer
![Mixer op](images/ops/Ops_WebAudio_Mixer.svg)

**Full Name:** `Ops.WebAudio.Mixer`

Mix audio signals together.

**`\inputsymbol`{=latex} Inputs**

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

**`\outputsymbol`{=latex} Output**

- **Audio Out** (Object)

**Example:** [cables.gl/edit/J7YdCp](https://cables.gl/edit/J7YdCp)

**Doc:** [cables.gl/op/Ops.WebAudio.Mixer](https://cables.gl/op/Ops.WebAudio.Mixer)

### MusicalScales
![MusicalScales op](images/ops/Ops_WebAudio_MusicalScales.svg)

**Full Name:** `Ops.WebAudio.MusicalScales`

Outputs a musical scale array (major, minor, ...) as strings, steps and midi notes.

**`\inputsymbol`{=latex} Inputs**

- **Root Note Index** (Number: Integer)
- **Root Note** (Number: String)
- **Scale Type Index** (Number: Integer)
- **Scale Type** (Number: String)
- **Include Upper Root Note** (Number: Boolean)
- **Octave** (Number: Integer)
- **the octave of the scale** (only for string & midi note outputs)
- **Append Octave To Names** (Number: Boolean)

**`\outputsymbol`{=latex} Output**

- **Note Names Array** (Array)
- **Note Step Number Array** (Array)
- **Midi Note Array** (Array)
- **Current Scale** (String)

**Example:** [cables.gl/edit/8Ekchu](https://cables.gl/edit/8Ekchu)

**Doc:** [cables.gl/op/Ops.WebAudio.MusicalScales](https://cables.gl/op/Ops.WebAudio.MusicalScales)

### Output_v2
![Output_v2 op](images/ops/Ops_WebAudio_Output_v2.svg)

**Full Name:** `Ops.WebAudio.Output_v2`

Sends an audio signal to your speakers.

**`\inputsymbol`{=latex} Inputs**

- **Audio In** (Object:AudioNode)
- **Volume** (Number)
- **Mute** (Number: Boolean)
- **Show Audio Suspended Button** (Number: Boolean)

**`\outputsymbol`{=latex} Output**

- **Current Volume** (Number)
- **Number Of Channels** (Number)
- **Context State** (String)

**Example:** [cables.gl/edit/teZhCp](https://cables.gl/edit/teZhCp)

**Doc:** [cables.gl/op/Ops.WebAudio.Output_v2](https://cables.gl/op/Ops.WebAudio.Output_v2)

### ThreeBandEqualizer
![ThreeBandEqualizer op](images/ops/Ops_WebAudio_ThreeBandEqualizer.svg)

**Full Name:** `Ops.WebAudio.ThreeBandEqualizer`

3 filters in one - an eq to quickly process an audio signal.

**`\inputsymbol`{=latex} Inputs**

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

**`\outputsymbol`{=latex} Output**

- **Audio Out** (Object)

**Example:** [cables.gl/edit/tD2Vxp](https://cables.gl/edit/tD2Vxp)

**Doc:** [cables.gl/op/Ops.WebAudio.ThreeBandEqualizer](https://cables.gl/op/Ops.WebAudio.ThreeBandEqualizer)

### WaveformMesh
![WaveformMesh op](images/ops/Ops_WebAudio_WaveformMesh.svg)

**Full Name:** `Ops.WebAudio.WaveformMesh`

Outputs the waveform of an audio file as a geometry.

**`\inputsymbol`{=latex} Inputs**

- **Render** (Trigger)
- **Audio Buffer** (Object:AudioBuffer)
- **Render Active** (Number: Boolean)
- **Show Bottom Half** (Number: Boolean)
- **Center Origin** (Number: Boolean)
- **Width** (Number)
- **Samples Per Pixel** (Number: Integer)
- **Calculate Tex Coords** (Number: Boolean)

**`\outputsymbol`{=latex} Output**

- **Spline Points** (Array)
- **Next** (Trigger)
- **Geometry** (Object)

**Example:** [cables.gl/edit/VqDkCp](https://cables.gl/edit/VqDkCp)

**Doc:** [cables.gl/op/Ops.WebAudio.WaveformMesh](https://cables.gl/op/Ops.WebAudio.WaveformMesh)

### Waveshaper
![Waveshaper op](images/ops/Ops_WebAudio_Waveshaper.svg)

**Full Name:** `Ops.WebAudio.Waveshaper`

add waveshaping (distortion, overdrive, fuzz) to an audio stream.

**`\inputsymbol`{=latex} Inputs**

- **Audio In** (Object:AudioNode)
- **Oversampling Index** (Number: Integer)
- **Distortion Amount** (Number: Integer)
- **Waveshape Array In** (Array)
- **array input for the waveshaper** (custom distortion transfer function)
- **Output Gain** (Number)

**`\outputsymbol`{=latex} Output**

- **Audio Out** (Object)
- **Curve Out** (Array)
- **distortion curve array output** (one-dimensional)
- **Curve Length** (Number)

**Example:** [cables.gl/edit/6Vl87I](https://cables.gl/edit/6Vl87I)

**Doc:** [cables.gl/op/Ops.WebAudio.Waveshaper](https://cables.gl/op/Ops.WebAudio.Waveshaper)


