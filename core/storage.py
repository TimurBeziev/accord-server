from typing import List


class Chat:
    def __init__(self, chat_id, chat_name, user, port):
        self.id = chat_id
        self.name = chat_name
        self.user = user
        self.peer_port = port

    def get_port(self):
        return self.peer_port


class Storage:
    def __init__(self):
        self.chats = dict()

    def add_chat(self, chat: Chat):
        self.chats[chat.id] = chat

    def get_chat_port(self):
        list_of_peers_ports: List = list(self.chats.values())
        print(list_of_peers_ports)
        return
