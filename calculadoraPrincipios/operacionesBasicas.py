from capturarDatos import capturarDatos
from mensajesOBasicas import mensajesOBasicas


class operacionesBasicas():

    capturarDatos = capturarDatos()
    mensajes = mensajesOBasicas()

    def __init__(self):
        self.mensajes.opcionesOperacionesBasicas()
        opcionBasicas = self.capturarDatos.seleccionarMenu()
        if opcionBasicas == "1":
            self.suma()
        if opcionBasicas == "2":
            self.resta()
        if opcionBasicas == "3":
            self.multiplicacion()
        if opcionBasicas == "4":
            self.division()

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