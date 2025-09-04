#练习 3. 在 opencv 窗口实时显示高斯模糊后的（彩色）图像
import cv2
cap = cv2.VideoCapture(0)#将第一个摄像机的捕获的文件读取
while True:#一直读取视频流中的数据
     ret, im = cap.read()#没有参数，默认为0，表示从第一个可用的摄像头中读取视频流，ret为读到的布尔值，表示视频文件是否成功打开，im为读取到的的视频帧
     cv2.imshow('video test', im)#展示读取到的数据，窗口标题为“video test”
     key = cv2.waitKey(10)#waitkey控制着imshow的持续时间，表示视频内容持续显示10秒
     blur = cv2.GaussianBlur(im, (0, 0), 5)#im为输入的图像，（0,0）表示在滤波处理过程中其邻域图像的高度和宽度，5表示在卷积核在水平方向上（X 轴方向）的标准差，y轴没有写，默认为0，而其卷积核由默认计算可得：sigmaY=0.3×[（ksize.height-1）×0.5-1]+0.8
     cv2.imshow("GauS",blur)#展示读取到的数据，窗口标题为“GauS”
     if key == 27:#Esc的ASCII码为27，如果按Esc，则退出显示
        break
     if key == ord(' '):
        cv2.imwrite(r'videos/gaosi_result.jpg',im)#ord为返回空格的ASCII码，如果按下空格，则截屏，将其存到videos文件夹下，保存为vid_result.jpg
cap.release()#释放cap
cv2.destroyAllWindows()#关闭所有窗口
