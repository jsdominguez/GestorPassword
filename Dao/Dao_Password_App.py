from Dao.Conexion import Conexion

class DaoPasswordApp(Conexion):

    def __init__(self):
        super().__init__()

    def agregar_password(self, objPasswordApp):
        try:

            myConexion = super().conectar()
            myCursor = myConexion.cursor()

            query = '''insert into password_app(nombre_app, url, usuario, password, descripcion) 
                        values(%s,%s,%s,%s,%s)'''

            datos = (objPasswordApp.getNombreApp(),
                     objPasswordApp.getUrl(),
                     objPasswordApp.getUsuario(),
                     objPasswordApp.getPassword(),
                     objPasswordApp.getDescription())

            myCursor.execute(query, datos)
            myConexion.commit()
            super().desconectar()

            return True

        except Exception as Err:
            print("Error en Dao:agregar_password", Err)

    def listar_passwords(self,id=0):
        try:
            myConexion = super().conectar()
            myCursor = myConexion.cursor()
            query = "SELECT * FROM password_app"
            datos = []
            if id != 0:
                query += " WHERE id=%s"
                datos.append(id)

            myCursor.execute(query,tuple(datos))
            resultado = myCursor.fetchall()

            super().desconectar()

            return resultado

        except Exception as Err:
            print("Error en Dao : listar_passwords", Err)

    def eliminar_password_id(self,id):
        try:

            myConexion = super().conectar()
            myCursor = myConexion.cursor()

            query = '''DELETE FROM password_app WHERE id=%s'''

            myCursor.execute(query, (id,))
            cantidad_afectados = myCursor.rowcount
            myConexion.commit()
            super().desconectar()

            return cantidad_afectados

        except Exception as Err:
            print("Error en Dao : eliminar_password_id", Err)

    def editar_datos_info(self, objDatosPassword):
        try:

            myConexion = super().conectar()
            myCursor = myConexion.cursor()

            query = '''UPDATE password_app 
                      SET nombre_app = %s, url = %s, usuario = %s, password = %s, descripcion = %s
                      WHERE id = %s'''

            datos = (objDatosPassword.getNombreApp(),
                     objDatosPassword.getUrl(),
                     objDatosPassword.getUsuario(),
                     objDatosPassword.getPassword(),
                     objDatosPassword.getDescription(),
                     objDatosPassword.getId())

            myCursor.execute(query, datos)
            cantidad_afectados = myCursor.rowcount
            myConexion.commit()
            super().desconectar()

            return cantidad_afectados

        except Exception as Err:
            print("Error en Dao: editar_datos_info", Err)
