from ..data import database, servicio_repository
from ..models import clinica as clinica_model
from ..models import servicio, servicio_consulta, servicio_hospedaje


class ClinicaController:
    def __init__(self, nombre: str, rif: str):
        database.crear_tablas()
        self.__clinica = clinica_model.Clinica(nombre=nombre, rif=rif, servicios=servicio_repository.listar())

    def crear_servicio_consulta(
        self,
        fecha: str,
        nombre_mascota: str,
        nombre_cliente: str,
        costo_base: float,
        nombre_veterinario: str,
        especialidad: int,
    ) -> servicio.Servicio:
        nuevo_servicio = servicio_consulta.ServicioConsulta(
            fecha=fecha,
            nombre_mascota=nombre_mascota,
            nombre_cliente=nombre_cliente,
            costo_base=costo_base,
            nombre_veterinario=nombre_veterinario,
            especialidad=especialidad,
        )
        servicio_repository.crear(nuevo_servicio)
        self.__clinica.agregar_servicio(nuevo_servicio)
        return nuevo_servicio

    def crear_servicio_hospedaje(
        self,
        fecha: str,
        nombre_mascota: str,
        nombre_cliente: str,
        costo_base: float,
        dias_estadia: int,
        tipo_habitacion: int,
    ) -> servicio.Servicio:
        nuevo_servicio = servicio_hospedaje.ServicioHospedaje(
            fecha=fecha,
            nombre_mascota=nombre_mascota,
            nombre_cliente=nombre_cliente,
            costo_base=costo_base,
            dias_estadia=dias_estadia,
            tipo_habitacion=tipo_habitacion,
        )
        servicio_repository.crear(nuevo_servicio)
        self.__clinica.agregar_servicio(nuevo_servicio)
        return nuevo_servicio

    def listar_servicios(self) -> list[servicio.Servicio]:
        self.__clinica._servicios = servicio_repository.listar()
        return self.__clinica._servicios

    def obtener_servicio(self, cod_servicio: int) -> servicio.Servicio | None:
        return servicio_repository.obtener_por_id(cod_servicio)

    def actualizar_servicio(self, servicio_editado: servicio.Servicio) -> bool:
        actualizado = servicio_repository.actualizar(servicio_editado)
        if actualizado:
            self.listar_servicios()
        return actualizado

    def eliminar_servicio(self, cod_servicio: int) -> bool:
        eliminado = servicio_repository.eliminar(cod_servicio)
        if eliminado:
            self.listar_servicios()
        return eliminado

    def total_facturado(self) -> float:
        self.listar_servicios()
        return self.__clinica.total_facturado()

    def __str__(self):
        self.listar_servicios()
        return str(self.__clinica)
