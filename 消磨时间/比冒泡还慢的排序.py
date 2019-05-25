import time

oneList = [1,3,28,21,9999,6666,34567,54,14878,5,99998]
start = time.clock()
# upBond = max(oneList)
# lowBond = min(oneList)
find = 0
count = len(oneList)
for i in range(99999):
	if i in oneList:
		print(i,end = " ")
		find += 1
	if find == count:
		break 

costT_1 = time.clock() - start
print()
print("costT_1 : " + str(costT_1) + " ms")
print()

oneList = [1,3,28,21,9999,6666,34567,54,14878,5,99998]
start = time.clock()
count = len(oneList)
for i in range(count):
	for j in range(i+1,count):
		if oneList[i] > oneList[j]:
			tmpN = oneList[j]
			oneList[j] = oneList[i]
			oneList[i] = tmpN

for per_n in oneList:
	print(per_n,end = " ")

costT_2 = time.clock() - start
print()
print("costT_2 : " + str(costT_2) + " ms")
print()

