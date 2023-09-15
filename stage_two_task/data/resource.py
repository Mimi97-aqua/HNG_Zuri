from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Float, Boolean, CheckConstraint, UniqueConstraint
import os

# Configurations
app = Flask(__name__)
base_directory = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(base_directory, "persons.db")

# Initialization
db = SQLAlchemy(app)


# Flask CLI commands for db
@app.cli.command('db_create')
def db_create():
    db.create_all()
    print('Database successfully created.')


@app.cli.command('db_drop')
def db_drop():
    db.drop_all()
    print('Database successfully dropped')


@app.cli.command('db_seed')
def db_seed():
    person1 = Person(
        name='Emma Busu',
        gender=False,
        email='emma@gmail.com',
        age=30,
        weight=72.5
    )

    person2 = Person(
        name='Matt Sher',
        gender=True,
        email='matt@gmail.com',
        age=25,
        weight=67.2
    )

    person3 = Person(
        name='Liam Song',
        gender=True,
        email='liam@gmaill.com',
        age=47,
        weight=79.0
    )

    # Add objects
    db.session.add(person1)
    db.session.add(person2)
    db.session.add(person3)
    db.session.commit()  # Save objects
    print('Database successfully seeded.')


# Database model
class Person(db.Model):
    __tablename__ = 'persons'
    user_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    gender = Column(Boolean)
    email = Column(String, unique=True)
    age = Column(Integer)
    weight = Column(Float)

    __table_args__ = (
        CheckConstraint('name IS NOT NULL', name='check_name_not_null'),
        UniqueConstraint('email', name='unique_email'),
        CheckConstraint('age >= 0', name='check_age_positive'),
        CheckConstraint('weight >= 0.0', name='check_weight_positive')
    )

    def serialize(self):
        return {
            'user_id': self.user_id,
            'name': self.name,
            'gender': self.gender,
            'email': self.email,
            'age': self.age,
            'weight': self.weight
        }
