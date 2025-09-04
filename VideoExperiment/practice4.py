#将视频读入数组中
import numpy as np
import cv2

cap = cv2.VideoCapture(r'videos/video1.avi')#读取视频进入文件中
wid = int(cap.get(3))#获取在视频流的帧的宽度
hei = int(cap.get(4))#在视频流的帧的高度
framerate = int(cap.get(5))#获取帧速率
framenum = int(cap.get(7))#获取视频文件中的帧数

video = np.zeros((framenum,hei,wid,3),dtype='float16')#定义一个长宽高分别为视频文件中的帧数,在视频流的帧的宽度,视频流的帧的高度全为0的数组
cnt = 0
while(cap.isOpened()):#当视频在播放的时候一直循环
     a,b=cap.read()#将视频流中的数据读到b中
     c=1#用于计数
     cv2.imshow('%d'%cnt, b)#显示这一帧的图片
     cv2.waitKey(1)#显示一秒这一帧图像
     b = b.astype('float16')/255#将b的数值类型转化
     video[cnt]=b#将b中的视频帧数据赋值给video
     print(cnt)#显示帧数
     cnt+=1


