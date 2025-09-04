import cv2
import matplotlib.pyplot as plt
import numpy as np

def cv_show(img, name):
    cv2.imshow(name, img)
    cv2.waitKey(0)  # 等待输入任意键，注意必须是英文
class My_Histogram:
    def my_histogram (img):
        # 计算每个灰度值频率
        a = np.array([0]*256)
        # x轴坐标
        b = np.array([0]*256)
        for i in range(255):
            b[i]=i
        i = 0
        while i < len(img):
            j = 0
            while j < len(img[i]):
                a[img[i][j]] += 1
                j += 1
            i += 1
        plt.bar(b, a)
        plt.show()

    def my_hist_equal(img):
        h = [0]*256
        hs = [0] * 256
        hp = [0]*256
        g=img.copy()
        hang = img.shape[0]
        lie = img.shape[1]
        sum=hang*lie*1
        # 统计灰度直方图中不同灰度像素个数
        for i in range(len(img)):
            for j in range(len(img[i])):
                h[img[i][j]] += 1

        # 计算图像各灰度级的累计分布hp极其对应的百分比,。
        for i in range(1,256):
            hs[i]=h[i]/sum
            hp[i]=hs[i]+hp[i-1]

        # 改变图像值：
        for i in range(1,255):
            index=np.where(img==i)
            g[index]=hp[i]*255
        # 显示图像
        x = [i for i in range(256)]
        # 统计改变之后的图像灰度值！
        y=[0]*256
        for i in range(hang):
            for j in range(lie):
                y[g[i][j]] += 1
        plt.bar(x,y,width=1.0)
        plt.show()
        return g


img = cv2.imread(r'images\morning.jpg', 0)  # 读取图片
My_Histogram.my_histogram(img)
out=My_Histogram.my_hist_equal(img)
cv_show(img,'past')
cv_show(out,'now')
