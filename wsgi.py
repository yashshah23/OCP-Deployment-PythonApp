from email.mime import application
import os
from flask import Flask
app = Flask(__name__)
application = app

@app.route("/")
def main():
    return "Welcome!"

@app.route("/how_are_you")
def hello():
    return "I am good! How about you?"

if __name__ == "__main__":
    app.run()