from flask import Flask,request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    print("hello world")
    return "hello world, from the Flask!<h1>yaswanth</h1>"

@app.route('/service', methods=['POST'])
def process_json():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        json = request.json
        print(json["data"])
        return "working"
    else:
        return 'Content-Type not supported!'