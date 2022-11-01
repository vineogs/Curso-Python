#Exercício Python 006: Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

valor = int(input('Informe um valor: '))

dobro = valor * 2
triplo = valor * 3
raiz = valor**(1/2)

print("O dobro de {} é {}, o triplo {} e a raiz {}".format(valor, dobro, triplo, raiz))