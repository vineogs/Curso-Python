#Exercício Python 057: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto.

exec = 1

while exec == 1:
    sexo = input("Digite o sexo da pessoa (F) (M): ").upper()
    if sexo == 'F':
        print("Sexo feminino selecionado!")
        exec = 0
    elif sexo == 'M':
        print("Sexo masculino selecionado!")
        exec = 0
    else:
        print("Valor invalido, por favor digitar novamente: ")