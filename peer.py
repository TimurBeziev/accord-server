import socket
import sys

import chatroom
from typing import List


class Peer:
    def __init__(self, ip_address, port, username="User") -> None:
        self.ip_address = ip_address
        self.port = port
        self.username = username
        self.chat_rooms: List[chatroom.ChatRoom] = []
        self.connection_sockets: List = []

    def wait_for_incoming_connections(self):
        get_incoming_connections(self.ip_address, self.port)

    def create_chat_room(self, users: List) -> None:
        chat_room = chatroom.ChatRoom()
        chat_room.add_users(users)
        self.chat_rooms.append(chat_room)
        self.connect_to_users(chat_room)

    def connect_to_users(self, chat: chatroom.ChatRoom) -> None:
        users = chat.get_users_info()
        print(users)
        sockets: List = []
        for user in users:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((user[0], user[1]))
            sockets.append(sock)
        broadcast(sockets)


def broadcast(sockets: List):
    while True:
        message = sys.stdin.readline()
        for sock in sockets:
            sock.send(message.encode())


def get_incoming_connections(ip_address, port) -> None:
    print("Ready for incoming connections!")
    listening_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listening_socket.bind((ip_address, int(port)))
    listening_socket.listen(100)
    conn, addr = listening_socket.accept()
    while True:
        data = conn.recv(1024)
        if len(data) > 0:
            print(data.decode())
