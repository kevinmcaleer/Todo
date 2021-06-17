# ToDo Web UI
# Kevin McAleer
# June 2021

from flask import Flask, request, render_template, session, redirect, flash, url_for
from app import app, db
from forms import ItemForm, NameForm
from models import Todo_item
from datetime import date

@app.route('/', methods=['GET','POST'])
def index():
    name = None
    form = NameForm()
    items = Todo_item.query.all()
    if form.validate_on_submit():
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
            flash('It looks like you changed your name')
        session['name'] = form.name.data
        return redirect(url_for('index'))
    return render_template('index.html', 
        form=form, name=session.get('name'), items=items)

@app.route('/new_item', methods=['GET','POST'])
def newitem():
    form = ItemForm()
    if form.validate_on_submit():
        newitem = Todo_item()
        newitem.title = form.title.data
        newitem.creation_date = date.today()
        newitem.due_date = form.due_date.data
        newitem.flag = form.flag.data
        newitem.icon = form.icon.data
        newitem.notes = form.notes.data
        newitem.priority = form.priority.data
        newitem.status = form.status.data
        newitem.state = form.state.data
        newitem.list_name = form.list_name.data
        db.session.add(newitem)
        db.session.commit()
        redirect(url_for('index'))
    return render_template('new_item.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)