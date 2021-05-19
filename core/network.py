import enum
import socket
import logging

logging.getLogger().setLevel(logging.INFO)


class ISocketConnection:
    class Status(enum.Enum):
        INITIAL = 0
        READ = 2
        PROCESS = 3
        READY = 4

    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'read') and
                callable(subclass.read) and
                hasattr(subclass, 'write') and
                callable(subclass.write) and
                hasattr(subclass, 'close') and
                callable(subclass.close) and
                hasattr(subclass, 'fileno') and
                callable(subclass.fileno))

    # Write msg to a socket object
    def read(self):
        raise NotImplementedError

    # Read byte_len bytes from socket object and returns them
    def write(self):
        raise NotImplementedError

    # Closes socket object
    def close(self):
        raise NotImplementedError

    # Returns socket object file descriptor
    def fileno(self):
        raise NotImplementedError


class SocketConnection(ISocketConnection):
    def __init__(self, connection: tuple, blocking: bool):
        self.status = self.Status.INITIAL
        self.conn, self.addr = connection
        self.conn.setblocking(blocking)
        logging.info(f'Accept new connection on {self.addr}')

    def write(self, msg: bytearray):
        self.conn.send(msg, encoding='UTF-8')

    def read(self, byte_len: int):
        return self.conn.recv(byte_len)

    def close(self):
        self.conn.close()

    def fileno(self):
        return self.conn.fileno()

    def ready(self):
        return self.status is self.Status.READY


class ISocketConnectionHandler:
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'handle') and
                callable(subclass.handle))

    def handle(self):
        raise NotImplementedError


# TODO Implement class
class SocketConnectionHandler(ISocketConnectionHandler):
    def __init__(self):
        pass

    def handle(self, connection: ISocketConnection):
        pass


class Network:
    def __init__(self, handler=SocketConnectionHandler, NetworkConnection=SocketConnection):
        self.__NetworkConnection = NetworkConnection
        self.__handler = handler()
        self.connections = []

    def accept(self, connection: tuple, blocking: bool):
        self.connections.append(self.__NetworkConnection(connection, blocking))

    def close(self, connection: ISocketConnection):
        connection.close()
        if connection in self.connections:
            self.connections.remove(connection)

    def handle(self, connection: ISocketConnection):
        # TODO Make it async
        # WARNING: Blocking method
        self.__handler.handle(connection)
