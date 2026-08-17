from ..models import Orden, Computadora, Monitor, Teclado, Mouse

orden = Orden([])

computadora1 = Computadora("HP", Monitor("HP", "24 pulgadas"), Teclado("HP", "USB"), Mouse("HP", "USB"))
computadora2 = Computadora("Gamer", Monitor("Gamer", "27 pulgadas"), Teclado("Gamer", "USB"), Mouse("Gamer", "USB"))
computadora3 = Computadora("Oficina", Monitor("Oficina", "22 pulgadas"), Teclado("Oficina", "USB"), Mouse("Oficina", "USB"))

orden.agregarComputadora(computadora1)
orden.agregarComputadora(computadora2)
orden.agregarComputadora(computadora3)

print(orden)