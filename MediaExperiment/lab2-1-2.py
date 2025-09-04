import wave
# 导入 wave 模块
import matplotlib.pyplot as plt
# 用于绘制波形图
import numpy as np
# 用于计算波形数据
import os
import warnings
warnings.filterwarnings("ignore")

# 用于系统处理，如读取本地音频文件
f = wave.open(r"./sound/single_sound.wav",'rb')
params = f.getparams ()
nchannels,sampwidth, framerate, nframes = params [:4]
print(framerate)
#
# 读取单通道音频
# 通过第一步，可以继续读取音频数据本身，保存为字符串格式
strData = f.readframes(nframes)
# （2） 如果需要绘制波形图，则需要将字符串格式的音频数据转化为 int 类型
waveData = np.fromstring(strData,dtype=np.int16)
# 此处需要使用到 numpy 进行数据格式的转化
# （3） 将幅值归一化
# waveData = waveData*1.0/(max(abs(waveData)))
# 这一步去掉也可画出波形图，大家可以尝试不用此步，找出波形图的不同
# （4） 绘制图像
time = np.arange(0,nframes)*(1.0 / framerate)#计算音频的时间
plt.plot(time,waveData)#俩个列表的长度都不一样！这个必须是单声道！
plt.xlabel("Time(s)")
plt.ylabel("Amplitude")
plt.title("Single channel wavedata")
plt.show()
f.close()