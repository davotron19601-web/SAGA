import os
import psycopg
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

load_dotenv()

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


def obtener_conexion():
    return psycopg.connect(os.getenv("DATABASE_URL"))


def fila_a_dict(fila):
    return {
        "id": fila[0],
        "nombre": fila[1],
        "email": fila[2],
        "carrera": fila[3],
    }


@app.get("/saludo")
def saludo():
    return {"mensaje": "hola"}


@app.get("/estudiantes")
def obtener_estudiantes():
    with obtener_conexion() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT id, nombre, email, carrera FROM estudiantes ORDER BY id")
            filas = cur.fetchall()
    return [fila_a_dict(fila) for fila in filas]


@app.get("/estudiantes/{id}")
def obtener_estudiante(id: int):
    with obtener_conexion() as conn:
        with conn.cursor() as cur:
            cur.execute(
                "SELECT id, nombre, email, carrera FROM estudiantes WHERE id = %s",
                (id,),
            )
            fila = cur.fetchone()
    if fila is None:
        raise HTTPException(status_code=404, detail="Estudiante no encontrado")
    return fila_a_dict(fila)

    raise HTTPException(
        status_code=404,
        detail="Estudiante no encontrado"
    )
