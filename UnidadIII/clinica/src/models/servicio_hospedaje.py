from . import servicio


class ServicioHospedaje(servicio.Servicio):
    ESTANDARD = 1
    PREMIUM = 2

    def __init__(
        self,
        fecha: str,
        nombre_mascota: str,
        nombre_cliente: str,
        costo_base: float,
        dias_estadia: int,
        tipo_habitacion: int,
    ):
        super().__init__(fecha, nombre_mascota, nombre_cliente, costo_base)
        self.__dias_estadia = dias_estadia
        self.__tipo_habitacion = tipo_habitacion

    @property
    def _dias_estadia(self):
        return self.__dias_estadia

    @_dias_estadia.setter
    def _dias_estadia(self, value):
        self.__dias_estadia = value

    @property
    def _tipo_habitacion(self):
        return self.__tipo_habitacion

    @_tipo_habitacion.setter
    def _tipo_habitacion(self, value):
        self.__tipo_habitacion = value

    def costo_total(self):
        if self.__tipo_habitacion == 1:  # Estándar
            return self._costo_base * self.__dias_estadia  # sin recargo por hospedaje
        elif self.__tipo_habitacion == 2:  # Premium
            return self._costo_base * self.__dias_estadia * 1.15  # 15% de recargo por hospedaje

    def __str__(self):
        return "\n".join(
            [
                super().__str__(),
                f"Días de estadía: {self.__dias_estadia}",
                f"Tipo de habitación: {self.__tipo_habitacion}",
            ]
        )
