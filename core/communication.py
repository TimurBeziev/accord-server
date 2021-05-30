import json

import requests
from flask import Blueprint, request, make_response, render_template, redirect
from flask.json import jsonify
from core.dht import DHT
from core.user import User
from core.storage import Chat, Storage


class AccordBP:
    def __init__(self, dht, user, storage):
        self.storage = storage
        self.dht: DHT = dht
        self.user = user
        self.accord = Blueprint('accord', __name__)

        @self.accord.get('/node/join_network')
        def join_network():
            """ This method returns DHT of the node in JSON format
            """
            return jsonify(self.dht)

        @self.accord.get('/new_chat')
        def ui_create_new_1v1_chat():
            """ This method creates new 1v1 Chat class
            It receives 3 parameters such as chat_id, chat_name and user_port
            """
            chat_id = request.args.get('chat_id', type=str)
            chat_name = request.args.get('chat_name', type=str)
            # user_ip = request.args.get('user_ip', type=int)
            user_port = request.args.get('user_port', type=int)
            link = 'http://localhost' + ':' + str(user_port) + '/node/join_network'
            response = requests.get(link)
            if response:
                peer_info = json.loads(response.text)[1:-1]
                peer_info = json.loads(peer_info)
                peer = User(user_address=('localhost', peer_info["port"]),
                            user_name=peer_info["name"],
                            user_id=peer_info["id"])
                self.dht.add_user(peer)

                chat1: Chat = Chat(chat_id, chat_name, peer, user_port)
                storage.add_chat(chat1)
            else:
                print('An error has occurred.')
            return redirect("/")

        @self.accord.route('/', methods=('GET', 'POST'))
        def home():
            data = ""
            storage.get_chat_port()
            if request.method == 'POST':
                data += request.form['data']
                print(data)
            return render_template("app.html", message=data)

    def get_bp(self):
        return self.accord
