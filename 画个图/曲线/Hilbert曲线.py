import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

#-----------------------------坐标转换----------------------------
def rot(n,x,y,rx,ry):
	if ry == 0:
		if rx == 1:
			x = (n - 1 - x)
			y = (n - 1 - y)

		tmp = x
		x = y
		y = tmp

	return x,y

def xy2d(n,x,y):
	rx,ry,s,d = 0,0,0,0
	s = n//2
	while s:
		rx = 1 if (x & s) > 0 else 0
		ry = 1 if (y & s) > 0 else 0
		d += s * s * ((3 * rx) ^ ry)
		x,y = rot(s,x,y,rx,ry)
		s = s//2

	return d

def d2xy(n,d):
	rx,ry,t,s,x,y = d,d,d,1,0,0
	while s < n:
		rx = 1 if (1 & (t // 2)) else 0
		ry = 1 if (1 & (t ^ rx)) else 0
		x,y = rot(s,x,y,rx,ry)
		x += s * rx
		y += s * ry
		t = t//4
		s *= 2

	return x,y
#-----------------------------n:2的次幂----------------------------
n = pow(2,4)
x = np.arange(0,n)
y = np.arange(0,n)

allxy = []
for per_y in y:
	for per_x in x:
		d = xy2d(n,per_x,per_y)
		allxy.append([per_x,per_y,d])	

for i in range(len(allxy)):
	for j in range(i + 1, len(allxy)):
		if allxy[j][2] < allxy[i][2]:
			temp = allxy[j]
			allxy[j] = allxy[i]
			allxy[i] = temp
#-----------------------------画静态图----------------------------
allxy = np.array(allxy)
plt.figure()
plt.plot(allxy[:,0],allxy[:,1],'-',color = "purple",linewidth=2)
plt.show()
# #-----------------------------画动态图----------------------------
fig, ax = plt.subplots()
xdata, ydata = [], []
ln, = ax.plot([], [], '--', color = "purple", animated=False)

def init():
    ax.set_xlim(-0.25, n-0.25)
    ax.set_ylim(-0.25, n-0.25)
    return ln,

def update(frame):
    xdata.append(allxy[frame][0])
    ydata.append(allxy[frame][1])
    lnT, = ax.plot([], [], '-*', animated=False)
    lnT.set_data(xdata[-2:], ydata[-2:])
    ln.set_data(xdata[:-1], ydata[:-1])
    return ln,lnT

ani = FuncAnimation(fig, update, frames=range(0,pow(n,2)),
                    init_func=init, blit=True)

plt.show()