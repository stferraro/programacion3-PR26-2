import statistics

def add_medicamento(nombre_medicamento):
    nombre_medicamento = nombre_medicamento.capitalize()
    if nombre_medicamento in medicamentos.keys():
        print('Medicamentos ya existe, se actualizará el precio')
        precio = float(input('Precio: '))
        medicamentos[nombre_medicamento] = precio
    else:
        precio = float(input('Precio: '))
        medicamentos[nombre_medicamento] = precio


def main():
    nombre_medicamento = input('Nombre del medicamento(no para salir): ')
    while nombre_medicamento != 'no':
        add_medicamento(nombre_medicamento)
        nombre_medicamento = input('Nombre del medicamento(no para salir): ')
        if nombre_medicamento.lower() == 'no':
            print('Saliste del sistema')
            break
        
def imprimir_medicamentos(medicamentos):
    for nombre, precio in medicamentos.items():
        print(f'Nombre: {nombre} | Precio: ${precio:.2f}')
    print("-" * 30)
        
        
def sumar(medicamentos):
    precios = list(medicamentos.values())
    total = sum(precios) 
    return total 

def promedio(medicamentos):
    lista_precios = list(medicamentos.values())
    return statistics.mean(lista_precios)

def maximo_valor(medicamentos):
    return max(medicamentos.keys(), key=medicamentos.get)
    
def minimo_valor(medicamentos):
    return min(medicamentos.keys(), key=medicamentos.get)

def imprimir_valores(medicamentos):
    lista_valores = [sumar(medicamentos), 
                    promedio(medicamentos), 
                    maximo_valor(medicamentos), 
                    minimo_valor(medicamentos)
                ]
    print('\n'.join([f'Total: {lista_valores[0]}', 
            f'Promedio: {lista_valores[1]:.2f}', 
            f'Medicamento mas costoso:{lista_valores[2]}',
            f'Medicamento mas barato:{lista_valores[3]}',
        ]))

medicamentos = {}       
main()
imprimir_medicamentos(medicamentos)
imprimir_valores(medicamentos)