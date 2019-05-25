import ssl
import base64
import asyncio
import aiohttp
from aiohttp import web
#-----------socket---------------------

async def handle_echo(reader, writer):
    while True:
        try:
            msg =await reader.read(64)
            msg = msg.decode()
            print(msg)
            writer.write(bytes("hahaha", encoding="utf-8"))
            return writer.drain()
        except Exception as e:
            writer.write(bytes("hahaha", encoding="utf-8"))
            return writer.drain()
    writer.close()

def serverSocket():
    port = 8888
    host = '127.0.0.1'   
    loop = asyncio.get_event_loop()
    coro = asyncio.start_server(handle_echo, host, port, loop=loop)
    server = loop.run_until_complete(coro)
    print('Serving on {}'.format(server.sockets[0].getsockname()))
    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass
    server.close()
    loop.run_until_complete(server.wait_closed())
    loop.close()

#------------http---------------------

routes = web.RouteTableDef()
@routes.post('/')
async def post_handler(request):
    while True:
        try: 
            msg = await request.text()
            msg =  eval(msg)
            msg = base64.b64decode(msg["data"]).decode()
            print(msg)
            return web.Response(text= "hahaha")
        except Exception as e:
            return web.Response(text= "emmmmm")
    request.close()

def serverHttp():
    port = 8888
    host = '127.0.0.1'   
    app = web.Application()
    app.add_routes(routes)
    web.run_app(app, host=host, port=port)

#------------https---------------------
def serverHttps():
    port = 8888
    host = '127.0.0.1'   
    app = web.Application()
    app.add_routes(routes)
    
    ssl_context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    ssl_context.load_cert_chain('./ssl/server.crt', './ssl/server.key')
    web.run_app(app, host=host, port=port, ssl_context=ssl_context)

# serverSocket()
# serverHttp()