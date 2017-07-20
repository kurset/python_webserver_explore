from flask import Flask

flask_app = Flask(__name__)


@flask_app.route('/')
def hello():
    return 'hello world'

app = flask_app.wsgi_app
