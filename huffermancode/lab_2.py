from PIL import Image
import numpy as np
# 导入所需的库

# 嵌入过程
# cover = Image.open('cover.jpg')
# cover = cover.convert('RGB')
# cover = np.asarray(cover)
# cover 数组被转换成只读数组，导致不能对其赋值。添加 copy=True
cover = Image.open(r'images/cover.jpg').convert('RGB')
cover = np.array(cover, copy=True)# 将封面图像转换为数组

msg = Image.open(r'images/msg_1.png')
# 转换成二值图像，因为 msg 变量没有经过转换，应该将其转换成二值图像以便嵌入信息。
msg = msg.convert('1')# 将图像转换为二值图像（黑白）

# msg = np.asarray(msg)
msg = msg.resize((cover.shape[1], cover.shape[0]))  # 修改代码，将msg的大小改为和cover相同
msg = np.array(msg, copy=True)# 将调整后的消息图像转换为数组

# 嵌入过程
# 遍历封面图像的每个像素
for i in range(cover.shape[0]):
    for j in range(cover.shape[1]):
        if cover[i, j, 0] % 2 == 1:# 如果封面像素的红色通道值是奇数
            if cover[i, j, 0] != 255:# 如果红色通道值不等于255，则将其加1
                cover[i, j, 0] += 1
            else: # 否则，将其减1
                cover[i, j, 0] -= 1
        if msg[i, j]:# 如果相应的消息像素是白色（1），则将红色通道值加1
            cover[i, j, 0] += 1
cover = Image.fromarray(np.uint8(cover))# 将修改后的封面数组转换回图像
cover.save('encoded_cover.png')# 保存编码后的封面图像

# 提取过程
encoded = Image.open('encoded_cover.png')# 打开编码后的封面图像
encoded = encoded.convert('RGB')# 将编码后的封面图像转换为数组
encoded = np.asarray(encoded)
# decoded = np.random.randint(0, 1, size=(encoded.shape[0], encoded.shape[1]))
decoded = np.zeros((encoded.shape[0], encoded.shape[1]), dtype=np.bool_)  # 使用布尔类型存储提取的信息
# 遍历编码后的封面图像的每个像素
for i in range(encoded.shape[0]):
    for j in range(encoded.shape[1]):
        if encoded[i, j, 0] % 2 == 1:# 如果编码后的封面像素的红色通道值是奇数，则将提取数组对应位置的像素设为1
            decoded[i, j] = 1
        else:    # 否则，将其设为0
            decoded[i, j] = 0
# cover = Image.fromarray(np.bool_(decoded))
# 转换成灰度图像，因为提取出的信息是布尔类型，需要将其转换成灰度图像以便保存。
cover = Image.fromarray(np.uint8(decoded * 255))# 将提取的数组转换为图像
cover.save('decoded.png')# 保存提取的图像
