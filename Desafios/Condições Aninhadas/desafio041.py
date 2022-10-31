from datetime import date

anoAtual = date.today().year

anoNascimento = int(input("Informe o ano de nascimento: "))

idade = anoAtual - anoNascimento

if idade <= 9:
    print("Competitor mirim")
elif idade <= 14:
    print("Competidor infatil")
elif idade <= 19:
    print("Competidor junior")
elif idade <= 25:
    print("Competidor senior")
else:
    print("Competidor master")