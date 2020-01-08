

from PIL import Image
import cv2
import numpy as np

import json

with open('labels.json') as data_file:
    data = json.load(data_file)


# img = "0-1y-1p.png"
# image = cv2.imread(img)
# height, width, channels = image.shape
# img = image


for object in data:
    img = object['image']
    obj = object['meshes']
    image = cv2.imread(img)
    height, width, channels = image.shape
    img = image
    for shape in obj:
        print(obj[shape])
        shape = obj[shape]
        x1 = shape['x1'] * width
        x2 = shape['x2'] * width

        y1 = shape['y1'] * height 
        y2 = shape['y2'] * height 
        y1 = width - y1
        y2 = width - y2
        cv2.rectangle(img,(int(x1),int(y1)),(int(x2),int(y2)),(0,0,255),1)

    cv2.imshow('image',img)
    cv2.waitKey(0)



#img = np.zeros((500, 500, 3), np.uint8)

# red = [0,0,255]
# x1 =  0.7887953908949934 * width
# x2 = 0.8806406091209397 * width

# y1 = 0.6334476262158504 * width 
# y2 = 0.7133784295793628 * width 
# y1 = width - y1
# y2 = width - y2
# print(x1, y1, x2, y2, width)





# cv2.rectangle(img,(int(x1),int(y1)),(int(x2),int(y2)),(0,0,255),1)

# cv2.imshow('image',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()




# import matplotlib.pyplot as plt

# #plt.plot([0.405989645969694,0.563242684998714], [0.3648840839466498,0.526871574934477])
# plt.scatter(0.4059896459696940, 0.3648840839466498)
# plt.scatter(0.563242684998714,0.526871574934477)
# plt.scatter(0.7600610903490587, 0.5542237639520611)
# plt.scatter(0.8397976348290886,0.6224923826179124)

# plt.show() 
