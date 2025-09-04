# import cv2
# import numpy as np
#
# # 读取灰度图像
# image = cv2.imread(r"images/Couple.bmp", cv2.IMREAD_GRAYSCALE)
#
# if image is None:
#     print("Failed to read image")
#     exit()
#
# # 计算直方图
# hist = cv2.calcHist([image], [0], None, [256], [0, 256])
#
# # 查找直方图谷底的阈值
# threshold = 0
# min_val = np.inf
# for i in range(1, len(hist) - 1):
#     prev_val = hist[i - 1][0]
#     curr_val = hist[i][0]
#     next_val = hist[i + 1][0]
#
#     if curr_val < prev_val and curr_val < next_val and curr_val < min_val:
#         min_val = curr_val
#         threshold = i
#
# # 图像二值化
# _, binary_image = cv2.threshold(image, threshold, 255, cv2.THRESH_BINARY)
#
# # 显示原始图像和二值化图像
# cv2.imshow("Original Image", image)
# cv2.imshow("Binary Image", binary_image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# import cv2
# import numpy as np
#
# # 读取二值图像
# image = cv2.imread(r"images/noise.bmp", cv2.IMREAD_GRAYSCALE)
#
# if image is None:
#     print("Failed to read image")
#     exit()
#
# # 定义结构元素
# kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
#
# # 开操作去除噪声
# result = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)
#
# # 显示原始图像和处理后的图像
# cv2.imshow("Original Image", image)
# cv2.imshow("Processed Image", result)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# #实现区域生长图像分割
# import cv2
# import numpy as np
# def region_growing(image, seed):
#     # 创建空的标记图像，与原始图像相同大小，用于记录分割结果
#     height, width = image.shape[:2]
#     segmented = np.zeros((height, width), dtype=np.uint8)
#
#     # 记录生长区域的像素点
#     region_points = []
#
#     # 获取种子点的灰度值
#     seed_value = image[seed[0], seed[1]]
#
#     # 定义生长方向（上、下、左、右）
#     directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
#
#     # 将种子点添加到生长区域中
#     region_points.append(seed)
#
#     while len(region_points) > 0:
#         # 取出当前待生长的像素点
#         current_point = region_points.pop(0)
#
#         # 遍历当前像素点的邻域
#         for direction in directions:
#             x = current_point[0] + direction[0]
#             y = current_point[1] + direction[1]
#
#             # 判断邻域像素点是否在图像范围内
#             if x >= 0 and x < height and y >= 0 and y < width:
#                 # 判断邻域像素点是否已经被访问过
#                 if segmented[x, y] == 0:
#                     # 计算邻域像素点与种子点的灰度差值
#                     diff = abs(int(image[x, y]) - int(seed_value))
#
#                     # 判断差值是否满足生长条件
#                     if diff <= threshold:
#                         # 将邻域像素点标记为属于生长区域
#                         segmented[x, y] = 255
#
#                         # 将邻域像素点添加到生长区域中
#                         region_points.append((x, y))
#
#     return segmented
#
#
# # 读取图像
# image = cv2.imread(r"images/test.bmp", 0)
#
# # 设置种子点
# seed_point = (100, 100)
#
# # 设置生长阈值
# threshold = 10
#
# # 进行区域生长分割
# segmented_image = region_growing(image, seed_point)
#
# # 显示原始图像和分割结果
# cv2.imshow('Original Image', image)
# cv2.imshow('Segmented Image', segmented_image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# #实现otsu图像分割
# import cv2
# def otsu_threshold(image):
#     # 将图像转换为灰度图像
#     gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#
#     # 使用OTSU算法计算最佳阈值
#     _, threshold = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
#
#     # 对图像进行阈值分割
#     segmented_image = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
#
#     return segmented_image
#
#
# # 读取图像
# image = cv2.imread(r"images/source.bmp")
#
# # 使用OTSU方法进行图像分割并进行阈值分割
# segmented_image = otsu_threshold(image)
#
# # 显示原始图像和分割结果
# cv2.imshow('Original Image', image)
# cv2.imshow('Segmented Image', segmented_image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# 编程实现求目标的骨架
# import cv2
# import numpy as np
# from skimage.morphology import skeletonize
#
# # 读取图像
# image = cv2.imread(r"images/source.bmp", 0)
#
# # 二值化图像
# _, binary_image = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
#
# # 骨架化
# skeleton = skeletonize(binary_image)
#
# # 将骨架转换为灰度图像
# skeleton_image = np.where(skeleton, 255, 0).astype(np.uint8)
#
# # 显示原始图像和骨架图像
# cv2.imshow('Original Image', image)
# cv2.imshow('Skeleton Image', skeleton_image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# import cv2
# import numpy as np
# from skimage.morphology import skeletonize
#
# # 读取图像
# image = cv2.imread(r"images/source.bmp", 0)
#
# # 自适应阈值二值化图像
# binary_image = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
#
# # 骨架化
# skeleton = skeletonize(binary_image)
#
# # 将骨架转换为灰度图像
# skeleton_image = np.where(skeleton, 255, 0).astype(np.uint8)
#
# # 显示原始图像和骨架图像
# cv2.imshow('Original Image', image)
# cv2.imshow('Skeleton Image', skeleton_image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# import cv2
# import numpy as np
# from skimage.morphology import skeletonize
#
# # 读取图像
# image = cv2.imread(r"images/source.bmp", 0)
#
# # 二值化图像
# _, binary_image = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
#
# # 将二值化图像转换为只包含0和1的图像
# binary_image = binary_image.astype(bool)
#
# # 骨架化
# skeleton = skeletonize(binary_image)
#
# # 将骨架转换为灰度图像
# skeleton_image = np.where(skeleton, 255, 0).astype(np.uint8)
#
# # 显示原始图像和骨架图像
# cv2.imshow('Original Image', image)
# cv2.imshow('Skeleton Image', skeleton_image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

