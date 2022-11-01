#Exercício Python 034: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input("Informe o salario: "))

if salario > 1250:
    aumento = salario + (salario * 0.10)
else:
    aumento = salario + (salario * 0.15)
print("O novo salario é de: R${:.2f}".format(aumento))