from flask import Flask

import utils

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Hello, World!<h2>"

@app.route('/api', methods=['GET'])
def api():
    return "{}"