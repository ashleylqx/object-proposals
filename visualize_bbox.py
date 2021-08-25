import scipy.misc
import scipy.io
import cv2
import numpy as np
import pdb
from random import randint
img_name = 'i2206349266.jpeg'
#img_name = 'i1000274881.jpeg'
rgb_ima = '/research/dept2/qxlai/DataSets/MIT1003/ALLSTIMULI/'+img_name #'i1000274881.jpeg'
#box_path = '/research/dept2/qxlai/DataSets/MIT1003/randomPrim/'+img_name+'.mat'  #'i1000274881.jpeg.mat'
box_path = '/research/dept2/qxlai/DataSets/MIT1003/mcg/'+img_name+'.mat'
#box_path = '/research/dept2/qxlai/DataSets/MIT1003/objectness/'+img_name+'.mat'

#save_path = img_name.replace('.jpeg', '_rP_ds.jpeg')  #'i1000274881_rP.jpeg'
save_path = img_name.replace('.jpeg', '_mcg.jpeg')
#save_path = img_name.replace('.jpeg', '_obj.jpeg')
color=(0,0,255)

#image = scipy.misc.imread(rgb_ima, mode='RGB')
image = cv2.imread(rgb_ima)
h,w,_ = image.shape
boxes = scipy.io.loadmat(box_path)['proposals'][0][0][0][:20,:]
pdb.set_trace()
print('cv2: h, w, c', image.shape)

#for cord in boxes:
for idx in range(boxes.shape[0]):
    cord = boxes[idx, :]
    print(cord)
    pt1, pt2 = (cord[0], cord[1]) , (cord[2], cord[3])
    pt1 = int(pt1[0]), int(pt1[1])
    pt2 = int(pt2[0]), int(pt2[1])
    #pdb.set_trace()
    cv2.rectangle(image, pt1, pt2, color, 2)
    color = [randint(0, 255), randint(0, 255), randint(0, 255)]

cv2.imwrite(save_path, image)
