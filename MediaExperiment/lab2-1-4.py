import wave
# 导入 wave 模块
import matplotlib.pyplot as plt
# 用于绘制波形图
import numpy as np
# 用于计算波形数据
import os

def calEnergy(wave_data) :
    energy = []
    sum = 0
    frameSize = 256
    for i in range(len(wave_data)): #:计算每一帧的数据和
        sum = sum + (wave_data[i] * wave_data[i])#采样点数据平方
        if (i + 1) % frameSize == 0 :
             energy.append(sum)
             sum = 0
        elif i == len(wave_data) - 1 :
            energy.append(sum)
    return energy


f = wave.open(r"./sound/birdsound.wav",'rb' )
params = f.getparams ()
nchannels,sampwidth, framerate, nframes = params [:4]
print(framerate)

strData = f.readframes(nframes)
waveData = np.fromstring(strData,dtype=np.int16)
waveData = np.reshape(waveData,[nframes,nchannels])#需要转化为单维度数组才能用！
f.close()
energy = calEnergy(waveData[:, 0])
print(np.arange(0, len(energy)))
time2 = np.arange(0, len(energy)) * (len(waveData[:, 0]) / len(energy) / framerate)
print(time2)
plt.plot(time2, energy)
plt.ylabel("short energy")
plt.xlabel("time (seconds)")
plt.show()