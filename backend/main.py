from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
origins = [
    "http://127.0.0.1:5500",
    "http://localhost:5500",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
lista_estudiantes = [
    {
        "id": 1,
        "nombre": "Ana Martínez",
        "email": "ana.martinez@example.com",
        "carrera": "Ingeniería de Sistemas"
    },
    {
        "id": 2,
        "nombre": "Carlos Pérez",
        "email": "carlos.perez@example.com",
        "carrera": "Administración de Empresas"
    },
    {
        "id": 3,
        "nombre": "Lucía Fernández",
        "email": "lucia.fernandez@example.com",
        "carrera": "Diseño Gráfico"
    }
]

@app.get("/saludo")
def saludo():
    return {"mensaje": "hola"}

@app.get("/estudiantes")
def obtener_estudiantes():
    return lista_estudiantes

@app.get("/estudiantes/{id}")
def obtener_estudiante(id: int):
    for estudiante in lista_estudiantes:
        if estudiante["id"] == id:
            return estudiante

    raise HTTPException(
        status_code=404,
        detail="Estudiante no encontrado"
    )
