from core.connection_handler import UnsecureTCPConnectionHandler as ConnectionHandler
from core.client import ConsoleClient as Client
from core.server import AsyncTCPSocketServer as Server
from core.storage import IStorage as Storage
import asyncio
import logging

logging.getLogger().setLevel(logging.INFO)


class AsyncAccordPeer:
    def __init__(self, address):
        self.host, self.port = address
        self.loop = asyncio.get_event_loop()

    def connect(self):
        logging.info("Connecting peer")
        storage = Storage()
        server = Server(self.host, self.port, ConnectionHandler, storage)
        client = Client(storage)
        self.loop.create_task(server.start())
        self.loop.create_task(client.start())
        try:
            self.loop.run_forever()
        except KeyboardInterrupt:
            pass
        self.__disconnect()

    def __disconnect(self):
        logging.info("Disconnecting peer")
