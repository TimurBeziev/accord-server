from flask import Flask
from core.dht import DHT
from core.user import User
from core.storage import Storage
from core.encoder import AccordJsonEncoder as encoder
from core.communication import AccordBP

import argparse
import random

app = Flask(__name__, template_folder="flask-version/templates", static_folder="flask-version/templates")
app.json_encoder = encoder


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('port', type=int)
    parser.add_argument('username', type=str)
    return parser.parse_args()


def main():
    args = parse_args()
    user = User(user_address=('localhost', args.port),
                user_name=args.username,
                user_id=random.getrandbits(50))  # change to 160 for unique

    dht = DHT(user)
    storage = Storage()
    app.register_blueprint(AccordBP(dht, user, storage).get_bp())
    app.run(host='localhost', port=args.port, debug=True)


if __name__ == '__main__':
    main()
