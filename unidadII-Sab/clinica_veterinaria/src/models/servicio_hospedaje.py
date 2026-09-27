from .servicio import Servicio
from datetime import date

class ServicioHospedaje(Servicio):
    
    def __init__(self, codigo: str, fecha: date, nombre_mascota: str, nombre_dueño: str, costo_base: float, tipo_habitacion: str, dias_estadia: int):
        super().__init__(codigo, date.today(), nombre_mascota, nombre_dueño, costo_base)
        self.__tipo_habitacion = tipo_habitacion
        self.__dias_estadia = dias_estadia

    @property
    def _tipo_habitacion(self):
        return self.__tipo_habitacion

    @_tipo_habitacion.setter
    def _tipo_habitacion(self, value):
        self.__tipo_habitacion = value

    @property
    def _dias_estadia(self):
        return self.__dias_estadia

    @_dias_estadia.setter
    def _dias_estadia(self, value):
        self.__dias_estadia = value

        
    def get_costo_total(self):
        '''
        metodo que calcula el costo total de un servicio hospedaje
        si el tipo de habitacion es premium, se aplica un 20% de descuento 
        y se multiplica por el numero de dias de estadia, 
        si no retorna el costo base multiplicado por el numero de dias de estadia
        '''
        if self.__tipo_habitacion.lower() == "premiun":
            return self._costo_base * 0.2 + self._costo_base * self.__dias_estadia
        return super().get_costo_total() * self.__dias_estadia
    
    def __str__(self):
        return "\n".join([
            super().__str__(),
            f"Tipo habitacion: {self._tipo_habitacion}",
            f"Dias estadia: {self._dias_estadia}"
        ])