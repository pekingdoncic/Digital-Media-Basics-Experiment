
import cv2
import numpy as num


#读取视频进入文件中
capture = cv2.VideoCapture(r'videos/video1.avi')
#计算帧数：
nbFrames = int(capture.get(cv2.CAP_PROP_FRAME_COUNT))
#计算帧率
fps = capture.get(cv2.CAP_PROP_FPS)
#这个计算俩帧之间的间隔
wait = 1 / fps * 1000 / 1
#持续时间：（视频总长）
duration = (wait * nbFrames)/1000
# duration =nbFrames/fps
print('Num. Frames = ', nbFrames)
# print(wait)
print('Frame Rate = ', fps, 'fps')
print('Duration = ', duration, 'sec')