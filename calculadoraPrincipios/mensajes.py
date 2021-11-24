class mensajes():

    def __init__(self):
        pass

    def iniciarCalculadora(self):
        print("Bienvenido Acontinuacion seleccione una opcion:")

    def mostrarOpciones(self):
        print("1.Operaciones Basicas")
        print("2.Porcentaje")
        print("3.Cambiar de Base")

    def opcionesOperacionesBasicas(self):
        print("1.Suma")
        print("2.Resta")
        print("3.Multiplicacion")
        print("4.Division")

    def mostarPrimerMensajeOperacion(self, operacion):
        print("Digite los numeros para hacer la operacion de {}".format(operacion))

    def mostrarResultado(self, expresion):
        print("El resultado es {}".format(expresion))

    def errorDivision(self):
        print("La Dividendo no puede ser 0!")

    def mostrarOpcionesPorcentaje(self):
        print("1.Sumar Porcentaje")
        print("2.Restar Porcentaje")
        print("3.Calcular Porcentaje")