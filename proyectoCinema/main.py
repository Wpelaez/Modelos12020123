## REALIZADO POR WILLMAR PELAEZ - 20182020132
from flask import Flask, render_template, url_for, request, redirect, flash
from accionesFacade import accionesFacade
from servicioPago import servicioPago
import calendar

app = Flask(__name__)
app.secret_key = "123"
baseDatos = accionesFacade.obtenerInstancia()
carritoCompraPelicula = []
usuarioEnLinea = []

@app.route("/")
def index():
    peliculas = baseDatos.obtenerInfoPeliculas()
    if usuarioEnLinea:
        usuario = usuarioEnLinea[-1]
    else:
        usuario = None
    return render_template("index.html", peliculas=peliculas, usuario=usuario)

@app.route("/multiplex/<string:idPelicula>")
def seleccionarMultiplex(idPelicula):
    multiplex = baseDatos.obtenerDatosMultiplex(idPelicula)
    return render_template("seleccionMultiplex.html", multiplex=multiplex, idPelicula=idPelicula)

@app.route("/Presentacion/<string:idPelicula>/<string:idMultiplex>")
def seleccionarPresentacion(idPelicula, idMultiplex):
    multiplexSeleccionado = baseDatos.DatosDeUnMultiplex(idMultiplex)
    presentaciones = baseDatos.obtenerPresentaciones(idPelicula, idMultiplex, "DISPONIBLE")
    return render_template("seleccionarPresentacion.html", multi=multiplexSeleccionado,
                                presentaciones=presentaciones, usuarioEnSesion=bool(usuarioEnLinea))

@app.route("/seleccionarSilla/<string:idPresentacion>", methods=['GET', 'POST'])
def seleccionarSilla(idPresentacion):
    if request.method == 'POST':
        sillas = request.form.getlist("sillasSeleccionadas")
        for silla in sillas:
            baseDatos.sillaEnEspera(idPresentacion, silla, carritoCompraPelicula)
        print(carritoCompraPelicula)
        return redirect(url_for("carritoCompra"))
    else:
        sillas = baseDatos.obtenerSillasPresentacion(idPresentacion)
        return render_template("seleccionarSilla.html", sillas=sillas)

@app.route("/opcionesUsuario/<string:idPresentacion>", methods=['GET', 'POST'])
@app.route("/opcionesUsuario", defaults={'idPresentacion': None}, methods=['GET', 'POST'])
def opcionesUsuario(idPresentacion):
    if request.method == "POST":
        if request.form.get("formularioEscojido") == "usuarioNuevo":
            if not baseDatos.clienteEncontrado(request.form.get("username")):
                NOMBRE = request.form.get("nombre")
                APELLIDO = request.form.get("apellido")
                TELEFONO = request.form.get("telefono")
                CEDULA = request.form.get("cedula")
                USERNAME = request.form.get("username")
                baseDatos.registrarCliente(NOMBRE, APELLIDO, TELEFONO, CEDULA, USERNAME)
                if usuarioEnLinea:
                    usuarioEnLinea.pop()
                usuarioEnLinea.append(USERNAME)
            else:
                flash("Nombre De Usuario Ya Esta en Uso!")
                return redirect(url_for("opcionesUsuario"))
        elif request.form.get("formularioEscojido") == "buscarUsuario":
            if baseDatos.clienteEncontrado(request.form.get("nombreUsuario")):
                if usuarioEnLinea:
                    usuarioEnLinea.pop()
                username = baseDatos.obtenerDatosCliente(request.form.get("nombreUsuario"))[1]
                usuarioEnLinea.append(username)
            else:
                flash("Usuario No encontrado!")
                return redirect(url_for("opcionesUsuario"))
        if idPresentacion is None:
            return redirect(url_for("index"))
        else:
            return redirect(url_for("seleccionarSilla", idPresentacion=idPresentacion))
    else:
        return render_template("opcionesUsuario.html")

@app.route("/carritoCompra", methods=['GET', 'POST'])
def carritoCompra():
    if request.method == "POST":
        idArticulo = request.form.get("id")
        entidad = request.form.get("entidad")
        baseDatos.restaurarInventario(carritoCompraPelicula, idArticulo, entidad)
        return redirect(url_for("carritoCompra"))
    else:
        datosCarritoCompra = baseDatos.datosArticulosCarrito(carritoCompraPelicula)
        total = baseDatos.calcularPrecioTotal(carritoCompraPelicula)
        return render_template("carritoCompra.html", datosCarritoCompra=datosCarritoCompra,
                               total=total)

