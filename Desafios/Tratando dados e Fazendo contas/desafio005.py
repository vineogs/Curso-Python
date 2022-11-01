#Exercício Python 005: Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor.

valor = int(input('Informe um valor: '))

ante = valor - 1
suce = valor + 1

print("O antecessor de {} é {} e o sucessor é {}".format(valor, ante, suce))