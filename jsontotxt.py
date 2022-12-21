# 处理同一个数据集下多个json文件时，仅运行一次class_txt即可
import json
import os
import numpy as np

"存储标签与预测框到txt文件中"


def convert(size,box):
    dw = 1. / size[0]
    dh = 1. / size[1]
    x = (box[0] + box[2]) / 2.0
    y = (box[1] + box[3]) / 2.0
    w = box[2] - box[0]
    h = box[3] - box[1]
    x = x * dw
    w = w * dw
    y = y * dh
    h = h * dh
    return (x,y,w,h)


def json_txt(json_path, txt_path):
    "json_path: 需要处理的json文件的路径"
    "txt_path: 将json文件处理后txt文件存放的文件夹名"

    # 生成存放json文件的路径
    if not os.path.exists(txt_path):
        os.mkdir(txt_path)
    # 读取json文件
    with open(json_path, 'r') as f:
        dict = json.load(f)
    # 得到images和annotations信息
#    images_value = dict.get("filename")  # 得到某个键下对应的值
    annotations_value = dict.get("annotations")  # 得到某个键下对应的值
    # 使用images下的图像名的id创建txt文件

    nano_path = '../datasets/light/images/'
    need_path = '../datasets/light/labels/'
    # nano_path = './images/eval'
    # need_path = './labels/val/'
    dir = os.listdir(nano_path)

    for i in dir:
        file_name = os.path.basename(i)
        file_name1=file_name.split('\\')[-1]
        file_name2 = file_name1.split('.')[0]
        print(file_name2)
        with open(need_path + file_name2 + '.txt', 'w') as f:
            for j in annotations_value:

               n=j.get("filename")
               # print(n)
               filename1 = n.split("\\")[-1]
               filename2 = filename1.split('.')[0]
               # print(filename2,"   ",file_name2)
               if(filename2==file_name2):
                   inbox_value = j.get("inbox")
                   for w in inbox_value:
                      b = w.get("color")
                      if (b=="red"):
                          bndbox_value = w.get("bndbox")
                          new_box = [bndbox_value.get(i) for i in w.get('bndbox')]
                          box=convert([2704, 1520], new_box)
                          f.write("0")
                          f.write(" ")
                          for x in box:
                             f.write(str(x))
                             f.write(" ")
                          f.write('\n')
                      if (b=="green"):
                          bndbox_value = w.get("bndbox")
                          new_box = [bndbox_value.get(i) for i in w.get('bndbox')]
                          box = convert([2704, 1520], new_box)
                          f.write("1")
                          f.write(" ")
                          for x in box:
                              f.write(str(x))
                              f.write(" ")
                          f.write('\n')
                      if (b == "yellow"):
                          bndbox_value = w.get("bndbox")
                          new_box = [bndbox_value.get(i) for i in w.get('bndbox')]
                          box = convert([2704, 1520], new_box)
                          f.write("2")
                          f.write(" ")
                          for x in box:
                              f.write(str(x))
                              f.write(" ")
                          f.write('\n')

json_txt('../datasets/light/train.json', '../datasets/light/labels/')


