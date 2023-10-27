class Caneta:
    def __init__(self, cor):
        self.cor = cor
        self.dono = None

class Pessoa:
    def __init__(self, nome):
        self.nome = nome
        self.caneta = None
    
    def pegar_caneta (self, caneta):
        self.caneta = caneta
        caneta.dono = self

pessoa1 = Pessoa ("Mikael")
caneta1 = Caneta ("Rosa")

pessoa1.pegar_caneta(caneta1)
print(pessoa1.nome)