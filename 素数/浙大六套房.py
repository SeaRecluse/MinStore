import primesieve
from primesieve import *
import time

#===========================================================
# aim_min = 6541367000
# aim_max = 6541368000

# mid_p = aim_max ** 0.5
# p_list = primes(2,mid_p+1)

# count = 0
# start = time.time()

# for n in range(aim_min,aim_max):
# 	for p in p_list:
# 		if (n % p) == 0:
# 			q = n/p
# 			q_list = primes(q-1,q)
# 			if q in q_list:
# 				count += 1

# print(count)
# print("cost time: " + str(time.time() - start) + " s")
#===========================================================
idx = 0
count = 0
start = time.time()
while idx < 10:
	aim_min = 65 * 100000000 + idx * 10000000 + 1367000
	aim_max = 65 * 100000000 + idx * 10000000 + 1368000

	mid_p = aim_max ** 0.5
	p_list = primes(2,mid_p+1)

	for n in range(aim_min,aim_max):
		for p in p_list:
			if (n % p) == 0:
				q = n/p
				q_list = primes(q-1,q)
				if q in q_list:
					count += 1
	idx += 1

print(count)
print("cost time: " + str(time.time() - start) + " s")
#===========================================================
# import xlrd
# import xlwt

# myWorkbook = xlwt.Workbook()
# mySheet = myWorkbook.add_sheet('A Test Sheet')

# count = 0
# for n in range(aim_min,aim_max):
# 	count += 1
# 	mySheet.write(0, count, n)

# count = 0
# for p in p_list:
# 	count += 1
# 	mySheet.write(count, 0, p)

# myWorkbook.save('excelFile.xls')

#============================================================
# from openpyxl import Workbook
# from openpyxl.utils import get_column_letter

# # 在内存中创建一个workbook对象，而且会至少创建一个 worksheet
# wb = Workbook()

# #获取当前活跃的worksheet,默认就是第一个worksheet
# ws = wb.active

# count = 1
# for n in range(aim_min,aim_max):
# 	count += 1
# 	ws.cell(row = 1, column = count).value = n

# count = 1
# for p in p_list:
# 	count += 1
# 	ws.cell(row = count, column = 1).value = p

# row = 1
# col = 1
# sumP = []
# count = 0
# for n in range(aim_min,aim_max):
# 	col += 1
# 	for p in p_list:
# 		row += 1
# 		if (n % p) == 0:
# 			q = n/p
# 			q_list = primes(q-1,q)
# 			if q in q_list:
# 				count += 1
# 				ws.cell(row = row, column = col).value = 1
# 			else:
# 				ws.cell(row = row, column = col).value = 0
# 		else:
# 			ws.cell(row = row, column = col).value = 0

# 	ws.cell(row = row + 1, column = col).value = count
# 	sumP.append(count)
# 	row = 1
# 	count = 0

# count = len(p_list) + 2
# ws.cell(row = count, column = 1).value = "合计"

# sumAll = 0
# for n in range(len(sumP)):
# 	sumAll += sumP[n]
# 	ws.cell(row = count, column = n + 2).value = sumP[n]

# ws.cell(row = count, column = 1002).value = sumAll
# #保存
# wb.save(filename="primes.xlsx")