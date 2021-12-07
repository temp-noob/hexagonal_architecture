import typing
from flask import Flask, request, jsonify

from src.interactors import request_orchestrators
from src.entities.person import Person

app = Flask(__name__)

@app.route('/getPetOwnersInfo', methods=['GET'])
def query_pet_owners_info():
    pet_name = request.args.get('name')
    person_info: typing.List[Person] = request_orchestrators.get_pet_owners_info(pet_name)
    return jsonify({'PersonInfo': person_info})

@app.route('/addPet', methods=['POST'])
def add_pet():
    req_json = request.data
    request_orchestrators.add_pet(req_json)

@app.route('/addPerson', methods=['POST'])
def add_person():
    req_json = request.data
    request_orchestrators.add_person(req_json)

app.run(debug=True)
