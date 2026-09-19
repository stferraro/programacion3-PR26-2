from statistics import mean

recaudaciones = [450.0, 1200.0, 800.0, 350.0, 950.0, 600.0]

def get_total_ventas():
    return sum(recaudaciones)

def promedio():
    return mean(recaudaciones)

def monto_alto():
    return max(recaudaciones)

def monto_menor():
    return min(recaudaciones)

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