from src.models.rectangulo import Rectangulo
from src.models.cuadrado import Cuadrado
from src.models.triangulo import Triangulo

FIGURAS = {
    "1": {
        "nombre": "Rectangulo",
        "clase": Rectangulo,
        "campos": ["base", "altura"],
    },
    "2": {
        "nombre": "Cuadrado",
        "clase": Cuadrado,
        "campos": ["lado"],
    },
    "3": {
        "nombre": "Triangulo",
        "clase": Triangulo,
        "campos": ["lado1", "lado2", "lado3"],
    },
}


def mostrar_menu():
    print("\n--- Figuras Geométricas ---")
    for clave, figura in FIGURAS.items():
        print(f"{clave}) {figura['nombre']}")
    print("0) Salir")


def pedir_valores(campos):
    valores = []
    for campo in campos:
        valor = input(f"  {campo}: ")
        valores.append(float(valor))
    return valores


def iniciar_aplicacion():
    while True:
        mostrar_menu()
        opcion = input("Elija una figura: ")

        if opcion == "0":
            print("Hasta luego.")
            break

        figura_info = FIGURAS.get(opcion)
        if figura_info is None:
            print("Opción inválida.")
            continue

        try:
            valores = pedir_valores(figura_info["campos"])
            figura = figura_info["clase"](*valores)
        except ValueError as error:
            print(f"Error: {error}")
            continue

        print(figura)


if __name__ == "__main__":
    iniciar_aplicacion()
