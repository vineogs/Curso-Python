salario = float(input("Informe o salario: "))

if salario > 1250:
    aumento = salario + (salario * 0.10)
else:
    aumento = salario + (salario * 0.15)
print("O novo salario é de: R${:.2f}".format(aumento))