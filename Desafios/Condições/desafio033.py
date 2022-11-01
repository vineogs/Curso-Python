#Exercício Python 033: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

n1 = int(input("Digite um valor: "))
n2 = int(input("Digite um valor: "))
n3 = int(input("Digite um valor: "))

if n1 > n2 and n1 > n3:
    print("O maior número é: {}".format(n1))
elif n2 > n3:
    print("O maior número é: {}".format(n2))
else:
    print("O maior número é: {}".format(n3))
