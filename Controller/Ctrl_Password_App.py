from Dao.Dao_Password_App import DaoPasswordApp
from Controller.Validations.Validations_Password_App import Validations_Password_App
import os
from typing import List

class Ctrl_Password_App:

    def __init__(self):
        self.__objDao_PasswordApp = DaoPasswordApp()
        self.__objValidations_Password_App = Validations_Password_App(self.__objDao_PasswordApp)


    def agregar_Usuario(self):
        self.__objDao_PasswordApp.agregar_password(self.__objValidations_Password_App.getDatosEntrada())


    def listar_passwords(self, _id:int = 0, _headers:List[str] = None):
        registros = self.__objDao_PasswordApp.listar_passwords(id = _id)
        registros_presentes = self.__objValidations_Password_App.existen_registros_PasswordApp(_id = _id)

        if registros_presentes:
            set_headers = self.__objValidations_Password_App.set_headers(_headers = _headers)
            self.__objValidations_Password_App.listar(_registros=registros, headers=set_headers)
        else:
            print("\n","[x] No existen registros para realizar estar operacion [x]")
            return False
        return True


    def view_passwords_id(self ,_id : int = 0, _strOperacion : str ="buscar"):
        existen_registros = self.__objValidations_Password_App.existen_registros_PasswordApp(_id = _id)

        if existen_registros:

            self.listar_passwords(_headers=["ID", "NOMBRE"])

            id_encontrado = self.__objValidations_Password_App.validar_id(_id = _id, _strOperacion = _strOperacion)

            while id_encontrado == 0:
                os.system("cls")
                print("\n", "[x] ID No encontrado , intente nuevamente [x]")
                self.listar_passwords(_headers=["ID", "NOMBRE"])
                id_encontrado = self.__objValidations_Password_App.validar_id(_id = _id,  _strOperacion = _strOperacion)

            self.listar_passwords(_id = id_encontrado)
            return id_encontrado

        else:
            print("[x] No existen registros para ejecutar esta operacion ")


    def eliminar_passwords_id(self):
        existen_registros = self.listar_passwords(_headers=["ID", "NOMBRE"])
        if existen_registros:
            id = input("\nIngrese id a eliminar : ")
            filas_afectadas = self.__objDao_PasswordApp.eliminar_password_id(id)
            if filas_afectadas == 1:
                print("\nID", id, "eliminado")
            else:
                os.system("cls")
                print("\n","[x] ID Incorrecto, intente nuevamente [x]")
                self.eliminar_passwords_id()


    def editar_passwords_id(self):
        id = int(self.view_passwords_id(_strOperacion = "editar"))
        objDatosPassword = self.__objValidations_Password_App.getDatosEntrada()
        objDatosPassword.setId(id)
        is_password_editado = self.__objDao_PasswordApp.editar_datos_info(objDatosPassword)
        if is_password_editado == 1:
            print("\nModificacion Realizada")
        else:
            print("Ocurrio un error en editar_passwords_id")