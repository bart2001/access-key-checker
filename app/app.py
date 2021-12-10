from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/check', methods=['GET'])
def check():
    hour = request.args.get('hour', '')
    return f"hour={hour}"