from abc import ABC, abstractmethod
from pydantic import BaseModel, Field
from typing import List, Optional, Any
import json



class Item(BaseModel, ABC):
    """
    Represents a generic item in any given TTRPG system.
    
    Attributes:
        name (str): The name of the item.
        description (Optional[str]): A brief description of the item.
        weight (Optional[float]): The weight of the item.
        value (Optional[int]): The value of the item.
        durability (Optional[int]): The durability of the item.
        subinventory (Optional[List['Item']]): List of items in the item's subinventory.
        subinventory_limit (Optional[int]): Optional limit for the subinventory.
        equip_slot (Optional[str]): The slot to which the item can be equipped.
        required_proficiency (Optional[str]): The ability required to be proficient with the item.
    """
    name: str = Field(..., description="The name of the item.")
    description: Optional[str] = Field(default=None, description="A brief description of the item.")
    weight: Optional[float] = Field(default=0.0, description="The weight of the item.")
    value: Optional[int] = Field(default=0, description="The value of the item.")
    durability: Optional[int] = Field(default=100, description="The durability of the item.")
    resources: Optional[List[str]] = Field(default_factory=list, description="List of resources the item provides.")
    subinventory: Optional[List['Item']] = Field(default_factory=list, description="List of items in the item's subinventory.")
    subinventory_limit: Optional[int] = Field(default=None, description="Optional limit for the subinventory.")
    equip_slot: Optional[str] = Field(default=None, description="The slot to which the item can be equipped.")
    required_proficiency: Optional[str] = Field(default=None, description="The ability required to be proficient with the item.")
    
    def modify_value(self, modifier: int) -> None:
        """
        Modify the value of the item.
        
        Args:
            modifier (int): The amount to modify the value by.
        """
        if self.value is not None:
            self.value += modifier
    
    def set_name(self, name: str) -> None:
        """
        Set the name of the item.
        
        Args:
            name (str): The new name of the item.
        """
        self.name = name
    
    def set_description(self, description: str) -> None:
        """
        Set the description of the item.
        
        Args:
            description (str): The new description of the item.
        """
        self.description = description
    
    def add_to_subinventory(self, item: 'Item') -> None:
        """
        Add an item to the subinventory.
        
        Args:
            item ('Item'): The item to add to the subinventory.
        """
        if self.subinventory_limit is None or len(self.subinventory) < self.subinventory_limit:
            self.subinventory.append(item)
        else:
            raise ValueError("Subinventory limit reached.")
    
    @abstractmethod
    def use(self, target: Optional[Any] = None) -> Any:
        """
        Use the item. This method should be overridden by subclasses.
        
        Args:
            target (Optional[Any]): The target on which the item is used. Default is None.
        
        Returns:
            Any: The result of using the item.
        """
        raise NotImplementedError("This method should be overridden by subclasses.")
    
    @abstractmethod
    def get_details(self) -> str:
        """
        Get the details of the item. This method should be overridden by subclasses.
        
        Returns:
            str: The details of the item.
        """
        raise NotImplementedError("This method should be overridden by subclasses.")
    
    @abstractmethod
    def check_proficiency(self, ability: str) -> bool:
        """
        Check if the character is proficient with the item based on the required ability.
        
        Args:
            ability (str): The ability to check proficiency against.
        
        Returns:
            bool: True if the character is proficient, False otherwise.
        """
        pass

class BaseItem(Item):
    """
    Base implementation of the Item class.
    """
    #implement the abstract methods
    def use(self) -> None:
        print(f"{self.name} used.")
    
    def check_proficiency(self) -> bool:
        return True
    
    def get_details(self) -> str:
        return f"{self.name} - {self.description}"