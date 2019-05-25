import weakref
import engine
import time
import sapi5

savePath = "./saveTTS/"

_activeEngines = weakref.WeakValueDictionary()
try:
    eng = _activeEngines[None]
except KeyError:
    eng = engine.Engine()
    _activeEngines[None] = eng

""" RATE"""
rate = eng.getProperty('rate')   # getting details of current speaking rate
# print (rate)                        #printing current voice rate
eng.setProperty('rate', 150)     # setting up new voice rate


"""VOLUME"""
volume = eng.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
# print (volume)                          #printing current volume level
eng.setProperty('volume',1.0)    # setting up volume level  between 0 and 1

"""VOICE"""
voices = eng.getProperty('voices')       #getting details of current voice
#eng.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
eng.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female


def saveTTS(outA,saveWav = False):
	if saveWav == False:
		sapi5.saveWav = False		

	else:
		saveTTS(outA)
		sapi5.saveWav = True
		tmpT = time.time()
		sapi5.outfile = savePath + str(tmpT) + ".wav"


	eng.say(outA)
	eng.runAndWait()
	eng.stop()

# saveTTS("Nice to see you")
