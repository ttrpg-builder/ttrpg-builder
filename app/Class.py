from abc import ABC, abstractmethod
from pydantic import BaseModel, Field
from typing import List, Optional, Any

class Class(BaseModel, ABC):
    """
    Abstract base class for a class in a TTRPG system.
    
    Attributes:
        name (str): The name of the class.
        level (int): The level of the class.
        klasse (int): The main class type.
        subklasse (int): The subclass type.
        classtype (int): The type of the class.
    """
    name: str = Field(..., description="The name of the class.")
    level: int = Field(default=0, description="The level of the class.")
    klasse: int = Field(default=0, description="The main class type.")
    subklasse: int = Field(default=0, description="The subclass type.")
    classtype: int = Field(default=0, description="The type of the class.")
    
    def __init__(self, name: str):
        super().__init__(name=name)
    
    def level_up(self, character: Any) -> None:
        """
        Level up the class and update the character.
        
        Args:
            character (Any): The character to level up.
        """
        self.level += 1
        if self.classtype:
            character.special_level_up(self.classtype)
        character.add_feature(self.get_features(self.klasse, self.level))
    
    @abstractmethod
    def get_features(self, klasse: int, level: int) -> Any:
        """
        Abstract method to get the features of the class.
        
        Args:
            klasse (int): The main class type.
            level (int): The level of the class.
        
        Returns:
            Any: The features of the class.
        """
        pass
    
    def __str__(self) -> str:
        """
        Get the string representation of the class.
        
        Returns:
            str: The string representation of the class.
        """
        return f"{self.name} level {self.level}"