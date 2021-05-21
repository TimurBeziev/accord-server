from core import connection_handler as ch

import asyncio
import logging

logging.getLogger().setLevel(logging.INFO)


class AsyncTCPSocketServer:
    def __init__(self, host, port, handler: ch.IConnectionHandler):
        self.addr = (host, port)
        self._loop = asyncio.get_event_loop()
        self._server = asyncio.start_server(handler.handle, host=host, port=port, loop=self._loop)

    def serve(self):
        logging.info(f'Start running server on {self.addr}')
        self._server = self._loop.run_until_complete(self._server)
        try:
            self._loop.run_forever()
        except KeyboardInterrupt:
            logging.info('Shutdown server')
        self.__shutdown()

    def __shutdown(self):
        for task in asyncio.Task.all_tasks():
            task.cancel()
        self._loop.close()
