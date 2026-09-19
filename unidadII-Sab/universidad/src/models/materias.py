class Materias:
    
    def __init__(self, nombre, creditos, nota):
        self.__nombre = nombre
        self.__creditos = creditos
        self.__nota = nota

    @property
    def _nombre(self):
        return self.__nombre

    @_nombre.setter
    def _nombre(self, value):
        self.__nombre = value

    @property
    def _creditos(self):
        return self.__creditos

    @_creditos.setter
    def _creditos(self, value):
        self.__creditos = value

    @property
    def _nota(self):
        return self.__nota

    @_nota.setter
    def _nota(self, value):
        self.__nota = value
        
    def get_valor(self):
        return self._creditos * self._nota
        
    def __str__(self):
        return f"\n{self._nombre}\n{self._creditos}\n{self._nota}"
