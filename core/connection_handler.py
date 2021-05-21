import asyncio
import logging

logging.getLogger().setLevel(logging.INFO)


class IConnectionHandler:
    @staticmethod
    async def handle(reader, writer):
        raise NotImplementedError

    @staticmethod
    async def authorize(reader, writer):
        raise NotImplementedError


class UnsecureTCPConnectionHandler(IConnectionHandler):
    TIMEOUT = 10.0

    @staticmethod
    async def handle(reader, writer):
        peername = writer.get_extra_info('peername')
        logging.info(f'Accepted connection from {peername}')
        while True:
            try:
                data = await asyncio.wait_for(
                        reader.readline(), timeout=UnsecureTCPConnectionHandler.TIMEOUT)
                if data:
                    logging.info(f'Get data from {peername} : {data}')
                    writer.write(data)
                else:
                    logging.info(f'Connection with {peername} closed by {peername}')
                    break
            except asyncio.exceptions.TimeoutError:
                logging.info(f'Connection with {peername} close by timeout')
                break
            except asyncio.exceptions.CancelledError:
                break
        writer.close()

    @staticmethod
    async def authorize(reader, writer):
        pass