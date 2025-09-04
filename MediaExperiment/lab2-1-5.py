import wave
# 导入 wave 模块
import matplotlib.pyplot as plt
# 用于绘制波形图
import numpy as np
# 用于计算波形数据
import os
import math

def ZeroCR(wave_data,frameSize,overLap):
    wlen = len(wave_data)
    step = frameSize - overLap
    frameNum = math.ceil(wlen/step)#帧的数量
    zcr = np.zeros((frameNum,1))
    print(zcr)
    for i in range(frameNum):#每帧过零的次数计算
       curFrame = wave_data[np.arange(i*step,min(i*step+frameSize,wlen))]
       curFrame = curFrame - np.mean(curFrame)
       zcr[i] = sum(curFrame[0:-1]*curFrame[1::]<=0)
    return zcr



f = wave.open(r"./sound/birdsound.wav",'rb' )
params = f.getparams ()
nchannels,sampwidth, framerate, nframes = params [:4]
print(framerate)

strData = f.readframes(nframes)
waveData = np.fromstring(strData,dtype=np.int16)
waveData = np.reshape(waveData,[nframes,nchannels])#需要转化为单维度数组才能用！

frameSize = 256
overLap = 0
zcr = ZeroCR(waveData[:, 0], frameSize, overLap)
time3 = np.arange(0, len(zcr)) * (len(waveData[:, 0]) / len(zcr) / framerate)

plt.plot(time3, zcr)
plt.ylabel("ZCR")
plt.xlabel("time (seconds)")
plt.show()
