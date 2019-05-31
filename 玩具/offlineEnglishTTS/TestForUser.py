import main
import time

saveChoice = True

#main.init(voiceChoice = [0-2],voiceRate = [1-1000],voiceVolume = [0.0-1.0])
#默认(voiceChoice = 1,voiceRate = 150,voiceVolume = 1.0)
#只有 voiceChoice = 0 可以兼容中文，Windows huihui

main.init(0)

res = {'data': '帅帅帅'}	
start = time.time()	
main.saveTTS(res["data"])
print("cost : " + str(time.time() - start) + " s")


# main.init(1)
# res = {'data': 'hahaha'}
# start = time.time()
# main.saveTTS(res["data"],saveChoice)
# print("cost : " + str(time.time() - start) + " s")