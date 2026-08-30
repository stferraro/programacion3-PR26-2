from . import dispositivo_entrada

class Teclado(
    dispositivo_entrada.DispositivoEntrada
):
    
    contadorTeclado = 0
    
    def __init__(self, tipoEntrada, marca):
        Teclado.contadorTeclado += 1
        self.__idTeclado = Teclado.contadorTeclado
        super().__init__(tipoEntrada, marca)

    def __str__(self):
        return '\n'.join([
            "Id: " + str(self.__idTeclado),
            super().__str__()
        ])
        
