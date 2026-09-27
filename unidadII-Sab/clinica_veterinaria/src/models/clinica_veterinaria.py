class ClinicaVeterinaria:
    
    def __init__(self, nombre: str, rif: str, servicios: list):
        self.__nombre = nombre
        self.__rif = rif
        self.__servicios = servicios

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

    def add_servicio(self, servicio: Servicio):
        self.__servicios.append(servicio)

    def get_total_ganancia(self):
        '''
        metodo que calcula el total de ganancia de los servicios
        de la clinica veterinaria
        '''
        return sum([s.get_costo_total() for s in self.__servicios])
    
    def __str__(self):
        datos_clinica = "\n".join([
            f"Nombre: {self._nombre}",
            f"RIF: {self._rif}",
        ])
        servicios = "\n".join([s.__str__() for s in self.__servicios])
        "\n".join([
            datos_clinica,
            servicios
        ])
        ganancia = self.get_total_ganancia()
        return "\n".join([
            datos_clinica,
            servicios,
            f"Ganancia Total: {ganancia:.2f} $$"
        ])