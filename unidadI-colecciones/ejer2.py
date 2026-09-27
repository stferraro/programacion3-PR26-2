from statistics import mean

ventas_cajas = [320.0, 1150.0, 890.0, 410.0, 980.0, 550.0]

def get_total_ventas():
    return sum(ventas_cajas)

def promedio():
    return mean(ventas_cajas)

def monto_alto():
    return max(ventas_cajas)

def monto_menor():
    return min(ventas_cajas)

def main():
    while True:
        opcion = int(input('Inserta la opcion a hacer: '))
        if opcion == 1:
            print(f'El total de piezas es: {get_total_ventas()}')
        elif opcion == 2:
            print(f'El promedio es : {promedio():.2f}')
        elif opcion == 3:
            print(f'El valor mas alto es : {monto_alto()}')
        elif opcion == 4:
            print(f'El valor mas bajo es : {monto_menor()}')
        elif opcion == 0:
            break
        else:
            opcion = int(input('Error, inserta la opcion a hacer: '))

main()