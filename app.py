from flask import Flask

from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
import os
basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =\
    'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'security - its a thang'
bootstrap = Bootstrap(app)

db = SQLAlchemy(app)