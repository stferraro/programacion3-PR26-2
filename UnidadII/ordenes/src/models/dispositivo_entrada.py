class DispositivoEntrada:
    
    def __init__(self, tipoEntrada, marca):
        self.__tipoEntrada = tipoEntrada
        self.__marca = marca

    @property
    def _tipoEntrada(self):
        return self.__tipoEntrada

    @_tipoEntrada.setter
    def _tipoEntrada(self, value):
        self.__tipoEntrada = value

    @property
    def _marca(self):
        return self.__marca

    @_marca.setter
    def _marca(self, value):
        self.__marca = value
        
    def __str__(self):
        return '\n'.join([
            'Tipo Entrada: ' + self.__tipoEntrada, 
            'Marca: ' + self.__marca
        ])
