import random
import base64
import json
import wave
import os
from pickle import dump
import cv2
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import glob

def wav2img(wav_file,img_file):
    wav = wave.open(wav_file, "r")
    frames = wav.readframes(-1)
    sound_info = np.frombuffer(frames, "int16")
    frame_rate = wav.getframerate()
    wav.close()
    fig = plt.figure()
    fig.set_size_inches((1.12, 1.12))
    ax = plt.Axes(fig, [0., 0., 1., 1.])
    ax.set_axis_off()
    fig.add_axes(ax)
    plt.set_cmap("hot")
    plt.specgram(sound_info, Fs=frame_rate)

    plt.savefig(img_file, format="png")
    plt.close(fig)
    return img_file

wavList = glob.glob("./leagcy/*.wav")
for per_wav in wavList:
    per_wav2img = per_wav.replace("wav","png")
    wav2img(per_wav,per_wav2img)
