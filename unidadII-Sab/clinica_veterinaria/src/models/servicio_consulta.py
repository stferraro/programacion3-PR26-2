from .servicio import Servicio
from datetime import date

class ServicioConsulta(Servicio):
    
    def __init__(self,codigo: str, fecha: date, nombre_mascota: str, nombre_dueño: str, costo_base: float, nombre_veterinario: str, especialidad: str):
        super().__init__(codigo, date.today(), nombre_mascota, nombre_dueño, costo_base)
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
        
    def get_costo_total(self):
        '''
        metodo que calcula el costo total de un servicio consulta
        si la especialidad es cirugia, se aplica un 40% de descuento 
        y se multiplica por el costo base, 
        si la especialidad es dermatología, se aplica un 25% de descuento 
        y se multiplica por el costo base, 
        si no retorna el costo base
        '''
        if self.__especialidad.lower() == "Cirugia":
            return self._costo_base * 0.4 + self._costo_base
        elif self.__especialidad.lower() == "dermatología":
            return self._costo_base * 0.25 + self._costo_base
        return super().get_costo_total()
    
    def __str__(self):
        return "\n".join([
            super().__str__(),
            f"Nombre veterinario: {self._nombre_veterinario}",
            f"Especialidad: {self._especialidad}"
        ])