class Servicio:
    
    def __init__(self, codigo: str, fecha: date, nombre_mascota: str, nombre_dueño: str, costo_base: float):
        self.__codigo = codigo
        self.__fecha = fecha
        self.__nombre_mascota = nombre_mascota
        self.__nombre_dueño = nombre_dueño
        self.__costo_base = costo_base

    @property
    def _codigo(self):
        return self.__codigo

    @_codigo.setter
    def _codigo(self, value):
        self.__codigo = value

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
    def _nombre_dueño(self):
        return self.__nombre_dueño

    @_nombre_dueño.setter
    def _nombre_dueño(self, value):
        self.__nombre_dueño = value

    @property
    def _costo_base(self):
        return self.__costo_base

    @_costo_base.setter
    def _costo_base(self, value):
        self.__costo_base = value
        
    def get_costo_total(self):
        return self._costo_base
    
    def __str__(self):
        fecha = self._fecha.strftime("%d/%m/%Y")
        return "\n".join([
            f"Servicio: {self._codigo}",
            f"Fecha: {fecha}",
            f"Nombre mascota: {self._nombre_mascota}",
            f"Nombre dueño: {self._nombre_dueño}",
            f"Costo base: {self._costo_base}"
        ])
    
