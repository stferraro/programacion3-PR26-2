from . import persona

class Paciente(persona.Persona):
    
    def __init__(self, nombre, apellido, cedula, telefono, correo, edad, sexo, consultas):
        super().__init__(nombre, apellido, cedula, telefono, correo)
        self.__edad = edad
        self.__sexo = sexo
        self.__consultas = consultas

    @property
    def _edad(self):
        return self.__edad

    @_edad.setter
    def _edad(self, value):
        self.__edad = value

    @property
    def _sexo(self):
        return self.__sexo

    @_sexo.setter
    def _sexo(self, value):
        self.__sexo = value
        
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
            f"Edad: {self.__edad}",
            f"Sexo: {self.__sexo}",
            f"--------------------------------".center(50),
            f"consultas realizadas: {len(self.__consultas)}",
            f"Consultas:\n{datos_consultas}"
        ])