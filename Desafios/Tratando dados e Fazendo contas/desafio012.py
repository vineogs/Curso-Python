#Exercício Python 012: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

valor = float(input("Informe o valor do produto: "))

desconto = valor * 0.05
valorDescontado = valor - desconto

print("O novo preço do produto é de R${}".format(valorDescontado))