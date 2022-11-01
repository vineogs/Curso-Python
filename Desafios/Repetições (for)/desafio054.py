#Exercício Python 054: Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas
# ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date
anoAtual = date.today().year
maior = 0
menor = 0

for i in range(1, 8):
    ano = int(input("Digite o ano de nascimento: "))
    if anoAtual - ano >= 18:
        maior += 1
    else:
        menor += 1
print("Tem {} pessoas de menor e {} pessoas de maior".format(menor, maior))
