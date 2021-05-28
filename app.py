from flask      import Flask
from core.dht   import DHT
from core.user  import User
from core.communication import AccordBP
from core.encoder import AccordJsonEncoder as encoder

import argparse
import random


app = Flask(__name__)
app.json_encoder = encoder


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('port', type=int)
    parser.add_argument('username', type=str)
    return parser.parse_args()


def main():
    args = parse_args()
    dht = DHT(User(
        user_address=('localhost', args.port),
        user_name=args.username,
        user_id=random.getrandbits(160)
        ))
    app.register_blueprint(AccordBP(dht).get_bp())
    app.run(host='localhost', port=args.port)


if __name__ == '__main__':
    main()
