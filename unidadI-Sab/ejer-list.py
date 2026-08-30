lista_productos = ['Pan', 'Leche', 'Jugo']
lista_precios = [1.50, 2.00, 2.50]
lista_cantidades = [0, 0, 0]
lista_total_precios = [0, 0, 0]

def registra_producto(producto):
    indice = lista_productos.index(producto)
    lista_cantidades[indice] += 1


def registra_precio_per_product(producto):
    indice = lista_productos.index(producto)
    precio_unitario = lista_precios[indice]
    lista_total_precios[indice] += precio_unitario
    
def suma_total():
    return sum(lista_total_precios)

def producto_mas_vendido():
    cantidad_maxima = max(lista_cantidades)
    nombres = []
    for i in range(len(lista_cantidades)):
        if lista_cantidades[i] == cantidad_maxima:
            nombres.append(lista_productos[i])
    return nombres, cantidad_maxima

def main():
    producto = input('Inserta un producto(Pan, Leche, Jugo, 0 para salir): ')
    while producto != '0':
        if producto in lista_productos:
            registra_producto(producto)
            registra_precio_per_product(producto)
            
        else:
            
            print('Error, producto no válido')

        producto = input('Inserta un producto(Pan, Leche, Jugo, 0 para salir): ')

    nombres, cantidad = producto_mas_vendido()
    print(lista_cantidades)
    print(lista_total_precios)
    print(f' Total Recaudado en el dia: {suma_total()} $$ ')
    print(f' Producto(s) mas vendido(s): {nombres} ({cantidad} unidades) ')

main()
