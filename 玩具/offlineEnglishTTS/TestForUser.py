import main
import time

saveChoice = True

res = {'data': 'Hello world, , , , , ,Hello world'}	
start = time.time()	
main.saveTTS(res["data"])
print("cost : " + str(time.time() - start) + " s")

res = {'data': 'hahaha'}
start = time.time()
main.saveTTS(res["data"],saveChoice)
print("cost : " + str(time.time() - start) + " s")