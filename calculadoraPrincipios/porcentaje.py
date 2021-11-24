from capturarDatos import capturarDatos
from mensajes import mensajes

class porcentaje():

    capturarDatos = capturarDatos()
    mensajes = mensajes()

    def __init__(self):
        pass

    def sumarPorcentaje(self):
        self.mensajes.mostarPrimerMensajeOperacion("Sumar Porcentaje")
        numero = self.capturarDatos.capturarNumero("numero")
        porcentaje = self.capturarDatos.capturarNumero("Porcentaje")
        resultado = numero + (numero * (porcentaje/100))
        self.mensajes.mostrarResultado(resultado)

    def restarPorcentaje(self):
        self.mensajes.mostarPrimerMensajeOperacion("Restar Porcentaje")
        numero = self.capturarDatos.capturarNumero("numero")
        porcentaje = self.capturarDatos.capturarNumero("Porcentaje")
        resultado = numero - (numero * (porcentaje / 100))
        self.mensajes.mostrarResultado(resultado)

    def calcularPorcentaje(self):
        self.mensajes.mostarPrimerMensajeOperacion("Calcular Porcentaje")
        numero = self.capturarDatos.capturarNumero("Numero")
        porcentaje = self.capturarDatos.capturarNumero("Porcentaje")
        resultado = numero * (porcentaje/100)
        self.mensajes.mostrarResultado(resultado)