class Cliente:
    def __init__(self, nombre: str, apellido: str, cedula: str, telefono: str, edad: int, genero: str):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__cedula = cedula
        self.__telefono = telefono
        self.__edad = edad
        self.__genero = genero

    @property
    def _nombre(self):
        return self.__nombre

    @_nombre.setter
    def _nombre(self, value):
        self.__nombre = value

    @property
    def _apellido(self):
        return self.__apellido

    @_apellido.setter
    def _apellido(self, value):
        self.__apellido = value

    @property
    def _cedula(self):
        return self.__cedula

    @_cedula.setter
    def _cedula(self, value):
        self.__cedula = value

    @property
    def _telefono(self):
        return self.__telefono

    @_telefono.setter
    def _telefono(self, value):
        self.__telefono = value
        
    @property
    def _edad(self):
        return self.__edad
    
    @_edad.setter
    def _edad(self, value):
        self.__edad = value
        
    @property
    def _genero(self):
        return self.__genero
    
    @_genero.setter
    def _genero(self, value):
        self.__genero = value   
        
    def __str__(self):
        return "\n".join([
            f"Nombre: {self.__nombre}",
            f"Apellido: {self.__apellido}",
            f"Cédula: {self.__cedula}",
            f"Teléfono: {self.__telefono}",
            f"Edad: {self.__edad}",
            f"Género: {self.__genero}"
        ])
