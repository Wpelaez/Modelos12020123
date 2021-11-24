from mensajes import mensajes
from capturarDatos import capturarDatos
from operacionesBasicas import operacionesBasicas
from porcentaje import porcentaje

class calculadora():

    mensajesObj = mensajes()
    capturarDatos = capturarDatos()
    operacionesBasicas = operacionesBasicas()
    porcentaje = porcentaje()

    def __init__(self):
        self.iniciarCalculadora()

    def iniciarCalculadora(self):
        self.mensajesObj.iniciarCalculadora()
        self.seleccionarOperaciones()

    def seleccionarOperaciones(self):
        self.mensajesObj.mostrarOpciones()
        opcion = self.capturarDatos.seleccionarMenu()
        if opcion == "1":
            self.mensajesObj.opcionesOperacionesBasicas()
            opcionBasicas = self.capturarDatos.seleccionarMenu()
            if opcionBasicas == "1":
                self.operacionesBasicas.suma()
            if opcionBasicas == "2":
                self.operacionesBasicas.resta()
            if opcionBasicas == "3":
                self.operacionesBasicas.multiplicacion()
            if opcionBasicas == "4":
                self.operacionesBasicas.division()
        elif opcion == "2":
            self.mensajesObj.mostrarOpcionesPorcentaje()
            opcionPorcentaje = self.capturarDatos.seleccionarMenu()
            if opcionPorcentaje == "1":
                self.porcentaje.sumarPorcentaje()
            if opcionPorcentaje == "2":
                self.porcentaje.restarPorcentaje()
            if opcionPorcentaje == "3":
                self.porcentaje.calcularPorcentaje()
        else:
            print("WIP")