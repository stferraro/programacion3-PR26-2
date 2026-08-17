from datetime import datetime

class Consulta:
    
    contador_consultas = 0
    
    def __init__(self, id_consulta, fecha, hora, motivo, diagnostico, tratamiento, precio):
        Consulta.contador_consultas += 1
        self.__id_consulta = Consulta.contador_consultas
        self.__fecha = datetime.strptime(fecha, "%d/%m/%Y")
        self.__hora = datetime.strptime(hora, "%H:%M").time()
        self.__motivo = motivo
        self.__diagnostico = diagnostico
        self.__tratamiento = tratamiento
        self.__precio = precio
        

    @property
    def _id_consulta(self):
        return self.__id_consulta

    @_id_consulta.setter
    def _id_consulta(self, value):
        self.__id_consulta = value

    @property
    def _fecha(self):
        return self.__fecha

    @_fecha.setter
    def _fecha(self, value):
        self.__fecha = value

    @property
    def _hora(self):
        return self.__hora

    @_hora.setter
    def _hora(self, value):
        self.__hora = value

    @property
    def _motivo(self):
        return self.__motivo

    @_motivo.setter
    def _motivo(self, value):
        self.__motivo = value

    @property
    def _diagnostico(self):
        return self.__diagnostico

    @_diagnostico.setter
    def _diagnostico(self, value):
        self.__diagnostico = value

    @property
    def _tratamiento(self):
        return self.__tratamiento

    @_tratamiento.setter
    def _tratamiento(self, value):
        self.__tratamiento = value

    @property
    def _precio(self):
        return self.__precio

    @_precio.setter
    def _precio(self, value):
        self.__precio = value
        
    def __str__(self):
        return "\n".join([
            f"ID Consulta: {self.__id_consulta}",
            f"Fecha: {self.__fecha.strftime('%d/%m/%Y')}",
            f"Hora: {self.__hora}",
            f"Motivo: {self.__motivo}",
            f"Diagnostico: {self.__diagnostico}",
            f"Tratamiento: {self.__tratamiento}",
            f"Precio: {self.__precio}"
        ])
        
    def print_txt(self):
        try:
            with open("resources/consultas.txt", "a") as file:
                file.write(str(self) + "\n")
        except Exception as e:
            print(f"Error al escribir en el archivo: {e}")
