jugadores= {}
resultados = {}
acumulador_dinero = {}

def agregar_jugador():
    cedula = input("Ingrese la cedula de la persona")
    while cedula in jugadores.keys():
        cedula = input("error, Ingrese la cédula del jugador: ")
    else:
        nombre_completo = input("Ingrese el nombre completo del jugador: ")
        jugadores[cedula] = nombre_completo
    
def agregar_resultado(cedula):
    posicion = int(input("Ingrese la posición del jugador en el torneo (1, 2, 3 o cualquier otro número): "))
    if posicion == 1 :
        puntos = 25
    elif posicion == 2:
        puntos = 18
    elif posicion == 3:
        puntos = 12
    else:
        puntos = 0
    resultados[cedula] = puntos
    
def asignar_dinero(cedula):
    posicion = resultados.get(cedula, 0)
    if posicion == 1 :
        dinero = 1000
    elif posicion == 2:
        dinero = 500
    elif posicion == 3:
        dinero = 250
    else:        
        dinero = 0
    acumulador_dinero[cedula] = acumulador_dinero.get(cedula, 0) + dinero
    return acumulador_dinero[cedula]

def imprimir_resultados():
    print("Resultados del torneo:")
    for cedula, puntos in resultados.items():
        nombre_completo = jugadores[cedula]
        dinero = asignar_dinero(cedula)
        print(f"Jugador: {nombre_completo}, Cédula: {cedula}, Puntos: {puntos}, Dinero ganado: {dinero}$$")
        
def main():
    num_jugadores = int(input("Ingrese el número de jugadores: "))
    for _ in range(num_jugadores):
        agregar_jugador()
    for cedula in jugadores.keys():
        cedula = input("Ingrese la cédula del jugador para asignar su posición: ")
        agregar_resultado(cedula)
        
    print(jugadores)
    print(resultados)
    
main()