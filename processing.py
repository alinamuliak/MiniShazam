"""
this module contains functions to detect bpm of the song, extract pitch curve and plot or play the results.
"""

import essentia.standard as es
import matplotlib.pyplot as plt
import numpy as np
from IPython.display import Audio
from IPython.core.display import display
from mir_eval.sonify import pitch_contour


def detect_bpm(audio_filename: str) -> float:
  sampling_rate = 44100
  audio = es.MonoLoader(filename=audio_filename, sampleRate=sampling_rate)()
  bpm = es.PercivalBpmEstimator()(audio)
  return bpm


def plot_audio_and_tempo(audio_filename) -> None:
  sampling_rate = 44100
  audio = es.MonoLoader(filename=audio_filename, sampleRate=sampling_rate)()
  bpm = detect_bpm(audio_filename)
  time = np.array(range(len(audio))) / sampling_rate
  plt.plot(time, audio)
  markers = np.arange(0, len(audio) / sampling_rate, bpm / 180)
  for marker in markers:
      plt.axvline(x=marker, color='red')

  plt.title("Audio waveform on top of a tempo grid")
  plt.xlabel("Time [sec]")
  plt.ylabel("Amplitude")
  plt.show()


def extract_pitches(audio_filename: str) -> tuple:
  audio = loader = es.EqloudLoader(filename=audio_filename, sampleRate=44100)()
  pitch_extractor = es.PredominantPitchMelodia(frameSize=2048, hopSize=128)
  pitch_values, pitch_confidence = pitch_extractor(audio)

  pitch_times = np.linspace(0.0, len(audio)/44100, len(pitch_values))
  return pitch_times, pitch_values, pitch_confidence


def plot_pitch_curve(pitch_attributes) -> None:
  pitch_times, pitch_values, pitch_confidence = pitch_attributes
  f, axarr = plt.subplots(2, sharex=True)
  axarr[0].plot(pitch_times, pitch_values)
  axarr[0].set_title('estimated pitch [Hz]')
  axarr[1].plot(pitch_times, pitch_confidence)
  axarr[1].set_title('pitch confidence')
  plt.show()


def compose_determined_pitch(pitch_times, pitch_values):
  synthesized_melody = pitch_contour(pitch_times, pitch_values, 44100).astype(np.float32)
  es.AudioWriter(filename='test.mp3', format='mp3')(es.StereoMuxer()([0 for _ in range(len(synthesized_melody))], synthesized_melody))
  display(Audio('test.mp3'))
