import psycopg2

DB_HOST = "localhost"
DB_NAME = "cineJungla"
DB_USER = "postgres"
DB_PASS = "123"
conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
cursor = conn.cursor()

class multiplex():

    def __init__(self):
        pass

    def obtenerDatosMultiplex(self, idMultiplex):
        cursor.execute("SELECT MULTIPLEX.ID, MULTIPLEX.NOMBRE, MULTIPLEX.TELEFONO, "
                            "MULTIPLEX.DIRECCION, MULTIPLEX.DIRECCIONIMG, "
                            "MULTIPLEX.CIUDAD, MULTIPLEX.PAIS"
	                    " FROM MULTIPLEX"
	                    f" WHERE MULTIPLEX.ID = {idMultiplex};")
        return cursor.fetchone()