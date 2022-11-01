#Exercício Python 004: Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

algo = input('Digite algo: ')

print(type(algo))
print(algo.isalnum())
print(algo.isalpha())
print(algo.isascii())
print(algo.isdigit())
print(algo.islower())
print(algo.isdecimal())
print(algo.isidentifier())
print(algo.isnumeric())
print(algo.isprintable())
print(algo.isspace())
print(algo.istitle())
print(algo.isupper())

