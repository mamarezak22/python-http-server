import asyncio
from .request import HTTPRequest,parse_request_msg
from .router import router,register_routes


async def handle_connection(reader , writer):
    print("Serving HTTP on 0.0.0.0 port 4239 (http://0.0.0.0:4239/)")
    request_msg = await reader.read(1024)
    request : HTTPRequest = parse_request_msg(request_msg)
    print(f"request hits the {request.url.raw_url}")
    response = router.handle_request(request)
    writer.write(response.message.encode())
    await writer.drain()
    writer.close()


async def main():
    register_routes()
    server = await asyncio.start_server(handle_connection,"0.0.0.0","4239")

    async with server:
        await server.serve_forever()

if __name__== "__main__":
    asyncio.run(main())
