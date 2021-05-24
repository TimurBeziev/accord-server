import asyncio
import logging

logging.getLogger().setLevel(logging.INFO)


class AsyncTCPSocketServer:
    def __init__(self, host, port, handler, storage):
        self.addr = (host, port)
        self._loop = asyncio.get_event_loop()
        self._server = asyncio.start_server(lambda r, w: handler.handle(r, w, storage),
                                            host=host, port=port)

    def __del__(self):
        self.__shutdown()

    async def start(self):
        logging.info(f'Start running server on {self.addr}')
        self._loop.create_task(self._server)

    def __shutdown(self):
        logging.info('Shutdown server')
        # Should cancel only server tasks
