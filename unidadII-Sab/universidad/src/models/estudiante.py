class Estudiante:
    
    def __init__(self, nombre, apellido, cedula, carrera, correo, telefono):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__cedula = cedula
        self.__carrera = carrera
        self.__correo = correo
        self.__telefono = telefono
        self.__materias = []

    @property
    def _nombre(self):
        return self.__nombre

    @_nombre.setter
    def _nombre(self, value):
        self.__nombre = value

    @property
    def _apellido(self):
        return self.__apellido

    @_apellido.setter
    def _apellido(self, value):
        self.__apellido = value

    @property
    def _cedula(self):
        return self.__cedula

    @_cedula.setter
    def _cedula(self, value):
        self.__cedula = value

    @property
    def _carrera(self):
        return self.__carrera

    @_carrera.setter
    def _carrera(self, value):
        self.__carrera = value

    @property
    def _correo(self):
        return self.__correo

    @_correo.setter
    def _correo(self, value):
        self.__correo = value

    @property
    def _telefono(self):
        return self.__telefono

    @_telefono.setter
    def _telefono(self, value):
        self.__telefono = value
        
    @property
    def _materias(self):
        return self.__materias

    @_materias.setter
    def _materias(self, value):
        self.__materias = value
        
    def agregar_materia(self, materia):
        self._materias.append(materia)
        
    def get_promedio_ponderado(self):
        suma_valores = 0
        suma_creditos = 0
        for materia in self._materias:
            suma_valores += materia.get_valor()
            suma_creditos += materia._creditos
        return suma_valores / suma_creditos

    def aprobo_semestre(self, nota_minima=10.0):
        return self.get_promedio_ponderado() >= nota_minima

    def __str__(self):
        datos_estudiante = "\n".join([
            f"Nombre: {self._nombre}",
            f"Apellido: {self._apellido}",
            f"Cedula: {self._cedula}",
            f"Carrera: {self._carrera}",
            f"Correo: {self._correo}",
            f"Telefono: {self._telefono}",
            ])
        for materia in self._materias:
            datos_estudiante += f"\n{materia}"
            
        return datos_estudiante