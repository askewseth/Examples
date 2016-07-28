from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://new:pass@localhost/testdb'

db = SQLAlchemy(app)


class Example(db.Model):
    """newex = Example(1, "first entry")"""
        __tablename__ = 'example'

        id = db.Column('id', db.Integer, primary_key=True)
        # If error thrown change to db.Unicode
        data = db.Column('data', db.String(100))

        # Allows you to access and add to the database easily
        def __init__(self, id, data):
            self.id = id
            self.data = data


class Person(db.Model):
    """person1 = Person(name='Anthony')"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    # Relationship to Pet
    pets = db.relationship('Pet',
                           # 'Virtual' Column in table
                           backref='owner',
                           # person.pets returns query
                           lazy='dynamic')


class Pet(db.Model):
    """pet1 = Pet(name='Spot', owner=person1)"""

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    # Relationship to Person
    owner_id = db.Column(db.Integer, db.ForeignKey('person.id'))
