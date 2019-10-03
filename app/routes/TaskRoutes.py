from app.controller.TaskController import TaskController
from app.controller import auth
from flask import Blueprint


taskroutes = Blueprint("taskroutes", __name__)


@taskroutes.route('/addtask', methods=['POST'])
@auth.auth.login_required
def addtask():
    return TaskController.addtask()

@taskroutes.route('/taskdone', methods=['GET'])
@auth.auth.login_required
def markdone():
    return TaskController.markdone()

@taskroutes.route('/deletetask', methods=['POST'])
@auth.auth.login_required
def deletetask():
    return TaskController.deletetask()

@taskroutes.route('/showtasks', methods=['GET'])
@auth.auth.login_required
def alltasks():
    return TaskController.alltasks()

@taskroutes.errorhandler(500)
def error(e):
    return "Put the information properly !! 500 error"

@taskroutes.errorhandler(400)
def error(e):
    return "check your input data properly !! 400 error"



