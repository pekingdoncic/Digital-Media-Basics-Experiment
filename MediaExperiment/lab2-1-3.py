import wave
# 导入 wave 模块
import matplotlib.pyplot as plt
# 用于绘制波形图
import numpy as np
# 读取多频道音频
f = wave.open(r"./sound/birdsound.wav",'rb')
params = f.getparams ()
nchannels,sampwidth, framerate, nframes = params [:4]
print(framerate)
#(1) 通过第一步，可以继续读取音频数据本身，保存为字符串格式
strData = f.readframes(nframes)
# （2） 如果需要绘制波形图，则需要将字符串格式的音频数据转化为 int 类型
waveData = np.fromstring(strData,dtype=np.int16)

# 此处需要使用到 numpy 进行数据格式的转化
# （3） 将幅值归一化
waveData = waveData*1.0/(max(abs(waveData)))
waveData = np.reshape(waveData,[nframes,nchannels])
f.close()
#这两行代码是在之后添加的！我又理解错误了！

time = np.arange(0,nframes)*(1.0 / framerate)
plt.figure()
plt.subplot(5,1,1)
plt.plot(time,waveData[:,0])
plt.xlabel("Time(s)")
plt.ylabel("Amplitude")
plt.title("Ch-1 wavedata")
plt.subplot(5,1,3)
plt.plot(time,waveData[:,1])
plt.xlabel("Time(s)")
plt.ylabel("Amplitude")
plt.title("Ch-2 wavedata")
# plt.subplot(5,1,5)
# plt.plot(time,waveData[:,2])
# plt.xlabel("Time(s)")
# plt.ylabel("Amplitude")
# plt.title("Ch-3 wavedata")
plt.show()