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
        name='Emma Busu'
    )

    person2 = Person(
        name='Matt Sher'
    )

    person3 = Person(
        name='Liam Song'
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
    user_id = Column(String(64), primary_key=True, nullable=False, unique=True)
    name = Column(String(255), nullable=False)

    __table_args__ = (
        CheckConstraint("user_id ~ '^[0-9]+$'", name="check_id_is_string"),
        CheckConstraint("name ~ '^[A-Za-z]+$'", name='check_name_string'),
        CheckConstraint('user_id IS NOT NULL', name='check_name_not_null'),
        CheckConstraint('name IS NOT NULL', name='check_name_not_null'),
        CheckConstraint('user-id >= 0', name='check_user_id_positive'),
    )

    def serialize(self):
        return {
            'user_id': self.user_id,
            'name': self.name
        }
