import psycopg2

DB_HOST = "localhost"
DB_NAME = "cineJungla"
DB_USER = "postgres"
DB_PASS = "123"
conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
cursor = conn.cursor()

class facturasnack():

    def __init__(self):
        pass

    def insertarFacturaNueva(self, idFactura):
        cursor.execute(f"""
                        INSERT INTO FACTURASNACK 
                            VALUES('{idFactura}');
                    """)
        conn.commit()

    def obtenerFactura(self, numFactura):
        cursor.execute(f"""
                            SELECT FACTURASNACK.NUMFACTURA
                                FROM FACTURASNACK
                                WHERE FACTURASNACK.NUMFACTURA = '{numFactura}';
                        """)
        return cursor.fetchone()