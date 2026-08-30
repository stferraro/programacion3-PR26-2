'''En una ferretería se necesita implementar un sistema de almacenamiento en Python.El sistema debe:

    - Registrar un nuevo al producto al inventario. El usuario debe introducir el nombre del producto y la cantidad que se tiene en stock.
    Si el producto ya existe en el inventario, se actualizara con la nueva cantidad. Si no existe en el inventario, se registrara.
    - Eliminar un producto del inventario. El usuario debe introducir el nombre del producto que se quiere eliminar.
    - Sistema visualiza producto con cantidad mas alta en el inventario.
    - Sistema visualiza cantidad del producto especificado. El usuario debe introducir el nombre del producto que se quiere consultar y se mostrara 
    la cantidad que tiene en stock. Si el producto no existe en el inventario, se mostrará un mensaje diciendo que el producto no existe.
    - Sistema visualiza el inventario completo. Se mostrará el nombre del producto y la cantidad que tiene en stock.
    
'''

def registro_producto(nombre):
    if nombre in inventario:
        cantidad = inventario[nombre]
    else:
        cantidad = float(input("Ingrese la cantidad: "))
    inventario[nombre] = cantidad
    
def eliminar_producto(nombre):
    if nombre in inventario:
        del inventario[nombre]
    else:
        print(f"El producto {nombre} no existe")
    
def producto_max_stock():
    producto_max_stock = max(inventario.values())
    producto = max(inventario.keys(), key=inventario.get)
    print(f"El producto con cantidad mas alta en el inventario es {producto} con cantidad {producto_max_stock}")
    
def producto_cantidad(nombre):
    if nombre in inventario:
        cantidad = inventario[nombre]
        print(f"La cantidad de {nombre} es {cantidad}")
    else:
        print(f"El producto {nombre} no existe")
        
def inventario_completo():
    for producto in inventario:
        print(f"{producto}: {inventario[producto]}")
        
def menu():
    print("***MENU".center(50, "*"))
    print("1. Registrar producto")
    print("2. Eliminar producto")
    print("3. Mostrar producto con cantidad mas alta en el inventario")
    print("4. Mostrar cantidad del producto especificado")
    print("5. Mostrar inventario completo")
    print("6. Salir")
    print("*".center(50, "*"))
    opcion = int(input("Elija una opcion: "))
    return opcion


def main():
    while True:
        opcion = menu()
        if opcion == 1:
            nombre = input("Ingrese el nombre del producto: ")
            registro_producto(nombre)
        elif opcion == 2:
            nombre = input("Ingrese el nombre del producto que se quiere eliminar: ")
            eliminar_producto(nombre)
        elif opcion == 3:
            producto_max_stock()
        elif opcion == 4:
            nombre = input("Ingrese el nombre del producto que se quiere consultar: ")
            producto_cantidad(nombre)
        elif opcion == 5:
            inventario_completo()
        elif opcion == 6:
            break
        else:
            print("Opcion invalida")

inventario = {}
main()
    