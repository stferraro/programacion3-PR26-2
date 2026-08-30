from . import persona

class Doctor(persona.Persona):
    
    def __init__(self, nombre, apellido, cedula, telefono, correo, especialidad, consultas):
        super().__init__(nombre, apellido, cedula, telefono, correo)
        self.__especialidad = especialidad
        self.__consultas = consultas

    @property
    def _especialidad(self):
        return self.__especialidad

    @_especialidad.setter
    def _especialidad(self, value):
        self.__especialidad = value

    @property
    def _consultas(self):
        return self.__consultas

    @_consultas.setter
    def _consultas(self, value):
        self.__consultas = value
        
    def add_consulta(self, consulta):
        self.__consultas.append(consulta)
        
        
    def __str__(self):
        datos_consultas = "\n".join([str(consulta) for consulta in self.__consultas])
        return "\n".join([
            super().__str__(),
            f"Especialidad: {self.__especialidad}",
            f"--------------------------------".center(50),
            f"consultas realizadas: {len(self.__consultas)}",
            f"Consultas:\n{datos_consultas}"
        ])

        
        
        