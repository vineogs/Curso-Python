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