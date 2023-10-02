from flask import Flask
from api import api

app = Flask(__name__)
app.register_blueprint(api)


@app.route("/")
def hello():
    return "Hello World!"


if __name__ == "__main__":
    app.run()
