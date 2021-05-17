import socket
import select
import logging

logging.getLogger().setLevel(logging.INFO)


class AsyncTCPServer:
    BYTES_TO_READ: int = 1024
    MAX_TCP_CONNECTIONS: int = 160

    def __init__(self, ip, port):
        # Using TCP/IP protocol to comminicate
        # TODO change to reliable UDP
        self.address = (ip, port)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setblocking(False)
        self.sock.bind((ip, port))

        self.sock.listen(AsyncTCPServer.MAX_TCP_CONNECTIONS)
        self.input = [self.sock]
        self.output = []
    
    def serve(self):
        logging.info(f'Start running server on {self.address}')
        logging.info('CTRL+C to stop server')
        try:
            while self.input:
               readables, writeables, _ = select.select(self.input, self.output, [])
               self.__handle_readables(readables)
               self.__handle_writeables(writeables)
        except KeyboardInterrupt:
            self.shutdown()
            logging.info('Shutdown server')

    def shutdown(self):
        self.__clear_resource(self.sock)

    # This method handles input events for our server
    # For example new connection is input event for self.sock
    def __handle_readables(self, readables):
        for resource in readables:
            if resource is self.sock: # new connection
                conn, addr = resource.accept()
                conn.setblocking(False)
                self.input.append(conn)
                logging.info(f'Accept new connection at {addr}')
            else: # trying to read for input data from resource
                data = ""
                try:
                    # TODO read data here
                    data = resource.recv(AsyncTCPServer.BYTES_TO_READ)
                    logging.info(f'Read data from {resource}')
                except ConnectionResetError:
                    # If unable to get resoure from input socket 
                    # (closed from another side)
                    logging.info(f'Connection with {resource} dropped')
                    pass

                if data:
                    # TODO process data here
                    resource.send(bytes(str(data), encoding='UTF-8'))
                else:
                    self.__clear_resource(resource)

    def __handle_writeables(self, writeables):
        pass

    def __clear_resource(self, resource):
        if resource in self.input:
            self.input.remove(resource)
        if resource in self.output:
            self.output.remove(resource)
        resource.close()
        logging.info(f'Closing connection {str(resource)}')

