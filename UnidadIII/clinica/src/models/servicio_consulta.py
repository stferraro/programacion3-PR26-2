from . import servicio


class ServicioConsulta(servicio.Servicio):
    CIRUGIA = 1
    DERMATOLOGIA = 2
    CONSULTA_GENERAL = 3

    def __init__(
        self,
        fecha: str,
        nombre_mascota: str,
        nombre_cliente: str,
        costo_base: float,
        nombre_veterinario: str,
        especialidad: str,
    ):
        super().__init__(fecha, nombre_mascota, nombre_cliente, costo_base)
        self.__nombre_veterinario = nombre_veterinario
        self.__especialidad = especialidad

    @property
    def _nombre_veterinario(self):
        return self.__nombre_veterinario

    @_nombre_veterinario.setter
    def _nombre_veterinario(self, value):
        self.__nombre_veterinario = value

    @property
    def _especialidad(self):
        return self.__especialidad

    @_especialidad.setter
    def _especialidad(self, value):
        self.__especialidad = value

    def costo_total(self):
        if self.__especialidad == 1:  # Cirugía
            return self._costo_base * 1.40  # 20% de rec
        elif self.__especialidad == 2:  # Dermatología
            return self._costo_base * 1.25  # 15% de recargo por consulta
        elif self.__especialidad == 3:  # Consulta general
            return self._costo_base

    def __str__(self):
        return "\n".join(
            [
                super().__str__(),
                f"Nombre del veterinario: {self.__nombre_veterinario}",
                f"Especialidad: {self.__especialidad}",
            ]
        )
