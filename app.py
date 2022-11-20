from flask import Flask, render_template
from flask_restful import Resource, Api
from random import randint

app = Flask(__name__, template_folder="html")
api = Api(app)


@app.route('/')
def hello_world(**args):
    return render_template("index.html", name=f"{randint(1, 100)}", **args)


if __name__ == '__main__':
    app.run()
