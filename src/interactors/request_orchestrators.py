from main import DB
import typing
from src.entities.person import Person
from src.entities.pets import Pet

def add_pet(req_json: typing.Dict) -> None:
    new_pet: Pet = Pet(
        name = req_json["name"],
        species=req_json["species"],
        age=req_json["int"],
        breed=req_json["breed"],
        owners=req_json["owners"]
    )
    DB.add_pet(new_pet)

def add_person(req_json: typing.Dict) -> None:
    new_person: Person = Person(
        name = req_json["name"],
        contact=req_json["contact"],
        age=req_json["age"],
        address=req_json["address"],
        year_of_joining=req_json["year_of_joining"]
    )
    DB.add_person(new_person)

def get_pet_owners_info(pet_name: str) -> typing.List[Person]:
    pet: Pet = DB.get_pet(pet_name)
    person_names: typing.List[str] = pet.owners
    resp: typing.List[Person] = []
    for person_name in person_names:
        resp.append(DB.get_person(person_name))
    return person_names
