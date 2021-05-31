from flask.json import JSONEncoder
from core.dht import DHT
from core.user import User
from core.storage import Chat, Message


class AccordJsonEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, User)\
                or isinstance(obj, DHT)\
                or isinstance(obj, Chat)\
                or isinstance(obj, Message):
            return obj.serialize()
        return super(AccordJsonEncoder, self).default(obj)
