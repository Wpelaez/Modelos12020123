from capturarDatos import capturarDatos
from mensajesPorcentaje import mensajesPorcentaje


class porcentaje():

    capturarDatos = capturarDatos()
    mensajes = mensajesPorcentaje()

    def __init__(self):
        self.mensajes.mostrarOpcionesPorcentaje()
        opcionPorcentaje = self.capturarDatos.seleccionarMenu()
        if opcionPorcentaje == "1":
            self.sumarPorcentaje()
        if opcionPorcentaje == "2":
            self.restarPorcentaje()
        if opcionPorcentaje == "3":
            self.calcularPorcentaje()

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