#练习 2. 从摄像头读取视频并保存其中某一帧
import cv2
#将第一个摄像机的捕获的文件读取
cap = cv2.VideoCapture(0)
while True:#一直读取视频流中的数据
     ret, im = cap.read()#没有参数，默认为0，表示从第一个可用的摄像头中读取视频流，ret为读到的布尔值，表示视频文件是否成功打开，im为读取到的的视频帧
     cv2.imshow('video test', im)#展示读取到的数据
     key = cv2.waitKey(10)#waitkey控制着imshow的持续时间，表示视频内容持续显示10秒
     if key == 27:#Esc的ASCII码为27，如果按Esc，则退出显示
        break
     if key == ord(' '):#ord为返回空格的ASCII码，如果按下空格，则截屏，将其存到videos文件夹下，保存为vid_result.jpg
        cv2.imwrite(r'videos/vid_result.jpg',im)
cap.release()#释放cap
cv2.destroyAllWindows()#关闭所有窗口
