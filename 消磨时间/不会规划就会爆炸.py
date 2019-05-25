import math
import numpy as np
import matplotlib.pyplot as plt

test_list = []
k = np.random.random_integers(1, high=10)
for i in range(5000):
    test_list.append(np.random.random_integers(-50, high=50))

tmpDict = {}
sumDict = {}
sumList = []
for i in range(1,len(test_list) + 1):
    tmpDict.update( {"{}".format(str(i)) : []} )

    for j in range(len(test_list) - i + 1):
        tmp = test_list[j:j+i]
        tmpDict[str(i)].append(tmp)
        tmpSum = sum(tmp)
        if tmpSum in sumDict.keys():
            sumDict[str(tmpSum)].append(tmp)
        else:
            sumDict.update( {"{}".format(str(tmpSum)) : []} )
            if tmpSum not in sumList:
                sumList.append(tmpSum)
            sumDict[str(tmpSum)].append(tmp)

sumList.sort()
c = len(sumList)
res = 0
res_list = []
for i in range(c):
    idx = c - i - 1
    if k == 0:
        break
    elif k >= len(sumDict[str(sumList[idx])]):
        k -= len(sumDict[str(sumList[idx])])
        res += len(sumDict[str(sumList[idx])]) * sumList[idx]
        res_list.extend(sumDict[str(sumList[idx])])

    else:
        res += sumList[idx] * k
        res_list.extend(sumDict[str(sumList[idx])][:k])

        break

for l in res_list:
    print(l)
print(res)