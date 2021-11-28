class mensajesPorcentaje():

    def __init__(self):
        pass

    def mostrarOpcionesPorcentaje(self):
        print("1.Sumar Porcentaje")
        print("2.Restar Porcentaje")
        print("3.Calcular Porcentaje")

    def mostarPrimerMensajeOperacion(self, operacion):
        print("Digite los numeros para hacer la operacion de {}".format(operacion))

    def mostrarResultado(self, expresion):
        print("El resultado es {}".format(expresion))