from pydantic import BaseModel
from typing import Optional

class Pet(BaseModel):
    id: int
    name: str
    age: int
    race: str

    def _init_(self, **data):
        # Llamamos al constructor original de BaseModel
        super()._init_(**data)

        # Validamos nombre
        if not self.name.replace(" ", "").isalpha():
            raise ValueError("El nombre solo puede tener letras y espacios")

        # Validamos raza
        if not self.race.replace(" ", "").isalpha():
            raise ValueError("La raza solo puede tener letras y espacios")

        # Validamos edad
        if not isinstance(self.age, int) or self.age <= 0:
            raise ValueError("La edad debe ser un número entero positivo")