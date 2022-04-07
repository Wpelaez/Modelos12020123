import psycopg2

DB_HOST = "localhost"
DB_NAME = "cineJungla"
DB_USER = "postgres"
DB_PASS = "123"
conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
cursor = conn.cursor()

class empleado():

    def __init__(self):
        pass

    def obtenerDatosEmpleados(self, idMultiplex):
        cursor.execute(f"""
                        SELECT EMPLEADO.ID, EMPLEADO.NOMBRE, EMPLEADO.APELLIDO, EMPLEADO.SALARIO, EMPLEADO.TELEFONO,
                                EMPLEADO.CEDULA, EMPLEADO.FECHAINICIOCONTRATO, ROLESEMPLEADO.NOMBREROL, MULTIPLEX.NOMBRE
                            FROM EMPLEADO, ROLESEMPLEADO, MULTIPLEX
                            WHERE EMPLEADO.IDMULTIPLEX = {idMultiplex} AND ROLESEMPLEADO.ID = EMPLEADO.IDROL
                                AND MULTIPLEX.ID = EMPLEADO.IDMULTIPLEX;                        
                    """)
        return cursor.fetchall()