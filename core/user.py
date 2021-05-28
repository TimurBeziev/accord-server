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
