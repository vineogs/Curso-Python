#Exercício Python 016: Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.

from math import trunc
real = float(input("Digite um valor Real (utlizando .)"))

print("A parte real de {} é: {}".format(real, trunc(real)))