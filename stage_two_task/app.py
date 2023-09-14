from flask import jsonify
from data.resource import *
import json


# Fetch details of a person
@app.route('/api/<int:user_id>', methods=['GET'])
def read(user_id: int):
    person = Person.query.get(user_id)
    if person:
        data = person.serialize()
        result = json.dumps(data, indent=4)
        return result, 200, {'Content-Type': 'application/json'}
    else:
        return jsonify(message='That user_id does not exist'), 401


# print(app.url_map)
if __name__ == "__main__":
    app.run()
