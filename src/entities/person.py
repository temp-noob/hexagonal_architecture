"""
    Entity definitions for People Entity
"""

from dataclasses import dataclass

@dataclass
class Person:
    name: str
    contact: str
    age: int
    address: str
    year_of_joining: int