@app.route("/checkout", methods=['GET', 'POST'])
def checkout():
    total = baseDatos.calcularPrecioTotal(carritoCompraPelicula)
    if not carritoCompraPelicula:
        flash("Carrito Vacio!")
        return redirect(url_for("index"))
    if not usuarioEnLinea:
        flash("No hay usuario en Linea!")
        return redirect(url_for("index"))
    datosCliente = baseDatos.obtenerDatosCliente(usuarioEnLinea[0])

    if request.method == "POST":
        metodoPago = request.form.get("tipoPago")
        servicioPagoOBJ = servicioPago()
        if metodoPago == "efectivo":
            servicioPagoOBJ.setEstrategiaPago("efectivo", usuarioEnLinea[-1], carritoCompraPelicula)
        elif metodoPago == "puntos":
            servicioPagoOBJ.setEstrategiaPago("puntos", usuarioEnLinea[-1], carritoCompraPelicula)
        resultadoPago = servicioPagoOBJ.realizarPago()
        if resultadoPago == "exito":
            carritoCompraPelicula.clear()#AQUIVAMOS
            return redirect(url_for("factura", numeroFactura=servicioPagoOBJ.obtenerNumeroFactura()))
        else:
            flash("Error! " + resultadoPago)
            return redirect(url_for("carritoCompra"))
    else:
        return render_template("checkout.html", total=total, datosUser=datosCliente)

@app.route("/factura/<string:numeroFactura>")
def factura(numeroFactura):
    if not baseDatos.facturaExiste(numeroFactura):
        flash("La Factura No existe!")
        return redirect(url_for("index"))
    if not baseDatos.facturaEsDelUsuarioLinea(numeroFactura, nickname=usuarioEnLinea[-1]):
        flash("La Factura No le Pertenece al usuario en linea!")
        return redirect(url_for("index"))
    articulos = baseDatos.obtenerArticulosNumFactura(numeroFactura)
    datosFactura = baseDatos.obtenerDatosFactura(numeroFactura)
    cliente = baseDatos.obtenerUsuarioPorId(datosFactura[2])
    calificacionServicio = baseDatos.obtenerOpinion(numeroFactura, "servicio")
    return render_template("factura.html", numeroFactura=numeroFactura, articulos=articulos,
                            datosFactura=datosFactura, cliente=cliente,
                            calificacionServicio=calificacionServicio)

@app.route("/verFacturas")
def verFacturas():
    if not usuarioEnLinea:
        flash("No hay Usuario en linea!")
        return redirect(url_for("index"))
    idCliente = baseDatos.obteneridCliente(usuarioEnLinea[-1])
    facturas = baseDatos.obtenerFacturasCliente(idCliente)
    esValidaSnack = []
    for factura in facturas:
        estadoConfirmacion = baseDatos.confirmarPresetacionActivas(factura[0], usuarioEnLinea[-1])
        esValidaSnack.append(estadoConfirmacion)
    return render_template("tablaFacturas.html", usuario=usuarioEnLinea[-1],
                           facturas=zip(facturas, esValidaSnack))

@app.route("/PortalComida/confirmarFactura", methods=['GET', 'POST'])
def confirmarFacturaComida():
    if not usuarioEnLinea:
        flash("No hay Usuario en linea!")
        return redirect(url_for("index"))
    if request.method == 'POST':
        numFactura = request.form.get("numeroFactura")
        estadoConfirmacion = baseDatos.confirmarPresetacionActivas(numFactura, usuarioEnLinea[-1])
        if estadoConfirmacion.get("esApta"):
            idMultiplex = estadoConfirmacion.get("idMultiplex")
            datosMultiplexValidos = baseDatos.obtenerInformacionMultiplexValidos(idMultiplex)
            return render_template("confirmarMultiplex.html", multiplexValidos=datosMultiplexValidos)
        else:
            flash("Error! " + estadoConfirmacion.get("error"))
            return redirect(url_for("confirmarFacturaComida"))
    else:
        return render_template("confirmarFactura.html")

