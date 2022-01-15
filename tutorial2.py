# numpy與圖片的關係
import cv2
import numpy as np

#img = cv2.imread('colorcolor.jpg')
#print(type(img))      #array 是陣列 #nd 是多維 #ndarray 是多維陣列 #陣列是速度很快的列表
#print(img.shape)       #這是來取的陣列的形狀大小


img = np.empty((300, 300, 3), np.uint8)

for row in range(300):
    for col in range(300):
        img[row][col] = [0,255,0]

cv2.imshow('img', img)
cv2.waitKey(0)