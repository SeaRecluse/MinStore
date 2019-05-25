import numpy as np
import cv2
import os

BLACK = [0, 0, 0]

def fillingImg(img):
    top, bottom, left, right = 0,0,0,0
    img_h = img.shape[0]
    img_w = img.shape[1]
    w_ex = bg_w/img_w
    h_ex = bg_h/img_h

    if h_ex > w_ex:
        img_h *= w_ex
        img_w = bg_w
        img_h = int(img_h)
        top = int((bg_h - img_h)/2)
        bottom = int(bg_h - img_h - top)

    elif h_ex < w_ex:
        img_w *= h_ex
        img_h = bg_h
        img_w = int(img_w)
        left = int((bg_w - img_w)/2)
        right = int(bg_w - img_w - left)

    else:
        img_h = bg_h
        img_w = bg_w

    img = cv2.resize(img, (int(img_w),int(img_h)), interpolation=cv2.INTER_AREA)  
    img = cv2.copyMakeBorder(img, top , bottom, left , right , cv2.BORDER_CONSTANT, value=BLACK)

    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_gray = cv2.cvtColor(img_gray, cv2.COLOR_GRAY2RGB)

    return img,img_gray
    # if color:
    #     return img
    # else:       
    #     img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #     img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
    #     return img

# img = cv2.imread("bg10.png")
# cv2.imshow("img1",img)

img = cv2.imread("data114.jpg")

bg_h = 480
bg_w = 640

img,img_gray = fillingImg(img)

count = 9
while count > 0:
	# img_tmp = cv2.addWeighted(img, count/10, img, 0.0, 0)
	img_gray= cv2.addWeighted(img_gray, count/10, img_gray, 0.5, 0)
	cv2.imwrite("bg" + str(count) + ".png",img_gray)
	count -= 1

# cv2.imshow("bg3",img)
# cv2.waitKey(0)