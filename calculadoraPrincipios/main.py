from calculadora import calculadora
from capturarDatos import capturarDatos

#Crear Calculadora que haga operaciones Basicas, Porcentaje, Cambiar de base un num

capturarDatos = capturarDatos()

while True:
    calculadoraObj = calculadora()
    if not capturarDatos.reiniciarCalculadora():
        break
