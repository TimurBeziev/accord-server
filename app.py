from flask import Flask, request, render_template, url_for
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


@app.route('/', methods=('GET', 'POST'))
def home():
    data = ""
    if request.method == 'POST':
        data += request.form['data']
    return render_template("app.html")


@app.route('/postmethod', methods=['POST'])
def get_post_data():
    data = request.form['data']
    return data


@app.route('/getmessage')
def get_python_data():
    return request.form['data']


# метод который шлет запрос по нужному айпи айди
def main():
    args = parse_args()
    user = User(user_address=('localhost', args.port),
                user_name=args.username,
                user_id=random.getrandbits(160))
    dht = DHT(user)
    storage = Storage()
    app.register_blueprint(AccordBP(dht, user, storage).get_bp())
    app.run(host='localhost', port=args.port, debug=True)


if __name__ == '__main__':
    main()
