import zipfile
import os
from PIL import Image
import cv2 as cv
import numpy as np
import random
import pickle
import time

# 生成train.txt和test.txt两个索引文件
train_txt_path = os.path.join(r"E:\class_learning\junior_practice\code\yolov7-u7\datasets\light", "train0.txt")
train_dir = os.path.join(r"E:\class_learning\junior_practice\code\yolov7-u7\datasets\light", "images")


# valid_txt_path = os.path.join("/home/aistudio/data", "test.txt")
# valid_dir = os.path.join("/home/aistudio/data", "test")

def gen_txt(txt_path, img_dir):
    f = open(txt_path, 'w')

    img_list = os.listdir(img_dir)  # 获取类别文件夹下所有png图片的路径
    for i in range(len(img_list)):
        if not img_list[i].endswith('jpg'):  # 若不是jpg文件，跳过
            continue
        img_path = os.path.join(img_list[i])
        line = img_path +'\n'
        f.write(line)
    f.close()

gen_txt(train_txt_path, train_dir)
# gen_txt(valid_txt_path, valid_dir)

def data_to_txt(datas, save_path):
    with open(save_path, 'w') as f:
        for i in datas:
            f.write(f'{i}\n')

# 构造带标签的数据列表
datas_with_label = []
with open(r'E:\class_learning\junior_practice\code\yolov7-u7\datasets\light\train0.txt', 'r') as f:
    for line in f.readlines():
        line = line.strip()
        datas_with_label.append(f'E:\class_learning\junior_practice\code\yolov7-u7\datasets\light\images\{line}')  # 图片绝对路径 标签
#print(datas_with_label)

# 打乱带标签的数据列表
np.random.shuffle(datas_with_label)

# 按照8:2划分训练集和验证集
train_datas = datas_with_label[len(datas_with_label)//10*2:]
val_datas = datas_with_label[:len(datas_with_label)//10*2]
print('train_datas len:', len(train_datas))
print('val_datas len:', len(val_datas))

# 写入train.txt、val.txt文件
data_to_txt(train_datas, r'E:\class_learning\junior_practice\code\yolov7-u7\datasets\light\train.txt')
data_to_txt(val_datas, r'E:\class_learning\junior_practice\code\yolov7-u7\datasets\light\val.txt')