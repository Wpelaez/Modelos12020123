import psycopg2

DB_HOST = "localhost"
DB_NAME = "cineJungla"
DB_USER = "postgres"
DB_PASS = "123"
conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
cursor = conn.cursor()

class pelicula_cliente():

    def __init__(self):
        pass

    def obtenerCalificacion(self, idCliente, idPelicula):
        cursor.execute(f"""
                        SELECT PELICULA_CLIENTE.IDPELICULA, PELICULA_CLIENTE.IDCLIENTE, PELICULA_CLIENTE.CALIFICACION, PELICULA_CLIENTE.OPINION
                            FROM PELICULA_CLIENTE
                            WHERE PELICULA_CLIENTE.IDPELICULA = {idPelicula} AND PELICULA_CLIENTE.IDCLIENTE = {idCliente};
                        """)
        return cursor.fetchone()

    def agregarCalificacion(self, idCliente, idPelicula, calificacion, opinion):
        cursor.execute(f"""
                        INSERT INTO PELICULA_CLIENTE 
                            VALUES ({idPelicula}, {idCliente}, {calificacion}, '{opinion}');
                        """)
        conn.commit()

    def modificarOpinion(self, idCliente, idPelicula, calificacion, opinion):
        cursor.execute(f"""
                            UPDATE PELICULA_CLIENTE 
                                SET CALIFICACION = {calificacion}, OPINION = '{opinion}'
                                WHERE PELICULA_CLIENTE.IDPELICULA = {idPelicula} AND PELICULA_CLIENTE.IDCLIENTE = {idCliente};
                        """)
        conn.commit()