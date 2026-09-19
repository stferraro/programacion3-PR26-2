from src.models.estudiante import Estudiante
from src.models.materias import Materias

NOTA_MINIMA_APROBACION = 10.0

MATERIAS_DISPONIBLES = [
    {"nombre": "Programación III", "creditos": 4},
    {"nombre": "Cálculo III", "creditos": 4},
    {"nombre": "Física II", "creditos": 3},
    {"nombre": "Bases de Datos", "creditos": 3},
    {"nombre": "Estructuras de Datos", "creditos": 4},
    {"nombre": "Inglés Técnico", "creditos": 2},
    {"nombre": "Ética Profesional", "creditos": 2},
    {"nombre": "Sistemas Operativos", "creditos": 3},
    {"nombre": "Redes de Computadoras", "creditos": 3},
    {"nombre": "Electiva Humanística", "creditos": 2},
]


def crear_estudiante_de_prueba():
    estudiante = Estudiante(
        nombre="Juan",
        apellido="Pérez",
        cedula="V-12345678",
        carrera="Ingeniería en Informática",
        correo="juan.perez@mail.com",
        telefono="555-1234",
    )

    notas_inscritas = [
        (MATERIAS_DISPONIBLES[0], 18.0),  # Programación III
        (MATERIAS_DISPONIBLES[1], 15.0),  # Cálculo III
        (MATERIAS_DISPONIBLES[2], 13.0),  # Física II
        (MATERIAS_DISPONIBLES[3], 9.0),   # Bases de Datos
        (MATERIAS_DISPONIBLES[5], 16.0),  # Inglés Técnico
    ]

    for materia_info, nota in notas_inscritas:
        materia = Materias(materia_info["nombre"], materia_info["creditos"], nota)
        estudiante.agregar_materia(materia)

    return estudiante


def mostrar_resultado(estudiante):
    print("--- Resumen del estudiante ---")
    print(estudiante)

    promedio = estudiante.get_promedio_ponderado()
    print(f"\nPromedio ponderado: {promedio:.2f}")

    if estudiante.aprobo_semestre(NOTA_MINIMA_APROBACION):
        print(f"Resultado: APROBÓ el semestre (nota mínima: {NOTA_MINIMA_APROBACION:.2f})")
    else:
        print(f"Resultado: NO aprobó el semestre (nota mínima: {NOTA_MINIMA_APROBACION:.2f})")


def iniciar_aplicacion():
    estudiante = crear_estudiante_de_prueba()
    mostrar_resultado(estudiante)


if __name__ == "__main__":
    iniciar_aplicacion()
