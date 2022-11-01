#Exercício Python 66: Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).

contador = 0
resultado = 0

while True:
    valor = int(input("Digite um valor: "))
    if valor == 999:
        break
    contador += 1
    resultado += valor

print(f"Voce digitou {contador} numeros e a soma entre todos eles foi de {resultado}")