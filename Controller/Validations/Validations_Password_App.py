from tabulate import tabulate
from Model.PasswordApp import PasswordApp
from typing import List


class Validations_Password_App:

    def __init__(self, objDao):
        self.__objDao_PasswordApp = objDao

    def getDatosEntrada(self):
        try:
            nombre_app = input("Ingrese el nombre: ")
            url = input("Ingrese el url: ")
            usuario = input("Ingrese el nombre de usuario: ")
            password = input("Ingrese el password: ")
            descripcion = input("Ingrese descripcion: ")
            return PasswordApp(nombre_app, url, usuario, password, descripcion)

        except Exception as Err:
            print("Error en getDatosEntrada", Err)

    def existen_registros_PasswordApp(self, _id=0):
        try:
            cantidad_registros = self.__objDao_PasswordApp.listar_passwords(_id)
            if len(cantidad_registros) > 0:
                return True
            return False

        except Exception as Err:
            print("Error en existen_registros_PasswordApp", Err)

    def set_headers(self, _headers:List[str] = None):
        try:
            if _headers != None:
                return _headers
            return ["ID", "NOMBRE", "URL", "USUARIO", "PASSWORD", "DESCRIPCION"]
        except Exception as Err:
            print("Error en set_headers", Err)

    def validar_id(self, _id=0, _strOperacion="buscar"):
        try:
            id = _id
            if id == 0:
                id = input(f"\nIngrese id a {_strOperacion} : ")

            if self.existen_registros_PasswordApp(id):
                return id
            else:
                return 0

        except Exception as Err:
            print("Error en validar_id", Err)

    def listar(self, _registros, headers):
        try:
            tabla_registros = []
            registros_obtenidos = _registros
            cnt_headers = len(headers)

            if cnt_headers != 0:
                registros_obtenidos = self.get_registros_campos_especificos(_registros, cnt_headers)

            for fila_registro in registros_obtenidos:
                tabla_registros.append(fila_registro)

            tabla_format = tabulate(tabla_registros, headers, tablefmt="fancy_grid")

            print()
            print(tabla_format)

        except Exception as Err:
            print("Error en listar", Err)

    def get_registros_campos_especificos(self, registros, cnt_campos):
        try:
            registros_campos_espeficos = []
            for fila_registro in registros:
                campos = []
                for campo in range(0, cnt_campos):
                    campos.append(fila_registro[campo])
                registros_campos_espeficos.append(tuple(campos))
            return tuple(registros_campos_espeficos)

        except Exception as Err:
            print("Error en get_registros_campos_especificos", Err)