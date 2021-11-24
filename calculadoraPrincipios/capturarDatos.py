
class capturarDatos():

    def __init__(self):
        pass

    def seleccionarMenu(self):
        return input("Digite una opcion: ")

    def definirCantidadNumeros(self):
        return int(input("Digite la cantidad de numeros: "))

    def capturarNumero(self, texto):
        #Queda para agregar restriccion en caso de poner Flotantes
        while True:
            numero = input("Digite el {}: ".format(texto))
            if numero.isdigit():
                numero = int(numero)
                break
            else:
                print("Valor No valido")
        return numero

    def continuarOperacion(self):
        opcion = input("Continuar Operando? S/N: ")
        if opcion == "S" or opcion == "s":
            return True
        else:
            return False

    def reiniciarCalculadora(self):
        opcion = input("Reiniciar Calculadora? S/N :")
        if opcion == "S" or opcion == "s":
            return True
        else:
            return False
