from typing import Optional, Dict, Any
from pydantic import BaseModel


class Child(BaseModel):
    """
    Class representing a child's information.
    """
    def __init__(self, id: int, name: str, age: int, city: str, gender: str):
        self.id = id
        self.name = name
        self.age = age
        self.city = city
        self.gender = gender
        
    
    def to_dict(self) -> Dict[str, Any]:
        """Converts the Child object to a dictionary."""
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age
        }

class NodoABB:
    """
    Node of the Binary Search Tree (ABB).
    """
    def __init__(self, child: Child):
        self.child = child
        self.left: Optional['NodoABB'] = None
        self.right: Optional['NodoABB'] = None
    
    def to_dict(self) -> Dict[str, Any]:
        """Converts the node and its subtrees to a dictionary."""
        return {
            "child": self.child.to_dict(),
            "left": self.left.to_dict() if self.left else None,
            "right": self.right.to_dict() if self.right else None
        }

class ABB:
    """
    Implementation of a Binary Search Tree (ABB) to store children's information.
    """
    def __init__(self):
        self.root: Optional[NodoABB] = None
    
    def insert(self, child: Child) -> None:
        """Inserts a new child into the tree."""
        if not self.root:
            self.root = NodoABB(child)
        else:
            self.root = self._insert_recursive(self.root, child)
    
    def _insert_recursive(self, node: Optional[NodoABB], child: Child) -> NodoABB:
        """Helper method for recursive insertion."""
        if not node:
            return NodoABB(child)
        
        if child.id < node.child.id:
            node.left = self._insert_recursive(node.left, child)
        else:
            node.right = self._insert_recursive(node.right, child)
        
        return node
    
    def is_balanced(self) -> bool:
        """Checks if the tree is balanced."""
        return self._is_balanced_recursive(self.root)
    
    def _get_balance_height(self, node: Optional[NodoABB]) -> int:
        """
        Calculates the height of a subtree and checks its balance.
        Returns -1 if the subtree is not balanced, otherwise returns the height.
        """
        if not node:
            return 0
            
        left_height = self._get_balance_height(node.left)
        if left_height == -1:
            return -1
            
        right_height = self._get_balance_height(node.right)
        if right_height == -1:
            return -1
            
        if abs(left_height - right_height) > 1:
            return -1
            
        return max(left_height, right_height) + 1
    
    def _is_balanced_recursive(self, node: Optional[NodoABB]) -> bool:
        """Helper method for recursive balance checking."""
        return self._get_balance_height(node) != -1
    
    def to_dict(self) -> Dict[str, Any]:
        """Converts the tree to a dictionary for serialization."""
        if not self.root:
            return {}
        
        def build_dict(node: Optional[NodoABB]) -> Optional[Dict[str, Any]]:
            if not node:
                return None
            
            return {
                "child": node.child.to_dict(),
                "left": build_dict(node.left),
                "right": build_dict(node.right),
                "is_balanced": self._get_balance_height(node) != -1
            }
        
        return build_dict(self.root)
    
    def find_by_id(self, id: int) -> Optional[Child]:
        """Finds a child by their ID."""
        return self._find_recursive(self.root, id)
    
    def _find_recursive(self, node: Optional[NodoABB], id: int) -> Optional[Child]:
        """Helper method for recursive search."""
        if not node:
            return None
        
        if id == node.child.id:
            return node.child
        elif id < node.child.id:
            return self._find_recursive(node.left, id)
        else:
            return self._find_recursive(node.right, id)
    
    def clear(self) -> None:
        """Clears the tree, removing all nodes."""
        self.root = None
        