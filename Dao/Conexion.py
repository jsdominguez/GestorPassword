import mysql.connector as mysql

class Conexion:

    def __init__(self):
        self.__host = "localhost"
        self.__user = "root"
        self.__password = ""
        self.__database = "bd_app_passwords"
        self.__conexion = None

    def conectar(self):

        try:

            self.__conexion = mysql.connect(
                host= self.__host,
                user= self.__user,
                password= self.__password,
                database= self.__database
            )

            return self.__conexion

        except Exception:
            print("Error en la conexion", Exception)


    def desconectar(self):
        try:
            self.__conexion.close()

        except Exception as Err:
            print("Error al cerrar la conexion",Err)
