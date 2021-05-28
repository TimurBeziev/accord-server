from flask.json import JSONEncoder
from core.dht import DHT
from core.user import User


class AccordJsonEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, User) or isinstance(obj, DHT):
            return obj.serialize()
        return super(AccordJsonEncoder, self).default(obj)
