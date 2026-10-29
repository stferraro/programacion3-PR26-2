from .vehiculo import Vehiculo

class Concesionario:
    
    def __init__(self, nombre: str, direccion: str):
        self.__nombre = nombre
        self.__direccion = direccion
        self.__vehiculos = []

    @property
    def _nombre(self):
        return self.__nombre

    @_nombre.setter
    def _nombre(self, value):
        self.__nombre = value

    @property
    def _direccion(self):
        return self.__direccion

    @_direccion.setter
    def _direccion(self, value):
        self.__direccion = value

    @property
    def _vehiculos(self):
        return self.__vehiculos

    @_vehiculos.setter
    def _vehiculos(self, value):
        self.__vehiculos = value

    def agregar_vehiculo(self, vehiculo: Vehiculo):
        self.__vehiculos.append(vehiculo)

    def mostrar_vehiculos(self):
        for vehiculo in self.__vehiculos:
            print(vehiculo)
            print("-" * 40)
            
    def calcular_total_ventas(self):
        return sum(vehiculo.get_precio_final() for vehiculo in self.__vehiculos)
    
    def __str__(self):
        datos_concesionario = "\n".join([
            f"Nombre: {self.__nombre}",
            f"Dirección: {self.__direccion}",
        ])
        datos_vehiculos = "\n".join([str(vehiculo) for vehiculo in self.__vehiculos])
        return f"{datos_concesionario}\n\nVehículos:\n{datos_vehiculos}\n\nTotal de ventas: ${self.calcular_total_ventas():,.2f}"