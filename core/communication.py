from flask import Blueprint, request, make_response
from flask.json import jsonify
from core.storage import *


class AccordBP:
    def __init__(self, dht, user, storage):
        self.storage = storage
        self.dht = dht
        self.user = user
        self.accord = Blueprint('accord', __name__)

        @self.accord.get('/node/join_network')
        def join_network():
            """ This method returns DHT of the node in JSON format
            """
            return jsonify(self.dht)

        @self.accord.post('/ui/new_chat')
        def ui_create_new_1v1_chat():
            """ This method creates new 1v1 Chat class
            It receives 3 parameters such as chat_id,
            chat_name and user_id
            """
            chat_id   = request.args.get('chat_id', type=int)
            chat_name = request.args.get('chat_name', type=str)
            try:
                user = dht.get_user(request.args.get('user_id', type=int))
                storage.add_chat(Chat(chat_id, chat_name, user))
            except Exception:
                return make_response(status_code=500, text='Internal server error!')
            return make_response(status_code=200)

    def get_bp(self):
        return self.accord
