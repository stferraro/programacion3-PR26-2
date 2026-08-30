from ..models import empleado_contratado, empleado_planta, empresa


def crear_empleados_mock():
    gerente = empleado_planta.EmpleadoPlanta(
        nombre="Carlos",
        apellido="Pérez",
        cedula="V-12345678",
        salario=1200.0,
        antiguedad=10,
        cargo=empleado_planta.EmpleadoPlanta.GERENTE,
    )
    supervisor_1 = empleado_planta.EmpleadoPlanta(
        nombre="María",
        apellido="Rodríguez",
        cedula="V-23456789",
        salario=900.0,
        antiguedad=6,
        cargo=empleado_planta.EmpleadoPlanta.SUPERVISOR1,
    )
    supervisor_2 = empleado_planta.EmpleadoPlanta(
        nombre="Luis",
        apellido="Torres",
        cedula="V-34567890",
        salario=850.0,
        antiguedad=4,
        cargo=empleado_planta.EmpleadoPlanta.SUPERVISOR2,
    )
    contratado = empleado_contratado.EmpleadoContratado(
        nombre="Sofía",
        apellido="Martínez",
        cedula="V-45678901",
        salario=700.0,
        proyecto_asignado="Migración de sistemas",
        meses_contrato=6,
    )
    return [gerente, supervisor_1, supervisor_2, contratado]


def main():
    mi_empresa = empresa.Empresa(nombre="Tech Solutions C.A.", rif="J-12345678-9", direccion="Av. Principal, Caracas")
    for emp in crear_empleados_mock():
        mi_empresa.agregar_empleado(emp)
    mi_empresa.print_txt()

    with open("resources/nomina.txt") as file:
        print(file.read())


main()
