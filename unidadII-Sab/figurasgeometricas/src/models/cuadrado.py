from src.models.figura_geometrica import FiguraGeometrica


class Cuadrado(FiguraGeometrica):
    
    def __init__(self, lado):
        self.lado = lado
    
    def get_area(self):
        return self.lado ** 2
    
    def get_perimetro(self):
        return 4 * self.lado
    
    def __str__(self):
        return f"Cuadrado: lado = {self.lado:.2f}, área = {self.get_area():.2f}, perímetro = {self.get_perimetro():.2f}"