from pydantic import BaseModel, Field
from typing import Optional

# Modelo de datos para mascotas
class Pet(BaseModel):
    id: int
    name: str = Field(..., min_length=1)
    age: int = Field(..., ge=0, description="Age must be non-negative")
    species: str

# Nodo del árbol de búsqueda binaria (BST)
class BSTNode:
    def __init__(self, pet: Pet):
        self.pet = pet
        self.left = None
        self.right = None

# Árbol de búsqueda binaria (BST)
class BST:
    def __init__(self):
        self.root = None

    def insert(self, pet: Pet):
        if not self.root:
            self.root = BSTNode(pet)
        else:
            self._insert(self.root, pet)

    def _insert(self, node: BSTNode, pet: Pet):
        if pet.age < node.pet.age:
            if node.left:
                self._insert(node.left, pet)
            else:
                node.left = BSTNode(pet)
        else:
            if node.right:
                self._insert(node.right, pet)
            else:
                node.right = BSTNode(pet)

    def in_order(self):
        pets = []
        self._in_order(self.root, pets)
        return pets

    def _in_order(self, node, pets):
        if node:
            self._in_order(node.left, pets)
            pets.append(node.pet)
            self._in_order(node.right, pets)
