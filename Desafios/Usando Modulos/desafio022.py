#Exercício Python 022: Crie um programa que leia o nome completo de uma pessoa e mostre:
#- O nome com todas as letras maiúsculas e minúsculas.
#- Quantas letras ao todo (sem considerar espaços).
#- Quantas letras tem o primeiro nome.

nome = input("Digite seu nome completo: ")
print("{}".format(nome.upper()))
print("{}".format(nome.lower()))
completo = len(''.join(nome.split()))
print("Quantidade de letras sem espaço: {}".format(completo))
primeiro = nome.split()
print("Quantidade de letras do primeiro nome: {}".format(len(primeiro[0])))
