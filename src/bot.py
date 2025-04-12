import sqlite3
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class FacebookBot:
    def __init__(self):
        self.conn = sqlite3.connect("database.db")
        self._init_db()

    def _init_db(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS mascotas (
                id INTEGER PRIMARY KEY,
                nombre TEXT NOT NULL,
                raza TEXT NOT NULL
            )
        ''')
        self.conn.commit()

    def responder(self, mensaje: str) -> str:
        mensaje = mensaje.lower()
        if "razas" in mensaje:
            return self._listar_razas()
        return "Respuesta predeterminada"

    def _listar_razas(self) -> str:
        cursor = self.conn.cursor()
        cursor.execute("SELECT DISTINCT raza FROM mascotas")
        razas = [r[0] for r in cursor.fetchall()]
        return f"Razas disponibles: {', '.join(razas)}" if razas else "No hay mascotas"

bot = FacebookBot()

@app.get("/")
def home():
    return {"status": "API activa"}

@app.post("/webhook")
async def webhook(mensaje: dict):
    return {"respuesta": bot.responder(mensaje.get("text", ""))}
