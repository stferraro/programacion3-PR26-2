class Empleado:
    def __init__(self, nombre: str, apellido: str, cedula: str, salario: float):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__cedula = cedula
        self.__salario = salario

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
    def _salario(self):
        return self.__salario

    @_salario.setter
    def _salario(self, value):
        self.__salario = value

    def salario_total(self):
        return self.__salario

    def __str__(self):
        return "\n".join(
            [
                f"Nombre: {self.__nombre}",
                f"Apellido: {self.__apellido}",
                f"Cédula: {self.__cedula}",
                f"Salario: {self.__salario}",
            ]
        )
