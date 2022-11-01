#Exercício Python 030: Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

numero = int(input("Informe um valor: "))

if numero % 2 == 0:
    print("Número par!")
else:
    print("Número impar!")
