import json
import socket
import chatroom
from typing import List
import input_handler

InputHandler = input_handler.InputHandler


class Peer:
    def __init__(self, ip_address, port, username="User") -> None:
        self.ip_address = ip_address
        self.port = port
        self.username = username
        self.listening_socket = socket.create_server((self.ip_address, self.port), backlog=10)
        self.chat_rooms: List[chatroom.ChatRoom] = []
        self.connection_sockets: List = []

    def wait_for_incoming_connections(self) -> None:
        print("Ready for incoming connections!")
        while True:
            conn, addr = self.listening_socket.accept()
            get_data(conn)

    def create_chat_room(self, users: List) -> None:
        chat_room = chatroom.ChatRoom(users)
        self.chat_rooms.append(chat_room)
        self.connect_to_users(chat_room)

    def connect_to_users(self, chat: chatroom.ChatRoom) -> None:
        users = chat.get_users_info()
        for user in users:
            sock = socket.create_connection((user[0], user[1]))
            self.connection_sockets.append(sock)
        self.start_messaging()

    def start_messaging(self):
        while True:
            message = input()
            message = InputHandler(self.username, message).get_processed_message()
            e = json.loads(message)
            self.broadcast(self.connection_sockets, message)

    def broadcast(self, sockets: List, message: str) -> None:
        for sock in sockets:
            sock.sendall(message.encode())


def parse_json(data):
    username, message = data["username"], data["body"]
    return username, message


def get_data(connection) -> None:
    while True:
        # TODO
        # изменить костыль на что-то нормальное
        # работает только с process_message

        data = connection.recv(15)
        bytes_to_read = data[9:13].decode()
        if len(bytes_to_read) > 0:
            temp = connection.recv(int(bytes_to_read))
            data += temp
            if len(data) > 0:
                output = parse_json(json.loads(data.decode()))
                print(output[0] + " > " + output[1])
