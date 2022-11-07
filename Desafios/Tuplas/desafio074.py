from random import randint

n1 = randint(0,10)
n2 = randint(0,10)
n3 = randint(0,10)
n4 = randint(0,10)
n5 = randint(0,10)

tupla = (n1, n2, n3, n4, n5)

lista = sorted(tupla)
print(tupla)
print(f"Menor valor = {lista[0]}")
print(f"Maior valor = {lista[4]}")