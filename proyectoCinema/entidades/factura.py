import psycopg2

DB_HOST = "localhost"
DB_NAME = "cineJungla"
DB_USER = "postgres"
DB_PASS = "123"
conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
cursor = conn.cursor()

class factura():

    def __init__(self):
        pass

    def buscarNumeroFactura(self, numFactura):
        cursor.execute(f"""
                            SELECT FACTURA.NUMEROFACTURA
                                FROM FACTURA
                                WHERE FACTURA.NUMEROFACTURA = '{numFactura}';
                        """)
        return cursor.fetchone()

    def agregarFactura(self, numFactura, valor, idCliente, tipoValor, fecha):
        cursor.execute(f"""
                        INSERT INTO FACTURA 
                            VALUES ('{numFactura}', {valor}, {idCliente}, {tipoValor}, NULL, NULL, '{fecha}'); 
                        """)
        conn.commit()

    def obtenerDatosFactura(self, numFactura):
        cursor.execute(f"""
                        SELECT FACTURA.NUMEROFACTURA, FACTURA.VALOR, FACTURA.IDCLIENTE, FACTURA.IDTIPOVALOR, TIPOVALOR.NOMBRE,
                                FACTURA.CALIFICACIONSERVICIO, FACTURA.OPINIONSERVICIO, FACTURA.FECHA
                            FROM FACTURA, TIPOVALOR
                            WHERE FACTURA.NUMEROFACTURA = '{numFactura}' AND TIPOVALOR.ID = FACTURA.IDTIPOVALOR;        
                    """)
        return cursor.fetchone()

    def obtenerDatosFacturaPorIdCliente(self, idCliente):
        cursor.execute(f"""
                        SELECT FACTURA.NUMEROFACTURA, FACTURA.VALOR, FACTURA.IDCLIENTE, FACTURA.IDTIPOVALOR, TIPOVALOR.NOMBRE
                            FROM FACTURA, TIPOVALOR
                            WHERE FACTURA.IDCLIENTE = {idCliente} AND TIPOVALOR.ID = FACTURA.IDTIPOVALOR;        
                        """)
        return cursor.fetchall()

    def ingresarOpinionServicio(self, numFactura, opinonServicio, califacionServicio):
        cursor.execute(f"""
                        UPDATE FACTURA 
                            SET CALIFICACIONSERVICIO = {califacionServicio},
                                OPINIONSERVICIO = '{opinonServicio}'
                            WHERE FACTURA.NUMEROFACTURA = '{numFactura}';
                        """)
        conn.commit()

    def obtenerFacturasPorFecha(self, numeroMes, year):
        cursor.execute(f"""
                        SELECT FACTURA.NUMEROFACTURA, FACTURA.VALOR, FACTURA.IDCLIENTE, FACTURA.IDTIPOVALOR, TIPOVALOR.NOMBRE,
                                FACTURA.CALIFICACIONSERVICIO, FACTURA.OPINIONSERVICIO, FACTURA.FECHA
                            FROM FACTURA, TIPOVALOR
                            WHERE EXTRACT(MONTH FROM FACTURA.FECHA) = {numeroMes} AND EXTRACT(YEAR FROM FACTURA.FECHA) = {year}
                                AND TIPOVALOR.ID = FACTURA.IDTIPOVALOR;
                    """)
        return cursor.fetchall()