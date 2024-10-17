from abc import ABC, abstractmethod
from pydantic import BaseModel, Field
from typing import List, Optional

class Species(BaseModel, ABC):
    """
    Abstract base class for a species of creatures in a TTRPG system.
    
    Attributes:
        name (str): The name of the species.
        description (Optional[str]): A brief description of the species.
        lifespan (Optional[int]): The average lifespan of the species.
        habitat (Optional[str]): The typical habitat of the species.
        abilities (Optional[List[str]]): List of abilities the species possesses.
    """
    name: str = Field(..., description="The name of the species.")
    description: Optional[str] = Field(default=None, description="A brief description of the species.")
    lifespan: Optional[int] = Field(default=None, description="The average lifespan of the species.")
    habitat: Optional[str] = Field(default=None, description="The typical habitat of the species.")
    abilities: Optional[List[str]] = Field(default_factory=list, description="List of abilities the species possesses.")
    
    
    def set_name(self, name: str) -> None:
        """
        Set the name of the species.
        
        Args:
            name (str): The new name of the species.
        """
        self.name = name
    
    def set_description(self, description: str) -> None:
        """
        Set the description of the species.
        
        Args:
            description (str): The new description of the species.
        """
        self.description = description
    
    def set_lifespan(self, lifespan: int) -> None:
        """
        Set the lifespan of the species.
        
        Args:
            lifespan (int): The new lifespan of the species.
        """
        self.lifespan = lifespan
    
    def set_habitat(self, habitat: str) -> None:
        """
        Set the habitat of the species.
        
        Args:
            habitat (str): The new habitat of the species.
        """
        self.habitat = habitat
    
    def add_ability(self, ability: str) -> None:
        """
        Add an ability to the species.
        
        Args:
            ability (str): The ability to add.
        """
        self.abilities.append(ability)
    
    @abstractmethod
    def get_details(self) -> str:
        """
        Abstract method to get the details of the species. This should be implemented by subclasses.
        
        Returns:
            str: The details of the species.
        """
        pass