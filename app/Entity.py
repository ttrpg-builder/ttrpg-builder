from abc import ABC, abstractmethod
from pydantic import BaseModel, Field
from typing import List, Any
import json

# Define the classes for stats, actions, inventory items, and resources

class Stat(BaseModel):
    name: str
    value: int

class Action(BaseModel):
    name: str
    description: str

class InventoryItem(BaseModel):
    name: str
    quantity: int

class Resource(BaseModel):
    name: str
    amount: int

class AbstractEntity(BaseModel, ABC):
    name: str = Field(..., description="The name of the entity.")
    description: str = Field(..., description="A brief description of the entity.")
    stats: List[Stat] = Field(default_factory=list, description="Statistics of the entity.")
    type: List[str] = Field(default_factory=list, description="The types of the entity.")
    actions: List[Action] = Field(default_factory=list, description="List of actions the entity can perform.")
    inventory: List[InventoryItem] = Field(default_factory=list, description="List of items in the entity's inventory.")
    resources: List[Resource] = Field(default_factory=list, description="Resources owned by the entity.")
    
    def get_name(self) -> str:
        return self.name

    def get_description(self) -> str:
        return self.description
    
    
    @abstractmethod
    def dump(self, format: str = 'json') -> str:
        """Dump the entity to a specified format."""
        pass

    @abstractmethod
    def load(self, data: str, format: str = 'json') -> None:
        """Load the entity from a specified format."""
        pass



