# Exercício Python 039: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua
# idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do
# alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

anoAtual = date.today().year

anoNascimento = int(input("Informe o ano de nascimento: "))

idade = anoAtual - anoNascimento

if idade == 18:
    print("Você está na idade de se alistar")
elif idade < 18:
    diferenca = 18 - idade
    print("Você ainda não vai se alistar, faltam {} anos".format(diferenca))
elif idade > 18:
    diferenca = idade - 18
    print("Você já deveria ter se alistado, você passou {} anos do prazo".format(diferenca))