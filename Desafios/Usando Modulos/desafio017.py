#Exercício Python 017: Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.

from math import hypot
cat1 = float(input("Digite o valor do cateto oposto: "))
cat2 = float(input("Digite o valor do cateto adjacente: "))

hip = hypot(cat1, cat2)

print("A hipotenusa é: {:.2f}".format(hip))