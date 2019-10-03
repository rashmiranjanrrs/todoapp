from flask import request, jsonify
from app.model.Task import Task
from app.model.User import User
from app.controller import auth

import datetime

class TaskController:


    def addtask():
        data = request.get_json()
        content = data['content']
        task = Task(content, user=User.query.filter_by(username=auth.auth.username()).first())
        Task.addtask(task)
        return jsonify({
            'username': auth.auth.username(),
            'task-id': task.id,
            'content': task.content
        })

    def markdone():
        data = request.get_json()
        task_id = data['task_id']
        task = Task.query.get(task_id)
        if task is None:
            return jsonify({
                'status': 'Failed'
            })
        task.done = True
        task.end_date = datetime.datetime.now()
        Task.markdone(task.end_date)
        return jsonify({
            'content': task.content,
            'add_date': task.add_date,
            'end_date': task.end_date,
            'task_completed': task.done
        })

    def deletetask():
        data = request.get_json()
        task_id = data['task_id']
        task = Task.query.filter_by(id=task_id).first()
        if not task:
            return jsonify({'message': 'No task found!'})

        deleted_task = jsonify({
            'status': 'success',
            'task_id': task.id,
            'content': task.content,
            'task_completed': task.done
        })
        Task.deletetask(task)
        return deleted_task

    def alltasks():
        user = User.query.filter_by(username= auth.auth.username()).first()
        if user is None:
            return jsonify({
                'status': 'failed'
            })
        task_list = {}
        for task in user.tasks:
            task_list[task.id] = {'content': task.content,
                                  'add_date': task.add_date,
                                  'task_completed': task.done}
        return jsonify(task_list)
