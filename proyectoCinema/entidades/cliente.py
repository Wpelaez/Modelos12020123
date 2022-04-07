import psycopg2

DB_HOST = "localhost"
DB_NAME = "cineJungla"
DB_USER = "postgres"
DB_PASS = "123"
conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
cursor = conn.cursor()

class cliente():

    def __init__(self):
        pass

    def buscarClientePorNick(self, nickname):
        cursor.execute(f"""
                        SELECT CLIENTE.ID, CLIENTE.USERNAME, CLIENTE.PUNTOS
                            FROM CLIENTE 
                            WHERE LOWER(CLIENTE.USERNAME) = LOWER('{nickname}');
                        """)
        return cursor.fetchone()

    def crearCliente(self, ID, NOMBRE, APELLIDO, TELEFONO, CEDULA, USERNAME):
        cursor.execute(f"""
                        INSERT INTO CLIENTE 
	                        VALUES ({ID}, '{NOMBRE}', '{APELLIDO}', '{TELEFONO}', {CEDULA}, '{USERNAME}', 0);
                        """)
        conn.commit()

    def nuevoIdCliente(self):
        cursor.execute("""
                        SELECT MAX(cliente.id)
                            FROM CLIENTE;
                        """)
        return cursor.fetchone()

    def obtenerDatosClientePorID(self, idCliente):
        cursor.execute(f"""
            SELECT CLIENTE.ID, CLIENTE.NOMBRE, CLIENTE.APELLIDO, CLIENTE.TELEFONO, CLIENTE.CEDULA, CLIENTE.USERNAME, CLIENTE.PUNTOS
                FROM CLIENTE 
                WHERE CLIENTE.ID = '{idCliente}'                    
        """)
        return cursor.fetchone()

    def modificarPuntosCliente(self, puntos, idCliente):
        cursor.execute(f"""
                        UPDATE CLIENTE 
                            SET PUNTOS = {puntos}
                            WHERE CLIENTE.ID = {idCliente};
                    """)
        conn.commit()