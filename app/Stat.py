from abc import ABC, abstractmethod
from pydantic import BaseModel, Field
from typing import Optional

"""
This module defines the Stat class, which represents a generic stat
for an entity in a game or simulation. The class includes attributes such as
name, value, and description, and provides methods to modify these attributes.

A stat is generally a numerical value that represents some aspect of an entity,
such as strength, or intelligence.
"""

class Stat(BaseModel, ABC):
    """
    Represents a generic stat for an entity.
    
    Attributes:
        name (str): The name of the stat.
        value (Optional[int]): The value of the stat.
        description (Optional[str]): A brief description of the stat.
    """
    name: str = Field(..., description="The name of the stat.")
    value: Optional[int] = Field(default=0, description="The value of the stat.")
    description: Optional[str] = Field(default=None, description="A brief description of the stat.")

    def get(self) -> int:
        """
        Get the value of the stat.
        
        Returns:
            int: The value of the stat.
        """
        return self.value

    def set_value(self, value: int) -> None:
        """
        Set the value of the stat.
        
        Args:
            value (int): The new value of the stat.
        """
        self.value = value

    def modify_value(self, modifier: int) -> None:
        """
        Modify the value of the stat.
        
        Args:
            modifier (int): The amount to modify the value by.
        """
        if self.value is not None:
            self.value += modifier
    
    def set_name(self, name: str) -> None:
        """
        Set the name of the stat.
        
        Args:
            name (str): The new name of the stat.
        """
        self.name = name
    
    def set_description(self, description: str) -> None:
        """
        Set the description of the stat.
        
        Args:
            description (str): The new description of the stat.
        """
        self.description = description

    @abstractmethod
    def get_modifier(self) -> int:
        """
        Abstract method to get the modifier of the stat. 
        This should be implemented by subclasses.
        In general, the modifier is a derived value based on the base value of the stat.
        And could be something like stat - 10 rounded down to neares even number / 2.
        
        Returns:
            int: The modifier of the stat.
        """
        pass
    

class BaseStat(Stat):
    """Base implementation of the Stat class.
    """
    def get_modifier(self) -> int:
        return self.value
