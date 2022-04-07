from estrategiaPago import estrategiaPago
from accionesFacade import accionesFacade
from datetime import datetime

class pagoPuntos(estrategiaPago):

    __baseDatos = accionesFacade.obtenerInstancia()
    __nickname = ""
    __totalPuntos = 0
    __totalEfectivo = 0
    __carritoCompra = None
    __numeroFactura = None

    def __init__(self, nickname, carritoCompra):
        self.__nickname = nickname
        self.__carritoCompra = carritoCompra

    def pagar(self):
        datosCliente = self.__baseDatos.obtenerDatosCliente(self.__nickname)
        #numSillasGenerales = 0
        carritoArticulosValidos = []
        for articulo in self.__carritoCompra:
            if articulo.get("entidad") == "silla":
                idPresentacion = articulo.get("id").get("idPresentacion")
                idSilla = articulo.get("id").get("idSilla")
                datosSilla = self.__baseDatos.obtenerDatosSilla(idPresentacion, idSilla)
                if datosSilla[9] == 2:
                    carritoArticulosValidos.append(articulo)
                    self.sumarPuntosATotal("silla")
        puntosCliente = datosCliente[2]
        if self.__totalPuntos > 0 and puntosCliente >= self.__totalPuntos:
            self.__numeroFactura = self.__baseDatos.generarNumeroFactura()
            self.__baseDatos.agregarFactura(self.__numeroFactura,
                                            self.__totalEfectivo,
                                            datosCliente[0], 1, datetime.now())
            for articulo in carritoArticulosValidos:
                self.asignarFacturaArticuloValido(articulo, articulo.get("entidad"))
            carritoArticulosNoValidos = [x for x in self.__carritoCompra if x not in carritoArticulosValidos]
            for articulo in carritoArticulosNoValidos:
                self.liberarArticuloNoPagado(articulo, articulo.get("entidad"))
            self.__baseDatos.modificarPuntosCliente(datosCliente[0], puntosCliente - self.__totalPuntos)
            return "exito"
        elif self.__totalPuntos <= 0:
            return "No hay articulos validos para pagar con puntos!"
        elif puntosCliente < self.__totalPuntos:
            return "Puntos Insuficientes!"

    def getNumeroFactura(self):
        return self.__numeroFactura

    def sumarPuntosATotal(self, entidad):
        if entidad == "silla":
            self.__totalPuntos += 100
            self.__totalEfectivo += self.ObtenerPrecioEnEfectivo("silla")

    def ObtenerPrecioEnEfectivo(self, entidad):
        if entidad == "silla":
            datos = self.__baseDatos.obtenerDatosTipoSilla("2")
            return int(datos[2])

    def liberarArticuloNoPagado(self, articulo, entidad):
        if entidad == "silla":
            idPresentacion = articulo.get("id").get("idPresentacion")
            idSilla = articulo.get("id").get("idSilla")
            self.__baseDatos.liberarSilla(idPresentacion, idSilla)

    def asignarFacturaArticuloValido(self, articulo, entidad):
        if entidad == "silla":
            idPresentacion = articulo.get("id").get("idPresentacion")
            idSilla = articulo.get("id").get("idSilla")
            self.__baseDatos.asignarNumeroFacturaSilla(idPresentacion, idSilla,
                                                       self.__numeroFactura,
                                                       self.ObtenerPrecioEnEfectivo("silla"))