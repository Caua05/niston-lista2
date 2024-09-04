class Funcionario:
    def __init__(self, nome, salario, cargo):
        self.nome = nome
        self.salario = salario
        self.cargo = cargo

    def aumentar_salario(self, percentual):
        if percentual < 0:
            raise ValueError("O percentual de aumento não pode ser negativo.")
        aumento = self.salario * (percentual / 100)
        self.salario += aumento

    def __str__(self):
        return (f"Nome: {self.nome}\n"
                f"Salário: R${self.salario:.2f}\n"
                f"Cargo: {self.cargo}")


funcionario1 = Funcionario(nome="Cauã", salario=3000.00, cargo="Analista")
print(funcionario1)
funcionario1.aumentar_salario(10)
print("\nApós aumento:")
print(funcionario1)
