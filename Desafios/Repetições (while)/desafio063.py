#Exercício Python 063: Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci.

num = int(input("Digite um valor: "))
ante = 0

contador = 0
termos = int(input("Quantos termos serao mostrados: "))

while contador < termos:
    resultado = num + ante
    ante = num
    num = resultado
    contador += 1

print(resultado)