@app.route("/snacks", methods=['GET', 'POST'])
def snacks():
    if request.method == 'POST':
        idMultiplex = request.form.get("idMultiplex")
        datosMultiplex = baseDatos.DatosDeUnMultiplex(idMultiplex)
        productosSnackMultiplex = baseDatos.obtenerProductosSnackMultiples(idMultiplex)
        if request.form.get("accion") == "llenarCarrito":
            baseDatos.eliminarSillasAbandonadas(carritoCompraPelicula)
            for articulo in productosSnackMultiplex:
                idArticulo = articulo[0]
                cantidad = int(request.form.get(f"{idArticulo}"))
                baseDatos.llenarCarritoSnacks(carritoCompraPelicula, idArticulo, cantidad)
            print(carritoCompraPelicula)
            return redirect(url_for("carritoCompra"))
        else:
            return render_template("snacks.html", productosSnackMultiplex=productosSnackMultiplex,
                                            datosMultiplex=datosMultiplex)
    else:
        return redirect(url_for("index"))

@app.route("/calificar", methods=['GET', 'POST'])
def calificar():
    if request.method == "POST":
        if request.form.get("accion") == "subirOpinion":
            elementoCalificar = request.form.get("elementoCalificar")
            opinion = request.form.get("opinion")
            calificacion = request.form.get("calificacion")
            id = request.form.get("idElemento")
            baseDatos.ingresarOpinion(elementoCalificar, opinion, calificacion, id)
            flash("Opinion Subida con Exito!")
            return redirect(url_for("index"))
        else:
            if request.form.get("numFactura"):
                elementoCalificar = "servicio"
                idElemento = request.form.get("numFactura")
                calificacion = baseDatos.obtenerOpinion(idElemento, elementoCalificar)
            elif request.form.get("idPelicula"):
                elementoCalificar = "pelicula"
                idPelicula = request.form.get("idPelicula")
                idElemento = f"{idPelicula}, {baseDatos.obteneridCliente(usuarioEnLinea[-1])}"
                calificacion = baseDatos.obtenerOpinion(idElemento, "pelicula")
            else:
                elementoCalificar = "ERROR"
                idElemento = "0"
                calificacion = None
            return render_template("calificacion.html", elementoCalificar=elementoCalificar,
                                   idElemento=idElemento, calificacion=calificacion)
    else:
        return redirect(url_for("index"))

@app.route("/logout")
def logout():
    if usuarioEnLinea:
        usuarioEnLinea.pop()
        #print(carritoCompraPelicula)
        baseDatos.restaurarBaseDatosCarritoAbandonado(carritoCompraPelicula)
        #print(carritoCompraPelicula)
    return redirect(url_for("index"))

@app.route("/calificarPelicula")
def calificarPelicula():
    if not usuarioEnLinea:
        return redirect(url_for("index"))
    idPeliculas = baseDatos.idPeliculasValidasCalificar(usuarioEnLinea[-1])
    if not idPeliculas:
        flash("El usuario aun no cuenta con funciones finalizadas!")
        return redirect(url_for("index"))
    datosPeliculas = [baseDatos.datosPeliculaPorId(x) for x in idPeliculas]
    calificaciones = []
    for idPelicula in idPeliculas:
        id = f"{idPelicula}, {baseDatos.obteneridCliente(usuarioEnLinea[-1])}"
        calificacion = baseDatos.obtenerOpinion(id, "pelicula")
        calificaciones.append(calificacion)
    return render_template("tablaPeliculasCalificar.html",
                           datos=zip(datosPeliculas, calificaciones))

@app.route("/admin")
def admin():
    return render_template("menuAdmin.html")

@app.route("/tablaAdminEmpleado", methods=['GET', 'POST'])
def tablaEmpleados():
    if request.method == "POST":
        empleados = baseDatos.obtenerDatosEmpleados(request.form.get("idMultiplex"))
        return render_template("tablaAdminEmpleado.html", empleados=empleados)
    else:
        redirect(url_for("index"))

@app.route("/tablaVenta", methods=['GET', 'POST'])
def tablaVenta():
    if request.method == "POST":
        if request.form.get("total"):
            totales = baseDatos.obtenerTotalesFacturaYear(2022, "total")
        elif request.form.get("sillasTotales"):
            totales = baseDatos.obtenerTotalSillasPorFecha(2022)
        else:
            totales = []
        return render_template("tablaVenta.html", totales=totales, year=2022,
                               meses=[calendar.month_name[x] for x in range(1, 13, 1)])
    else:
        redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
