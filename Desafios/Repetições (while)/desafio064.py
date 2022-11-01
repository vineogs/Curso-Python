#Exercício Python 064: Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

exec = 1
contador = 0
resultado = 0

while exec == 1:
    valor = int(input("Digite um valor: "))
    if valor != 999:
        contador += 1
        resultado += valor
    elif valor == 999:
        exec = 0

print("Voce digitou {} numeros e a soma entre todos eles foi de {}".format(contador, resultado))