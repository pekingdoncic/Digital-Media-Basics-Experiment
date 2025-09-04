import cv2
import numpy as np

cap = cv2.VideoCapture(r'videos/video1.avi')#读取视频进入文件中
ret, frame1 = cap.read()#将视频中第一帧数据读入
prvs = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)#将该帧图像转化为灰度图
#创建一个与给定数组形状相同（每个元素有三个分量），每个元素的第二个分量为255的数组
hsv = np.zeros_like(frame1)
hsv[..., 1] = 255
# print(hsv)

while (1):
    ret, frame2 = cap.read()#读取一帧
    next = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)#将该帧图像转化为灰度图
    #计算稠密光流（每个像素的光流都要计算）参数依次是：
    # 前一帧图像，后一帧图像，
    # pyr_scale： 金字塔上下两层之间的尺度关系，该参数一般设置为pyrScale=0.5，表示图像金字塔上一层是下一层的2倍降采样
    # levels：图像金字塔的层数
    #winsize：均值窗口大小，winsize越大，算法对图像噪声越鲁棒，并且能提升对快速运动目标的检测效果，但也会引起运动区域模糊。
    #iterations：算法在图像金字塔每层的迭代次数
    #poly_n：用于在每个像素点处计算多项式展开的相邻像素点的个数。poly_n越大，图像的近似逼近越光滑，算法鲁棒性更好，也会带来更多的运动区域模糊。通常，poly_n=5 or 7
    #poly_sigma：标准差，poly_n=5时，poly_sigma = 1.1；poly_n=7时，poly_sigma = 1.5
    #flags:操作标志
    flow = cv2.calcOpticalFlowFarneback(prvs, next, None, 0.5, 3, 15, 3, 5, 1.2, 0)
    #将笛卡尔坐标转化为极坐标
    mag, ang = cv2.cartToPolar(flow[..., 0], flow[..., 1])
    hsv[..., 0] = ang * 180 / np.pi / 2
    hsv[..., 2] = cv2.normalize(mag, None, 0, 255, cv2.NORM_MINMAX)#将数据规范化
    rgb = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)#图像格式转化
    print(hsv[..., 2])
    cv2.imshow('frame2', rgb)#显示图像
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
    elif k == ord('s'):#按下s键，将视频截图存为‘opticalfb.png’
        cv2.imwrite('opticalfb.png', frame2)
    cv2.imwrite('opticalhsv.png', rgb)
    prvs = next#更新帧，将下一帧赋值给上一帧
print(hsv)
print(rgb)
cap.release()
cv2.destroyAllWindows()