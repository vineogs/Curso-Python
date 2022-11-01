#Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial.

valor = int(input("Digite o valor a ser fatorado: "))
fator = valor - 1

while fator > 1:
    valor *= fator
    fator -= 1

print(valor)