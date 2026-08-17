import logging

from . import servicio

logger = logging.getLogger(__name__)


class Clinica:
    def __init__(self, nombre: str, rif: str, servicios: list[servicio.Servicio] = None):
        self.__nombre = nombre
        self.__rif = rif
        self.__servicios = servicios if servicios is not None else []

    @property
    def _nombre(self):
        return self.__nombre

    @_nombre.setter
    def _nombre(self, value):
        self.__nombre = value

    @property
    def _rif(self):
        return self.__rif

    @_rif.setter
    def _rif(self, value):
        self.__rif = value

    @property
    def _servicios(self):
        return self.__servicios

    @_servicios.setter
    def _servicios(self, value):
        self.__servicios = value

    def agregar_servicio(self, servicio: servicio.Servicio):
        self.__servicios.append(servicio)

    def eliminar_servicio(self, cod_servicio: int):
        self.__servicios = [s for s in self.__servicios if s._cod_servicio != cod_servicio]

    def total_facturado(self):
        return sum(servicio.costo_total() for servicio in self.__servicios)

    def __str__(self):
        servicios_str = "\n".join(str(servicio) for servicio in self.__servicios)
        return "\n".join(
            [
                f"Nombre de la clínica: {self.__nombre}",
                f"RIF: {self.__rif}",
                "".center(50, "*"),
                f"Servicios:\n{servicios_str}" if servicios_str else "Servicios: Ninguno",
                "".center(50, "*"),
                f"Total facturado: {self.total_facturado():.2f}",
            ]
        )

    def print_txt(self):
        try:
            with open("resources/facturacion.txt", "w") as file:
                file.write(str(self))
        except FileNotFoundError as fe:
            logger.error(f"Error al escribir en el archivo: {fe}")
