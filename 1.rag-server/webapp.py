from flask import Flask

flaskApp = Flask(__name__)

@flaskApp.route("/")

def index():
    return "Hello World!"

if __name__ == "__main__":
    flaskApp.run(port=5000)