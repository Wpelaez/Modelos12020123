import psycopg2

DB_HOST = "localhost"
DB_NAME = "cineJungla"
DB_USER = "postgres"
DB_PASS = "123"
conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
cursor = conn.cursor()

class productoSnack_facturaSnack():


    def __init__(self):
        pass

    def insertarProductoYFactura(self, idProducto, numFactura, cantidad, valorVenta):
        cursor.execute(f"""
                            INSERT 
                                INTO PRODUCTOSNACK_FACTURASNACK 
                                VALUES({idProducto}, '{numFactura}', {cantidad}, {valorVenta});
                        """)
        conn.commit()

    def obtenerProductosNumFactura(self, numFactura):
        cursor.execute(f"""
                            SELECT PRODUCTOSNACK_FACTURASNACK.IDPRODUCTOSNACK, PRODUCTOSNACK_FACTURASNACK.IDFACTURA,
                                    PRODUCTOSNACK_FACTURASNACK.CANTIDAD, PRODUCTOSNACK_FACTURASNACK.VALORVENTA
                                FROM PRODUCTOSNACK_FACTURASNACK
                                WHERE PRODUCTOSNACK_FACTURASNACK.IDFACTURA = '{numFactura}';
                        """)
        return cursor.fetchall()