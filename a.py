
class Estudante:
    def __init__ (self, nome, idade):
        self.nome= nome
        self.idade = idade
    
    def apresentar(self):
        print(f"O nome do estudante é {self.nome} e sua idade é {self.idade}.")

estudante1 = Estudante ("Isa", 18)
estudante1.apresentar()


class Livro:
    def __init__(self, titulo, autor, ano_publicado):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicado = ano_publicado
    
    def descricao (self):
        print (f"O livro entitulado {self.titulo} foi escrito pelo autor {self.autor} e foi publicado em {self.ano_publicado}.")

livro1 = Livro ("Meu livro, eu que escrevi,", "Dani,", "13/05/2004")
livro1.descricao()

