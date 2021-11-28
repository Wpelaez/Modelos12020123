from mensajesCalculadora import mensajesCalculadora
from capturarDatos import capturarDatos
from operacionesBasicas import operacionesBasicas
from porcentaje import porcentaje


class calculadora():

    mensajesObj = mensajesCalculadora()
    capturarDatos = capturarDatos()

    def __init__(self):
        self.iniciarCalculadora()

    def iniciarCalculadora(self):
        self.mensajesObj.iniciarCalculadora()
        self.seleccionarOperaciones()

    def seleccionarOperaciones(self):
        self.mensajesObj.mostrarOpciones()
        opcion = self.capturarDatos.seleccionarMenu()
        if opcion == "1":
            operacionesBasicas()
        elif opcion == "2":
            porcentaje()
        else:
            print("WIP")
