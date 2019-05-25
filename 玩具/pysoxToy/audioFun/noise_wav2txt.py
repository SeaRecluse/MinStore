# -*- coding: utf-8 -*-
import wave
import pylab as pl
import numpy as np
import math

def plantWav(fileName):
	# 打开WAV文档
	f = wave.open(fileName, "r")
	# 读取格式信息
	# (nchannels, sampwidth, framerate, nframes, comptype, compname)
	params = f.getparams()
	nchannels, sampwidth, framerate, nframes = params[:4]
	# 读取波形数据
	str_data = f.readframes(nframes)
	f.close()
	#将波形数据转换为数组
	wave_data = np.fromstring(str_data, dtype=np.short)
	wave_data.shape = -1, 2
	wave_data = wave_data.T
	time = np.arange(0, nframes) * (1.0 / framerate)
	
	return time,wave_data
	#用左右声道模拟音频对比
	len_track = len(wave_data[0])

	noise_str = "Channel 0: " + str(wave_data[0][0])
	for n in range(1,len_track):
	    noise_str += (", " + str(wave_data[0][n]))

	noise_str += "\nChannel 1: " + str(wave_data[1][0])
	for n in range(1,len_track):
	    noise_str += (", " + str(wave_data[1][n]))

	f = open("noise_tmp.txt","a")
	f.write(noise_str)
	f.close()

time1,d1 = plantWav("./1111Clip.wav")
time2,d2 = plantWav("./output.wav")
# wave_data_left_track = []
# wave_data_right_track = []

# for n in range(len_track):
#     if wave_data[0][n]:
#         wave_data_left_track.append(wave_data[0][n])
#         if wave_data[1][n]:
#             wave_data_right_track.append(wave_data[1][n])
#         else:
#             wave_data_right_track.append(0)
#     elif wave_data[1][n]:
#          wave_data_left_track.append(0)
#          wave_data_right_track.append(wave_data[1][n])

# 绘制波形
pl.subplot(211)
pl.plot(time1, d1[0], c = "r")
pl.subplot(212)
pl.plot(time2, d2[0], c = "g")
pl.xlabel("time (seconds)")
pl.show()