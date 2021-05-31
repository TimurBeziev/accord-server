import json


class User:
    def __init__(self, user_address, user_name, user_id):
        self.host, self.port = user_address
        self.name = user_name
        self.id = user_id

    def serialize(self):
        return {
            'id': self.id,
            'host': self.host,
            'port': self.port,
            'name': self.name
        }

    def get_username(self):
        return self.name

    @staticmethod
    def load_from_dict(data: dict):
        return User((data['host'], data['port']),
                    data['name'],
                    data['id'])

    @staticmethod
    def deserialize(data: str):
        data = json.loads(data)
        return User((data['host'], data['port']),
                    data['name'],
                    data['id'])
