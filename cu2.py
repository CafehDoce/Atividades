
class Livro:
    def __init__(self, titulo, autor, ano_publicado):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicado = ano_publicado

    def descricao (self):
        print (f"Título: {self.titulo}, Autor: {self.autor}, Publicado: {self.ano_publicado}.")

livro2 = Livro ('Nome livro 2', 'Dieimes', 2023)
livro3 = Livro ('Nome livro 3', 'Dieimes', 2023)

print (livro2.descricao())
print (livro3.descricao())