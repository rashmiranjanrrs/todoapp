# Handle your routes here with Blueprints

from app.controller.UserController import UserController
from flask import Blueprint

userroutes = Blueprint("userroutes", __name__)


@userroutes.route('/signup', methods=['POST'])
def signup():
    return UserController.signup()

@userroutes.errorhandler(400)
def error(e):
    return "check your input data properly!! 400 error"
    
