#Exercício Python 013: Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input("Informe o salario do funcionario"))

aumento = salario * 0.15
novoSalario = salario + aumento

print("O novo salario do funcionario é de: R${}".format(novoSalario))