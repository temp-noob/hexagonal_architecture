'''
    Postgres adapter for reposotory defined
'''
from sqlalchemy import Column, Integer, MetaData, String, Text, create_engine
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.types import JSON
import contextlib
import os
import typing

from src.repositories.repository import Repository
from src.entities.person import Person
from src.entities.pets import Pet

class PsqlAdapter(Repository):

    def __init__(self):
        uname, pwd, host, db, port = os.environ['PSQL_USERNAME'], os.environ['PSQL_PWD'], \
                    os.environ['PSQL_HOST'], os.environ['PSQL_DB'], int(os.environ['PSQL_PORT'])
        
        try:
            conn_str = f"postgresql://{uname}:{pwd}@{host}:{port}/{db}"
            self.__engine = create_engine(conn_str)
        except Exception as exc:
            #TODO: deal with exception
            print(conn_str, str(exc))
            pass

        try:
            metadata = MetaData()
            metadata.reflect(self.__engine)
            Base = automap_base(metadata=metadata)
            Base.prepare()
            self.__pet_table = Base.classes.pet
            self.__person_table = Base.classes.person
        except Exception as exc:
            #TODO: deal with exception
            print(exc)
            pass 

    @contextlib.contextmanager
    def get_session(self):
        if self._session == None:
            Session = sessionmaker(bind=self.__engine)
            self._session = Session()

        session = self._session

        yield session

        try:
            session.commit()
        except Exception as exc:
            session.rollback()
            raise exc
        finally:
            session.close()
    
    def add_pet(self, pet: Pet) -> typing.Union[None, Exception]:
        new_pet = self.__pet_table(name=pet.name, species=pet.species, age=pet.age, \
            breed=pet.breed, owners=pet.owners)
        with self.get_session() as session:
            session.add(new_pet)

    def update_pet(self, pet: Pet) -> typing.Union[None, Exception]:
        pass

    def get_pet(self, name: str) -> typing.Union[typing.List[Pet], Exception]:
        with self.get_session() as session:
            data = session.query(self.__pet_table).\
                filter(self.__pet_table.name==name).all()
            resp = [Pet(name=datum.name, species=datum.species, \
                age=datum.age, breed=datum.breed, owners=datum.owners) \
                    for datum in data]
        return resp

    def delete_pet(self, name: str) -> typing.Union[typing.List[Pet], Exception]:
        pass

    def add_person(self, person: Person) -> typing.Union[None, Exception]:
        new_person = self.__person_table(name=person.name, contact=person.contact, age=person.age, \
            address=person.address, year_of_joining=person.year_of_joining)
        with self.get_session() as session:
            session.add(new_person)

    def update_person(self, person: Person) -> typing.Union[None, Exception]:
        pass
    
    def get_person(self, name: str) -> typing.Union[typing.List[Person], Exception]:
        with self.get_session() as session:
            data = session.query(self.__person_table).\
                filter(self.__person_table.name==name).all()
            resp = [Person(name=datum.name, contact=datum.contact, \
                age=datum.age, address=datum.address, year_of_joining=datum.year_of_joining) \
                    for datum in data]
        return resp

    def delete_person(self, name: str) -> typing.Union[typing.List[Person], Exception]:
        pass
