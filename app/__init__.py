from flask import Flask
from flask_caching import Cache
from flask_sqlalchemy import SQLAlchemy
# local imports
import pymysql #MYSQL-python is not working for me
from config import app_config

pymysql.install_as_MySQLdb() #for avioding MySQLdb error
db = SQLAlchemy()
cache = Cache(config={'CACHE_TYPE': 'simple'})


def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config['production'])
    app.config.from_pyfile('config.py')

    db.init_app(app)
    cache.init_app(app)

    from .routes.TaskRoutes import taskroutes as taskroutes_blueprint
    app.register_blueprint(taskroutes_blueprint)
    from .routes.UserRoutes import userroutes as userroutes_blueprint
    app.register_blueprint(userroutes_blueprint)
    return app
