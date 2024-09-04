class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def detalhes(self):
        return f"Título: {self.titulo}\nAutor: {self.autor}"

livro = Livro("Cabeça Fria, Coração Quente.", "Abel Ferreira")


informacoes = livro.detalhes()

print(informacoes)
