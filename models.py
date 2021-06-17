from app import db
from datetime import date

class Todo_list(db.Model):
    """ Models the Todo List"""
    __tablename__ = 'todo_lists'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, default="New List")
    items = db.relationship('Todo_item', backref="list")


class Todo_item(db.Model):
    """ Models the Todo Items """
    __tablename__ = 'todo_items'
    id = db.Column(db.Integer, primary_key=True)
    creation_date = db.Column(db.DateTime, default=date.today())
    title = db.Column(db.String, default="empty")
    status = db.Column(db.String, default="NOT_STARTED")
    priority = db.Column(db.String, default="LOW")
    flag = db.Column(db.Boolean, default=False)
    url = db.Column(db.String, default="")
    due_date = db.Column(db.Date)
    icon = db.Column(db.String, default="")
    state = db.Column(db.Boolean, default=False)
    notes = db.Column(db.String, default="")
    list_name = db.Column(db.Integer, db.ForeignKey('todo_lists.id'))

