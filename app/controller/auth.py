from app.model.User import User
from flask_httpauth import HTTPBasicAuth
from app import cache

auth = HTTPBasicAuth()
@auth.get_password
def pass_auth(username):
    c_password = cache.get('password')
    if c_password == '' or c_password is None:
        user = User.query.filter_by(username=username).first()
        if user is not None:
            password = user.password
            cache.set('password',password)
            return password
        else:
            return None
    
    else:
        return c_password
