#Exercício Python 055: Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor
# peso lidos.

pesos = []

for i in range(5):
    valor = float(input("Digite o peso: "))
    pesos.append(valor)

maior = pesos[0]
menor = pesos[0]

for f in range(len(pesos)):
    if pesos[i] > maior:
        maior = pesos[i]
    if pesos[i] < menor:
        menor = pesos[i]

print("O maior valor é {} e o menor valor é {}".format(maior,menor))