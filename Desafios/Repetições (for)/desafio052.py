#Exercício Python 052: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

valor = int(input("Digite um valor: "))
total = 0
for i in range(1, valor + 1):
    if total % i == 0:
        total += 1
    print("{}".format(i))
print("O número {} foi divisivel {} vezes".format(valor, total))
if total == 2:
    print("E por isso ele é Primo!")
else:
    print("E por isso ele não é primo!")