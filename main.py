#Prerequisitos:
"""
En un repositorio nuevo, primero se debe crear y activar un entorno virtual con el comando:
        <<python -m venv .venv>> 
        
Luego se debe activar con el comando:
        <<.venv\Scripts\activate>>  (en Windows)
        <<source .venv/bin/activate>> (en MacOS o Linux)
        
Después se debe instalar FastAPI y Uvicorn (el servidor ASGI recomendado para correr aplicaciones FastAPI) con el comando:
        <<pip install fastapi uvicorn>>
        
Finalmente, para correr la aplicación, se debe usar el comando:
        <<fastapi dev main.py>>
"""


#Importación de FastAPI
"""
El condigo a continuación importa el modulo (python lo lee como clase) FastAPI desde el paquete fastapi.
"""
from fastapi import FastAPI


#Creación de la aplicación FastAPI
"""
cuando se importa FastAPI, python la lee como una clase que debe ser instanciada. 
Con el siguiente comando se crea una instancia de la clase FastAPI (llamada *app*) y con ello se crea la aplicación web.
"""
app = FastAPI() 


#Definición del path operation decorator
"""
El codigo de abajo es un decorator (porque empieza con @) que le dice a FastAPI que la función de abajo corresponde al path / con una operation get.

Se le llama *path operation decorator* porque es un decorador que define una operación (metodo http) en un path específico.

El cliente hace la solicitud http al path (el cliente dice "traigame lo que haya en /") y el servidor responde con lo que retorne la función asociada a ese path operation decorator.
"""
@app.get("/") 

#Definición del path operation function
   #La función de abajo será llamada por FastAPI cuando reciba un request en la URL "/" usando una operación GET.
   #Es una función asincrona pq es una llamada al server que puede demorar.
async def root(): 
#Retorna algo
   #La función tiene que retornar algo para que tenga sentid     
    return {
        "mensaje":"Haz accedido al root de la API, bienvenido!",
        "razon de ser":"Es una buena practica definir un root en una API y que este devuelva algo útil",
        "estado":"Si puedes ver toda esta información, es porque la API está corriendo correctamente",
        "hotel?":"trivago"
        }
    
    
    
    
#Definición de otro path operation decorator y función de ejemplo
"""
En el siguiente ejemplo se define otro path operation decorator y función que responde a requests GET en el path /saludo/{nombre}.
El path incluye un parámetro de path llamado nombre, que es una variable que el cliente puede definir al hacer la solicitud.
Por ejemplo, si el cliente hace una solicitud GET a /saludo/Ana, el valor del parámetro nombre será "Ana".
"""    
@app.get("/saludo/{nombre}")
async def saludar_nombre(nombre: str):
    return {"mensaje":f"Hola, {nombre}. ¡Bienvenido a nuestra API!"}