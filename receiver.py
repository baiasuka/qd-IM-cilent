import socket
import json
import asyncio

# 消息比特字符终结标识
MESSAGE_OVER_SIGN = b'xx@oo$n'


class Receiver:
    def __init__(self, port=6666, limit=1024):
        self._port = port
        self._limit = limit

    @staticmethod
    async def msgHandler(reader, writer):
        """

        :param reader:
        :param writer:
        :return:
        """
        # 获取请求内容
        raw_data = await reader.readuntil(MESSAGE_OVER_SIGN)
        # 二进制转字符串
        recieved_msg = raw_data.decode("utf-8")[0:-7]
        # 字符串解析为字典
        request = json.loads(recieved_msg)
        print(request["content"])
        await writer.drain()

    async def main(self):
        """
        主运行函数
        :return:
        """
        print("qd-IM-cilent-receiver start")
        server = await asyncio.start_server(self.msgHandler,
                                            '0.0.0.0', self._port, limit=self._limit)
        async with server:
            await server.serve_forever()

def run_receiver():
    while 1:
        asyncio.run(Receiver().main())


if __name__ == '__main__':
    while 1:
        asyncio.run(Receiver().main())
