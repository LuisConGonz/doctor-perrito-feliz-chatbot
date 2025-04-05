import pytest

def test_respuesta_facebook_bot():
    """Prueba que el chatbot responda correctamente."""
    from src.bot import FacebookBot  # Ajusta la importación según tu estructura
    bot = FacebookBot()
    respuesta = bot.responder("¿Qué razas tienen?")
    assert "labrador" in respuesta.lower()  # Ejemplo básico
