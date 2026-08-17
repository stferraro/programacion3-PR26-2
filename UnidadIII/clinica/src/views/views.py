from ..models import clinica, servicio_consulta, servicio_hospedaje


def crear_servicios_mock():
    consulta_1 = servicio_consulta.ServicioConsulta(
        fecha="10/03/2026",
        nombre_mascota="Firulais",
        nombre_cliente="Carlos Pérez",
        costo_base=25.0,
        nombre_veterinario="Dra. Ana Gómez",
        especialidad=servicio_consulta.ServicioConsulta.CIRUGIA,
    )
    consulta_2 = servicio_consulta.ServicioConsulta(
        fecha="15/03/2026",
        nombre_mascota="Michi",
        nombre_cliente="María Rodríguez",
        costo_base=20.0,
        nombre_veterinario="Dr. Luis Torres",
        especialidad=servicio_consulta.ServicioConsulta.DERMATOLOGIA,
    )
    hospedaje_1 = servicio_hospedaje.ServicioHospedaje(
        fecha="20/03/2026",
        nombre_mascota="Rocky",
        nombre_cliente="Pedro Ramírez",
        costo_base=15.0,
        dias_estadia=5,
        tipo_habitacion=servicio_hospedaje.ServicioHospedaje.ESTANDARD,
    )
    hospedaje_2 = servicio_hospedaje.ServicioHospedaje(
        fecha="25/03/2026",
        nombre_mascota="Luna",
        nombre_cliente="Sofía Martínez",
        costo_base=18.0,
        dias_estadia=3,
        tipo_habitacion=servicio_hospedaje.ServicioHospedaje.PREMIUM,
    )
    return [consulta_1, consulta_2, hospedaje_1, hospedaje_2]


def main():
    mi_clinica = clinica.Clinica(nombre="Clínica Veterinaria San Roque", rif="J-12345678-9")
    for servicio in crear_servicios_mock():
        mi_clinica.agregar_servicio(servicio)
    mi_clinica.print_txt()


main()
