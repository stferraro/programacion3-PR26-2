from .vehiculo import Vehiculo
from .cliente import Cliente

class Moto(Vehiculo):
    
    def __init__(self, cliente: Cliente, marca: str, modelo: str, año: int, precio: float, color: str, cilindrada: int, tipo_motor: str):
        super().__init__(cliente, marca, modelo, año, precio, color)
        self.__cilindrada = cilindrada
        self.__tipo_motor = tipo_motor

    @property
    def _cilindrada(self):
        return self.__cilindrada

    @_cilindrada.setter
    def _cilindrada(self, value):
        self.__cilindrada = value

    @property
    def _tipo_motor(self):
        return self.__tipo_motor

    @_tipo_motor.setter
    def _tipo_motor(self, value):
        self.__tipo_motor = value
        
    def get_subtotal(self):
        if self.__cilindrada > 250:
            return super().get_subtotal() + (self.__cilindrada * 0.50) + 150
        return super().get_subtotal() + (self.__cilindrada * 0.50)

        
    