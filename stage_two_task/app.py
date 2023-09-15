from flask import jsonify, request
from data.resource import *
import json


# CREATE: Adding a new person
@app.route('/api', methods=['GET', 'POST'])
def create():
    if request.method == 'GET':
        persons = Person.query.all()
        data = [person.serialize() for person in persons]
        result = json.dumps(data, indent=4)
        return result, 200, {'Content-Type': 'application/json'}
    elif request.method == 'POST':
        name = request.json.get('name')
        gender = request.json.get('gender')
        email = request.json.get('email')
        age = request.json.get('age')
        weight = request.json.get('weight')

        person_new = Person(name=name, gender=gender, email=email, age=age, weight=weight)
        db.session.add(person_new)
        db.session.commit()

        data = person_new.serialize()
        result = json.dumps(data, indent=4)
        return result, 201, {'Content-Type': 'application/json'}
    else:
        return jsonify(message='Incorrect HTTP verb'), 405


# READ: Fetch details of a person
# UPDATE: Modify details of a person
# DELETE: Removing a person
@app.route('/api', methods=['GET', 'PUT', 'DELETE'])
def rud_operations():
    user_id = request.args.get('user_id')
    name = request.args.get('name')
    gender = request.args.get('gender')
    email = request.args.get('email')
    age = request.args.get('age')
    weight = request.args.get('weight')

    person = None

    if user_id:
        person = Person.query.get(user_id)
    elif name:
        person = Person.query.filter_by(name=name).first()
    elif gender:
        person = Person.query.filter_by(gender=gender).first()
    elif email:
        person = Person.query.filter_by(email=email).first()
    elif age:
        person = Person.query.filter_by(age=age).first()
    elif weight:
        person = Person.query.filter_by(weight=weight).first()

    if request.method == 'GET':
        if person:
            data = person.serialize()
            result = json.dumps(data, indent=4)
            return result, 200, {'Content-Type': 'application/json'}
        else:
            return jsonify(message='That user_id does not exist'), 401
    elif request.method == 'PUT':
        if person:
            # Update info
            name = request.json.get('name')
            gender = request.json.get('gender')
            email = request.json.get('email')
            age = request.json.get('age')
            weight = request.json.get('weight')

            # Modify info
            person.name = name
            person.gender = gender
            person.email = email
            person.age = age
            person.weight = weight

            # Save changes to db
            db.session.commit()

            data = person.serialize()
            result = json.dumps(data, indent=4)
            return result, 200, {'Content-Type': 'application/json'}
        else:
            return jsonify(message='This user_id does not exist'), 401
    elif request.method == 'DELETE':
        if person:
            db.session.delete(person)
            db.session.commit()
            return jsonify(message='Person has been successfully deleted.'), 202
        else:
            return jsonify(message='A person with this user_id does not exist.'), 401
    else:
        return jsonify(message='Incorrect HTTP verb'), 405


# print(app.url_map)
if __name__ == "__main__":
    app.run()
