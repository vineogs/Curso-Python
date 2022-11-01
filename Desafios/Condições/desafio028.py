#Exercício Python 028: Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

import random
random.seed

numero = random.randint(0, 5)

chute = int(input("Digite seu chute: "))

if chute == numero:
    print("PARABENS, você ganhou!!!")
else:
    print("Sinto muito, você perdeu!")
