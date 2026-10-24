from .cliente import Cliente

class Vehiculo:
    def __init__(self, cliente: Cliente, marca: str, modelo: str, año: int, precio: float, color: str):
        self.__cliente = cliente
        self.__marca = marca
        self.__modelo = modelo
        self.__año = año
        self.__precio = precio
        self.__color = color
        
    @property
    def _cliente(self):
        return self.__cliente
    
    @_cliente.setter
    def _cliente(self, value):
        self.__cliente = value

    @property
    def _marca(self):
        return self.__marca

    @_marca.setter
    def _marca(self, value):
        self.__marca = value

    @property
    def _modelo(self):
        return self.__modelo

    @_modelo.setter
    def _modelo(self, value):
        self.__modelo = value

    @property
    def _año(self):
        return self.__año

    @_año.setter
    def _año(self, value):
        self.__año = value

    @property
    def _precio(self):
        return self.__precio

    @_precio.setter
    def _precio(self, value):
        self.__precio = value

    @property
    def _color(self):
        return self.__color

    @_color.setter
    def _color(self, value):
        self.__color = value
        
    def get_descuento(self):
        if self.__cliente._edad < 25:
            return 0.05
        elif self.__cliente._edad >= 25 and self.__cliente._edad <= 60 \
            and self.__cliente._genero.lower() == "femenino":
            return 0.07
        elif self.__cliente._edad > 60:
            return 0.10
        return 0.0
    
    def get_subtotal(self):
        return self.__precio
        
    def get_precio_final(self):
        return self.get_subtotal() - (self.get_subtotal() * self.get_descuento())

    def __str__(self):
        return "\n".join([
            "".center(40, "*"),
            " Datos del cliente ".center(40, "*"),
            f"{self.__cliente}",
            " Datos del vehículo ".center(40, "*"),
            f"Marca: {self.__marca}",
            f"Modelo: {self.__modelo}",
            f"Año: {self.__año}",
            f"Precio: {self.__precio}",
            f"Color: {self.__color}",
            f"Subtotal: {self.get_subtotal()}",
            f"Descuento: {self.get_descuento():.0%}",
            f"Precio final: {self.get_precio_final()}"
        ])
        
    

