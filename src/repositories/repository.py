'''
    Repository for DB interaction of aimin people/pets
'''

import typing
from abc import ABC, abstractmethod

from src.entities.person import Person
from src.entities.pets import Pet


class Repository(ABC):

    @abstractmethod
    def add_pet(self, pet: Pet) -> typing.Union[None, Exception]:
        """
            abstract method to add pet to aiminpetpeople db
        """

    @abstractmethod
    def update_pet(self, pet: Pet) -> typing.Union[None, Exception]:
        """
            abstract method to add pet to aiminpetpeople db
        """

    @abstractmethod
    def get_pet(self, name: str) -> typing.Union[typing.List[Pet], Exception]:
        """
            abstract method to add pet to aiminpetpeople db
        """

    @abstractmethod
    def delete_pet(self, name: str) -> typing.Union[typing.List[Pet], Exception]:
        """
            abstract method to add pet to aiminpetpeople db
        """

    @abstractmethod
    def add_person(self, person: Person) -> typing.Union[None, Exception]:
        """
            abstract method to add pet to aiminpetpeople db
        """

    @abstractmethod
    def update_person(self, person: Person) -> typing.Union[None, Exception]:
        """
            abstract method to add pet to aiminpetpeople db
        """

    @abstractmethod
    def get_person(self, name: str) -> typing.Union[typing.List[Person], Exception]:
        """
            abstract method to add pet to aiminpetpeople db
        """

    @abstractmethod
    def delete_person(self, name: str) -> typing.Union[typing.List[Person], Exception]:
        """
            abstract method to add pet to aiminpetpeople db
        """