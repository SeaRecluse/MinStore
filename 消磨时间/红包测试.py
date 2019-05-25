import random
import numpy as np

# ===============================================================================
print("第一总是很倒霉。")
flag = True
while flag:
	num_list = []
	tmp_num = 0
	tmp_sum = 0
	get_num = -10
	for i in range(1,10):
		tmp_sum = i * 11 - get_num
		tmp_num = random.randint(1,tmp_sum)
		get_num += tmp_num
		num_list.append(tmp_num)
	num_list.append(100 - get_num)

	if num_list[-1] < 5:
		flag = False

num_list = []
tmp_num = 0
tmp_sum = 0
get_num = 0
for i in range(1,10):
	tmp_sum = i * 11 - get_num
	tmp_num = random.randint(1,tmp_sum)
	get_num += tmp_num
	num_list.append(tmp_num)
	print(num_list[-1])
num_list.append(100 - get_num)
print(num_list[-1])
print()
#===============================================================================
print("幻象术")
rand_list = []
for i in range(0,10):
	rand_list.append(0)

max_count = 10000
sum_list = []
count = 0
while count < max_count:
	num_list = []
	tmp_num = 0
	tmp_sum = 0
	get_num = -10
	for i in range(1,10):
		tmp_sum = i * 11 - get_num
		tmp_num = random.uniform(1,tmp_sum)
		get_num += tmp_num
		num_list.append(tmp_num)

		if tmp_num > 10:
			rand_list[i - 1] += 1


	num_list.append(100 - get_num)
	if num_list[-1] > 10:
		rand_list[-1] += 1
	
	for i in range(0,10):
		try:
			sum_list[i] += num_list[i]
		except:
			sum_list.append(0)
			sum_list[i] += num_list[i]
	count += 1

avg_num = 0
for i in range(0,10):
	sum_list[i] = sum_list[i]/max_count
	# print(rand_list[i]/max_count)
	print(sum_list[i])
	avg_num += sum_list[i]

print("Avg: " + str(avg_num/10))

arr = np.array(sum_list)
#求均值
arr_mean = np.mean(arr)
#求方差
arr_var = np.var(arr)
#求标准差
arr_std = np.std(arr,ddof=1)

print("平均值为：%f" % arr_mean)
print("方差为：%f" % arr_var)
print("标准差为:%f" % arr_std)
print()
#===============================================================================
print("没毛病")
count = 0
sum_list = []
while count < 10000:
	a = [random.randint(0, 100) for i in range(9)]
	a.append(0)
	a.append(100)
	a.sort()

	b = [a[i + 1] - a[i] for i in range(10)]

	for i in range(0,10):
		try:
			sum_list[i] += b_1[i]
		except:
			sum_list.append(0)
			sum_list[i] += b[i]
	count += 1

avg_num = 0
for i in range(0,10):
	sum_list[i] = sum_list[i]/10000
	print(sum_list[i])
	avg_num += sum_list[i]

print("Avg: " + str(avg_num/10))
	
arr = np.array(sum_list)
#求均值
arr_mean = np.mean(arr)
#求方差
arr_var = np.var(arr)
#求标准差
arr_std = np.std(arr,ddof=1)

print("平均值为：%f" % arr_mean)
print("方差为：%f" % arr_var)
print("标准差为:%f" % arr_std)