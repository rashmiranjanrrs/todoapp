# Define your CRUD operations related to TASK table here

# Use the database connection from Database serive in this Task constructor, so that it will
# available in all TASK crud operations

# CRUD means -> Create, Read, Update, Delete actions for a table.
from app import db
import datetime

class Task(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  content = db.Column(db.Text)
  add_date = db.Column(db.DateTime, default=datetime.datetime.now())
  end_date = db.Column(db.DateTime)
  done = db.Column(db.Boolean, default=False)
  user = db.relationship('User', backref='tasks', lazy=True)
  user_id = db.Column(db.Integer, db.ForeignKey('user.id'), default=False)

  def __init__(self, content, user):
    self.content = content
    self.user = user

  def __repr__(self):
    return '<Task %r>' % self.content

  def addtask(task):
    db.session.add(task)
    db.session.commit()

  def markdone(end_date):
    db.session.commit()

  def deletetask(task):
    db.session.delete(task)
    db.session.commit()



 # def __init__(self):
    # select your task table from the db connection and use in Methods

