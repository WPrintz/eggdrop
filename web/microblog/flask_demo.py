# https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world
# To run the application you set the FLASK_APP=flask_demo.py;  $ flask run

from app import app

# from flask import Flask
# app = Flask(__name__)
#
# from app import routes

# @app.route("/")
# def index():
#     return "Index!"
#
# @app.route("/hello")
# def hello():
#     return "Hello World!"
#
# @app.route("/members")
# def members():
#     return "Members"
#
# @app.route("/members/<string:name>/")
# def getMember(name):
#     return "</string:name>"
#
# if __name__ == "__main__":
#     app.run()