#hough变换：

# import cv2
# import numpy as np
#
# # 读取图像并转为灰度图像
# image = cv2.imread(r"images/source.bmp")
# gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#
# # 边缘检测
# edges = cv2.Canny(gray_image, 50, 150)
#
# # Hough变换
# lines = cv2.HoughLines(edges, 1, np.pi/180, threshold=100)
#
# # 绘制检测到的直线
# if lines is not None:
#     for line in lines:
#         rho, theta = line[0]
#         a = np.cos(theta)
#         b = np.sin(theta)
#         x0 = a * rho
#         y0 = b * rho
#         x1 = int(x0 + 1000 * (-b))
#         y1 = int(y0 + 1000 * (a))
#         x2 = int(x0 - 1000 * (-b))
#         y2 = int(y0 - 1000 * (a))
#         cv2.line(image, (x1, y1), (x2, y2), (0, 0, 255), 2)
#
# # 显示原始图像和检测到的直线
# cv2.imshow('Original Image', image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
import cv2
import numpy as np

# 读取图像并转为灰度图像
image = cv2.imread(r"images/source.bmp")
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 边缘检测
edges = cv2.Canny(gray_image, 50, 150)

# Hough变换
lines = cv2.HoughLines(edges, 1, np.pi/180, threshold=100)

# 绘制检测到的直线
if lines is not None:
    for line in lines:
        rho, theta = line[0]
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a * rho
        y0 = b * rho
        x1 = int(x0 + 1000 * (-b))
        y1 = int(y0 + 1000 * (a))
        x2 = int(x0 - 1000 * (-b))
        y2 = int(y0 - 1000 * (a))
        cv2.line(image, (x1, y1), (x2, y2), (0, 0, 255), 2, cv2.LINE_AA)

# 显示原始图像和检测到的直线
cv2.imshow('Original Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
