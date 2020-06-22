import os
from flask import flask

app = Flask(__name__)


@app.rout('/')
def hello():
    return 'Hello world ...again'

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.et('PORT'),
            debug=True)
