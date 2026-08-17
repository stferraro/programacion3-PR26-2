from . import dispositivo_entrada


class Mouse(dispositivo_entrada.DispositivoEntrada):
    
    contadorMouse = 0
    
    def __init__(self, tipoEntrada, marca):
        Mouse.contadorMouse += 1
        self.__idMouse = Mouse.contadorMouse
        super().__init__(tipoEntrada, marca)

    def __str__(self):
        return f'\n'.join([
            "Id: " + str(self.__idMouse),
            super().__str__()
        ])