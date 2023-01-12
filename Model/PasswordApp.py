class PasswordApp:

    def __init__(self, nombre_app, url, usuario, password, descripcion):
        self.__id          = ""
        self.__nombre_app  = nombre_app
        self.__url         = url
        self.__usuario     = usuario
        self.__password    = password
        self.__descripcion = descripcion

    def getId(self): return self.__id

    def setId(self, id): self.__id = id

    def getNombreApp(self): return self.__nombre_app

    def getUrl(self): return self.__url

    def getUsuario(self): return self.__usuario

    def getPassword(self): return self.__password

    def getDescription(self): return self.__descripcion