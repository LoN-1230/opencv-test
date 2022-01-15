import cv2


#以下是取得視訊鏡頭的方法
cap = cv2.VideoCapture(0)  #視訊鏡頭 第一個鏡頭是0 外接鏡頭是1

while True:
    ret, frame = cap.read()         #cap.read()會回傳兩個值1.是取得下一貞(布林值)2.如果有成功的話會回傳取得道的下一貞圖片
    if ret:
        frame = cv2.resize(frame, (0, 0), fx =1, fy =1)
        cv2.imshow('video', frame)
    else:
        break
    if cv2.waitKey(1) == ord('q'):      #如果按下q影片停止撥放
        break














#以下是去讀取影片的每一貞，來去做一個撥放的動作
#cap = cv2.VideoCapture("thumb.mp4")

#while True:
#    ret, frame = cap.read()         #cap.read()會回傳兩個值1.是取得下一貞(布林值)2.如果有成功的話會回傳取得道的下一貞圖片
#    if ret:
#        frame = cv2.resize(frame, (0, 0), fx =0.5, fy =0.5)
#        cv2.imshow('video', frame)
#    else:
#        break
#    if cv2.waitKey(1) == ord('q'):      #如果按下q影片停止撥放
#        break
    











#以下是圖片匯入的部分
#img = cv2.imread('colorcolor.jpg')

## img = cv2.resize(img, (300,300)) #改變圖片大小
#img = cv2.resize(img, (0,0), fx=0.5, fy=0.5) #這是用倍數來改變圖片的大小
#cv2.imshow('img', img)
#cv2.waitKey(0) #假如()內是1000是1000毫秒 假如輸入0 就是無限久 .waitKey()是等待鍵盤按下去然後回傳
