import sys
from pathlib import Path
import pytest

sys.path.append(str(Path(__file__).parent.parent))
from src.bot import FacebookBot

@pytest.fixture
def bot():
    return FacebookBot()

def test_respuesta_razas(bot):
    respuesta = bot.responder("¿Qué razas tienen?")
    assert "disponibles" in respuesta or "No hay" in respuesta

def test_respuesta_default(bot):
    assert "predeterminada" in bot.responder("Hola")
