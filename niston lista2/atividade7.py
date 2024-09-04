class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def detalhes(self):
        return f"Marca: {self.marca}\nModelo: {self.modelo}\nAno: {self.ano}"


carro1 = Carro(marca="Ferrari", modelo="488 Pista", ano=2019)
print(carro1.detalhes())
