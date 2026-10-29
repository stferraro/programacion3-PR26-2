from .vehiculo import Vehiculo
from .cliente import Cliente

class Camion(Vehiculo):
    def __init__(self, cliente: Cliente, marca: str, modelo: str, año: int, precio: float, color: str, capacidad_carga: float, num_ejes: int = 2):
        super().__init__(cliente, marca, modelo, año, precio, color)
        self.__capacidad_carga = capacidad_carga
        self.__num_ejes = num_ejes

    @property
    def _capacidad_carga(self):
        return self.__capacidad_carga

    @_capacidad_carga.setter
    def _capacidad_carga(self, value):
        self.__capacidad_carga = value

    @property
    def _num_ejes(self):
        return self.__num_ejes

    @_num_ejes.setter
    def _num_ejes(self, value):
        self.__num_ejes = value
        
    def get_subtotal(self):
        return super().get_subtotal() + (self.__capacidad_carga * 150) + 300
    
    def __str__(self):
        return "\n".join([
            super().__str__(),
            f"Capacidad de carga: {self.__capacidad_carga} toneladas",
            f"Número de ejes: {self.__num_ejes}"
        ])