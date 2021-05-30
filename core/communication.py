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
            It receives 3 parameters such as chat_id,
            chat_name and user_id
            """
            # chat_id = request.args.get('chat_id', type=int)
            # chat_name = request.args.get('chat_name', type=str)
            # port = request.args.get('port', type=int)
            # user = request.args.get('user_id', type=int)
            response = requests.get('http://localhost:8081/node/join_network')
            print(response.json())
            # port = response.json()
            # print(port)
            if response:
                print('Success!')
                # print(response.json())
                # user = User(user_address=('localhost', response["port"]),
                #             user_name=args.username,
                #             user_id=random.getrandbits(160))
            else:
                print('An error has occurred.')
            # dht.add_user(user)
            # chat1: Chat = Chat(chat_id, chat_name, user, port)
            # storage.add_chat(chat1)
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
