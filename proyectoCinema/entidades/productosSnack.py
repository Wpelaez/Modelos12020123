import psycopg2

DB_HOST = "localhost"
DB_NAME = "cineJungla"
DB_USER = "postgres"
DB_PASS = "123"
conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
cursor = conn.cursor()

class productoSnack():

    def __init__(self):
        pass

    def obtenerProductosDelMultiplex(self, idMultiplex):
        cursor.execute(f"""
                        SELECT PRODUCTOSNACK.ID, PRODUCTOSNACK.DESCRIPCION, PRODUCTOSNACK.CANTIDAD, PRODUCTOSNACK.PRECIO, PRODUCTOSNACK.DIRECCIONIMG,
                                PRODUCTOSNACK.IDMULTIPLEX, PRODUCTOSNACK.IDTIPOSNACK, TIPOSNACK.NOMBRE
                            FROM PRODUCTOSNACK, TIPOSNACK
                            WHERE PRODUCTOSNACK.IDMULTIPLEX = {idMultiplex} AND TIPOSNACK.ID = PRODUCTOSNACK.IDTIPOSNACK;
                        """)
        return cursor.fetchall()

    def obtenerDatosSnack(self, idSnack):
        cursor.execute(f"""
                        SELECT PRODUCTOSNACK.ID, PRODUCTOSNACK.DESCRIPCION, PRODUCTOSNACK.CANTIDAD, PRODUCTOSNACK.PRECIO, PRODUCTOSNACK.DIRECCIONIMG,
                                PRODUCTOSNACK.IDMULTIPLEX, PRODUCTOSNACK.IDTIPOSNACK, TIPOSNACK.NOMBRE
                            FROM PRODUCTOSNACK, TIPOSNACK
                            WHERE PRODUCTOSNACK.ID = {idSnack} AND TIPOSNACK.ID = PRODUCTOSNACK.IDTIPOSNACK;                        
                        """)
        return cursor.fetchone()

    def modificarCantidadSnack(self, idSnack, nuevaCantidad):
        cursor.execute(f"""
                        UPDATE PRODUCTOSNACK 
                            SET CANTIDAD = {nuevaCantidad}
                            WHERE PRODUCTOSNACK.ID = {idSnack};        
                        """)
        conn.commit()