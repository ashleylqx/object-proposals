import scipy.misc
import scipy.io
import cv2
import numpy as np
import pdb
from random import randint
img_name = 'COCO_train2014_000000365817'
#img_name = 'COCO_train2014_000000467063'
#img_name = 'COCO_train2014_000000458025'
rgb_ima = '/research/dept2/qxlai/DataSets/MS_COCO/train2014/'+img_name+'.jpg' #'i1000274881.jpeg'
box_path = '/research/dept2/qxlai/DataSets/MS_COCO/MCG_boxes/MCG-COCO-train2014-boxes/'+img_name+'.mat'

save_path = img_name + '_mcg_2.jpg'
color=(0,0,255)

#image = scipy.misc.imread(rgb_ima, mode='RGB')
image = cv2.imread(rgb_ima)
h,w,_ = image.shape
#boxes = scipy.io.loadmat(box_path)['proposals'][0][0][0][:20,:]
boxes = scipy.io.loadmat(box_path)['boxes'][:20, :]
pdb.set_trace()
print('cv2: h, w, c', image.shape)

#for cord in boxes:
for idx in range(boxes.shape[0]):
    cord = boxes[idx, :]
    print(cord)
    #pt1, pt2 = (cord[0], cord[1]) , (cord[2], cord[3])
    pt1, pt2 = (cord[1], cord[0]) , (cord[3], cord[2])
    pt1 = int(pt1[0]), int(pt1[1])
    pt2 = int(pt2[0]), int(pt2[1])
    #pdb.set_trace()
    cv2.rectangle(image, pt1, pt2, color, 2)
    color = [randint(0, 255), randint(0, 255), randint(0, 255)]

cv2.imwrite(save_path, image)
