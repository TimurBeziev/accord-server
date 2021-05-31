import sys
from flask import *

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('app.html')

@app.route('/connect', methods=('GET', 'POST'))
def connect():
    print("l")
    return "hello"

if __name__ == "__main__":
    app.run(port=5000)