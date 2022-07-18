import os
from flask import Flask
from wsgiref.simple_server import make_server
app = Flask(__name__)
application = app

@app.route("/")
def main():
    return "Welcome!"

@app.route("/how_are_you")
def hello():
    return "I am good! How about you?"

if __name__ == "__main__":
    
    app.run(host = "0.0.0.0", port = 8080)