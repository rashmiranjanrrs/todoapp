# Create methods that will be called when particular api url is called.

# Eg. localhost:5000/api/user/login is the request url,
# You should define a function here to handle the login logic.

# Call the related CRUD operation method from your USER model to perform db queries
from flask import request, jsonify
from app.model.User import User
from flask_httpauth import HTTPBasicAuth

auth = HTTPBasicAuth()

class UserController:

  def signup():
    data = request.get_json()

    username = data['username']
    password = data['password']
    email = data['email']
    user = User(username, password, email)
    User.signup(user)
    return jsonify({
      'response': 'User ' + username + ' created successfully'
    })