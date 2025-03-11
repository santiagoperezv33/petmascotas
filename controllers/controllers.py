from models import Pet, BST

# Base de datos en memoria (diccionario para acceso rápido)
pets_db = {}

# Árbol de búsqueda binaria para organizar por edad
bst = BST()

def create_pet(pet: Pet):
    if pet.id in pets_db:
        return {"error": "Pet ID already exists"}, 400
    pets_db[pet.id] = pet
    bst.insert(pet)  # Insertar en el BST
    return pet

def get_pets():
    return list(pets_db.values())

def get_pet(pet_id: int):
    return pets_db.get(pet_id) or {"error": "Pet not found"}, 404

def update_pet(pet_id: int, updated_pet: Pet):
    if pet_id not in pets_db:
        return {"error": "Pet not found"}, 404
    if pet_id != updated_pet.id:
        return {"error": "Pet ID cannot be changed"}, 400
    pets_db[pet_id] = updated_pet
    return updated_pet

def delete_pet(pet_id: int):
    if pet_id in pets_db:
        del pets_db[pet_id]
        return {"message": "Pet deleted successfully"}
    return {"error": "Pet not found"}, 404

def get_pets_by_age():
    return bst.in_order()

def get_average_age():
    if not pets_db:
        return {"message": "No pets in database"}
    avg_age = sum(pet.age for pet in pets_db.values()) / len(pets_db)
    return {"average_age": avg_age}
