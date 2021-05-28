class Chat:
    def __init__(self, chat_id, chat_name, user):
        self.id = chat_id
        self.name = chat_name
        self.user = user


class Storage:
    def __init__(self):
        self.chats = dict()

    def add_chat(self, chat):
        self.chats[chat.id] = chat
