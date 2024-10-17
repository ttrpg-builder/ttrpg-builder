from abc import ABC, abstractmethod
from pydantic import BaseModel, Field
from typing import List, Optional, Any
import json
from math import floor

from Stat import Stat, BaseStat
from Item import Item, BaseItem
from Class import Class
from Species import Species

"""
This module defines the classes for stats, actions, inventory items, and resources
related to an entity in a game or simulation. It includes abstract base classes
for entities that can be extended to create specific types of entities.
"""

#TODO create own classfile
class Action(BaseModel):
    """
    Represents an action that an entity can perform.
    
    Attributes:
        name (str): The name of the action.
        description (str): A brief description of the action.
    """
    name: str
    description: str

#TODO create own classfile
class Resource(BaseModel):
    """
    Represents a resource owned by an entity.
    
    Attributes:
        name (str): The name of the resource.
        amount (int): The amount of the resource.
    """
    name: str
    amount: int


class Entity(BaseModel, ABC):
    """
    Abstract base class for an entity.
    
    Attributes:
        name (str): The name of the entity.
        description (str): A brief description of the entity.
        stats (List[Stat]): Statistics of the entity.
        type (List[str]): The types of the entity.
        actions (List[Action]): List of actions the entity can perform.
        inventory (List[Item]): List of items in the entity's inventory.
        resources (List[Resource]): Resources owned by the entity.
    """
    name: str = Field(..., description="The name of the entity.")
    description: str = Field(..., description="A brief description of the entity.")
    stats: List[Stat] = Field(default_factory=list, description="Statistics of the entity.")
    entityclass: Class = Field(default_factory=list, description="The entity class")
    species: Species = Field(default_factory=list, description="The species of the entity.")
    actions: List[Action] = Field(default_factory=list, description="List of actions the entity can perform.")
    inventory: List[Item] = Field(default_factory=list, description="List of items in the entity's inventory.")
    resources: List[Resource] = Field(default_factory=list, description="Resources owned by the entity.")
    
    def get_name(self) -> str:
        """
        Get the name of the entity.
        
        Returns:
            str: The name of the entity.
        """
        return self.name

    def get_description(self) -> str:
        """
        Get the description of the entity.
        
        Returns:
            str: The description of the entity.
        """
        return self.description
    
    def __str__(self) -> str:
        """
        Get a string representation of the entity.
        
        Returns:
            str: A string representation of the entity.
        """
        return f"""{self.name} - {self.description}
                Stats: {self.stats}
                Class: {self.entityclass}
                Species: {self.species}
                Actions: {self.actions}
                Inventory: {self.inventory}
                Resources: {self.resources}
                """
    
    @abstractmethod
    def dump(self, format: str = 'json') -> str:
        """
        Dump the entity to a specified format.
        
        Args:
            format (str): The format to dump the entity to. Default is 'json'.
        
        Returns:
            str: The entity data in the specified format.
        """
        pass

    @abstractmethod
    def load(self, data: str, format: str = 'json') -> None:
        """
        Load the entity from a specified format.
        
        Args:
            data (str): The entity data in the specified format.
            format (str): The format of the entity data. Default is 'json'.
        """
        pass


class BaseEntity(Entity):
    "Base entity class that implements the abstract methods of the Entity class."
    #implement the abstract methods
    def dump(self, format: str = 'json') -> str:
        if format == 'json':
            return json.dumps(self.dict(), indent=4)
        else:
            return str(self)
    def load(self, data: str, format: str = 'json') -> None:
        if format == 'json':
            entity = BaseEntity.parse_raw(data)
            self.name = entity.name
            self.description = entity.description
            self.stats = entity.stats
            self.actions = entity.actions
            self.inventory = entity.inventory
            self.resources = entity.resources
        else:
            raise ValueError("Unsupported format")

#if main 
if __name__ == "__main__":
    #create a new entity object and print it
    entity = BaseEntity(name="Entity", description="An entity in the game.")
    print(entity)
    
    #create a new entity object with every attribute and print it
    entity = BaseEntity(name="Entity", description="An entity in the game.", stats=[BaseStat(name="Health", value=100)], actions=[Action(name="Attack", description="Attack the enemy.")], inventory=[BaseItem(name="Sword", description="A sharp sword.")], resources=[Resource(name="Gold", amount=100)])
    print(entity)