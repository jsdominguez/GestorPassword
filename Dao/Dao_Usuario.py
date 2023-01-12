from Dao.Conexion import Conexion

class DaoUsuario(Conexion):

    def __init__(self):
        super().__init__()

    def usuario_existente(self):
        try:
            myConexion = super().conectar()
            myCursor = myConexion.cursor()

            query = "SELECT * FROM usuarios"
            myCursor.execute(query)
            resultado = myCursor.fetchall()

            super().desconectar()

            return resultado

        except Exception as Err:
            print("Error en Dao_usuario_existente", Err)

    def listar_usuario_id(self, id):
        try:

            myConexion = super().conectar()
            myCursor = myConexion.cursor()

            query = "SELECT * FROM usuarios WHERE Id=%s"
            myCursor.execute(query, (id,))
            resultado = myCursor.fetchall()

            super().desconectar()

            return resultado

        except Exception as Err:
            print("Error en Dao_listar_usuario_id", Err)

    def registrar_usuario(self, objUsuario):
        try:

            myConexion = super().conectar()
            myCursor = myConexion.cursor()

            query = '''insert into usuarios(User, Nombre, Apellido, Password_Master) 
                        values(%s,%s,%s,%s)'''

            datos = (objUsuario.getUser(),
                     objUsuario.getNombre(),
                     objUsuario.getApellido(),
                     objUsuario.getPassword_master())

            myCursor.execute(query, datos)
            myConexion.commit()
            super().desconectar()

            return True

        except Exception as Err:
            print("Error en Dao_registrar_usuario", Err)

    def validar_password_maestra(self,objUsuario):
        try:

            myConexion = super().conectar()
            myCursor = myConexion.cursor()

            query = "SELECT * FROM usuarios WHERE User=%s and Password_Master=%s"
            datos = (objUsuario.getUser(),
                     objUsuario.getPassword_master())

            myCursor.execute(query, datos)
            resultado = myCursor.fetchall()
            super().desconectar()

            return resultado

        except Exception as Err:
            print("Error en Dao_listar_usuario_id", Err)