import scipy.misc
import scipy.io
import cv2
import numpy as np
import pdb
from random import randint
#img_name = 'i2206349266.jpeg'
img_name = 'i1000274881.jpeg'
rgb_ima = '/research/dept2/qxlai/DataSets/MIT1003/ALLSTIMULI/'+img_name #'i1000274881.jpeg'
#box_path = '/research/dept2/qxlai/DataSets/MIT1003/randomPrim/randomPrim/'+img_name+'.mat'  #'i1000274881.jpeg.mat'
box_path = '/research/dept2/qxlai/DataSets/MIT1003/eb500/' + img_name.split('.')[0] + '_bboxes.mat'
save_path = img_name.replace('.jpeg', '_eb.jpeg')  #'i1000274881_rP.jpeg'
color=(0,0,255)

#image = scipy.misc.imread(rgb_ima, mode='RGB')
image = cv2.imread(rgb_ima)
h,w,_ = image.shape
#boxes = scipy.io.loadmat(box_path)['proposals'][0][0][0][:20,:]
boxes = scipy.io.loadmat(box_path)['bboxes'][:20, :]
#pdb.set_trace()
print('cv2: h, w, c', image.shape)

#for cord in boxes:
for idx in range(boxes.shape[0]):
    cord = boxes[idx, :]
    print(cord)
    pt1, pt2 = (cord[0], cord[1]) , (cord[2], cord[3])
    pt1 = min(int(pt1[0]*w), int(w)), min(int(pt1[1]*h), int(h))
    pt2 = min(int(pt2[0]*w), int(w)), min(int(pt2[1]*h), int(h))
    #pdb.set_trace()
    cv2.rectangle(image, pt1, pt2, color, 2)
    color = [randint(0, 255), randint(0, 255), randint(0, 255)]

cv2.imwrite(save_path, image)
