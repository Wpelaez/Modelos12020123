import psycopg2

DB_HOST = "localhost"
DB_NAME = "cineJungla"
DB_USER = "postgres"
DB_PASS = "123"
conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
cursor = conn.cursor()

class presentacion():

    def __init__(self):
        pass

    def multiplexDondePresenta(self, idPelicula):
        cursor.execute("SELECT DISTINCT PRESENTACION.IDMULTIPLEX"
	                    " FROM PRESENTACION"
	                    f" WHERE PRESENTACION.IDPELICULA = {idPelicula};")
        return cursor.fetchall()

    def obtenerPresentaciones(self, idPelicula, idMultiplex, estado):
        cursor.execute(f"""
                        SELECT PRESENTACION.ID, PRESENTACION.FECHAINICIO, PRESENTACION.FECHATERMINO, PRESENTACION.SALANUM, PRESENTACION.ESTADO
                                                 FROM PRESENTACION
                                                 WHERE PRESENTACION.IDMULTIPLEX = {idMultiplex} AND PRESENTACION.IDPELICULA = {idPelicula}
                                                    AND PRESENTACION.ESTADO = '{estado}';
                        """)
        return cursor.fetchall()

    def obtenerEstadoPresentacion(self, idPresentacion):
        cursor.execute(f"""
                        SELECT PRESENTACION.ID, PRESENTACION.ESTADO, PRESENTACION.IDMULTIPLEX, PRESENTACION.IDPELICULA
                            FROM PRESENTACION
                            WHERE PRESENTACION.ID = {idPresentacion};
                        """)
        return cursor.fetchone()