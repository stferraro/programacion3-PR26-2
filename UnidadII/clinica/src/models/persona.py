class Persona:
    
    def __init__(self, nombre, apellido, cedula, telefono, correo):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__cedula = cedula
        self.__telefono = telefono
        self.__correo = correo

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
    def _correo(self):
        return self.__correo

    @_correo.setter
    def _correo(self, value):
        self.__correo = value
        
    
    def __str__(self):
        return "\n".join([
            f"Nombre: {self.__nombre}",
            f"Apellido: {self.__apellido}",
            f"Cedula: {self.__cedula}",
            f"Telefono: {self.__telefono}",
            f"Correo: {self.__correo}"
        ])

        