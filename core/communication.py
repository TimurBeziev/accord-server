import json
from typing import List

import requests
from flask import Blueprint, request, make_response, render_template, redirect, Response
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
            Receives new user to add to dht
            """
            user = User.deserialize(request.args.get('user', type=str))
            self.dht.add_user(user)
            return jsonify(self.dht)

        @self.accord.get('/ui/join_network')
        def ui_join_network():
            """This method receives port of node to connect to
            """
            port = request.args.get('port', type=int)
            # TODO correctly process bad request
            r = requests.get(url=f'http://localhost:{port}/node/join_network',
                             params={'user': json.dumps(self.user.serialize())})
            users = [User.load_from_dict(user) for user in json.loads(r.json())]
            self.dht.add_users(users)
            for user in users:
                if user.id != self.user.id:
                    r = requests.get(url=f'http://localhost:{user.port}/node/connect_to_user',
                                     params={'user': json.dumps(self.user.serialize())})
            # TODO use flask.make_response()
            return "ok"

        @self.accord.get('/node/connect_to_user')
        def node_connect_to_user():
            """This method adds to dht user that requests the connection
            It receives user as param that needs to connect
            """
            user = User.deserialize(request.args.get('user', type=str))
            self.dht.add_user(user)
            # TODO use flask.make_response()
            return "ok"

        @self.accord.get('/node/write_message')
        def node_write_message():
            """ This method receives a new message to a specified chat.
            It receives 2 parameters chat_id, data
            """
            chat_id = request.args.get('chat_id', type=int)
            data = request.args.get('data', type=str)

            message = Message.deserialize(data)
            chat = self.storage.get_chat_by_id(chat_id)
            if chat is None:
                # User should be in DHT
                chat = Chat(chat_id, message.user.name, message.user)
                self.storage.add_chat(chat)
            chat.add_message(message)

        @self.accord.get('/ui/write_message')
        def ui_write_message():
            """ This method sends a new message to a specified chat on another node.
            It receives 4 parameters chat_id, data, timestamp, port
            """
            data = request.args.get('data', type=str)
            port = request.args.get('port', type=int)
            chat_id = request.args.get('chat_id', type=int)
            timestamp = request.args.get('timestamp', type=int)

            chat = self.storage.get_chat_by_id(chat_id)
            msg = Message(self.user, data, timestamp)
            chat.add_message(msg)
            # TODO correctly process bad request
            requests.get(url=f'http://localhost:{port}/node/write_message',
                         params={'chat_id': chat_id, 'data': json.loads(msg.serialize())})

        @self.accord.get('/ui/create_chat_with_user')
        def ui_create_chat_with_user():
            """This method created new chat with user
            It receives the user_id, chat_id
            """
            user_id = request.args.get('user_id', type=int)
            chat_id = request.args.get('chat_id', type=int)
            user = self.dht.get_user(user_id)
            chat = Chat(chat_id, user.name, user)
            self.storage.add_chat(chat)
            # TODO correctly process bad request
            return "ok"

        @self.accord.get('/ui/get_available_users')
        def ui_get_available_users():
            # returns dict (user_id, user)
            dht_users = list(self.dht.get_all_users())
            existing_users = []

            storage_chats: List[Chat] = list(storage.get_all_chats())
            for chat in storage_chats:
                existing_users.append(chat.get_user())

            difference = set(dht_users) - set(existing_users)
            return jsonify(list(difference))

        @self.accord.get('/ui/choose_user')
        def ui_choose_user():
            return render_template("choose_user.html")

        @self.accord.get('/check_for_new_chats')
        def check_for_new_messages():
            chats = self.storage.get_all_chats
            if chats is None:
                pass
            return jsonify(chats)

        @self.accord.route('/', methods=('GET', 'POST'))
        def home():
            data = ""
            if request.method == 'POST':
                data += request.form['data']
                print(data)
            return render_template("app.html", message=data)

    def get_bp(self):
        return self.accord
