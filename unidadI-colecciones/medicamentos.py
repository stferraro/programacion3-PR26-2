import statistics
medicamentos = {'123456789':{'Acetaminofen' : 2.50}}

def add_medicamento(cod_medicamento):
    if cod_medicamento in medicamentos.keys():
        nombre_medicamento = list(medicamentos[cod_medicamento].keys())[0]
        print('Medicamentos ya existe, se actualizará el precio')
        precio = float(input('Precio: '))
        medicamentos[cod_medicamento][nombre_medicamento] = precio
    else:
        nombre_medicamento = input('Nombre del medicamento: ')
        precio = float(input('Precio: '))
        medicamentos[cod_medicamento] = {}
        medicamentos[cod_medicamento][nombre_medicamento] = precio


def main():
    cod_medicamento = input('Codigo del medicamento(no para salir): ')
    while cod_medicamento != 'no':
        add_medicamento(cod_medicamento)
        cod_medicamento = input('Codigo del medicamento(no para salir): ')
        if cod_medicamento.lower() == 'no':
            print('Saliste del sistema')
            break
        
def imprimir_medicamentos(medicamentos):
    for codigo, info_interno in medicamentos.items():
        nombre_medicamento = list(info_interno.keys())[0]
        precio = info_interno[nombre_medicamento]
        print('\n'.join([f'Nombre: {nombre_medicamento}', f'Precio: {precio}']))
        
        
def sumar(medicamentos):
    total = 0  # 1. Creamos un acumulador que empieza en cero
    for codigo, info_interno in medicamentos.items():
        # 2. Obtenemos el precio (primer y único valor del diccionario interno)
        precios = list(info_interno.values())[0]
        total += precios # 3. Lo sumamos al total acumulado
    return total  # 4. Devolvemos el gran total

def promedio(medicamentos):
    lista_precios = []
    for codigo, info_interno in medicamentos.items():
        precios = list(info_interno.values())[0]
        lista_precios.append(precios)
        
    return statistics.mean(lista_precios)

def maximo_valor(medicamentos):
    if not medicamentos:
        return "No hay medicamentos"
        
    lista_nombres = []
    lista_precios = []
    
    # 1. Extraemos los datos en listas paralelas
    for info_interno in medicamentos.values():
        for nombre, precio in info_interno.items():
            lista_nombres.append(nombre)
            lista_precios.append(precio)
            
    # 2. Buscamos el precio más alto de la lista
    precio_mas_alto = max(lista_precios)
    
    # 3. Usamos .index() para saber en qué posición está ese precio
    posicion = lista_precios.index(precio_mas_alto)
    
    # 4. Devolvemos el nombre que está en esa misma posición
    return [lista_nombres[posicion], precio_mas_alto]

def minimo_valor(medicamentos):
    if not medicamentos:
        return "No hay medicamentos"
        
    lista_nombres = []
    lista_precios = []
    
    # 1. Extraemos los datos en listas paralelas
    for info_interno in medicamentos.values():
        for nombre, precio in info_interno.items():
            lista_nombres.append(nombre)
            lista_precios.append(precio)
            
    # 2. Buscamos el precio más bajo de la lista
    precio_mas_bajo = min(lista_precios)
    
    # 3. Usamos .index() para saber en qué posición está ese precio
    posicion = lista_precios.index(precio_mas_bajo)
    
    # 4. Devolvemos el nombre que está en esa misma posición
    return [lista_nombres[posicion], precio_mas_bajo]

def imprimir_valores(medicamentos):
    lista_valores = [sumar(medicamentos), 
                    promedio(medicamentos), 
                    maximo_valor(medicamentos), 
                    minimo_valor(medicamentos)
                ]
    print('\n'.join([f'Total: {lista_valores[0]}', 
            f'Promedio: {lista_valores[1]}', 
            f'Medicamento mas costoso:{lista_valores[2]}',
            f'Medicamento mas barato:{lista_valores[3]}',
        ]))

        
main()
imprimir_medicamentos(medicamentos)
medicamentos = {'123456789':{'Acetaminofen' : 2.50}}
imprimir_valores(medicamentos)