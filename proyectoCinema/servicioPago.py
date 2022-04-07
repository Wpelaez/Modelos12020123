from pagoEfectivo import pagoEfectivo
from pagoPuntos import pagoPuntos

class servicioPago():


    estrategiaPago = None

    def __init__(self):
        pass

    def realizarPago(self):
        return self.estrategiaPago.pagar()

    def setEstrategiaPago(self, estrategia, nickname, carritoCompra):
        if estrategia == "puntos":
            self.estrategiaPago = pagoPuntos(nickname, carritoCompra)
        elif estrategia == "efectivo":
            self.estrategiaPago = pagoEfectivo(carritoCompra, nickname)

    def obtenerNumeroFactura(self):
        return self.estrategiaPago.getNumeroFactura()