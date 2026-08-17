import logging

from . import empleado

logger = logging.getLogger(__name__)


class Empresa:
    def __init__(self, nombre: str, rif: str, direccion: str, empleados: list = None):
        self.__nombre = nombre
        self.__rif = rif
        self.__direccion = direccion
        self.__empleados = empleados if empleados is not None else []

    @property
    def _rif(self):
        return self.__rif

    @_rif.setter
    def _rif(self, value):
        self.__rif = value

    @property
    def _direccion(self):
        return self.__direccion

    @_direccion.setter
    def _direccion(self, value):
        self.__direccion = value

    @property
    def _empleados(self):
        return self.__empleados

    @_empleados.setter
    def _empleados(self, value):
        self.__empleados = value

    def agregar_empleado(self, empleado: empleado.Empleado):
        self.__empleados.append(empleado)

    def eliminar_empleado(self, empleado: empleado.Empleado):
        self.__empleados.remove(empleado)

    def calcular_nomina(self):
        return sum(empleado.salario_total() for empleado in self.__empleados)

    def __str__(self):
        empleados_str = "\n".join(str(empleado) for empleado in self.__empleados)
        return "\n".join(
            [
                f"Nombre: {self.__nombre}",
                f"RIF: {self.__rif}",
                f"Dirección: {self.__direccion}",
                f"Empleados:\n{empleados_str}",
            ]
        )

    def print_txt(self):
        try:
            with open("resources/nomina.txt", "w") as file:
                file.write(str(self))
        except FileNotFoundError as fe:
            logger.error("File not found: %s", fe)
