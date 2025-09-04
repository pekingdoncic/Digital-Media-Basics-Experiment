# import numpy as np
# import matplotlib.pyplot as plt
#
# # 输入图像的不同灰度值个数
# gray_levels = [0, 1, 2, 3, 4, 5,6,7,8,9,10,11,12,13,14,15]  # 灰度级别
# pixel_counts = [800, 650, 600, 430, 300, 230,200,170,150,130,110,96,80,70,50,30]  # 对应灰度级别的像素数量
#
# # 绘制直方图
# plt.bar(gray_levels, pixel_counts)
#
# # 设置标题和轴标签
# plt.title('Histogram')
# plt.xlabel('Gray Levels')
# plt.ylabel('Pixel Counts')
#
# # 显示直方图
# plt.show()

# import numpy as np
# import matplotlib.pyplot as plt
#
# # 输入16个不同灰度值的个数
# gray_levels = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]  # 灰度级别
# pixel_counts = [800, 650, 600, 430, 300, 230,200,170,150,130,110,96,80,70,50,30]  # 对应灰度级别的像素数量
#
# # 绘制原始直方图
# plt.bar(gray_levels, pixel_counts)
# plt.title('Original Histogram')
# plt.xlabel('Gray Levels')
# plt.ylabel('Pixel Counts')
# plt.show()
#
# # 计算累积分布函数
# cdf = np.cumsum(pixel_counts)
# print(cdf.max())
# cdf_normalized = cdf / cdf.max()
# # print(cdf_normalized)
# # 计算均衡化后的直方图
# equalized_pixel_counts = np.round(cdf_normalized * 800).astype(int)
# gray_level=np.round(cdf_normalized*16).astype(int)
# # for i in 16:
# #     for j in 16:
# #         if()
# print(gray_level)
# # print(pixel_counts[-1])
# # 绘制均衡化后的直方图
# plt.bar(gray_level, equalized_pixel_counts)
# plt.title('Equalized Histogram')
# plt.xlabel('Gray Levels')
# plt.ylabel('Pixel Counts')
# # plt.hist(16,pixel_counts)
# plt.show()

# import cv2
# import matplotlib.pyplot as plt
# import numpy as np
# img = cv2.imread(r'C:\Users\R9000X\Desktop\gray.png', 0)  # 读取图片
# plt.hist(img.ravel(), 256)  # 直方图函数，输入为一维数据
# plt.show()
#
# # 计算累积分布函数
# cdf = np.cumsum(img.ravel())
# cdf_normalized = cdf / cdf.max()
# # 计算均衡化后的直方图
# equalized_pixel_counts = np.round(cdf_normalized * 8).astype(int)
# gray_level=np.round(cdf_normalized*16).astype(int)

# 将彩色图像转换为灰度图像
# gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# cv2.imshow('Gray Image', gray_image,gray_image)
# def cv_show(img, name):
#     cv2.imshow(name, img)
#     cv2.waitKey(0)  # 等待输入任意键，注意必须是英文
#     cv2.destroyAllWindow()
#
# img = cv2.imread(r'C:\Users\R9000X\Desktop\mountains.jpg', 0)  # 灰度图
# # print(type(img))
# plt.hist(img.ravel(), 256)
# plt.show()
#
# equ = cv2.equalizeHist(img)  # 均衡化
# print(equ)
# plt.hist(equ.ravel(), 256)  # 显示均衡化后的直方图
# plt.show()
#
# res = np.hstack((img, equ))  # 显示原图和均衡化后图片
# cv_show(res, 'res')

# import cv2
# import numpy as np
# import matplotlib.pyplot as plt
#
# # 读取灰度图像
# gray_image = cv2.imread(r'C:\Users\R9000X\Desktop\gray.png', cv2.IMREAD_GRAYSCALE)
#
# # 计算直方图
# hist, bins = np.histogram(gray_image.flatten(), bins=256, range=[0, 256])
#
# # 计算累计直方图
# cumulative_hist = np.cumsum(hist)
#
# # 绘制直方图
# plt.figure(figsize=(12, 6))
# plt.subplot(1, 2, 1)
# plt.plot(hist, color='black')
# plt.title('Histogram')
# plt.xlabel('Pixel Value')
# plt.ylabel('Frequency')
#
# # 绘制累计直方图
# plt.subplot(1, 2, 2)
# plt.plot(cumulative_hist, color='black')
# plt.title('Cumulative Histogram')
# plt.xlabel('Pixel Value')
# plt.ylabel('Cumulative Frequency')
#
# # 显示图像
# plt.tight_layout()
# plt.show()

import cv2
import numpy as np
import matplotlib.pyplot as plt

# 读取灰度图像
gray_image = cv2.imread(r'C:\Users\R9000X\Desktop\gray.png', cv2.IMREAD_GRAYSCALE)

# 计算直方图
hist, bins = np.histogram(gray_image.flatten(), bins=256, range=[0, 256])

# 计算累计直方图
cumulative_hist = np.cumsum(hist)

# 进行直方图均衡化
equalized_image = cv2.equalizeHist(gray_image)

# 计算均衡化后的直方图
equalized_hist, _ = np.histogram(equalized_image.flatten(), bins=256, range=[0, 256])

# 计算均衡化后的累计直方图
equalized_cumulative_hist = np.cumsum(equalized_hist)

# 绘制原始图像的直方图
plt.figure(figsize=(12, 6))
plt.subplot(2, 2, 1)
plt.plot(hist, color='black')
plt.title('Original Histogram')
plt.xlabel('Pixel Value')
plt.ylabel('Frequency')

# 绘制原始图像的累计直方图
plt.subplot(2, 2, 2)
plt.plot(cumulative_hist, color='black')
plt.title('Original Cumulative Histogram')
plt.xlabel('Pixel Value')
plt.ylabel('Cumulative Frequency')

# 绘制均衡化后的图像的直方图
plt.subplot(2, 2, 3)
plt.plot(equalized_hist, color='black')
plt.title('Equalized Histogram')
plt.xlabel('Pixel Value')
plt.ylabel('Frequency')

# 绘制均衡化后的图像的累计直方图
plt.subplot(2, 2, 4)
plt.plot(equalized_cumulative_hist, color='black')
plt.title('Equalized Cumulative Histogram')
plt.xlabel('Pixel Value')
plt.ylabel('Cumulative Frequency')


# 显示均衡化后的图像
plt.figure(figsize=(8, 8))
plt.imshow(equalized_image, cmap='gray')
plt.title('Equalized Image')
plt.axis('off')
# 显示图像
plt.tight_layout()
plt.show()
cv2
