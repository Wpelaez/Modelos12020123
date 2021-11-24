from capturarDatos import capturarDatos
from mensajes import mensajes

class operacionesBasicas():

    capturarDatos = capturarDatos()
    mensajes = mensajes()

    def __init__(self):
        pass


    def suma(self):
        self.mensajes.mostarPrimerMensajeOperacion("Suma")
        resultado = self.capturarDatos.capturarNumero("numero")
        while True:
            resultado += self.capturarDatos.capturarNumero("numero")
            print(resultado)
            if not self.capturarDatos.continuarOperacion():
                break
        self.mensajes.mostrarResultado(resultado)

    def resta(self):
        self.mensajes.mostarPrimerMensajeOperacion("Resta")
        numeroBase = self.capturarDatos.capturarNumero("numero")
        sustraendo = 0
        while True:
            entrada = self.capturarDatos.capturarNumero("numero")
            sustraendo += entrada
            print(numeroBase - sustraendo)
            if not self.capturarDatos.continuarOperacion():
                break
        self.mensajes.mostrarResultado(numeroBase - sustraendo)

    def multiplicacion(self):
        self.mensajes.mostarPrimerMensajeOperacion("Multiplicacion")
        resultado = self.capturarDatos.capturarNumero("numero")
        while True:
            resultado *= self.capturarDatos.capturarNumero("numero")
            print(resultado)
            if not self.capturarDatos.continuarOperacion():
                break
        self.mensajes.mostrarResultado(resultado)


    def division(self):
        self.mensajes.mostarPrimerMensajeOperacion("Division")
        numeroBase = self.capturarDatos.capturarNumero("numero")
        while True:
            while True:
                dividendo = self.capturarDatos.capturarNumero("numero")
                if dividendo != 0:
                    break
                else:
                    self.mensajes.errorDivision()
            numeroBase /= dividendo
            print(numeroBase)
            if not self.capturarDatos.continuarOperacion():
                break
        self.mensajes.mostrarResultado(numeroBase)