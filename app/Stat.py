from abc import ABC, abstractmethod
from pydantic import BaseModel, Field
from typing import List, Any
import json

class Stat(BaseModel):
    name: str
    value: int
    description: str

    def get(self) -> int:
        return self.value

    def set_value(self, value: int) -> None:
        self.value = value

    def modify_value(self, modifier: int) -> None:
       self.value += modifier
    
    def set_name(self, name:str) -> None:
        self.name = name
    def set_description(self, description:str) -> None:
        self.description = descritption

