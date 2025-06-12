
import sounddevice as sd
import numpy as np
import librosa

def record_audio(duration=5, fs=22050):
    print("Recording...")
    audio = sd.rec(int(duration * fs), samplerate=fs, channels=1)
    sd.wait()
    print("Done.")
    return np.squeeze(audio)

def get_main_pitch(audio, sr=22050):
    pitches, magnitudes = librosa.piptrack(y=audio, sr=sr)
    index = magnitudes.argmax()
    pitch = pitches[index // pitches.shape[1], index % pitches.shape[1]]
    return pitch

def estimate_note(pitch):
    notes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    if pitch <= 0:
        return "Unknown"
    note_index = int(round(12 * np.log2(pitch / 440.0))) + 9  # A4 = 440 Hz
    return notes[note_index % 12]
