class Usuario:

    def __init__(self, user="", nombre="", apellido="", password_master=""):
        self.__id         = ""
        self.__user       = user
        self.__nombre     = nombre
        self.__apellido   = apellido
        self.__password_master = password_master

    def setCredentials(self,user, password_master):
        self.__user            = user
        self.__password_master = password_master

    def getId(self): return self.__id

    def getUser(self):  return self.__user

    def getNombre(self):   return self.__nombre

    def getApellido(self):  return self.__apellido

    def getPassword_master(self):return self.__password_master
