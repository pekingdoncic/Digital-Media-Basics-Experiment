import wave
# 导入 wave 模块
import matplotlib.pyplot as plt
# 用于绘制波形图
import numpy as np
# 读取多频道音频
f = wave.open(r"./sound/man_sound.wav",'rb')
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

# time = np.arange(0,nframes)*(1.0 / framerate)
# plt.figure()
# plt.subplot(5,1,1)
# plt.plot(time,waveData[:,0])
# plt.xlabel("Time(s)")
# plt.ylabel("Amplitude")
# plt.title("Ch-1 wavedata")
# plt.subplot(5,1,3)
# plt.plot(time,waveData[:,1])
# plt.xlabel("Time(s)")
# plt.ylabel("Amplitude")
# plt.title("Ch-2 wavedata")
# plt.show()
#绘制频谱图，NFFT为每个片段的数据点数（窗长度），Fs为采样频率，window为由np.hanning()计算得到的一行32列的向量（M为生成向量的列数，长度必须与NFFT相等），noverlap为窗之间的重叠长度
framesize = 32
NFFT = framesize
overlapSize = 1.0 / 2 * framesize
overlapSize = int(round(overlapSize)) # 取整
plt.specgram(waveData[:,0], NFFT=NFFT,
Fs=framerate,window=np.hanning(M=framesize), noverlap=overlapSize)
plt.ylabel('Frequency')
plt.xlabel('Time')
plt.ylim(0, 6000)
plt.title("Wide Band Spectrum")
plt.show()

framesize = 32
NFFT = framesize
overlapSize = 1.0 /4 * framesize
overlapSize = int(round(overlapSize)) # 取整
plt.specgram(waveData[:,0], NFFT=NFFT,
Fs=framerate,window=np.hanning(M=framesize), noverlap=overlapSize)
plt.ylabel('Frequency')
plt.xlabel('Time')
plt.ylim(0, 6000)
plt.title("Wide Band Spectrum")
plt.show()
# framesize = 2048
# framelength = framesize / framerate
# NFFT = framesize
# overlapSize = 1.0 /2 * framesize
# overlapSize = int(round(overlapSize))
# plt.specgram(waveData[:, 0],
#              NFFT=NFFT, Fs=framerate, window=np.hanning(M=framesize),
#              noverlap=overlapSize)
#
# plt.ylabel('Frequency')
# plt.xlabel('Time')
# plt.ylim(0, 6000)
# plt.title("Narrow Band Spectrum")
# plt.show()