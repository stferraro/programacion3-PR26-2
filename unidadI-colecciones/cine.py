'''sistema que simula la venta de boletos en un cine, en este escenario se tienen una lista de salas, 
cada sala tiene 40 asientos y esta identificada por una letra por ejemplo A, cada asiento se identifica
por un nombre cuyo formato es el siguiente: letra de la sala seguida del numero del asiento por ejemplo A1, A2, A3, etc.
en cada sala se ven diferentes peliculas, cada pelicula tiene un nombre, una duracion un horario.
el sistema simula la compra del boleto, por ende se seleciona la pelicula , la sala y el asiento, se visualiza si el asiento esta disponible
si no lo esta se muestra un mensaje de error, si el asiento esta disponible se muestra un mensaje de compra exitosa y se visualiza el boleto 
con el nombre de la pelicula, el horario, la sala y el asiento comprado, y el precio que es de 10 dolares si la persona a comprarlo tienen entre 5 y 18 años,
si tiene entre 19 y 60 años el precio es de 15 dolares, si tiene mas de 60 años el precio es de 12 dolares para menores de 5 años el boleto es gratis,
se debe validar que la edad ingresada sea un numero entero positivo, en caso de no serlo se muestra un mensaje de error el sistema debe tambien agregar el 16% 
de impuestos al precio final del boleto.
'''

import datetime

salas = []
asientos = []
peliculas = {}

def datos_salas(num_salas):
    for i in range(0, num_salas):
        nombre_sala = input("Nombre de la sala(ejemp. A, B)")
        salas.append(nombre_sala.upper())
        
def agrega_asientos(num_salas):
        for j in range (0, 41):
            for z in salas:
                indice = salas.index(z)
                sala = salas[indice]
                asientos.append(sala+str(j))
                
def agrega_pelicula(num_peliculas):
    for i in range (0, num_peliculas):
        nombre_pelicula = input('Nombre de la pelicula: ')
        horario = input('Horario: ')
        hora = int(horario[0:2])
        minutos = int(horario[3:5])
        horario = datetime.time(hora, minutos)
        peliculas[nombre_pelicula] = horario
        
def calcula_precio(edad):
    if edad > 0 and edad <=5:
        return 0
    elif edad > 5 and edad >= 18:
        return 10
    elif edad < 19 and edad >= 60:
        return 15
    else:
        return 12
    
def search_film():
    while True:
        pelicula = input('Nombre de la película: ')
        if pelicula in peliculas:
            return pelicula
        else:
            print('Película no encontrada. Intente de nuevo.')

def search_asiento(asiento):
    while True:
        if asiento in asientos:
            return asiento
        else:
            print('Asiento no disponible')

def search_sala(sala):
    while True:
        if sala in salas:
            return sala
        else:
            print('Sala no disponible')
    
def imprimir_datos(nombre, cedula, edad, precio, pelicula, sala, asiento, horario):
    print('Datos DEL BOLETO')
    print('****************')
    print(f'Pelicula: {pelicula}')
    print(f'Horario: {horario}')
    print(f'Nombre: {nombre}')
    print(f'Cedula: {cedula}')
    print(f'Edad: {edad}')
    print(f'Sala: {sala}')
    print(f'Asiento: {asiento}')
    print(f'Precio: {precio:.2f}$$')
    

def main():
    num_salas = int(input('Numero de salas en el cine: '))
    datos_salas(num_salas)
    agrega_asientos(num_salas)
    num_peliculas = int(input('Peliculas disponibles: '))
    agrega_pelicula(num_peliculas)
    while True:
        nombre_completo = input('Nombre del cliente: ')
        cedula = input('Cedula: (Ejem:V-123456789 )')
        edad = int(input('Edad de la persona: '))
        sala = input(f'Selecciona la sala: {salas} ')
        asiento = input(f'Selecciona el asiento: {asientos} ')
        pelicula = search_film()
        sala = search_sala(sala)
        asiento = search_asiento(asiento)
        precio = calcula_precio(edad)
        horario = peliculas.get(pelicula)
        hora = horario.strftime('%H:%M')
        lista_datos = [nombre_completo, cedula, edad, precio, pelicula, sala, asiento, hora]
        imprimir_datos(*lista_datos)
        asientos.remove(asiento)
        valor = input('Desea comprar otro boleto? (S/N) ')
        if valor.upper() == 'N':
            print('Gracias por su compra, vuelva pronto!')
            break
    
main()  







