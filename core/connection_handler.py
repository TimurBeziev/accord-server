from core.storage import IStorage

import asyncio
import logging

logging.getLogger().setLevel(logging.INFO)


class IConnectionHandler:
    @staticmethod
    async def handle(reader, writer, storage: IStorage):
        raise NotImplementedError

    @staticmethod
    async def authorize(reader, writer):
        raise NotImplementedError


class UnsecureTCPConnectionHandler(IConnectionHandler):
    TIMEOUT: float = 10.0

    @staticmethod
    async def handle(reader, writer, storage):
        peername = writer.get_extra_info('peername')
        logging.info(f'Accepted connection from {peername}')
        while True:
            try:
                query = await asyncio.wait_for(
                        reader.readline(), timeout=UnsecureTCPConnectionHandler.TIMEOUT)
                if query:
                    logging.info(f'Get query from {peername} : {query}')
                    data = await storage.fetch(query.decode())
                    writer.write(data.encode())
                else:
                    logging.info(f'Connection with {peername} closed by {peername}')
                    break
            except asyncio.exceptions.TimeoutError:
                logging.info(f'Connection with {peername} closed by timeout')
                break
            except asyncio.exceptions.CancelledError:
                break
        writer.close()

    @staticmethod
    async def authorize(reader, writer):
        pass
