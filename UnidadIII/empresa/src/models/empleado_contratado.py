from . import empleado


class EmpleadoContratado(empleado.Empleado):
    def __init__(
        self, nombre: str, apellido: str, cedula: str, salario: float, proyecto_asignado: str, meses_contrato: int
    ):
        super().__init__(nombre, apellido, cedula, salario)
        self.__proyecto_asignado = proyecto_asignado
        self.__meses_contrato = meses_contrato

    @property
    def _proyecto_asignado(self):
        return self.__proyecto_asignado

    @_proyecto_asignado.setter
    def _proyecto_asignado(self, value):
        self.__proyecto_asignado = value

    @property
    def _meses_contrato(self):
        return self.__meses_contrato

    @_meses_contrato.setter
    def _meses_contrato(self, value):
        self.__meses_contrato = value

    def salario_total(self):
        base = super().salario_total()
        return base - (base * 0.1)

    def __str__(self):
        return "\n".join(
            [
                super().__str__(),
                f"Proyecto Asignado: {self.__proyecto_asignado}",
                f"Meses de Contrato: {self.__meses_contrato}",
                "*".center(30, "*"),
                f"Salario Total: {self.salario_total(): .2f}",
            ]
        )
