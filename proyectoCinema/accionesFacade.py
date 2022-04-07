from entidades.pelicula import pelicula
from entidades.presentacion import presentacion
from entidades.multiplex import multiplex
from entidades.silla import silla
from entidades.cliente import cliente
from entidades.factura import factura
from entidades.productosSnack import productoSnack
from entidades.facturasnack import facturasnack
from entidades.productoSnack_facturaSnack import productoSnack_facturaSnack
from entidades.pelicula_cliente import pelicula_cliente
from entidades.empleado import empleado
import random

class accionesFacade():

    __BDPelicula = pelicula()
    __BDPresentacion = presentacion()
    __BDMultiplex = multiplex()
    __BDSilla = silla()
    __BDCliente = cliente()
    __BDFactura = factura()
    __BDProductoSnack = productoSnack()
    __BDFacturaSnack = facturasnack()
    __BDProductoFactura = productoSnack_facturaSnack()
    __BDPeliculaCliente = pelicula_cliente()
    __BDEmpleado = empleado()
    __instancia = None

    @staticmethod
    def obtenerInstancia():
        if accionesFacade.__instancia is None:
            accionesFacade()
        return accionesFacade.__instancia

    def __init__(self):
        if accionesFacade.__instancia is None:
            accionesFacade.__instancia = self

    def obtenerInfoPeliculas(self):
        return self.__BDPelicula.obtenerPeliculas()

    def obtenerMultiplexParaPelicula(self, idPelicula):
        return self.__BDPresentacion.multiplexDondePresenta(idPelicula)

    def obtenerDatosMultiplex(self, idPelicula):
        multiplex = []
        for indice in [x[0] for x in self.obtenerMultiplexParaPelicula(idPelicula)]:
            multiplex.append(self.__BDMultiplex.obtenerDatosMultiplex(indice))
        return multiplex

    def DatosDeUnMultiplex(self, idMultiplex):
        return self.__BDMultiplex.obtenerDatosMultiplex(idMultiplex)

    def obtenerPresentaciones(self, idPelicula, idMultiplex, estado):
        return self.__BDPresentacion.obtenerPresentaciones(idPelicula, idMultiplex, estado)

    def obtenerSillasPresentacion(self, idPresentacion):
        return self.__BDSilla.obtenerSillasPresentacion(idPresentacion)

    def sillaEnEspera(self, idPresentacion, idSilla, carritoCompra):
        identificadorSilla = {
            "idSilla": idSilla,
            "idPresentacion": idPresentacion
        }
        articuloDeseado = {
            "id": identificadorSilla,
            "entidad": "silla"
        }
        carritoCompra.append(articuloDeseado)
        self.__BDSilla.modificarEstadoSilla(idSilla, idPresentacion, "TOMADA")

    def clienteEncontrado(self, Username):
        if self.__BDCliente.buscarClientePorNick(Username):
            return True
        else:
            return False

    def registrarCliente(self, NOMBRE, APELLIDO, TELEFONO, CEDULA, USERNAME):
        idCliente = self.__BDCliente.nuevoIdCliente()[0]
        if idCliente is None:
            self.__BDCliente.crearCliente(1, NOMBRE, APELLIDO, TELEFONO, CEDULA, USERNAME)
        else:
            self.__BDCliente.crearCliente(idCliente+1, NOMBRE, APELLIDO, TELEFONO, CEDULA, USERNAME)

    def datosArticulosCarrito(self, carritoCompra):
        datosPorArticulo = []
        for articulo in carritoCompra:
            if articulo.get("entidad") == "silla":
                idPresentacion = articulo.get("id").get("idPresentacion")
                idSilla = articulo.get("id").get("idSilla")
                datosBD = self.__BDSilla.obtenerDatosSilla(idPresentacion, idSilla)
                dato = ["silla"] + [x for x in datosBD]
                datosPorArticulo.append(dato)
            elif articulo.get("entidad") == "snack":
                idSnack = articulo.get("id")
                datosBD = self.__BDProductoSnack.obtenerDatosSnack(idSnack)
                cantidad = articulo.get("cantidad")
                dato = ["snack"] + [cantidad] + [x for x in datosBD]
                datosPorArticulo.append(dato)
        return datosPorArticulo

    def restaurarInventario(self, carritoCompra, idArticulo, entidad):
        idArticulo = self.decifrarId(entidad, idArticulo)
        if entidad == "silla":
            idSilla = idArticulo.get("idSilla")
            idPresentacion = idArticulo.get("idPresentacion")
            self.restaurarEstadoSilla(carritoCompra, idSilla, idPresentacion)
        elif entidad == "snack":
            idSnack = idArticulo.get("id")
            self.restaurarEstadoSnack(idSnack, carritoCompra)

    def decifrarId(self, entidad, id):
        idArticulo = {}
        if entidad == "silla":
            identificadores = id.split(",")
            idPresentacion = identificadores[0]
            idSilla = identificadores[1]
            idArticulo = {
                "idPresentacion": idPresentacion,
                "idSilla": idSilla
            }
        elif entidad == "snack":
            idArticulo = {
                "id": id
            }
        return idArticulo

    def restaurarEstadoSnack(self, idSnack, carritoCompra):
        for articulo in carritoCompra:
            if articulo.get("id") == idSnack:
                carritoCompra.remove(articulo)
                break

    def restaurarEstadoSilla(self, carritoCompra, idSilla, idPresentacion):
        for articulo in carritoCompra:
            if articulo.get("id").get("idPresentacion") == idPresentacion \
                    and articulo.get("id").get("idSilla") == idSilla:
                        self.__BDSilla.modificarEstadoSilla(idSilla, idPresentacion, "DISPONIBLE")
                        carritoCompra.remove(articulo)
                        break

    def restaurarBaseDatosCarritoAbandonado(self, carritoCompra):
        for indice in range(len(carritoCompra)-1, -1, -1):
                if carritoCompra[indice].get("entidad") == "silla":
                    idSilla = carritoCompra[indice].get("id").get("idSilla")
                    idPresentacion = carritoCompra[indice].get("id").get("idPresentacion")
                    self.__BDSilla.modificarEstadoSilla(idSilla, idPresentacion, "DISPONIBLE")
                    carritoCompra.pop()

    def eliminarSillasAbandonadas(self, carritoCompra):
        carritoCompraTemp = []
        for indice in range(len(carritoCompra)-1, -1, -1):
            if carritoCompra[indice].get("entidad") == "silla":
                carritoCompraTemp.append(carritoCompra[indice])
                carritoCompra.pop()
        self.restaurarBaseDatosCarritoAbandonado(carritoCompraTemp)

    def calcularPrecioTotal(self, carritoCompra):
        total = 0
        for articulo in carritoCompra:
            if articulo.get("entidad") == "silla":
                idPresentacion = articulo.get("id").get("idPresentacion")
                idSilla = articulo.get("id").get("idSilla")
                datos = self.__BDSilla.obtenerDatosSilla(idPresentacion, idSilla)
                total += int(datos[7])
            if articulo.get("entidad") == "snack":
                idSnack = articulo.get("id")
                datos = self.__BDProductoSnack.obtenerDatosSnack(idSnack)
                cantidad = articulo.get("cantidad")
                total += int(datos[3]*cantidad)
        return total

    def obtenerDatosCliente(self, nickname):
        cliente = self.__BDCliente.buscarClientePorNick(nickname)
        return cliente

    def obtenerDatosSilla(self, idPresentacion, idSilla):
        return self.__BDSilla.obtenerDatosSilla(idPresentacion, idSilla)

    def asignarNumeroFacturaSilla(self, idPresentacion, idSilla, numFactura, valorVenta):
        self.__BDSilla.modificarEstadoSilla(idSilla, idPresentacion, "VENDIDA")
        self.__BDSilla.asignarNumeroFacturaSilla(numFactura, idPresentacion, idSilla, valorVenta)

    def generarNumeroFactura(self):
        idFactura = "ERROR"
        while True:
            numeroFactura = random.randint(100000, 999999)
            idFactura = "P" + str(numeroFactura)
            if not self.__BDFactura.buscarNumeroFactura(idFactura):
                break
        return idFactura

    def agregarFactura(self, numFactura, valor, idCliente, tipoValor, fecha):
        self.__BDFactura.agregarFactura(numFactura, valor, idCliente, tipoValor, fecha)

    def liberarSilla(self, idPresentacion, idSilla):
        self.__BDSilla.modificarEstadoSilla(idSilla, idPresentacion, "DISPONIBLE")

    def obtenerArticulosNumFactura(self, numFactura):
        articulos = []
        articulos += self.obtenerSillasNumeroFactura(numFactura)
        articulos += self.obtenerSnackNumFactura(numFactura)
        return articulos


    def obtenerSillasNumeroFactura(self, numFactura):
        articulos = []
        sillas = self.__BDSilla.obtenerSillasNumFactura(numFactura)
        for silla in sillas:
            idPresentacion = silla[0]
            idSilla = silla[1]
            articulo = {
                "entidad": "silla",
                "datos" : self.__BDSilla.obtenerDatosSilla(idPresentacion, idSilla),
                "precioVenta": self.obtenerPrecioVentaSilla(idPresentacion, idSilla, numFactura)[2]
            }
            articulos.append(articulo)
        return articulos

    def obtenerSnackNumFactura(self, numFactura):
        articulos = []
        snacks = self.__BDProductoFactura.obtenerProductosNumFactura(numFactura)
        for snack in snacks:
            idSnack = snack[0]
            articulo = {
                "entidad": "snack",
                "datos": self.__BDProductoSnack.obtenerDatosSnack(idSnack),
                "precioVenta": snack[3],
                "cantidad": snack[2]
            }
            articulos.append(articulo)
        return articulos

    def obtenerSnacksNumFactura(self, numFactura):
        pass

    def obtenerPrecioVentaSilla(self, idPresentacion, idSilla, numFactura):
        return self.__BDSilla.obtenerPrecioVentaSilla(idPresentacion, idSilla, numFactura)

    def obtenerDatosFactura(self, numFactura):
        return self.__BDFactura.obtenerDatosFactura(numFactura)

    def obtenerUsuarioPorId(self, idCliente):
        return self.__BDCliente.obtenerDatosClientePorID(idCliente)

    def obteneridCliente(self, nickname):
        cliente = self.__BDCliente.buscarClientePorNick(nickname)
        if cliente:
            return cliente[0]
        else:
            return -1

    def obtenerFacturasCliente(self, idCliente):
        return self.__BDFactura.obtenerDatosFacturaPorIdCliente(idCliente)

    def facturaEsDelUsuarioLinea(self, numFactura, idUsuario=None, nickname=None):
        if nickname is not None:
            identificadorUsuario = self.obteneridCliente(nickname)
        elif idUsuario is not None:
            identificadorUsuario = idUsuario
        else:
            return False
        datosFactura = self.__BDFactura.obtenerDatosFactura(numFactura)
        if int(datosFactura[2]) != int(identificadorUsuario):
            return False
        else:
            return True

    def facturaExiste(self, numFactura):
        if self.__BDFactura.buscarNumeroFactura(numFactura):
            return True
        else:
            return False

    def confirmarPresetacionActivas(self, numFactura, usuarioEnLinea):
        sillas = self.__BDSilla.obtenerSillasNumFactura(numFactura)
        confirmacion = {
            "esApta": None,
            "error": None,
            "idMultiplex": []
        }
        idMultiplex = []
        if not self.facturaExiste(numFactura):
            confirmacion["esApta"] = False
            confirmacion["error"] = "La factura No existe!"
        elif not self.facturaEsDelUsuarioLinea(numFactura, nickname=usuarioEnLinea):
            confirmacion["esApta"] = False
            confirmacion["error"] = "La Factura No le Pertenece al usuario en linea!"
        elif sillas:
            for silla in sillas:
                idPresentacion = silla[0]
                datosPresentacion = self.__BDPresentacion.obtenerEstadoPresentacion(idPresentacion)
                if datosPresentacion[1] == "DISPONIBLE":
                    idMultiplex.append(datosPresentacion[2])
            if idMultiplex:
                confirmacion["esApta"] = True
                idMultiplexSinRepetir = []
                for identificador in idMultiplex:
                    if identificador not in idMultiplexSinRepetir:
                        idMultiplexSinRepetir.append(identificador)
                confirmacion["idMultiplex"] = idMultiplexSinRepetir
            else:
                confirmacion["esApta"] = False
                confirmacion["error"] = "No hay funciones validas!"
        else:
            confirmacion["esApta"] = False
            confirmacion["error"] = "No hay Sillas en la factura!"
        return confirmacion

    def obtenerInformacionMultiplexValidos(self, idMultiplex):
        datosMultiplex = []
        for identificador in idMultiplex:
            datos = self.DatosDeUnMultiplex(identificador)
            datosMultiplex.append(datos)
        return datosMultiplex

    def obtenerProductosSnackMultiples(self, idMultiplex):
        return self.__BDProductoSnack.obtenerProductosDelMultiplex(idMultiplex)

    def llenarCarritoSnacks(self, carritoCompra, idProductoSnack, cantidad):
        if cantidad > 0:
            articulo = {
                "entidad": "snack",
                "id": str(idProductoSnack),
                "cantidad": cantidad
            }
            carritoCompra.append(articulo)

    def obtenerDatosTipoSilla(self, tipoSilla):
        return self.__BDSilla.obtenerDatosTipoSilla(tipoSilla)

    def insertarNuevaFacturaSnack(self, numFactura):
        self.__BDFacturaSnack.insertarFacturaNueva(numFactura)

    def insertarProductoYFactura(self, idProducto, numFactura, cantidad, valorVenta):
        self.__BDProductoFactura.insertarProductoYFactura(idProducto, numFactura, cantidad, valorVenta)

    def obtenerDatosSnack(self, idSnack):
        datos = self.__BDProductoSnack.obtenerDatosSnack(idSnack)
        return datos

    def insertarNumFacturaAFacturasSnack(self, numFactura):
        if not self.__BDFacturaSnack.obtenerFactura(numFactura):
            self.__BDFacturaSnack.insertarFacturaNueva(numFactura)

    def modificarPuntosCliente(self, idCliente, puntos):
        self.__BDCliente.modificarPuntosCliente(puntos, idCliente)

    def modificarCantidadSnack(self, idSnack, nuevaCantidad):
        self.__BDProductoSnack.modificarCantidadSnack(idSnack, nuevaCantidad)

    def obtenerOpinion(self, id, elementoCalificar):
        opinionResultado = {
            "calificacion": None,
            "opinion": None,
            "existe": False
        }
        id = self.decifrarIdElementoCalificar(id, elementoCalificar)

        if elementoCalificar == "servicio":
            datos = self.__BDFactura.obtenerDatosFactura(id.get("numFactura"))
            calificacion = datos[5]
            opinion = datos[6]
        elif elementoCalificar == "pelicula" \
            and self.__BDPeliculaCliente.obtenerCalificacion(id.get("idCliente"), id.get("idPelicula")):
            datos = self.__BDPeliculaCliente.obtenerCalificacion(id.get("idCliente"), id.get("idPelicula"))
            calificacion = datos[2]
            opinion = datos[3]
        else:
            calificacion = None
            opinion = None

        if calificacion:
            opinionResultado["calificacion"] = calificacion
            opinionResultado["existe"] = True
        if opinion:
            opinionResultado["opinion"] = opinion
            opinionResultado["existe"] = True
        return opinionResultado

    def ingresarOpinion(self, elementoCalificar, opinion, calificacion, id):
        identificador = self.decifrarIdElementoCalificar(id, elementoCalificar)
        if elementoCalificar == "servicio":
            numFactura = identificador.get("numFactura")
            self.__BDFactura.ingresarOpinionServicio(numFactura, opinion, calificacion)
        elif elementoCalificar == "pelicula":
            idCliente = identificador.get("idCliente")
            idPelicula = identificador.get("idPelicula")
            existenciaCalificacion = self.__BDPeliculaCliente.obtenerCalificacion(idCliente, idPelicula)
            if existenciaCalificacion:
                self.__BDPeliculaCliente.modificarOpinion(idCliente, idPelicula, calificacion, opinion)
            else:
                self.__BDPeliculaCliente.agregarCalificacion(idCliente, idPelicula, calificacion, opinion)

    def decifrarIdElementoCalificar(self, idElemento, tipoElemento):
        identificador = {}
        if tipoElemento == "servicio":
            identificador["numFactura"] = idElemento
        elif tipoElemento == "pelicula":
            idElemento = idElemento.split(",")
            identificador["idPelicula"] = idElemento[0]
            identificador["idCliente"] = idElemento[1]
        return identificador

    def idPeliculasValidasCalificar(self, nickname):
        idPeliculas = []
        idCliente = self.obteneridCliente(nickname)
        facturas = self.__BDFactura.obtenerDatosFacturaPorIdCliente(idCliente)
        for factura in facturas:
            numFactura = factura[0]
            sillas = self.__BDSilla.obtenerSillasNumFactura(numFactura)
            for silla in sillas:
                idPresentacion = silla[0]
                estadoPresentacion = self.__BDPresentacion.obtenerEstadoPresentacion(idPresentacion)
                if estadoPresentacion[1] == "FINALIZADA":
                    idPelicula = estadoPresentacion[3]
                    if idPelicula not in idPeliculas:
                        idPeliculas.append(idPelicula)
        return idPeliculas

    def datosPeliculaPorId(self, idPelicula):
        return self.__BDPelicula.obtenerDatosPelicula(idPelicula)

    def obtenerDatosEmpleados(self, idMultiplex):
        return self.__BDEmpleado.obtenerDatosEmpleados(idMultiplex)

    def obtenerFacturasPorFecha(self, mes, year):
        return self.__BDFactura.obtenerFacturasPorFecha(mes, year)


    def obtenerFacturaSillasVendidas(self):
        return self.__BDSilla.obtenerSillasVendidas()

    def obtenerTotalSillasPorFecha(self, year):
        totales = [0] * 12
        numeroFacturas = [x[3] for x in self.obtenerFacturaSillasVendidas()]
        for numeroFactura in numeroFacturas:
            factura = self.__BDFactura.obtenerDatosFactura(numeroFactura)
            if factura[7].year == year:
                totales[factura[7].month-1] += 1
        return totales



    def obtenerTotalPorMesFactura(self, mes, year, tipoVenta):
        total = 0
        if tipoVenta == "total":
            facturas = self.obtenerFacturasPorFecha(mes, year)
        else:
            facturas = []
        for factura in facturas:
            total += factura[1]
        return total

### Presentado por Willmar Pelaez - 20182020123

    def obtenerTotalesFacturaYear(self, year, tipoVenta):
        totales = []
        for mes in range(1, 13, 1):
            if tipoVenta == "total":
                totales.append(self.obtenerTotalPorMesFactura(mes, year, tipoVenta))
        return totales