from __future__ import print_function
import os, sys, zipfile
import json
import shutil

def convert(size, box):
    dw = 1. / (size[0])
    dh = 1. / (size[1])
    x = box[0] + box[2] / 2.0
    y = box[1] + box[3] / 2.0
    w = box[2]
    h = box[3]

    x = x * dw
    w = w * dw
    y = y * dh
    h = h * dh
    return (x, y, w, h)


json_file = '/media/sda4/tongan_project/PyTorch-YOLOv3-master/data/coco/annotations/instances_train2014.json'  # # Object Instance 类型的标注

data = json.load(open(json_file, 'r'))

ana_txt_save_path = "/media/sda4/tongan_project/PyTorch-YOLOv3-master/data/custom3"  # 保存的路径
if not os.path.exists(ana_txt_save_path):
    os.makedirs(ana_txt_save_path)
ana_labels_path=ana_txt_save_path+"/labels" #labesl文件夹
ana_images_path=ana_txt_save_path+"/images" #images文件夹
coco_path = "/media/sda4/tongan_project/PyTorch-YOLOv3-master/data/coco"
num=0
num1=num2=num3=num4=num6=num8=0
num11=num22=num33=num44=num66=num88=0
nu1=nu2=nu3=nu4=nu6=nu8=0
cot1=0
cot2=0
f_train_txt1 = open(os.path.join(ana_txt_save_path, "train.txt"), 'w')  # train_txt保存训练集每张图片的路径
f_train_txt2 = open(os.path.join(ana_txt_save_path, "valid.txt"), 'w')

for img in data['images']:
    # print(img["file_name"])
    filename = img["file_name"]
    img_width = img["width"]
    img_height = img["height"]
    # print(img["height"])
    # print(img["width"])
    img_id = img["id"]
    ana_txt_name = filename.split(".")[0] + ".txt"  # 对应的txt名字，与jpg一致
    pic_name=filename.split(".")[0]+".jpg"
    pic_path = coco_path + "/train2014/" + pic_name
    if(os.path.exists(pic_path)):
        #print(ana_txt_name)
        f_txt = open(os.path.join(ana_labels_path, ana_txt_name), 'w')#每行labels保存的路径
        cot=0
        for ann in data['annotations']:
            if ann['image_id'] == img_id:
                #annotation.append(ann)
                #print(ann["category_id"], ann["bbox"])
                box = convert((img_width, img_height), ann["bbox"])
                if(ann["category_id"]==1 or ann["category_id"]==2 or ann["category_id"]==3 or ann["category_id"]==4 or ann["category_id"]==6 or ann["category_id"]==8):
                    if (ann["category_id"]==1):
                        num1=num1+1
                        f_txt.write("0 %s %s %s %s\n" % (box[0], box[1], box[2], box[3]))
                    if (ann["category_id"]==2):
                        num2=num2+1
                        f_txt.write("1 %s %s %s %s\n" % (box[0], box[1], box[2], box[3]))
                    if (ann["category_id"]==3):
                        num3=num3+1
                        f_txt.write("2 %s %s %s %s\n" % (box[0], box[1], box[2], box[3]))
                    if (ann["category_id"]==4):
                        num4=num4+1
                        f_txt.write("3 %s %s %s %s\n" % (box[0], box[1], box[2], box[3]))
                    if (ann["category_id"]==6):
                        num6=num6+1
                        f_txt.write("4 %s %s %s %s\n" % (box[0], box[1], box[2], box[3]))
                    if (ann["category_id"]==8):
                        num8=num8+1
                        f_txt.write("6 %s %s %s %s\n" % (box[0], box[1], box[2], box[3]))

                    cot=cot+1
        f_txt.close()
        if (cot==0):
            ana_txt_name=ana_labels_path+"/"+ana_txt_name
            if(os.path.exists(ana_txt_name)):
                os.remove(ana_txt_name)
                print(ana_txt_name)
                print("删除成功")
        else:
            num=num+1
            if (ann["category_id"]==1):
                num11=num11+1
            if (ann["category_id"]==2):
                num22=num22+1
            if (ann["category_id"]==3):
                num33=num33+1
            if (ann["category_id"]==4):
                num44=num44+1
            if (ann["category_id"]==6):
                num66=num66+1
            if (ann["category_id"]==8):
                num88=num88+1
            new_path = ana_images_path + "/" + pic_name
            print(new_path)
            print("添加成功")
            if (ann["category_id"] == 1):
                if(nu1<5):
                    f_train_txt1.write("%s\n" % new_path)
                    nu1 = nu1 + 1
                    cot1=cot1+1
                else:
                    f_train_txt2.write("%s\n" % new_path)
                    nu1 = 0
                    cot2=cot2+1
            if (ann["category_id"] == 2):
                if (nu1 < 5):
                    f_train_txt1.write("%s\n" % new_path)
                    nu2 = nu2 + 1
                    cot1=cot1+1
                else:
                    f_train_txt2.write("%s\n" % new_path)
                    nu2 = 0
                    cot2=cot2+1
            if (ann["category_id"] == 3):
                if (nu1 < 5):
                    f_train_txt1.write("%s\n" % new_path)
                    nu3 = nu3 + 1
                    cot1=cot1+1
                else:
                    f_train_txt2.write("%s\n" % new_path)
                    nu3 = 0
                    cot2=cot2+1
            if (ann["category_id"] == 4):
                if (nu1 < 5):
                    f_train_txt1.write("%s\n" % new_path)
                    nu4 = nu4 + 1
                    cot1=cot1+1
                else:
                    f_train_txt2.write("%s\n" % new_path)
                    nu4 = 0
                    cot2=cot2+1
            if (ann["category_id"] == 6):
                if (nu1 < 5):
                    f_train_txt1.write("%s\n" % new_path)
                    nu6 = nu6 + 1
                    cot1=cot1+1
                else:
                    f_train_txt2.write("%s\n" % new_path)
                    nu6 = 0
                    cot2=cot2+1
            if (ann["category_id"] == 8):
                if (nu1 < 5):
                    f_train_txt1.write("%s\n" % new_path)
                    nu8 = nu8 + 1
                    cot1=cot1+1
                else:
                    f_train_txt2.write("%s\n" % new_path)
                    nu8 = 0
                    cot2=cot2+1

            #把图片复制到images文件夹下
            shutil.copy(pic_path, new_path)
            #if (num == 2):
               # b
print(num1,num2,num3,num4,num6,num8)
print(num,num11,num22,num33,num44,num66,num88)

print(cot,cot1,cot2)
f_train_txt1.close()
f_train_txt2.close()
