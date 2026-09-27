from src.models.figura_geometrica import FiguraGeometrica


class Triangulo(FiguraGeometrica):

    def __init__(self, lado1, lado2, lado3):
        if lado1 + lado2 <= lado3 or lado1 + lado3 <= lado2 or lado2 + lado3 <= lado1:
            raise ValueError(
                "Los lados no forman un triángulo válido: la suma de dos lados "
                "siempre debe ser mayor que el tercero."
            )
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def get_area(self):
        semiperimetro = self.get_perimetro() / 2
        return (
            semiperimetro
            * (semiperimetro - self.lado1)
            * (semiperimetro - self.lado2)
            * (semiperimetro - self.lado3)
        ) ** 0.5

    def get_perimetro(self):
        return self.lado1 + self.lado2 + self.lado3

    def __str__(self):
        return f"Triángulo: lado1 = {self.lado1:.2f}, lado2 = {self.lado2:.2f}, lado3 = {self.lado3:.2f}, área = {self.get_area():.2f}, perímetro = {self.get_perimetro():.2f}"
