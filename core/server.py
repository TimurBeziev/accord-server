from core.network import Network

import socket
import select
import logging

logging.getLogger().setLevel(logging.INFO)


class AsyncTCPSocketServer:
    BYTES_TO_READ: int = 1024
    MAX_TCP_CONNECTIONS: int = 20

    def __init__(self, ip, port):
        # Using TCP/IP protocol to communicate
        # TODO change to reliable UDP
        self.addr = (ip, port)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setblocking(False)
        self.sock.bind((ip, port))
        self.sock.listen(AsyncTCPSocketServer.MAX_TCP_CONNECTIONS)
        self.net = Network()

    def serve(self):
        logging.info(f'Start running server on {self.addr}')
        logging.info('CTRL+C to stop server')
        try:
            while True:
                r, w, _ = select.select([self.sock] + self.net.connections, self.net.connections, [])
                self.__handle_readables(r)
                self.__handle_writeables(w)
        except KeyboardInterrupt:
            self.shutdown()
            logging.info('Shutdown server')

    def shutdown(self):
        self.sock.close()

    def __handle_readables(self, r):
        for resource in r:
            if resource is self.sock:
                self.net.accept(resource.accept(), blocking=False)
            else:
                try:
                    self.net.handle(resource)
                except ConnectionResetError:
                    self.net.close(resource)

    def __handle_writeables(self, w):
        for resource in w:
            if resource.ready():
                resource.send()
