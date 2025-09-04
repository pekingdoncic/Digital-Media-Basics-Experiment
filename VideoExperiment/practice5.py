import numpy as np
import cv2

cap = cv2.VideoCapture(r'videos/video1.avi')#读取视频进入文件中

# Shi-Tomasi 算法检测拐角的参数
feature_params = dict(maxCorners=100,  qualityLevel=0.3,minDistance=7,blockSize=7)
#掩码 maxCorners：角点最大数量qualityLevel：品质因子，特征值越大的越好，用来筛选，品质因子越大，得到的角点越少minDistance：最小距离，相当于在这个距离中有其他角点比这个角点更适合，就舍弃这个弱的角点

# Parameters for lucas kanade optical flow (卢卡斯·卡纳德光流参数)
lk_params = dict(winSize=(15, 15),maxLevel=2,criteria=(cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))
#winSize：搜索窗口的大小 、maxLevel 最大的金字塔层数,criteria为制定的标准
# Create some random colors (创建一些随机颜色)
color = np.random.randint(0, 255, (100, 3))

# Take first frame and find corners in it (取第一帧，找出其中的角点)
ret, old_frame = cap.read()#将视频文件的一帧读入old_frame中
old_gray = cv2.cvtColor(old_frame, cv2.COLOR_BGR2GRAY)#颜色空间转换函数,将old_frameBGR格式的彩色图像转化成转换为灰度图像
#所有检测到的角点
p0 = cv2.goodFeaturesToTrack(old_gray, mask=None, **feature_params)#跟踪检测图像old_gray中的角点，mask为掩码

# Create a mask image for drawing purposes(创建用于绘图的遮罩图像)
mask = np.zeros_like(old_frame)

while (1):
    ret, frame = cap.read()
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)#将视频中每一帧图像转化为灰度图

    # calculate optical flow (计算光流)
    p1, st, err = cv2.calcOpticalFlowPyrLK(old_gray, frame_gray, p0, None, **lk_params)

    # Select good points (选择好的点)
    good_new = p1[st == 1]
    good_old = p0[st == 1]

    # draw the tracks (绘制轨迹)
    for i, (new, old) in enumerate(zip(good_new, good_old)):
        a, b = new.ravel()
        c, d = old.ravel()
    # print("a: ",a,"b: ",b)
    # e=int (a)
    # f=int (b)
    # print("e: ",e,"f: ",f)
    # mask = cv2.line(mask, (a, b), (c, d), color[i].tolist(), 2)
    # frame = cv2.circle(frame, (a, b), 5, color[i].tolist(), -1)
    #注意这里要将a，b，c，d转化成int类型，这样才不会让mask那个函数报错！

    #cv2.line表示给定一个图像mask，连接点pt1和pt2的坐标，在图中画一条直线，color[i].tolist()表明线的颜色，宽度为2
        mask = cv2.line(mask, (int (a+0.5),int (b+0.5)), (int (c+0.5),int (d+0.5)), color[i].tolist(), 2)
    #cv2.circle() 画圆，参数依次为：画圆的图、圆心、半径、圆的颜色、画圆的线条的粗细、画圆的线的类型、中心坐标和半径值中的小数位数。
        frame = cv2.circle(frame, (int (a+0.5),int (b+0.5)), 5, color[i].tolist(), -1)
    img = cv2.add(frame, mask)#将俩个图像叠加

    cv2.imshow('frame', img)#显示图像
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

    # Now update the previous frame and previous points (现在更新上一帧和上一点)
    old_gray = frame_gray.copy()
    p0 = good_new.reshape(-1, 1, 2)

cv2.destroyAllWindows()#关闭所有窗口
cap.release()#释放cap