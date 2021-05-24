from core.storage import IStorage

import asyncio
import json
import sys


class IClient:
    async def start(self):
        raise NotImplementedError


class ConsoleClient(IClient):
    def __init__(self, storage: IStorage):
        self.storage = storage

    async def start(self):
        loop = asyncio.get_event_loop()
        while True:
            request = await loop.run_in_executor(None, sys.stdin.readline)
            loop.create_task(self.handle(request))

    async def handle(self, request):
        request = json.loads(request)
        if request['type'] == 'connect':
            host = request['host']
            port = request['port']
            data = request['data']
            r, w = await asyncio.open_connection(host, port)
            w.write(data.encode())
            answer = await asyncio.wait_for(r.readline(), timeout=10.0)
            print(f'Accepted answer {answer}')
            w.close()
