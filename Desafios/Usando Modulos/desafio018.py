#Exercício Python 018: Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import radians, sin, cos, tan
angulo = float(input("Informe o ângulo: "))
seno = sin(radians(angulo))
coseno = cos(radians(angulo))
tangente = tan(radians(angulo))

print("o seno de {} é {:.2f}, o cosseno {:.2f} e a tangente {:.2f}".format(angulo, seno, coseno, tangente))
