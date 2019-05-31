import main
import time

saveChoice = True

main.voiceID = 0 #huihui
main.init()

res = {'data': '帅帅帅'}	
start = time.time()	
main.saveTTS(res["data"])
print("cost : " + str(time.time() - start) + " s")

# main.voiceID = 1
# main.init()
# res = {'data': 'hahaha'}
# start = time.time()
# main.saveTTS(res["data"],saveChoice)
# print("cost : " + str(time.time() - start) + " s")