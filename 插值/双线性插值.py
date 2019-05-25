# aim = 100
# w_x = 5
# w_y = 2
# w_z = 1

# x = aim//w_x
# y = aim//w_y
# z = aim//w_z

# allWays = []
# perWay = []

# def isSatisfy(x,y,z):
# 	if w_x * x + w_y * y + w_z * z == aim:
# 		return True
# 	return False
		
# for i in range(0,x+1):
# 	for j in range(0,y+1):
# 		for k in range(0,z+1):
# 			if isSatisfy(i,j,k):
# 				perWay = [i,j,k]
# 				print(str(w_x) + " * " + str(perWay[0]) + " + "\
# 				 + str(w_y) + " * " + str(perWay[1]) + " + "\
# 				 + str(w_z) + " * " + str(perWay[2]) + " = 100")
# 				allWays.append(perWay)

# print(len(allWays))

#!/usr/bin/python
# -*- coding: utf-8 -*-
 
__author__ = 'Alex Wang'
 
import numpy as np
import cv2
import time
 
'''
python implementation of bilinear interpolation
'''

def nearest_interpolation(img,out_dim):
    m = out_dim[0]
    n = out_dim[1]
    height,width,channels =img.shape
    emptyImage=np.zeros((m,n,channels),np.uint8)
    sh=m/height
    sw=n/width
    for i in range(m):
        for j in range(n):
            x=int(i/sh)
            y=int(j/sw)
            emptyImage[i,j]=img[x,y]
    return emptyImage

def bilinear_interpolation_2(img,out_dim):
    m = out_dim[0]
    n = out_dim[1]
    height,width,channels =img.shape
    emptyImage=np.zeros((m,n,channels),np.uint8)
    value=[0,0,0]
    sh=m/height
    sw=n/width
    for i in range(m):
        for j in range(n):
            x = i/sh
            y = j/sw
            p=(i+0.0)/sh-x
            q=(j+0.0)/sw-y
            x=int(x)-1
            y=int(y)-1
            for k in range(3):
                if x+1<m and y+1<n:
                    value[k]=int(img[x,y][k]*(1-p)*(1-q)+img[x,y+1][k]*q*(1-p)+img[x+1,y][k]*(1-q)*p+img[x+1,y+1][k]*p*q)
            emptyImage[i, j] = (value[0], value[1], value[2])
    return emptyImage

def S(x):
    x = np.abs(x)
    if 0 <= x < 1:
        return 1 - 2 * x * x + x * x * x
    if 1 <= x < 2:
        return 4 - 8 * x + 5 * x * x - x * x * x
    else:
        return 0
def bilinear_interpolation_3(img,out_dim):
    m = out_dim[0]
    n = out_dim[1]
    height,width,channels =img.shape
    emptyImage=np.zeros((m,n,channels),np.uint8)
    sh=m/height
    sw=n/width
    for i in range(m):
        for j in range(n):
            x = i/sh
            y = j/sw
            p=(i+0.0)/sh-x
            q=(j+0.0)/sw-y
            x=int(x)-2
            y=int(y)-2
            A = np.array([
                [S(1 + p), S(p), S(1 - p), S(2 - p)]
            ])
            if x>=m-3:
                m-1
            if y>=n-3:
                n-1
            if x>=1 and x<=(m-3) and y>=1 and y<=(n-3):
                B = np.array([
                    [img[x-1, y-1], img[x-1, y],
                     img[x-1, y+1],
                     img[x-1, y+1]],
                    [img[x, y-1], img[x, y],
                     img[x, y+1], img[x, y+2]],
                    [img[x+1, y-1], img[x+1, y],
                     img[x+1, y+1], img[x+1, y+2]],
                    [img[x+2, y-1], img[x+2, y],
                     img[x+2, y+1], img[x+2, y+1]],
 
                    ])
                C = np.array([
                    [S(1 + q)],
                    [S(q)],
                    [S(1 - q)],
                    [S(2 - q)]
                ])
                blue = np.dot(np.dot(A, B[:, :, 0]), C)[0, 0]
                green = np.dot(np.dot(A, B[:, :, 1]), C)[0, 0]
                red = np.dot(np.dot(A, B[:, :, 2]), C)[0, 0]
 
                # ajust the value to be in [0,255]
                def adjust(value):
                    if value > 255:
                        value = 255
                    elif value < 0:
                        value = 0
                    return value
 
                blue = adjust(blue)
                green = adjust(green)
                red = adjust(red)
                emptyImage[i, j] = np.array([blue, green, red], dtype=np.uint8)
 
 
    return emptyImage


def bilinear_interpolation(img,out_dim):
    src_h, src_w, channel = img.shape
    dst_h, dst_w = out_dim[1], out_dim[0]
    if src_h == dst_h and src_w == dst_w:
        return img.copy()
    dst_img = np.zeros((dst_h,dst_w,3),dtype=np.uint8)
    scale_x, scale_y = float(src_w) / dst_w, float(src_h) / dst_h
    for i in range(3):
        for dst_y in range(dst_h):
            for dst_x in range(dst_w):
 
                # find the origin x and y coordinates of dst image x and y
                # use geometric center symmetry
                # if use direct way, src_x = dst_x * scale_x
                src_x = (dst_x + 0.5) * scale_x - 0.5
                src_y = (dst_y + 0.5) * scale_y - 0.5
 
                # find the coordinates of the points which will be used to compute the interpolation
                src_x0 = int(np.floor(src_x))
                src_x1 = min(src_x0 + 1 ,src_w - 1)
                src_y0 = int(np.floor(src_y))
                src_y1 = min(src_y0 + 1, src_h - 1)
 
                # calculate the interpolation
                temp0 = (src_x1 - src_x) * img[src_y0,src_x0,i] + (src_x - src_x0) * img[src_y0,src_x1,i]
                temp1 = (src_x1 - src_x) * img[src_y1,src_x0,i] + (src_x - src_x0) * img[src_y1,src_x1,i]
                dst_img[dst_y,dst_x,i] = int((src_y1 - src_y) * temp0 + (src_y - src_y0) * temp1)
 
    return dst_img
 
 
if __name__ == '__main__':
    img = cv2.imread('bg_2.jpg')

    start = time.time()
    dst = bilinear_interpolation(img,(1000,800))
    print('cost %f seconds' % (time.time() - start))
    # cv2.imshow('result',dst)
    cv2.imwrite('result1.jpg',dst)

    start = time.time()
    dst = nearest_interpolation(img,(1000,800))
    print('cost %f seconds' % (time.time() - start))
    # cv2.imshow('result',dst)
    cv2.imwrite('result2.jpg',dst)

    start = time.time()
    dst = bilinear_interpolation_2(img,(1000,800))
    print('cost %f seconds' % (time.time() - start))
    # cv2.imshow('result',dst)
    cv2.imwrite('result3.jpg',dst)

    start = time.time()
    dst = bilinear_interpolation_3(img,(1000,800))
    print('cost %f seconds' % (time.time() - start)) 
    # cv2.imshow('result',dst)
    cv2.imwrite('result4.jpg',dst)

    cv2.waitKey()
