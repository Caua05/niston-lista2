class Aluno:
    def __init__(self, nome, notas):
        self.nome = nome
        self.notas = notas

    def calcular_media(self):
        if not self.notas:  
            return 0
        return sum(self.notas) / len(self.notas)


aluno1 = Aluno(nome="Maria", notas=[8.5, 7.0, 9.0, 6.5])
print(f"Nome: {aluno1.nome}")
print(f"Média das notas: {aluno1.calcular_media():.2f}")
