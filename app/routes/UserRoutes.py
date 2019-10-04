# Handle your routes here with Blueprints

from app.controller.UserController import UserController
from flask import Blueprint

userroutes = Blueprint("userroutes", __name__)
# You can call your controller method here

@userroutes.route('/signup', methods=['POST'])
def signup():
    try:
        if request.get_json()["username"] and request.get_json()["password"] and request.get_json()["email"]:
            return UserController.signup()
    except KeyError:
        return jsonify({"error":"please add all data(username,password and email)"}), 500

@userroutes.errorhandler(500)
def error(e):
    return "Input all the data(username,password,email)!! 500 error", 500

@userroutes.errorhandler(400)
def error(e):
    return "check your input properly!! 400 error", 400
    
