#Exercício Python 69: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:

#A) quantas pessoas tem mais de 18 anos.

#B) quantos homens foram cadastrados.

#C) quantas mulheres tem menos de 20 anos.

idade = []
sexo = []

velhos = 0
homens = 0
novas = 0

while True:
    idade.append(int(input("Digite a idade da pessoa: ")))

    sexo.append(str(input("Digite agora o sexo dela (F/M): ")).strip().lower())

    continuar = str(input('Cadastrar mais pessoas? (S/N)')).strip().lower()

    if continuar == 'n':
        break

for i in range(len(idade)):
    if idade[i] >= 18:
        velhos += 1
    if sexo[i] == 'm':
        homens += 1
    if sexo[i] == 'f' and idade[i] < 20:
        novas += 1

print(f'Tem {velhos} pessoas com mais de 18 anos\n'
      f'{homens} homens cadastrados\n'
      f'{novas} mulheres com menos de 20 anos cadastradas')