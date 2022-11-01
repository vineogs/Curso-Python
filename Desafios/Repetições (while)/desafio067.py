#Exercício Python 67: Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.

while True:
    tabuada = int(input('Digite um valor(-1 para sair): '))
    if tabuada < 0:
        break
    for i in range(1, 11):
        print(f'{tabuada} * {i} = {tabuada * i}')