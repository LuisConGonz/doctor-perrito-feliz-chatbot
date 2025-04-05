import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from src.facebook_bot import FacebookBot

def test_respuesta_facebook_bot():
    bot = FacebookBot()
    respuesta = bot.responder("¿Qué razas tienen?")
    assert "labrador" in respuesta.lower()

def test_respuesta_edad_requisitos():
    bot = FacebookBot()
    respuesta = bot.responder("¿Qué edad mínima necesito para adoptar?")
    assert "años" in respuesta.lower()
