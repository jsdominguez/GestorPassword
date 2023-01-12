import os
import time
from Dao.Dao_Usuario import DaoUsuario
from Model.Usuario import Usuario
from Controller.Ctrl_Password_App import Ctrl_Password_App

class Ctrl_Usuario:
    
    def __init__(self):
        self.__objDao_Usuario = DaoUsuario()

    def usuario_existente(self):
        registros = self.__objDao_Usuario.usuario_existente()
        return self.__exists_registre(registros)

    def set_credentials(self):
        usuario          = input("\nIngrese su usuario : ")
        password_maestra = input("Ingrese su password maestra : ")
        objUsuario = Usuario()
        objUsuario.setCredentials(usuario,password_maestra)
        return objUsuario

    def validar_password(self,objUsuario):
        registro = self.__objDao_Usuario.validar_password_maestra(objUsuario)
        if self.__exists_registre(registro):
            return registro
        else:
            return None

    def is_ok_password(self, registro : str = None):
        if registro == None:
            os.system("cls")
            print("Password o Usuario Incorrecto")
            return False
        else:
            os.system("cls")
            print("\nBienvenido", registro[0][3], registro[0][4])
            return True

    def agregar_usuario(self):
        print("Bienvenido , registre su informacion")
        nombre     = input("Ingrese su nombre: ")
        apellido   = input("Ingrese su apellido: ")
        password   = input("Ingrese su password maestra: ")
        usuario    = input("Ingrese su usuario: ")
        objUsuario = Usuario(usuario, nombre, apellido, password)
        self.__objDao_Usuario.registrar_usuario(objUsuario)
        os.system("cls")
        print("\nBienvenido",nombre,"\n")

    def choose_operation(self):
        try:
            return int(input("\nIngrese una opcion: "))
        except Exception:
            return 0

    def validar_opcion(self, opcion:int = 0):
        if opcion >= 1 and opcion <= 6:
            return True
        return False

    def ejecutar_operacion_seleccionada(self, opcion:int = 0):
        objCtrl_Password_App = Ctrl_Password_App()
        match opcion:
            case 1 :
                objCtrl_Password_App.agregar_Usuario()
            case 2 :
                objCtrl_Password_App.listar_passwords()
            case 3:
                objCtrl_Password_App.view_passwords_id()
            case 4:
                objCtrl_Password_App.editar_passwords_id()
            case 5:
                objCtrl_Password_App.eliminar_passwords_id()
            case 6:
                return True
        time.sleep(6)
        os.system("cls")
        return False

    def __exists_registre(self, registros : int = 0):
        if len(registros) > 0:
            return True
        return False

    def showMenu(self):
        print("\nSeleccione una de las siguientes opciones:\n")
        print("\t1-Añadir contraseña")
        print("\t2-Ver todas las contraseñas")
        print("\t3-Visualizar una contraseña")
        print("\t4-Modificar contraseña")
        print("\t5-Eliminar Contraseña")
        print("\t6-Salir")