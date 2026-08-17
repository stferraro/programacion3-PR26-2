from ..controller.clinica_controller import ClinicaController
from ..models import servicio_consulta, servicio_hospedaje

MENU = """
==== Clínica Veterinaria ====
1. Crear servicio
2. Listar servicios
3. Actualizar servicio
4. Eliminar servicio
5. Salir
6. Ver total facturado
"""


def pedir_datos_consulta() -> dict:
    print(f"Especialidades -> {servicio_consulta.ServicioConsulta.CIRUGIA}: Cirugía, ")
    print(
        f"{servicio_consulta.ServicioConsulta.DERMATOLOGIA}: Dermatología, "
        f"{servicio_consulta.ServicioConsulta.CONSULTA_GENERAL}: Consulta general"
    )
    return {
        "fecha": input("Fecha (dd/mm/aaaa): "),
        "nombre_mascota": input("Nombre de la mascota: "),
        "nombre_cliente": input("Nombre del cliente: "),
        "costo_base": float(input("Costo base: ")),
        "nombre_veterinario": input("Nombre del veterinario: "),
        "especialidad": int(input("Especialidad: ")),
    }


def pedir_datos_hospedaje() -> dict:
    print(
        f"Tipo de habitación -> {servicio_hospedaje.ServicioHospedaje.ESTANDARD}: Estándar, "
        f"{servicio_hospedaje.ServicioHospedaje.PREMIUM}: Premium"
    )
    return {
        "fecha": input("Fecha (dd/mm/aaaa): "),
        "nombre_mascota": input("Nombre de la mascota: "),
        "nombre_cliente": input("Nombre del cliente: "),
        "costo_base": float(input("Costo base: ")),
        "dias_estadia": int(input("Días de estadía: ")),
        "tipo_habitacion": int(input("Tipo de habitación: ")),
    }


def crear_servicio(controller: ClinicaController) -> None:
    tipo = input("Tipo de servicio (1: Consulta, 2: Hospedaje): ")
    if tipo == "1":
        nuevo_servicio = controller.crear_servicio_consulta(**pedir_datos_consulta())
    elif tipo == "2":
        nuevo_servicio = controller.crear_servicio_hospedaje(**pedir_datos_hospedaje())
    else:
        print("Tipo de servicio inválido.")
        return
    print(f"\nServicio creado con código {nuevo_servicio._cod_servicio}.")


def listar_servicios(controller: ClinicaController) -> None:
    print(f"\n{controller}")


def actualizar_servicio(controller: ClinicaController) -> None:
    cod_servicio = int(input("Código del servicio a actualizar: "))
    servicio_actual = controller.obtener_servicio(cod_servicio)
    if servicio_actual is None:
        print("No existe un servicio con ese código.")
        return

    if isinstance(servicio_actual, servicio_consulta.ServicioConsulta):
        datos = pedir_datos_consulta()
        servicio_actual._fecha = datos["fecha"]
        servicio_actual._nombre_mascota = datos["nombre_mascota"]
        servicio_actual._nombre_cliente = datos["nombre_cliente"]
        servicio_actual._costo_base = datos["costo_base"]
        servicio_actual._nombre_veterinario = datos["nombre_veterinario"]
        servicio_actual._especialidad = datos["especialidad"]
    else:
        datos = pedir_datos_hospedaje()
        servicio_actual._fecha = datos["fecha"]
        servicio_actual._nombre_mascota = datos["nombre_mascota"]
        servicio_actual._nombre_cliente = datos["nombre_cliente"]
        servicio_actual._costo_base = datos["costo_base"]
        servicio_actual._dias_estadia = datos["dias_estadia"]
        servicio_actual._tipo_habitacion = datos["tipo_habitacion"]

    if controller.actualizar_servicio(servicio_actual):
        print("Servicio actualizado correctamente.")
    else:
        print("No se pudo actualizar el servicio.")


def eliminar_servicio(controller: ClinicaController) -> None:
    cod_servicio = int(input("Código del servicio a eliminar: "))
    if controller.eliminar_servicio(cod_servicio):
        print("Servicio eliminado correctamente.")
    else:
        print("No existe un servicio con ese código.")


def ver_total_facturado(controller: ClinicaController) -> None:
    print(f"\nTotal facturado: {controller.total_facturado():.2f}")


def main():
    controller = ClinicaController(nombre="Clínica Veterinaria San Roque", rif="J-12345678-9")

    acciones = {
        "1": crear_servicio,
        "2": listar_servicios,
        "3": actualizar_servicio,
        "4": eliminar_servicio,
        "6": ver_total_facturado,
    }

    while True:
        print(MENU)
        opcion = input("Seleccione una opción: ")
        if opcion == "5":
            print("¡Hasta luego!")
            break
        accion = acciones.get(opcion)
        if accion is None:
            print("Opción inválida.")
            continue
        accion(controller)


main()
