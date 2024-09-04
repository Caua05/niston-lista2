import math

class Circulo:
    def __init__(self, raio):
        self.raio = raio

    def calcular_area(self):
        return math.pi * (self.raio ** 2)

circulo = Circulo(5)
        
area = circulo.calcular_area()

print(f"A área do círculo é: {area:.2f}")
