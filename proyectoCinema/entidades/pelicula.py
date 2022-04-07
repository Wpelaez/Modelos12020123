import psycopg2

DB_HOST = "localhost"
DB_NAME = "cineJungla"
DB_USER = "postgres"
DB_PASS = "123"
conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
cursor = conn.cursor()

class pelicula():

    def __init__(self):
        pass

    def obtenerPeliculas(self):
        cursor.execute("""
                        SELECT PELICULA.ID, PELICULA.NOMBRE, PELICULA.GENERO,
                                                PELICULA.DURACION, PELICULA.DIRECCIONIMG,
                                                PELICULA.SINOPSIS, PELICULA.CLASIFICACION
                            FROM PELICULA;        
                    """)
        return cursor.fetchall()

    def obtenerDatosPelicula(self, idPelicula):
        cursor.execute(f"""
                        SELECT PELICULA.ID, PELICULA.NOMBRE, PELICULA.GENERO,
                                                PELICULA.DURACION, PELICULA.DIRECCIONIMG,
                                                PELICULA.SINOPSIS, PELICULA.CLASIFICACION
                            FROM PELICULA
                            WHERE PELICULA.ID = {idPelicula};
                        """)
        return cursor.fetchone()