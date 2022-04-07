import psycopg2

DB_HOST = "localhost"
DB_NAME = "cineJungla"
DB_USER = "postgres"
DB_PASS = "123"
conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
cursor = conn.cursor()

class silla():

    def __init__(self):
        pass

    def obtenerSillasPresentacion(self, idPresentacion):
        cursor.execute(f"""
                        SELECT SILLA.NUMSILLA, SILLA.ESTADO, SILLA.IDTIPOSILLA, TIPOSILLA.NOMBRE, TIPOSILLA.PRECIO
                            FROM SILLA, TIPOSILLA
                            WHERE SILLA.IDPRESENTACION = {idPresentacion} AND TIPOSILLA.ID = SILLA.IDTIPOSILLA
                            ORDER BY SILLA.NUMSILLA;
               """)
        return cursor.fetchall()

    def modificarEstadoSilla(self, idSilla, idPresentacion, estado):
        cursor.execute(f"""
                    UPDATE SILLA 
	                    SET ESTADO = '{estado}' 
	                    WHERE IDPRESENTACION = {idPresentacion} AND NUMSILLA = {idSilla};
                """)
        conn.commit()

    def obtenerDatosSilla(self, idPresentacion, idSilla):
        cursor.execute(f"""
                            SELECT SILLA.NUMSILLA, TIPOSILLA.NOMBRE, PRESENTACION.FECHAINICIO, PRESENTACION.SALANUM,
                                    PELICULA.NOMBRE, MULTIPLEX.NOMBRE, MULTIPLEX.CIUDAD, TIPOSILLA.PRECIO, PRESENTACION.ID, TIPOSILLA.ID
                                FROM SILLA, PRESENTACION, PELICULA, MULTIPLEX, TIPOSILLA
                                WHERE SILLA.NUMSILLA = {idSilla} AND SILLA.IDPRESENTACION = {idPresentacion} AND PRESENTACION.ID = SILLA.IDPRESENTACION
                                    AND PELICULA.ID = PRESENTACION.IDPELICULA AND MULTIPLEX.ID = PRESENTACION.IDMULTIPLEX
                                    AND TIPOSILLA.ID = SILLA.IDTIPOSILLA;        
                        """)
        return cursor.fetchone()

    def asignarNumeroFacturaSilla(self, numFactura, idPresentacion, idSilla, valorVenta):
        cursor.execute(f"""
                        UPDATE SILLA 
                            SET NUMEROFACTURA = '{numFactura}', VALORVENTA = {valorVenta}
                            WHERE SILLA.IDPRESENTACION = {idPresentacion} AND SILLA.NUMSILLA = {idSilla};            
                        """)
        conn.commit()

    def obtenerSillasNumFactura(self, numFactura):
        cursor.execute(f""" 
                        SELECT SILLA.IDPRESENTACION, SILLA.NUMSILLA, SILLA.NUMEROFACTURA 
                            FROM SILLA
                            WHERE SILLA.NUMEROFACTURA = '{numFactura}';
                        """)
        return cursor.fetchall()

    def obtenerPrecioVentaSilla(self, idPresentacion, idSilla, numFactura):
        cursor.execute(f"""
                        SELECT SILLA.IDPRESENTACION, SILLA.NUMSILLA, SILLA.VALORVENTA
                            FROM SILLA
                            WHERE SILLA.IDPRESENTACION = {idPresentacion} AND SILLA.NUMSILLA = {idSilla}
                                AND SILLA.NUMEROFACTURA = '{numFactura}';         
                        """)
        return cursor.fetchone()

    def obtenerDatosTipoSilla(self, tipoSilla):
        cursor.execute(f"""
                            SELECT TIPOSILLA.ID, TIPOSILLA.NOMBRE, TIPOSILLA.PRECIO 
                                FROM TIPOSILLA
                                WHERE TIPOSILLA.ID = {tipoSilla}
                        """)
        return cursor.fetchone()

    def obtenerSillasVendidas(self):
        cursor.execute(f"""
                        SELECT SILLA.IDPRESENTACION, SILLA.NUMSILLA, SILLA.ESTADO, SILLA.NUMEROFACTURA, SILLA.VALORVENTA,
                                SILLA.IDTIPOSILLA
                            FROM SILLA
                            WHERE SILLA.NUMEROFACTURA IS NOT NULL;
                        """)
        return cursor.fetchall()