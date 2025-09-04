# from PIL import Image
# class node:#节点的类#定义节点构造方法
#     def __init__(self, right=None, left=None, parent=None, weight=0, code=None):
#         self.left = left
#         self.right = right
#         self.parent = parent
#         self.weight = weight#权重
#         self.code = code#节点值
# def picture_convert(filename,newfilename):
#     picture = Image.open(filename)
#     picture = picture.convert('L')#将bmp图片转换为灰值图
#     picture.save(newfilename)#保存灰值图像
#     return picture #返回转换后的图片对象
#
# #统计每个像素出现的次数
# def pixel_number_caculate(list):
#     pixel_number={}
#     for i in list:
#         if i not in pixel_number.keys():
#             pixel_number[i]=1 #若此像素点不在字符频率字典里则直接添加
#         else:
#             pixel_number[i] += 1 #若存在在字符频率字典里则对应值加一
#     return pixel_number
#
# #构造节点，分别赋予其值和对应的权值
# def node_construct(pixel_number):
#     node_list = []
#     for i in range(len(pixel_number)):
#         node_list.append(node(weight=pixel_number[i][1], code=str(pixel_number[i][0])))
#     return node_list
#     #构造霍夫曼树
# def tree_construct(listnode):
#     listnode = sorted(listnode, key=lambda node:node.weight)
#     while len(listnode) != 1:
# #每次取最小权值的两个像素点进行合并
#         low_node0,low_node1 = listnode[0], listnode[1]
#         new_change_node = node()
#         new_change_node.weight = low_node0.weight + low_node1.weight
#         new_change_node.left = low_node0
#         new_change_node.right = low_node1
#         low_node0.parent = new_change_node
#         low_node1.parent = new_change_node
#         listnode.remove(low_node0)
#         listnode.remove(low_node1)
#         listnode.append(new_change_node)
#         #将每次更新后的node列表按权值进行排序
#         listnode = sorted(listnode, key=lambda node:node.weight)
#     return listnode
#     # 编码函数，返回编码表以及编码结果
# def Huffman_Coding(picture):
#     #得到图片的宽度和高度
#     width = picture.size[0]
#     height = picture.size[1]
#     im = picture.load()
#     print ("灰度图宽为"+str(width)+"像素" )
#     print ("灰度图高为"+str(height)+"像素")
#
#     # 将像素点保存在list中，原来的二维矩阵变为一维数组
#     list = []
#     for i in range(width):
#         for j in range(height):
#             list.append(im[i,j])
#     # 统计每个像素点的次数，并根据出现的次数由小到大排序
#     pixel_number = pixel_number_caculate(list)
#     pixel_number = sorted(pixel_number.items(),key=lambda item:item[1])
#     # 根据像素点的值和其出现次数构造节点list
#     node_list = node_construct(pixel_number)
#     # 构造霍夫曼树，保存头结点
#     head = tree_construct(node_list)[0]
#     # 构造编码表
#     coding_table = {}
#     for e in node_list:
#         new_change_node = e
#         coding_table.setdefault(e.code,"")
#         while new_change_node!=head:
#             if new_change_node.parent.left == new_change_node:
#                 coding table[e.code] = "1” + coding table[e.codelelse:
#     coding
#     table[e.code] = "g” + coding table[e.codelnew change node = new change node.parent
#     # 输出每个像素点灰度值和编码for key in coding table.keys():print (”信源像素点”+ key+"霍夫曼编码后的码字为:“+ coding table[key])
# coding:utf-8
from PIL import Image


# 构造节点的类
class node:
    # 定义节点构造方法
    def __init__(self, right=None, left=None, parent=None, weight=0, code=None):
        self.left = left
        self.right = right
        self.parent = parent
        self.weight = weight  # 权重
        self.code = code  # 节点值


# 将彩色图转为灰色图，此时图像的每个像素点可以用单独的像素值表示
def picture_convert(filename, newfilename):
    picture = Image.open(filename)
    # 将bmp图片转换为灰值图
    picture = picture.convert('L')
    # 保存灰值图像
    picture.save(newfilename)
    # 返回转换后的图片对象
    return picture


# 统计每个像素出现的次数
def pixel_number_caculate(list):
    pixel_number = {}
    for i in list:
            # 若此像素点不在字符频率字典里则直接添加
        if i not in pixel_number.keys():
            pixel_number[i] = 1
        # 若存在在字符频率字典里则对应值加 1
        else:
            pixel_number[i] += 1
    return pixel_number


# 构造叶子节点，分别赋予其值和对应的权值
def node_construct(pixel_number):
    node_list = []
    for i in range(len(pixel_number)):
        node_list.append(node(weight=pixel_number[i][1], code=str(pixel_number[i][0])))
    return node_list


# 构造霍夫曼树
def tree_construct(listnode):
    # 首先将待处理的节点按照权值从小到大排序
    listnode = sorted(listnode, key=lambda node: node.weight)
    while len(listnode) != 1:
        # 每次取最小权值的两个像素点进行合并
        low_node0, low_node1 = listnode[0], listnode[1]
        new_change_node = node()
        # 合并后的新节点权值为两个子节点权值之和
        new_change_node.weight = low_node0.weight + low_node1.weight
        # 将两个子节点作为新节点的左右子节点
        new_change_node.left = low_node0
        new_change_node.right = low_node1
        # 更新子节点的父节点为新节点
        low_node0.parent = new_change_node
        low_node1.parent = new_change_node
        # 从节点列表中移除已经合并的子节点，并加入新生成的节点
        listnode.remove(low_node0)
        listnode.remove(low_node1)
        listnode.append(new_change_node)
        # 将每次更新后的node列表按权值进行排序
        listnode = sorted(listnode, key=lambda node: node.weight)
    return listnode


