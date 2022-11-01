#Exercício Python 061: Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

pt = int(input("Digite o primeiro termo: "))
raz = int(input("Digite a razão: "))
contador = 1

while contador <= 10:
    print(pt)
    pt += raz
    contador += 1