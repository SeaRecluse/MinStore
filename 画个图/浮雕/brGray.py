import numpy as np
import cv2
import sys
import os
import time
import glob
import subprocess
from subprocess import Popen, PIPE, STDOUT

# kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]], np.float32) #锐化

# kernel = np.array([
#                 [1, 1, 1], 
#                 [1, -7, 1], 
#                 [1, 1, 1]
#                 ], np.float32) #边缘强调

kernel = np.array([
                [-1, -1, -1, -1, -1], 
                [-1, -1, -1, -1, -1], 
                [-1, -1, 24, -1, -1], 
                [-1, -1, -1, -1, -1], 
                [-1, -1, -1, -1, -1]
                ], np.float32) #边缘检测

# kernel = np.array([
#                 [1, 1, 1, 1, 1], 
#                 [1, 1, 1, 1, 1], 
#                 [1, 1, -23.5, 1, 1], 
#                 [1, 1, 1, 1, 1], 
#                 [1, 1, 1, 1, 1]
#                 ], np.float32) #边缘检测
def custom_blur(image):
    dst = cv2.filter2D(image, -1, kernel=kernel)
    return dst

def blur(image):
  dst = cv2.blur(image, (5, 1))
  return dst

fList = glob.glob('./*.jpg')
for fName in fList:
    os.remove(fName)

fList = glob.glob('./gray/*.jpg')
for fName in fList:
    os.remove(fName)

fList = glob.glob('./orig/*.png')
# count = len(fList)
limit = 4
idx = 0
for n in range(len(fList)):
    img_gray = cv2.imread(fList[n])
    # img_gray = blur(img_gray)
    # img_gray = custom_blur(img_gray)
    # img_gray = cv2.cvtColor(img_gray, cv2.COLOR_BGR2GRAY)
    # img_gray = cv2.cvtColor(img_gray, cv2.COLOR_GRAY2RGB)
    # img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    cv2.imwrite("./gray/" + str(n) + ".jpg", img_gray)
    if idx < limit:
        cv2.imwrite("./" + str(n) + ".jpg", img_gray)
        idx += 1
    print(fList[n] + "conver complete.")

# sys.path.append(r"C:\Users\SEARECLUSE\Desktop\testFace106\x64\Debug")
# print(sys.path)
# cmd = "testFace106.exe"

# with Popen(cmd, shell=True, stdout=PIPE, stderr=STDOUT) as res:
#     out = res.stdout.read()
#     log = bytes.decode(out,encoding = "gbk")
#     print(log)