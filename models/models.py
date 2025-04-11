else:
return self.root.add(pet)


def update(self, pet: Pet, id: int):
    if self.root == None:
        raise Exception("No existen mascotas en el listado")
    else:
        self.root.update(pet, id)


def inorder(self):
    if self.root == None:
        raise Exception("No existen mascotas en el listado")
    else:
        return self.root.get_inorder()


def delate(self, id, pet: Pet):
    if self.root == None:
        return "El arbol esta vacio"
    else:
        return self.root.delate(id)


class NodeABB:
    def __init__(self, pet: Pet):
        self.pet = pet
        self.left = None
        self.right = None
        self.size = 1

    # Agregar mascota y validacion de id
    def add(self, pet: Pet):
        if pet.id < self.pet.id:


@ @-44

, 52 + 63, 86 @ @


def add(self, pet: Pet):
    else:
    return "id erroneo"


# borrar mascota


# Actualizar mascota por id
def update(self, pet: Pet, id: int):
    if self.pet.id == id:
        self.pet.name = pet.name
        self.pet.age = pet.age
        self.pet.race = pet.race
    elif id < self.pet.id:
        if self.left:
            self.left.update(pet, id)
        else:
            raise Exception("No se encontró la mascota con el ID dado.")
    elif id > self.pet.id:
        if self.right:
            self.right.update(pet, id)
        else:
            raise Exception("No se encontró la mascota con el ID dado.")

    # Borrar mascota:


def delete(self, id):
    if id < self.pet.id:  # Buscar en la izquierda
        if id < self.pet.id:
            if self.left:
                self.left = self.left.delete(id)
            else:
                raise Exception(f"No se encontró la mascota con ID {id}")
            return self

        elif id > self.pet.id:  # Buscar en la derecha
        elif id > self.pet.id:
            if self.right:
                self.right = self.right.delete(id)
            else:
                raise Exception(f"No se encontró la mascota con ID {id}")
            return self

        else:  # Encontramos el nodo a eliminar
            if self.left == None:  # Solo tiene hijo derecho o esta solo
                return self.right
            if self.right == None:  # Solo tiene hijo izquierdo
                return self.left
    else:
        mascotas_a_reinsertar = []
    if self.left:
        mascotas_a_reinsertar += self.left.get_preorder()
    if self.right:
        mascotas_a_reinsertar += self.right.get_preorder()

    # Si tiene dos hijos, se reemplaza con el menor de la derecha
    min_node = self.right.get_min()
    self.pet = min_node.pet
    self.right = self.right.delete(min_node.pet.id)
    return self
    print(f"Mascota con ID {id} eliminada")


# Encuentra el menor en el subarbol derecho para que se remplace por el eliminado
def get_min(self):
    if self.left == None:
        return self
    return self.left.get_min()
    nuevo_root = None
    for pet in mascotas_a_reinsertar:
        if nuevo_root is None:
            nuevo_root = NodeABB(pet)
        else:
            nuevo_root.add(pet)

    return nuevo_root


def get_inorder(self):
    listPets = []
    if self.left is not None:
        listPets += self.left.get_inorder()
    listPets.append(self.pet)
    if self.right is not None:
        listPets += self.right.get_inorder()
    return listPets


def get_preorder(self):
    listPets = [self.pet]
    if self.left != None:
        listPets += self.left.get_preorder()
    if self.right != None:
        listPets += self.right.get_preorder()
    return listPets


def get_postorden(self):
    listPets = []
    if self.left != None:
        listPets += self.left.get_postorden()
    if self.right != None:
        listPets += self.right.get_postorden()
    listPets.append(self.pet)
    return listPets

    # Actualizar mascota por id


def update(self, id, pet: Pet):
    if id < self.pet.id:  # Buscar en la izquierda
        if self.left:
            self.left.update(id, pet)
        else:
            print(f"No se encontró una mascota con ID {id}")
    elif id > self.pet.id:  # Buscar en la derecha
        if self.right:
            self.right.update(id, pet)
        else:
            print(f"No se encontró una mascota con ID {id}")
    else:  # Si encontramos el nodo con el ID correspondiente
        self.pet = pet  # Se actualiza la mascota sin modificar la estructura

    return self

    # Listar mascotas por raza


def list_race(self, races=None):