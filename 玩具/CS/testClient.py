import sys
import json
import time
import base64
import socket
import asyncio
from aiohttp import ClientSession

#-----------socket---------------------
def clientSocket():
    obj = socket.socket()
    obj.connect(('127.0.0.1',8888,))
    sys.stdout.flush()
    msg = "hello world"
    while True:
        obj.sendall(bytes(msg, encoding="utf-8"))
        res = str(obj.recv(1024), encoding="utf-8")
        print(res)
        sys.stdout.flush()
        msg = "hello world"
        
    obj.close()

#------------http---------------------
url = "http://127.0.0.1:8888"
async def testClentHttp(loop):
    async with ClientSession(loop=loop) as session:
        while True:
            msg = "hello world"
            msg = base64.b64encode(msg.encode()).decode('ascii')
                
            headers = {'content-type': 'application/json'}
            my_data = {"data":"{}".format(msg)}

            async with session.post(url,data=json.dumps(my_data),headers=headers) as resp:
                print(await resp.text())
                time.sleep(3)

def clientHttp():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(testClentHttp(loop))

# clientSocket()
# clientHttp()