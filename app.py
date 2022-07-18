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
    
    ip = os.environ['OPENSHIFT_PYTHON_IP'] 
    port = os.environ['OPENSHIFT_PYTHON_PORT']
    httpd = make_server(ip, port, application)
    #app.run(host = ip, port = port)