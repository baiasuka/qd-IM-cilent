import socket
import json
import asyncio

# 消息比特字符终结标识
MESSAGE_OVER_SIGN = b'xx@oo$n'

class CilentCore:
    def __init__(self, s_host='47.102.106.106', s_port=5001):
        self._server_host = s_host
        self._server_port = s_port

    async def msgSender(self, msg):
        reader, writer = await asyncio.open_connection(self._server_host, self._server_port)
        request = json.dumps(msg)
        writer.write(bytes(request, encoding="utf-8")+MESSAGE_OVER_SIGN)
        row_data = await reader.readuntil(MESSAGE_OVER_SIGN)
        data = json.loads(row_data.decode("utf-8")[:-7])
        print(data)
        writer.close()
        await writer.wait_closed()

def run_core():
    while 1:
        content = input()
        msg = {"code": 200, "msg": "request", "data": {"route": "/message/send", "content": content, "target_addr": '47.102.106.106'}}
        asyncio.run(CilentCore().msgSender(msg))


if __name__ == '__main__':
    while 1:
        content = input()
        msg = {"code": 200, "msg": "request", "data": {"route": "/message/send", "content": content, "target_addr": '47.102.106.106'}}
        asyncio.run(CilentCore().msgSender(msg))
