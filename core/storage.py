from typing import List
import json


class Message:
    def __init__(self, user, data, timestamp):
        self.user = user
        self.data = data
        self.timestamp = timestamp

    def serialize(self):
        return {
            'user': self.user.serialize(),
            'data': self.data,
            'timestamp': self.timestamp
        }

    @staticmethod
    def deserialize(data: str):
        data = json.loads(data)
        return Message(User.load_from_dict(data['user']),
                       data['data'],
                       data['timestamp'])


class Chat:
    def __init__(self, chat_id, chat_name, user):
        self.id = chat_id
        self.name = chat_name
        self.user = user
        self.messages = []

    def add_message(self, message):
        self.messages.append(message)
        self.messages.sort(key=lambda x: x.timestamp)

    def get_messages(self):
        return self.messages

    def get_user(self):
        return self.user

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'messages': [message.serialize() for message in self.messages]
        }


class Storage:
    def __init__(self):
        self.chats = dict()

    def add_chat(self, chat: Chat):
        self.chats[chat.id] = chat

    def get_all_chats(self):
        return self.chats.values()

    def get_chat_by_id(self, chat_id):
        if chat_id not in self.chats.keys():
            return None
        return self.chats[chat_id]

    def get_chat_messages(self, chat: Chat):
        if chat is None:
            return None
        return chat.get_messages()

    def get_chat_port(self):
        list_of_peers_ports: List = list(self.chats.values())
        print(list_of_peers_ports)
        return


from core.user import User

if __name__ == '__main__':
    pass
    # msg1_str = '{"user": {"id": 12, "host": "localhost", "port": 8085, "name": "Alex"}, "data": "Hello, Bob!", ' \
    #            '"timestamp": 123}'
    # msg2_str = '{"user": {"id": 12, "host": "localhost", "port": 8085, "name": "Alex"}, "data": "Hello, Bob!", ' \
    #            '"timestamp": 123}'
    # msg1 = Message.deserialize(msg1_str)
    # msg2 = Message.deserialize(msg2_str)
    # print(json.dumps(msg1.serialize()))
    # print(json.dumps(msg2.serialize()))
    # --------------------------------------------------
    # user1 = User(('localhost', 8085), 'Alex', 12)
    # self_user = User(('localhost' , 8086), 'Bob', 22)
    # chat = Chat(1, 'chat1', user1)
    # msg1 = Message(user1, 'Hello, Bob!', 123)
    # msg2 = Message(self_user, 'Hello, Alex!', 1234)
    # chat.add_message(msg1)
    # chat.add_message(msg2)
    # chat.add_message(msg2)
    # chat.add_message(msg1)
    # print(json.dumps(chat.serialize()))
