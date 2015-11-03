from flask import Flask
import os
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
db = SQLAlchemy(app)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://apoorva:apoorva@localhost/todoapp'
from views import *

if __name__ == '__main__':
    app.run()
