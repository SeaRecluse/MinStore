import time
start = time.clock()

list_1 = ["a","b","c"]
list_2 = [("b","b_1","b_2"),("a","a_1")] 
list_2_all_enum = []
list_3 = []
for per_tuple in list_2:
	list_2_all_enum.append(per_tuple[0])

for per_enum in list_1:
	try:
		list_3.append(list_2[list_2_all_enum.index(per_enum)])
	except:
		print("None")

print(list_3)

costT_1 = time.clock() - start
#===============================================================================
start = time.clock()

list_1 = ["a","b","c"]
list_2 = [("b","b_1","b_2"),("a","a_1")] 
list_3 = []

for per_enum in list_1:
	flag = True
	for per_tuple in list_2:
		if per_enum ==per_tuple[0]:
			list_3.append(per_tuple)
			flag = False

	if flag:
		print("None")

print(list_3)

costT_2 = time.clock() - start
#===============================================================================
start = time.clock()

list_1 = ["a","b","c"]
list_2 = [("b","b_1","b_2"),("a","a_1")] 
list_3 = []

for per_enum in list_1:
	for per_tuple in list_2:
		if per_enum ==per_tuple[0]:
			list_3.append(per_tuple)
			break

	else:
		print("None")

print(list_3)

costT_3 = time.clock() - start
#===============================================================================
print("costT_1 : " + str(costT_1) + " ms")
print("costT_2 : " + str(costT_2) + " ms")
print("costT_3 : " + str(costT_3) + " ms")