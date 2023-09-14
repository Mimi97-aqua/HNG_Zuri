from flask import jsonify
from data.resource import *
from flask_marshmallow import Marshmallow
import json

# Initialization
ma = Marshmallow(app)


# Class definition for Marshmallow Person Schema
class PersonSchema(ma.Schema):
    class Meta:
        fields = ('user_id', 'name', 'gender', 'email', 'age', 'weight')


person_schema = PersonSchema()
persons_schema = PersonSchema(many=True)


# Fetch details of a person
@app.route('/api', methods=['GET'])
def read():
    persons = Person.query.all()
    result = persons_schema.dump(persons)
    result = json.dumps(result, indent=4)
    return result, 200, {'Content-Type': 'application/json'}


# print(app.url_map)
if __name__ == "__main__":
    app.run()
