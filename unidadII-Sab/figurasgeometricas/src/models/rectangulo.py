from src.models.figura_geometrica import FiguraGeometrica


class Rectangulo(FiguraGeometrica):
    
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def get_area(self):
        return self.base * self.altura
    
    def get_perimetro(self):
        return 2 * (self.base + self.altura)
    
    def __str__(self):
        return f"Rectángulo: base = {self.base:.2f}, altura = {self.altura:.2f}, área = {self.get_area():.2f}, perímetro = {self.get_perimetro():.2f}"