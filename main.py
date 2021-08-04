from flask import Flask, make_response, request, jsonify
from flask_mongoengine import MongoEngine
from configuration import mongodb_password, database_name

app = Flask(__name__)

DB_URI = "mongodb+srv://m001-student:{}@sandbox.j0jwd.mongodb.net/{}?retryWrites=true&w=majority".format(
    mongodb_password, database_name)
app.config["MONGODB_HOST"] = DB_URI

db = MongoEngine()
db.init_app(app)