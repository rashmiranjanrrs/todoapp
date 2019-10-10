from app.controller.TaskController import TaskController
from app.controller import auth
from flask import Blueprint
from app import cache


taskroutes = Blueprint("taskroutes", __name__)

@taskroutes.route('/addtask', methods=['POST'])
@auth.auth.login_required
def addtask():
    try:
        if request.get_json()["content"]:
            return TaskController.addtask()
    except KeyError:
        return jsonify({"error":"please add content"}), 500

@taskroutes.route('/taskdone', methods=['GET'])
@auth.auth.login_required
def markdone():
    try:
        if request.get_json()["task_id"]:
            return TaskController.markdone()
    except KeyError:
        return jsonify({"error":"please add task_id"}), 500

@taskroutes.route('/deletetask', methods=['POST'])
@auth.auth.login_required
def deletetask():
    try:
        if request.get_json()["task_id"]:
            return TaskController.deletetask()
    except KeyError:
        return jsonify({"error": "please add task_id"}), 500

@taskroutes.route('/showtasks', methods=['GET'])
@cach.cached(timeout=30)
@auth.auth.login_required
def alltasks():
    return TaskController.alltasks()

@taskroutes.errorhandler(500)
def error1(e):
    return "Put the information properly !! 500 error", 500

@taskroutes.errorhandler(400)
def error2(e):
    return "check your input properly !! 400 error", 400


