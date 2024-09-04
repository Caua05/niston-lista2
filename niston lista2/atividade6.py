class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def calcular_total(self):
        return self.preco * self.quantidade

# Exemplo de uso
produto1 = Produto(nome="Laptop", preco=1500.00, quantidade=3)
print(f"Nome: {produto1.nome}")
print(f"Preço unitário: R${produto1.preco}")
print(f"Quantidade: {produto1.quantidade}")
print(f"Valor total: R${produto1.calcular_total()}")
