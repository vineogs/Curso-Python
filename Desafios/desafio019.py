import random
aluno1 = input("Qual o primeiro aluno? ")
aluno2 = input("Qual o segundo aluno? ")
aluno3 = input("Qual o terceiro aluno? ")
aluno4 = input("Qual o quarto aluno? ")

random.seed

lista = [aluno1, aluno2, aluno3, aluno4]
sorteado = random.choice(lista)

print("Quem vai apagar o quadro é: {}".format(sorteado))