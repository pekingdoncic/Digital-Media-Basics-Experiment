import wave
# 导入 wave 模块
import matplotlib.pyplot as plt
# 用于绘制波形图
import numpy as np
# 用于计算波形数据
import os
import math


f = wave.open(r"./sound/birdsound.wav",'rb' )
params = f.getparams ()
nchannels,sampwidth, framerate, nframes = params [:4]
print(framerate)

strData = f.readframes(nframes)
waveData = np.fromstring(strData,dtype=np.int16)
waveData = np.reshape(waveData,[nframes,nchannels])#需要转化为单维度数组才能用！

framesize = 32
NFFT = framesize
overlapSize = 1.0 / 3 * framesize
overlapSize = int(round(overlapSize)) # 取整
plt.specgram(waveData[:,0], NFFT=NFFT,
Fs=framerate,window=np.hanning(M=framesize), noverlap=overlapSize)
plt.ylabel('Frequency')
plt.xlabel('Time')
plt.ylim(0, 6000)
plt.title("Wide Band Spectrum")
plt.show()

framesize = 2048
framelength = framesize / framerate
NFFT = framesize
overlapSize = 1.0 / 3 * framesize
overlapSize = int(round(overlapSize))
plt.specgram(waveData[:, 0],
             NFFT=NFFT, Fs=framerate, window=np.hanning(M=framesize),
             noverlap=overlapSize)

plt.ylabel('Frequency')
plt.xlabel('Time')
plt.ylim(0, 6000)
plt.title("Narrow Band Spectrum")
plt.show()