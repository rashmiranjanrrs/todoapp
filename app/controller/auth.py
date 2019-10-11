from app.model.User import User
from flask_httpauth import HTTPBasicAuth

auth = HTTPBasicAuth()
@auth.get_password
def pass_auth(username):
    user = User.query.filter_by(username=username).first()
    if user is not None:
        return user.password
    else:
        return None
