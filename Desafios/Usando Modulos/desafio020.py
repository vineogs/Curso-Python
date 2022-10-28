import random
random.seed

aluno1 = input("Qual o primeiro aluno? ")
aluno2 = input("Qual o segundo aluno? ")
aluno3 = input("Qual o terceiro aluno? ")
aluno4 = input("Qual o quarto aluno? ")

lista = [aluno1, aluno2, aluno3, aluno4]

random.shuffle(lista)

print("A sequencia de apresentação será: {}".format(lista))