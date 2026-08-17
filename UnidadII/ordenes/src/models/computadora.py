class Computadora:
    
    contadorComputadoras = 0
    
    def __init__(self, nombre, monitor, teclado, mouse):
        Computadora.contadorComputadoras += 1
        self._idComputadora = Computadora.contadorComputadoras
        self._nombre = nombre
        self._monitor = monitor
        self._teclado = teclado
        self._mouse = mouse

    @property
    def idComputadora(self):
        return self._idComputadora

    @idComputadora.setter
    def idComputadora(self, value):
        self._idComputadora = value

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, value):
        self._nombre = value

    @property
    def monitor(self):
        return self._monitor

    @monitor.setter
    def monitor(self, value):
        self._monitor = value

    @property
    def teclado(self):
        return self._teclado

    @teclado.setter
    def teclado(self, value):
        self._teclado = value

    @property
    def mouse(self):
        return self._mouse

    @mouse.setter
    def mouse(self, value):
        self._mouse = value
        
    def __str__(self):
        return '\n'.join([
            "Id: " + str(self._idComputadora),
            "Nombre: " + self._nombre,
            "Monitor: \n" + str(self._monitor),
            "Teclado: \n" + str(self._teclado),
            "Mouse: \n" + str(self._mouse)
        ])