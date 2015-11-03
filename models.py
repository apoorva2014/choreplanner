import datetime
from todoapp import db

class Todo (db.Model):
    __tablename__ = "todo"
    id = db.Column('id', db.Integer, primary_key=True)
    category_id = db.Column('category_id', db.Integer, db.ForeignKey('category.id'))
    priority_id = db.Column('priority_id', db.Integer, db.ForeignKey('priority.id'))
    description = db.Column('description', db.Unicode)
    creation_date = db.Column('creation_date', db.Date)
    is_done = db.Column('is_done', db.Boolean)

    priority = db.relationship('Priority', foreign_keys=priority_id)
    category = db.relationship('Category', foreign_keys=category_id)


class Priority (db.Model):
   __tablename__ = "priority"
   id = db.Column('id', db.Integer, primary_key=True)
   name = db.Column('name', db.Unicode)
   value = db.Column('value', db.Integer)


class Category (db.Model):
    __tablename__ = "category"
    id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column('name', db.Unicode)

db.create_all()

work = Category(name=u'work')
home = Category(name=u'home')
high = Priority(name=u'high',value=3)
medium = Priority(name=u'medium',value=2)
low = Priority(name=u'low',value=1)

db.session.add(work)
db.session.add(home)
db.session.add(high)
db.session.add(medium)
db.session.add(low)

db.session.commit()
