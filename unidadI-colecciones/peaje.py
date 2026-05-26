vehiculos = {'Moto': 5.30, 'Carro': 12, 'Camion': 16}
cantidad_vehiculos = {'Moto': 0, 'Carro': 0, 'Camion': 0}
valores_vehiculos = {'Moto': 0, 'Carro': 0, 'Camion': 0}

def valor_vehiculo(tipo_vehiculo):
    return vehiculos.get(tipo_vehiculo)

def total_recaudado(tipo_vehiculo):
    return sum(valores_vehiculos.values())

def total_recaudo_per_vehiculo(tipo_vehiculo):
    return valores_vehiculos.get(tipo_vehiculo)

def max_vehiculo():
    return max(cantidad_vehiculos, key=cantidad_vehiculos.get)

def imprimir_datos():
    print(f'El total recaudado en el dia es: {total_recaudado(tipo_vehiculo): .2f}$$')
    print(f'El total recaudado por las Motos es de : {total_recaudo_per_vehiculo('Moto'):.2f}$$')
    print(f'El total recaudado por los Carros es de : {total_recaudo_per_vehiculo('Carro'):.2f}$$')
    print(f'El total recaudado por los Camiones es de : {total_recaudo_per_vehiculo('Camion'):.2f}$$')
    print(f'El Vehìculo que mas pasa por el peaje es {max_vehiculo()} y ha pasado {cantidad_vehiculos.get(max_vehiculo())}')

def main():
    tipo_vehiculo = input('Inserta el tipo de vehiculo(0 para salir): ')
    while tipo_vehiculo != 0:
        valor = valor_vehiculo(tipo_vehiculo)
        valor = valor_vehiculo(tipo_vehiculo)
        valores_vehiculos[tipo_vehiculo]+= valor
        cantidad_vehiculos[tipo_vehiculo] += 1
        print(f'El vehiculo {tipo_vehiculo}, paga {valor: .2f}')
        tipo_vehiculo = input('Inserta el tipo de vehiculo(0 para salir): ')
        if tipo_vehiculo == '0':
            break
    
    

main()