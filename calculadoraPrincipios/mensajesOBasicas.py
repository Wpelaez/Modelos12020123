class mensajesOBasicas():

    def __init__(self):
        pass

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