import os
import typing
from cassandra.cluster import Cluster

from src.repositories.repository import Repository
from src.entities.person import Person
from src.entities.pets import Pet
from contextlib import contextmanager

class CsqlAdapter(Repository):

    def __init__(self) -> None:
        self.host, self.port, self.keyspace = os.environ['CSQL_HOST'], os.environ['PORT'], \
            os.environ['CSQL_KEYSPACE']

    @contextmanager
    def get_session(self):
        _cluster = Cluster(self.host, port=self.port)
        _session = _cluster.connect(self.keyspace)
        yield _session
        _cluster.shutdown()

    def add_pet(self, pet: Pet) -> typing.Union[None, Exception]:
        with self.get_session() as session:
            session.execute(
                """
                    INSERT INTO pet (name, species, age, breed, owners)
                    VALUES (%s, %s, %s, %s, %s)
                """,
                (pet.name, pet.species, pet.age, pet.breed, pet.owners)
            )

    def update_pet(self, pet: Pet) -> typing.Union[None, Exception]:
        pass

    def get_pet(self, name: str) -> typing.Union[typing.List[Pet], Exception]:
        with self.get_session() as session:
            data = session.execute(
                """
                    select * from pet where name=%s
                """,
                (name)
            )
            resp = [Pet(name=datum[0], species=datum[1], \
                age=datum[2], breed=datum[3], owners=datum[4]) \
                    for datum in data]
        return resp

    def delete_pet(self, name: str) -> typing.Union[typing.List[Pet], Exception]:
        pass

    def add_person(self, person: Person) -> typing.Union[None, Exception]:
        pass

    def update_person(self, person: Person) -> typing.Union[None, Exception]:
        pass

    def get_person(self, name: str) -> typing.Union[typing.List[Person], Exception]:
        pass

    def delete_person(self, name: str) -> typing.Union[typing.List[Person], Exception]:
        pass