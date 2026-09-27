piezas = {'cargadores': 110, 'cables_usb': 65, 'audifonos': 75, 'memoria_sd': 18, 'funda_laptop': 6}

def get_total_piezas():
    return sum(piezas.values())

def add_product(pieza):
    if pieza in piezas:
        cantidad = int(input('Cantidad: '))
        piezas[pieza] += cantidad
    else:
        cantidad = int(input('Cantidad: '))
        piezas[pieza] = cantidad

def del_pieza(pieza):
    if pieza in piezas:
        del piezas[pieza]
    else:
        print('El producto no esta disponible en el stock')
        
def promedio():
    return get_total_piezas()/len(piezas.values())

def product_mayor():
    valor = max(piezas, key=piezas.get)
    producto_max = piezas[valor]
    print(f'La pieza con menos stock es {valor} y tiene cantidad {producto_max}')

def product_menor():
    valor = min(piezas, key=piezas.get)
    producto_min = piezas[valor]
    print(f'La pieza con menos stock es {valor} y tiene cantidad {producto_min}')


def main():
    while True:
        opcion = int(input('Inserta la opcion a hacer: '))
        if opcion == 1:
            print(f'El total de piezas es: {get_total_piezas()}')
        elif opcion == 2:
            pieza = input('Inserta la pieza que quieres eliminar: ')
            add_product(pieza)
            print(piezas)
        elif opcion == 3:
            pieza = input('Inserta la pieza que quieres eliminar: ')
            del_pieza(pieza)
            print(piezas)
        elif opcion == 4:
            print(f'El promedio es : {promedio():.2f}')
        elif opcion == 5:
            product_mayor()
        elif opcion == 6:
            product_menor()
        elif opcion == 0:
            break
        else:
            opcion = int(input('Error, inserta la opcion a hacer: '))

main()