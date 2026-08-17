from . import empleado


class EmpleadoPlanta(empleado.Empleado):
    GERENTE = 1
    SUPERVISOR1 = 2
    SUPERVISOR2 = 3

    def __init__(self, nombre: str, apellido: str, cedula: str, salario: float, antiguedad: int, cargo: int):
        super().__init__(nombre, apellido, cedula, salario)
        self.__antiguedad = antiguedad
        self.__cargo = cargo

    @property
    def _antiguedad(self):
        return self.__antiguedad

    @_antiguedad.setter
    def _antiguedad(self, value):
        self.__antiguedad = value

    @property
    def _cargo(self):
        return self.__cargo

    @_cargo.setter
    def _cargo(self, value):
        self.__cargo = value

    def salario_total(self):
        res = super().salario_total()
        if self.__cargo == self.GERENTE:
            return self._salario * 1.2
        elif self.__cargo == self.SUPERVISOR1:
            return self._salario * 1.15
        elif self.__cargo == self.SUPERVISOR2:
            return self._salario * 1.10
        return res

    def __str__(self):
        return "\n".join(
            [
                super().__str__(),
                f"Antigüedad: {self.__antiguedad}",
                f"Cargo: {self.__cargo}",
                "*".center(30, "*"),
                f"Salario Total: {self.salario_total(): .2f}",
            ]
        )
