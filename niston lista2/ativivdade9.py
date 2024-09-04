class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def calcular_perimetro(self):
        return self.lado1 + self.lado2 + self.lado3

# Exemplo de uso
triangulo1 = Triangulo(lado1=5, lado2=7, lado3=10)
print(f"Lado 1: {triangulo1.lado1}")
print(f"Lado 2: {triangulo1.lado2}")
print(f"Lado 3: {triangulo1.lado3}")
print(f"Perímetro do triângulo: {triangulo1.calcular_perimetro()}")
