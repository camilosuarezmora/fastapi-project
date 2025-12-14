# En un repositorio nuevo, primero se debe crear y activar un entorno virtual. 

# pip install fastapi
# es el comando que descarga <<fastapi>> desde "pip", y 
from fastapi import FastAPI
#importa un modulo llamado FastAPI desde el paquete fastapi.

app = FastAPI() 

@app.get("/")
async def root():
    return {
        "message": "Bienvenido a la API del curso",
        "hotel":"trivago",
        "urna virtual pregunta del día":"Qué debería pasar por acá?"
        }