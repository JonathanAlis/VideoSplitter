import cv2
import numpy as np
import wave
import struct
import matplotlib.pyplot as plt
vName='out.mp4'
cap=cv2.VideoCapture(vName)
w= int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
h= int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps=  int(cap.get(cv2.CAP_PROP_FPS))
print('video size ',mWidth,'x',mHeight,', at ',mFps,' fps.')
cv2.namedWindow('Video',cv2.WND_PROP_FULLSCREEN)

frequency = 1000
num_samples = 48000
sampling_rate = 48000.0
amplitude = 16000
file = "test.wav"
sine_wave = [np.sin(2 * np.pi * frequency * x/sampling_rate) for x in range(num_samples)]
nframes=num_samples
comptype="NONE"
compname="not compressed"
nchannels=1
sampwidth=2
wav_file=wave.open(file, 'w')
wav_file.setparams((nchannels, sampwidth, int(sampling_rate), nframes, comptype, compname))
for s in sine_wave:
    wav_file.writeframes(struct.pack('h', int(s*amplitude)))
wav_file.close()