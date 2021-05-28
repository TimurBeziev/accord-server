import json


class DHT:
    def __init__(self, user):
        self.table = dict()
        self.add_user(user)

    def add_user(self, user):
        if user.id in self.table:
            # raise Exception("user already exists in table")
            return
        self.table[user.id] = user

    def remove_user(self, user_id):
        if user_id in self.table:
            self.table.pop(user_id)

    def get_user(self, user_id: int):
        return self.table[user_id]

    def get_all_users_dict(self):
        return self.table

    def serialize(self):
        return json.dumps([user.serialize() for user in self.table.values()])

