from ..models import servicio, servicio_consulta, servicio_hospedaje
from . import database


def _fila_a_servicio(fila) -> servicio.Servicio:
    if fila["tipo"] == "consulta":
        return servicio_consulta.ServicioConsulta(
            fecha=fila["fecha"],
            nombre_mascota=fila["nombre_mascota"],
            nombre_cliente=fila["nombre_cliente"],
            costo_base=fila["costo_base"],
            nombre_veterinario=fila["nombre_veterinario"],
            especialidad=fila["especialidad"],
            cod_servicio=fila["cod_servicio"],
        )
    return servicio_hospedaje.ServicioHospedaje(
        fecha=fila["fecha"],
        nombre_mascota=fila["nombre_mascota"],
        nombre_cliente=fila["nombre_cliente"],
        costo_base=fila["costo_base"],
        dias_estadia=fila["dias_estadia"],
        tipo_habitacion=fila["tipo_habitacion"],
        cod_servicio=fila["cod_servicio"],
    )


def crear(nuevo_servicio: servicio.Servicio) -> servicio.Servicio:
    if isinstance(nuevo_servicio, servicio_consulta.ServicioConsulta):
        tipo = "consulta"
        nombre_veterinario = nuevo_servicio._nombre_veterinario
        especialidad = nuevo_servicio._especialidad
        dias_estadia = None
        tipo_habitacion = None
    else:
        tipo = "hospedaje"
        nombre_veterinario = None
        especialidad = None
        dias_estadia = nuevo_servicio._dias_estadia
        tipo_habitacion = nuevo_servicio._tipo_habitacion

    with database.get_connection() as conexion:
        cursor = conexion.execute(
            """
            INSERT INTO servicios (
                tipo, fecha, nombre_mascota, nombre_cliente, costo_base,
                nombre_veterinario, especialidad, dias_estadia, tipo_habitacion
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                tipo,
                nuevo_servicio._fecha,
                nuevo_servicio._nombre_mascota,
                nuevo_servicio._nombre_cliente,
                nuevo_servicio._costo_base,
                nombre_veterinario,
                especialidad,
                dias_estadia,
                tipo_habitacion,
            ),
        )
        nuevo_servicio._cod_servicio = cursor.lastrowid
    return nuevo_servicio


def listar() -> list[servicio.Servicio]:
    with database.get_connection() as conexion:
        filas = conexion.execute("SELECT * FROM servicios ORDER BY cod_servicio").fetchall()
    return [_fila_a_servicio(fila) for fila in filas]


def obtener_por_id(cod_servicio: int) -> servicio.Servicio | None:
    with database.get_connection() as conexion:
        fila = conexion.execute("SELECT * FROM servicios WHERE cod_servicio = ?", (cod_servicio,)).fetchone()
    return _fila_a_servicio(fila) if fila else None


def actualizar(servicio_editado: servicio.Servicio) -> bool:
    if isinstance(servicio_editado, servicio_consulta.ServicioConsulta):
        nombre_veterinario = servicio_editado._nombre_veterinario
        especialidad = servicio_editado._especialidad
        dias_estadia = None
        tipo_habitacion = None
    else:
        nombre_veterinario = None
        especialidad = None
        dias_estadia = servicio_editado._dias_estadia
        tipo_habitacion = servicio_editado._tipo_habitacion

    with database.get_connection() as conexion:
        cursor = conexion.execute(
            """
            UPDATE servicios
            SET fecha = ?, nombre_mascota = ?, nombre_cliente = ?, costo_base = ?,
                nombre_veterinario = ?, especialidad = ?, dias_estadia = ?, tipo_habitacion = ?
            WHERE cod_servicio = ?
            """,
            (
                servicio_editado._fecha,
                servicio_editado._nombre_mascota,
                servicio_editado._nombre_cliente,
                servicio_editado._costo_base,
                nombre_veterinario,
                especialidad,
                dias_estadia,
                tipo_habitacion,
                servicio_editado._cod_servicio,
            ),
        )
    return cursor.rowcount > 0


def eliminar(cod_servicio: int) -> bool:
    with database.get_connection() as conexion:
        cursor = conexion.execute("DELETE FROM servicios WHERE cod_servicio = ?", (cod_servicio,))
    return cursor.rowcount > 0
