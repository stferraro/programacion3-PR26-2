lista_productos = ['Pan', 'Leche', 'Jugo']
lista_precios = [1.50, 2.00, 2.50]
lista_cantidades = [0, 0, 0]
lista_total_precios = [0, 0, 0]

def registrar_producto(producto):
    indice = producto - 1
    lista_cantidades[indice] += 1
    
def precio(producto):
    indice = producto - 1
    precio = lista_precios[indice]
    lista_total_precios[indice] += precio
    
def total():
    return sum(lista_total_precios)

def producto_max():
    valor_max = max(lista_cantidades)
    indice = lista_cantidades.index(valor_max)
    producto_max = lista_productos[indice]
    return producto_max, valor_max

def main():

    producto = int(input('Producto (1-Pan, 2-Leche, 3-Jugo, 0-Salir): '))
    while producto != 0:

        if producto in (1, 2, 3):
            registrar_producto(producto)
            precio(producto)
        else:
            print('Producto no válido')

        producto = int(input('Producto (1-Pan, 2-Leche, 3-Jugo, 0-Salir): '))

    print(lista_cantidades)
    print(lista_total_precios)
    print(f'El total vendido durante el dia es de: {total():.2f} $$')
    prod, cant = producto_max()
    print(f"El producto más vendido es {prod} con una cantidad de {cant}")


main()