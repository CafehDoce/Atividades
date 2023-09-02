def limparTela():
        import os
        os.system ("cls")

limparTela()
print("Boa Noite.")

def soma (numero1, numero2):
        print(numero1 + numero2)

soma (2,3)



def soma2 (numero11, numero2):
    return numero11 + numero2

resultado = soma2 (3,3)

print (resultado)



def exemplo(a, b, c):
       print(a, b, c)

exemplo(1, 2, 3)



def exemplo(a, b, c):
       print(a, b, c)
exemplo(a=1, c=3, b=2)



def minha_funcao(*args):
    for arg in args:
        print(arg)
    print(type(arg))

minha_funcao(1, 2, 3, 4)

def minha_funcao(**kwargs):
    for chave, valor in kwargs.items():
        print(f"A chave é {chave} e o valor é {valor}")
    print(type(kwargs))

minha_funcao(nome="João", idade=15, pais="Brasil" )



def minha_funcao():
      return "Função do modulo"

if __name__ == '__main__':
      print("Este script esta sendo execudato sozinho")

else: 
      print("Este script foi importado!")