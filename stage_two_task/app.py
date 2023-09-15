from flask import jsonify, request
from data.resource import *
import json
from sqlalchemy import or_


# CREATE: Adding a new person
@app.route('/api', methods=['POST'])
def create():
    if request.method == "POST":
        user_id = request.args.get('user_id')
        name = request.json.get('name')

        # Check if person already exists in db
        existing_person = Person.query.filter(or_(user_id=user_id, name=name)).first()

        if existing_person:
            return jsonify(message='Person already exists.'), 409
        else:
            new_person = Person(user_id=user_id, name=name)
            db.session.add(new_person)
            db.session.commit()

            data = new_person.serialize()
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

    person = None

    if user_id:
        person = Person.query.get(user_id)
    elif name:
        person = Person.query.filter_by(name=name).first()

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
            return jsonify(message='Person does not exist'), 400
    elif request.method == 'DELETE':
        if person:
            db.session.delete(person)
            db.session.commit()
            return jsonify(message='Person has been successfully deleted.'), 202
        else:
            return jsonify(message='A person matching this value does not exist.'), 401
    else:
        return jsonify(message='Incorrect HTTP verb'), 405


# print(app.url_map)
if __name__ == "__main__":
    app.run()
