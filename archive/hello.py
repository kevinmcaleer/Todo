from app import app
from forms import NameForm
from flask import session, redirect, render_template, url_for, flash

@app.route('/', methods=['GET','POST'])
def index():
    name = None
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
            flash('It looks like you changed your name')
        session['name'] = form.name.data
        return redirect(url_for('index'))
    return render_template('index.html', 
        form=form, name=session.get('name'))