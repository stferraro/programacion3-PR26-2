from .cliente import Cliente
from .vehiculo import Vehiculo

class Camioneta(Vehiculo):
    
    def __init__(self, cliente: Cliente, marca: str, modelo: str, año: int, precio: float, color: str, tipo_traccion: str, capacidad_pasajeros: int):
        super().__init__(cliente, marca, modelo, año, precio, color)
        self.__tipo_traccion = tipo_traccion
        self.__capacidad_pasajeros = capacidad_pasajeros

    @property
    def _tipo_traccion(self):
        return self.__tipo_traccion

    @_tipo_traccion.setter
    def _tipo_traccion(self, value):
        self.__tipo_traccion = value

    @property
    def _capacidad_pasajeros(self):
        return self.__capacidad_pasajeros

    @_capacidad_pasajeros.setter
    def _capacidad_pasajeros(self, value):
        self.__capacidad_pasajeros = value
        
    def get_subtotal(self):
        subtotal = super().get_subtotal()
        if self.__tipo_traccion.lower() == "4x4":
            subtotal *= 1.12
        if self.__capacidad_pasajeros > 5:
            subtotal += 400
        return subtotal
        
    def __str__(self):
        return "\n".join([
            super().__str__(),
            f"Tipo de tracción: {self.__tipo_traccion}",
            f"Capacidad de pasajeros: {self.__capacidad_pasajeros}"
        ])

        
    