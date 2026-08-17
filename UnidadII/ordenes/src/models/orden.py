class Orden:
    
    contadorOrdenes = 0
    
    def __init__(self, computadoras):
        Orden.contadorOrdenes += 1
        self.__idOrden = Orden.contadorOrdenes
        self.__computadoras = computadoras

    @property
    def computadoras(self):
        return self.__computadoras

    @computadoras.setter
    def computadoras(self, value):
        self.__computadoras = value
        
    def agregarComputadora(self, computadora):
        self.__computadoras.append(computadora)
        
    def searchComputadora(self, idComputadora):
        for computadora in self.__computadoras:
            if computadora.idComputadora == idComputadora:
                return computadora
        return None
    
    def updateComputadora(self, idComputadora, nuevaComputadora):
        for i, computadora in enumerate(self._computadoras):
            if computadora.idComputadora == idComputadora:
                self.__computadoras[i] = nuevaComputadora
                return True
        return False
        
    def deleteComputadora(self, computadora):
        if computadora in self._computadoras:
            self._computadoras.remove(computadora)
        
    def __str__(self):
        computadoras_str = '\n'.join([str(computadora) for computadora in self.__computadoras])
        return '\n'.join([
            "Id Orden: " + str(self.__idOrden),
            "Computadoras: \n" + computadoras_str
        ])
