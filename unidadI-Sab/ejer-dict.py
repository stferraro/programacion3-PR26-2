precios = {'Pan': 1.50, 'Leche': 2.00, 'Jugo': 2.50}
cantidades = {'Pan': 0, 'Leche': 0, 'Jugo': 0}
total_precios = {'Pan': 0, 'Leche': 0, 'Jugo': 0}

def registra_producto(producto):
    cantidades[producto] += 1


def registra_precio_per_product(producto):
    precio_unitario = precios[producto]
    total_precios[producto] += precio_unitario

def suma_total():
    return sum(total_precios.values())

def producto_mas_vendido():
    cantidad_maxima = max(cantidades.values())
    nombres = []
    for producto in cantidades:
        if cantidades[producto] == cantidad_maxima:
            nombres.append(producto)
    return nombres, cantidad_maxima

def main():
    producto = input('Inserta un producto(Pan, Leche, Jugo, 0 para salir): ')
    while producto != '0':
        if producto in precios:
            registra_producto(producto)
            registra_precio_per_product(producto)
        else:
            print('Error, producto no válido')

        producto = input('Inserta un producto(Pan, Leche, Jugo, 0 para salir): ')

    nombres, cantidad = producto_mas_vendido()
    print(cantidades)
    print(total_precios)
    print(f' Total Recaudado en el dia: {suma_total()} $$ ')
    print(f' Producto(s) mas vendido(s): {nombres} ({cantidad} unidades) ')

main()
