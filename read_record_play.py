"""This module contains functions for recording, saving and playing the .wav files."""
import sounddevice as sd
from scipy.io.wavfile import read, write
import numpy as np


def read_wav(path: str):
    """
    This function takes a path to the .wav file, reads it, and returns an audio piece and its sample rate.
    """

    sr, array = read(path)

    return sr, array


def play_wav(recording: np.array, sr: int) -> None:
    """
    This function takes in a recording as a NumPy array, its sampling rate, and plays it.
    """
    print("Playing...")
    sd.play(recording, sr)
    sd.wait()


def save_wav(recording: np.array, filename: str) -> None:
    """
    This function takes in the recording and saves it with a given filename.
    """
    scaled_recording = np.int16(recording/np.max(np.abs(recording)) * 32767)
    write(filename + ".wav", 8000, scaled_recording)


def record():
    """
    This function records an audio at an 8000 sampling rate and returns the recording as a NumPy array.
    """
    duration = 20
    sr = 8000

    print("Recording...")
    recording = sd.rec(int(duration * sr), samplerate=sr, channels=2)
    sd.wait()
    print("Recording finished.")

    return recording