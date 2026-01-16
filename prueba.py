"""
#Lab de la función root
def root():
    return {
        "message": "Bienvenido a la API del curso",
        "hotel":"trivago",
        "urna virtual pregunta del día":"Qué debería pasar por acá?"
        }
    
print(root())
"""

#Lab de lógica para listar usuarios por id
from pydantic import BaseModel


class User(BaseModel):
        id: int
        nombre: str
        apellido: str
        telefono: int
        direccion: str
        correo: str


 
users_list = [
        User(
                id = 1,
                nombre = "camilo", 
                apellido = "suarez", 
                telefono = 3188477656, 
                direccion="Cra 30 # 14 - 08", 
                correo="kamsz.m0@gmail.com"
        ),
        User(
                id = 2,
                nombre = "laura", 
                apellido = "mora", 
                telefono = 3171375428, 
                direccion="Algún lugar de lebrija", 
                correo="valenmora@gmail.com"
        ),
        User(
                id = 3,
                nombre = "jhoan", 
                apellido = "mora", 
                telefono = 3178499515, 
                direccion="Cra 30 # 14 - 09", 
                correo="camilosuarezm2007@gmail.com"
                )
]

for usuarios in users_list:
    if usuarios.id == 2 :
        print(usuarios)
    # for usuario in usuarios:
    #     if id == 2:        
    #         print(usuario)