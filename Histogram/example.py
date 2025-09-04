import cv2
import matplotlib.pyplot as plt
import numpy as np
# img = cv2.imread(r'C:\Users\R9000X\Desktop\mountains.jpg', 0)  # 读取图片
# plt.hist(img.ravel(), 256)  # 直方图函数，输入为一维数据
# plt.show()

def cv_show(img, name):
    cv2.imshow(name, img)
    cv2.waitKey(0)  # 等待输入任意键，注意必须是英文
    cv2.destroyAllWindow()

img = cv2.imread(r'images\morning.jpg', 0)  # 灰度图
# print(type(img))
plt.hist(img.ravel(), 256)
plt.show()

equ = cv2.equalizeHist(img)  # 均衡化
print(equ)
plt.hist(equ.ravel(), 256)  # 显示均衡化后的直方图
plt.show()

res = np.hstack((img, equ))  # 显示原图和均衡化后图片
cv_show(res, 'res')
