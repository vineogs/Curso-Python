#Exercício Python 020: O mesmo professor do desafio 019 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

import random
random.seed

aluno1 = input("Qual o primeiro aluno? ")
aluno2 = input("Qual o segundo aluno? ")
aluno3 = input("Qual o terceiro aluno? ")
aluno4 = input("Qual o quarto aluno? ")

lista = [aluno1, aluno2, aluno3, aluno4]

random.shuffle(lista)

print("A sequencia de apresentação será: {}".format(lista))