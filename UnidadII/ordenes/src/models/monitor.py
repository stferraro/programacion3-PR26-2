class Monitor:
    
    contadorMonitores = 0
    
    def __init__(self, marca, tamaño):
        Monitor.contadorMonitores += 1
        self.__idMonitor = Monitor.contadorMonitores
        self.__marca = marca
        self.__tamaño = tamaño

    @property
    def _idMonitor(self):
        return self.__idMonitor

    @_idMonitor.setter
    def _idMonitor(self, value):
        self.__idMonitor = value

    @property
    def _marca(self):
        return self.__marca

    @_marca.setter
    def _marca(self, value):
        self.__marca = value

    @property
    def _tamaño(self):
        return self.__tamaño

    @_tamaño.setter
    def _tamaño(self, value):
        self.__tamaño = value
        
    def __str__(self):
        return '\n'.join([
            "Id: " + str(self.__idMonitor),
            "Marca: " + self.__marca,
            "Tamaño: " + str(self.__tamaño)
        ])