# 编码函数，返回编码表以及编码结果
def Huffman_Coding(picture):
    # 得到图片的宽度和高度
    width = picture.size[0]
    height = picture.size[1]
    im = picture.load()#读取图片的像素信息，赋值给im
    print("灰度图宽为" + str(width) + "像素")
    print("灰度图高为" + str(height) + "像素")

    # 将像素点保存在list中，原来的二维矩阵变为一维数组
    list = []
    for i in range(width):
        for j in range(height):
            list.append(im[i, j])#将像素值添加到列表中

    # 统计每个像素点的次数，并根据出现的次数由小到大排序
    pixel_number = pixel_number_caculate(list)
    pixel_number = sorted(pixel_number.items(), key=lambda item: item[1])
    # for key in pixel_number:
    #     print("像素值为："+str(key)+"像素个数： "+str(pixel_number[key]))
    # print(type(pixel_number))
    # print(pixel_number)
    # print(type(pixel_number[1]))
    # print(pixel_number[1][1])

    # 根据像素点的值和其出现次数构造节点list
    node_list = node_construct(pixel_number)

    # 构造霍夫曼树,保存头结点
    head = tree_construct(node_list)[0]

    # 构造编码表
    coding_table = {}#创建一个空字典，用于存储每个像素值的编码
    for e in node_list:#遍历霍夫曼树的叶子节点
        new_change_node = e#将当前节点赋值给新节点
        coding_table.setdefault(e.code, "")#为当前节点的像素值设置默认编码为空字符串
        while new_change_node != head:#如果新节点不是头结点，则继续往上遍历
            if new_change_node.parent.left == new_change_node:#如果新节点在父节点的左子树中
                coding_table[e.code] = "1" + coding_table[e.code]#则将编码表中该像素值的编码前面添加一个"1"
            else:#如果新节点在父节点的右子树中
                coding_table[e.code] = "0" + coding_table[e.code]#则将编码表中该像素值的编码前面添加一个"0"
            new_change_node = new_change_node.parent#将当前节点赋值为其父节点，继续往上遍历
    ave=0.0
    # 输出每个像素点灰度值和编码
    num=0
    for key in coding_table.keys():#遍历编码表中的每个键（即像素值）
        print("信源像素点" + key + "霍夫曼编码后的码字为:" + coding_table[key])
        ave +=len(coding_table[key])*pixel_number[num][1]/(width*height)
        # print(pixel_number[num][1])
        # print(len(coding_table))
        # print(width*height)
        # ave += len(coding_table[key])/(len(coding_table))
        # print(len(coding_table[key]))
        num=num+1
    print("哈夫曼平均编码长度: "+ str (ave))
    print("不同灰度值的像素种类： "+ str(len(coding_table)))
    # print(num)
    # 输出编码表
    print("编码表为:", coding_table)
    # 将图像的编码结果转换成字符串并保存到txt里
    coding_result = ''#创建一个空字符串，用于存储图像的编码结果
    for i in range(width):#遍历图片宽度
        for j in range(height):#遍历图片高度
            for key, values in coding_table.items():#遍历编码表，获取每个键值对
                if str(im[i, j]) == key:#如果像素值与当前键相等
                    coding_result = coding_result + values#将当前键对应的编码添加到编码结果字符串中
    file = open('coding_result.txt', 'w')#打开一个名为'coding_result.txt'的文件，以写入模式打开
    file.write(coding_result)#将编码结果字符串写入文件中

    return width, height, coding_table, coding_result#返回图片宽度、高度、编码表和编码结果字符串


# 利用编码表进行译码
def Decoding(width, height, coding_table, coding_result):
    code_read_now = ''  # 定义一个字符串存储当前读到的编码
    new_pixel = []  # 存储新图像的像素值
    i = 0
    while (i != coding_result.__len__()):# 循环读取编码结果
        # 每次往后读一位
        code_read_now = code_read_now + coding_result[i]
        for key in coding_table.keys():    # 遍历编码表
            # 如果当前读到的编码在编码表里存在
            if code_read_now == coding_table[key]:
                new_pixel.append(key) # 将该编码对应的像素值添加到new_pixel列表中
                code_read_now = ''# 当前读到的编码清空
                break
        i += 1# 继续读取下一个编码

    # 构造新图像
    decode_image = Image.new('L', (width, height))#使用Image.new()函数创建一个新的灰度图像对象，并将其大小设置为(width, height)
    k = 0
    # 将new_pixel中的像素值赋予新图像
    for i in range(width):
        for j in range(height):
            decode_image.putpixel((i, j), (int(new_pixel[k])))
            k += 1
    decode_image.save('decode.bmp')# 将解码后的图像保存为decode.bmp文件
    print("译码已经完成: 图片存储为decode.bmp")#显示提示


# Main 函数
if __name__ == '__main__':
    picture = picture_convert(r'images/couple.bmp', 'images/new.bmp')#将位于'images/couple.bmp'路径下的一张图片转换成新的BMP格式，并保存在'images/new.bmp'路径下。
    width, height, coding_table, coding_result = Huffman_Coding(picture)#新生成的图片进行哈夫曼编码（Huffman coding）。函数Huffman_Coding返回四个变量：图片的宽度、高度、编码表和编码结果。
    Decoding(width, height, coding_table, coding_result)#调用Decoding函数对编码结果进行解码，还原出原始的图像。
