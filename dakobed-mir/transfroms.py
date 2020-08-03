import librosa
import numpy as np

y, sr = librosa.load('data/guitarset/audio/00_BN1-129-Eb_comp_mix.wav')

cqt_raw = librosa.core.cqt(y, sr=sr, n_bins=144, bins_per_octave=24, fmin=librosa.note_to_hz('C2'), norm=1)
magphase_cqt = librosa.magphase(cqt_raw)
