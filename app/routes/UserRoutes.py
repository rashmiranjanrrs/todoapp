# Handle your routes here with Blueprints

from app.controller.UserController import UserController
from flask import Blueprint

userroutes = Blueprint("userroutes", __name__)


@userroutes.route('/signup', methods=['POST'])
def signup():
    return UserController.signup()
  # You can call your controller method here