import typing
import strawberry

from src.entities.person import Person
from src.entities.pets import Pet
from src.interactors import request_orchestrators


@strawberry.type
class PetSchema(Pet):
    pass

@strawberry.type
class PersonSchema(Person):
    pass

@strawberry.type
class Query:
    pet: PetSchema = strawberry.field(resolver=request_orchestrators.add_pet)
    person: PersonSchema = strawberry.field(resolver=request_orchestrators.add_person)
    pet_owners_query: typing.AnyStr = strawberry.field(resolver=request_orchestrators.get_pet_owners_info)

def convertPetToDataclass(petgql: PetSchema) -> Pet:
    '''
        convert field by field to dataclass
    '''
    request_orchestrators.add_pet(pet)
    pass

def convertPersonToDataclass(persongql: PersonSchema) -> Person:
    '''
        convert field by field to dataclass
    '''
    request_orchestrators.add_person(person)
    pass

schema = strawberry.Schema(query=Query)
