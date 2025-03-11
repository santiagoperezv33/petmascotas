from models import Pet

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
        """Inserta un nuevo nodo en el BST."""
        if not self.root:
            self.root = BSTNode(pet)
        else:
            self._insert(self.root, pet)

    def _insert(self, node: BSTNode, pet: Pet):
        """Lógica interna para insertar en el BST."""
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
        """Retorna una lista de mascotas en orden de edad (ascendente)."""
        pets = []
        self._in_order(self.root, pets)
        return pets

    def _in_order(self, node, pets):
        """Lógica interna para recorrer el BST en orden."""
        if node:
            self._in_order(node.left, pets)
            pets.append(node.pet)
            self._in_order(node.right, pets)

    def search_by_age(self, age: int):
        """Busca mascotas por edad exacta."""
        return self._search_by_age(self.root, age)

    def _search_by_age(self, node, age: int):
        """Lógica interna para buscar por edad."""
        if not node:
            return None
        if node.pet.age == age:
            return node.pet
        elif age < node.pet.age:
            return self._search_by_age(node.left, age)
        else:
            return self._search_by_age(node.right, age)