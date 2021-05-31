import json
from typing import List

import requests
from flask import Blueprint, request, make_response, render_template, redirect
from flask.json import jsonify
from core.dht import DHT
from core.user import User
from core.storage import Chat, Storage, Message


class AccordBP:
    def __init__(self, dht, user, storage):
        self.storage = storage
        self.dht: DHT = dht
        self.user = user
        self.accord = Blueprint('accord', __name__)

        @self.accord.get('/node/join_network')
        def node_join_network():
            """ This method returns DHT of the node in JSON format.
            """
            return jsonify(self.dht)

        @self.accord.post('/node/write_message')
        def node_write_message():
            """ This method receives a new message to a specified chat.
            It receives 2 parameters chat_id, data
            """
            chat_id = request.args.get('chat_id', type=int)
            data = request.args.get('data', type=str)

            message = Message.deserialize(data)
            chat = self.storage.get_chat_by_id(chat_id)
            chat.add_message(message)

        @self.accord.post('/ui/write_message')
        def ui_write_message():
            """ This method sends a new message to a specified chat on another node.
            It receives 3 parameters chat_id, data, timestamp, port
            """
            data = request.args.get('data', type=str)
            port = request.args.get('port', type=int)
            chat_id = request.args.get('chat_id', type=int)
            timestamp = request.args.get('timestamp', type=int)

            chat = self.storage.get_chat_by_id(chat_id)
            msg = Message(self.user, data, timestamp)
            chat.add_message(msg)
            # TODO send request to localhost:port/node/write_message

        @self.accord.post('/ui/get_available_users')
        def ui_get_available_users():
            # returns dict (user_id, user)
            dht_users = self.dht.get_all_users_dict
            existing_users = []

            storage_chats: List[Chat] = storage.get_all_chats()
            for chat in range(len(storage_chats)):
                existing_users.append(storage_chats[chat].get_user())
            return dht_users - existing_users

        @self.accord.get('/new_chat')
        def ui_create_new_1v1_chat():
            """ This method creates new 1v1 Chat class.
            It receives 3 parameters such as chat_id, chat_name and user_port.
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
