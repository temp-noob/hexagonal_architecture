"""
    Entity definitions for Pet Entity
"""

from typing import List
from dataclasses import dataclass

@dataclass
class Pet:
    name: str
    species: str
    age: int
    breed: str
    owners: List[str]
