from estrategiaPago import estrategiaPago
from accionesFacade import accionesFacade
from datetime import datetime

class pagoEfectivo(estrategiaPago):

    __numeroFactura = None
    __carritoCompra = None
    __baseDatos = accionesFacade.obtenerInstancia()
    __nickname = None

    def __init__(self, carritoCompra, nickname):
        self.__carritoCompra = carritoCompra
        self.__nickname = nickname

    def pagar(self):
        self.__numeroFactura = self.__baseDatos.generarNumeroFactura()
        puntos = 0
        for articulo in self.__carritoCompra:
            if articulo.get("entidad") == "silla":
                idPresentacion = articulo.get("id").get("idPresentacion")
                idSilla = articulo.get("id").get("idSilla")
                datosSilla = self.__baseDatos.obtenerDatosSilla(idPresentacion, idSilla)
                self.__baseDatos.asignarNumeroFacturaSilla(idPresentacion, idSilla,
                                                           self.__numeroFactura, datosSilla[7])
                puntos += 10
            if articulo.get("entidad") == "snack":
                idSnack = articulo.get("id")
                cantidad = articulo.get("cantidad")
                precio = self.__baseDatos.obtenerDatosSnack(idSnack)[3]
                inventario = self.__baseDatos.obtenerDatosSnack(idSnack)[2]
                self.__baseDatos.insertarNumFacturaAFacturasSnack(self.__numeroFactura)
                self.__baseDatos.insertarProductoYFactura(idSnack, self.__numeroFactura, cantidad, precio)
                self.__baseDatos.modificarCantidadSnack(idSnack, inventario - cantidad)
                puntos += 5*cantidad
        pagoTotal = self.__baseDatos.calcularPrecioTotal(self.__carritoCompra)
        datosCliente = self.__baseDatos.obtenerDatosCliente(self.__nickname)
        self.__baseDatos.modificarPuntosCliente(datosCliente[0], datosCliente[2] + puntos)
        self.__baseDatos.agregarFactura(self.__numeroFactura, pagoTotal,
                                        datosCliente[0], 2, datetime.now())
        return "exito"

    def getNumeroFactura(self):
        return self.__numeroFactura