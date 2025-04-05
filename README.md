import sqlite3
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

DB_PATH = "database.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS mascotas (
            id INTEGER PRIMARY KEY,
            nombre TEXT NOT NULL,
            raza TEXT NOT NULL,
            edad INTEGER,
            adoptado BOOLEAN DEFAULT FALSE
        )
    ''')
    conn.commit()
    conn.close()

init_db()

class Mensaje(BaseModel):
    texto: str
    usuario: str

@app.post("/webhook")
async def webhook(mensaje: Mensaje):
    respuesta = procesar_mensaje(mensaje.texto)
    return {"respuesta": respuesta}

def procesar_mensaje(texto: str) -> str:
    texto = texto.lower()
    
    if "razas" in texto:
        return listar_razas()
    elif "adoptar" in texto:
        return "Para adoptar, visita: https://doctorperritofeliz.org/adopcion"
    elif "edad" in texto:
        return "La edad mínima es 21 años"
    else:
        return "Respuesta predeterminada. ¿Necesitas info sobre razas o adopción?"

def listar_razas() -> str:
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT DISTINCT raza FROM mascotas WHERE adoptado = FALSE")
    razas = [r[0] for r in cursor.fetchall()]
    conn.close()
    return f"Razas disponibles: {', '.join(razas) if razas else 'No hay mascotas disponibles'}"
