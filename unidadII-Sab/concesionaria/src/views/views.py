from src.models import Cliente, Carro, Camion, Camioneta, Moto, Concesionario


def crear_clientes():
    return [
        Cliente("Luis", "Gómez", "V-20111222", "555-1001", 22, "masculino"),
        Cliente("María", "Rodríguez", "V-15333444", "555-1002", 35, "femenino"),
        Cliente("José", "Martínez", "V-8555666", "555-1003", 65, "masculino"),
        Cliente("Carlos", "Pérez", "V-12777888", "555-1004", 40, "masculino"),
    ]


def crear_vehiculos(clientes):
    return [
        Carro(clientes[0], "Toyota", "Corolla", 2022, 20000, "Blanco", 4, "Manual"),
        Camion(clientes[1], "Volvo", "FH", 2020, 50000, "Rojo", 10, 3),
        Camioneta(clientes[2], "Ford", "Ranger", 2023, 30000, "Gris", "4x4", 5),
        Moto(clientes[3], "Yamaha", "MT-03", 2021, 5000, "Negro", 300, "4 tiempos"),
    ]


def main():
    concesionario = Concesionario("Autos del Centro", "Av. Principal #123")

    clientes = crear_clientes()
    for vehiculo in crear_vehiculos(clientes):
        concesionario.agregar_vehiculo(vehiculo)

    print(concesionario)
