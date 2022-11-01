#Exercício Python 70: Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:

#A) qual é o total gasto na compra.

#B) quantos produtos custam mais de R$1000.

#C) qual é o nome do produto mais barato.

produto = []
preco = []

soma = 0
caro = 0

while True:
    produto.append(str(input('Digite o nome do produto: ')).strip().lower())
    preco.append(float(input('Preco do produto: ')))

    continuar = str(input('Continuar? (S/N)')).strip().lower()

    if continuar == 'n':
        break

for i in range(len(produto)):
    soma += preco[i]

    if preco[i] > 1000:
        caro += 1

preco.sort()

print(f'A soma dos produtos foi {soma}\n'
      f'Tem {caro} produtos com mais de R%1000,00\n'
      f'O Produto mais caro custa R${preco[0]:.2f}')