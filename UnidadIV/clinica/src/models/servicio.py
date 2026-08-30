import datetime


class Servicio:
    def __init__(
        self,
        fecha: datetime,
        nombre_mascota: str,
        nombre_cliente: str,
        costo_base: float,
        cod_servicio: int = None,
    ):
        self.__cod_servicio = cod_servicio
        self.__fecha = fecha
        self.__nombre_mascota = nombre_mascota
        self.__nombre_cliente = nombre_cliente
        self.__costo_base = costo_base

    @property
    def _cod_servicio(self):
        return self.__cod_servicio

    @_cod_servicio.setter
    def _cod_servicio(self, value):
        self.__cod_servicio = value

    @property
    def _fecha(self):
        return self.__fecha

    @_fecha.setter
    def _fecha(self, value):
        self.__fecha = value

    @property
    def _nombre_mascota(self):
        return self.__nombre_mascota

    @_nombre_mascota.setter
    def _nombre_mascota(self, value):
        self.__nombre_mascota = value

    @property
    def _nombre_cliente(self):
        return self.__nombre_cliente

    @_nombre_cliente.setter
    def _nombre_cliente(self, value):
        self.__nombre_cliente = value

    @property
    def _costo_base(self):
        return self.__costo_base

    @_costo_base.setter
    def _costo_base(self, value):
        self.__costo_base = value

    def costo_total(self):
        return self.__costo_base

    def __str__(self):
        return "\n".join(
            [
                f"Codigo de servicio: {self.__cod_servicio}",
                f"Fecha: {self.__fecha}",
                f"Nombre de la mascota: {self.__nombre_mascota}",
                f"Nombre del cliente: {self.__nombre_cliente}",
                f"Costo base: {self.__costo_base:.2f}",
                f"Costo total: {self.costo_total():.2f}",
                "".center(50, "*"),
            ]
        )
