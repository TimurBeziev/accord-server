from flask import Blueprint
from flask.json import jsonify


class AccordBP:
    def __init__(self, dht, user):
        self.dht = dht
        self.user = user
        self.accord = Blueprint('accord', __name__)

        @self.accord.get('/join_network')
        def join_network():
            """ This method returns DHT of the node in JSON format
            """
            return jsonify(self.dht)

    def get_bp(self):
        return self.accord
