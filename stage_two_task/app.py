from flask import jsonify, request
from data.resource import *
import json


# CREATE: Adding a new person
@app.route('/api', methods=['POST'])
def create():
    if request.method == "POST":
        if request.is_json:
            data = request.get_json()
            name = data.get('name')
        else:
            name = request.args.get('name')

        if name:
            new_person = Person(name=name)
            db.session.add(new_person)
            db.session.commit()

            data = new_person.serialize()
            result = json.dumps(data, indent=4)
            return result, 201, {'Content-Type': 'application/json'}
        else:
            return jsonify(message='Name is required'), 400
    else:
        return jsonify(message='Incorrect HTTP verb'), 405


# READ: Fetch details of a person
# UPDATE: Modify details of a person
# DELETE: Removing a person
@app.route('/api/<int:user_id>', methods=['GET', 'PUT', 'DELETE'])
@app.route('/api/<string:name>', methods=['GET', 'PUT', 'DELETE'])
def rud_operations(user_id=None, name=None):

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
            return jsonify(message='Person matching these values does not exist.'), 401
    elif request.method == 'PUT':
        if person:
            # Update info
            user_id = request.json.get('user_id')
            name = request.json.get('name')

            # Modify info
            person.name = name

            # Save changes to db
            db.session.commit()

            data = person.serialize()
            result = json.dumps(data, indent=4)
            return result, 200, {'Content-Type': 'application/json'}
        else:
            return jsonify(message='Person does not exist'), 400
    elif request.method == 'DELETE':
        db.session.delete(person)
        db.session.commit()
        return jsonify(message='Person has been successfully deleted.'), 202
    else:
        return jsonify(message='Incorrect HTTP verb'), 405


# print(app.url_map)
if __name__ == "__main__":
    app.run()
