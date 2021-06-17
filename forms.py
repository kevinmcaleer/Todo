from flask_wtf import FlaskForm
from sqlalchemy.orm import defaultload
from wtforms import StringField, SubmitField
from wtforms.fields.core import BooleanField, DateField, SelectField
from wtforms.validators import DataRequired
from wtforms.widgets.core import CheckboxInput
from models import Todo_list

class NameForm(FlaskForm):
    name = StringField('Add item', validators=[DataRequired()])
    submit = SubmitField('Submit')

class ItemForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    status_choices = ['NOT_STARTED','IN_PROGRESS','COMPLETE']
    priority_choices = ['LOW','MEDIUM','HIGH']
    list_choices = Todo_list.query.all()
    status = SelectField('Status', choices=status_choices)
    priority = SelectField('Priority', choices=priority_choices)
    flag = BooleanField('Flag')
    url = StringField('URL')
    due_date = DateField('Date', format="%m/%d/%Y")
    icon = StringField('Icon')
    state = BooleanField('Active')
    notes = StringField('Notes')
    list_name = SelectField('List', choices=list_choices)
    submit = SubmitField('Submit')