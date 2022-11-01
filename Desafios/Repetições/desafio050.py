soma = 0

for i in range(1, 7):
    valor = int(input("Digite um valor: "))
    if valor % 2 == 0:
        soma = soma + valor
print(soma)