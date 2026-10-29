from .vehiculo import Vehiculo
from .cliente import Cliente

class Carro(Vehiculo):
    TRANSMISIONES = ("Manual", "Automática")

    def __init__(self, cliente: Cliente, marca: str, modelo: str, año: int, precio: float, color: str, num_puertas: int, tipo_transmision: str):
        super().__init__(cliente, marca, modelo, año, precio, color)
        self._tipo_transmision = tipo_transmision
        self.__num_puertas = num_puertas

    @property
    def _tipo_transmision(self):
        return self.__tipo_transmision

    @_tipo_transmision.setter
    def _tipo_transmision(self, value):
        if value not in Carro.TRANSMISIONES:
            raise ValueError("La transmisión debe ser 'Manual' o 'Automática'")
        self.__tipo_transmision = value

    @property
    def _num_puertas(self):
        return self.__num_puertas

    @_num_puertas.setter
    def _num_puertas(self, value):
        self.__num_puertas = value

    def get_descuento(self):
        descuento = super().get_descuento()
        if self._tipo_transmision == "Manual":
            return descuento + 0.05
        elif self._tipo_transmision == "Automática":
            return descuento + 0.08
        return descuento

    def __str__(self):
        return "\n".join([
            super().__str__(),
            f"Número de puertas: {self.__num_puertas}",
            f"Tipo de transmisión: {self.__tipo_transmision}"
        ])
