class FacebookBot:
    def responder(self, mensaje):
        if "razas" in mensaje.lower():
            return "Tenemos labradores y golden retrievers"
        elif "edad" in mensaje.lower():
            return "La edad mínima es 21 años"
        return "Por favor visita nuestro sitio web"
