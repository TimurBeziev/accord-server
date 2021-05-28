import sys
from flask import *

app = Flask(__name__)

@app.route('/', methods=('GET', 'POST'))
def home():
    data = ""
    if request.method == 'POST':
        data += request.form['data']
    return render_template('app.html', message=data)

@app.route('/postmethod', methods = ['POST'])
def get_post_data():
    data = request.form['data']
    return data

@app.route('/getmessage')
def get_python_data():
    return request.form['data']

if __name__ == "__main__":
    app.run(port=5000)