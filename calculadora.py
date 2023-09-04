nome = input ("Digite seu nome: ")
print ("Seja bem vindo a calculadora, {}!" .format(nome))

n1 = int (input ("Digite um número: "))
n2 = int (input ("Digite outro número: "))
calculo = input ("Opções de cálculo: +,-,*,/: ")

if calculo == "+" :
    print ("Seu resultado é:", n1 + n2)

if calculo == "-":
    print ("Seu resuldado é", n1 - n2)

if calculo == "*":
    print ("Seu resuldado é", n1 * n2)

if calculo == "/":
    print ("Seu resuldado é", n1 / n2)