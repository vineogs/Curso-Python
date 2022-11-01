#Exercício Python 051: Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10
# primeiros termos dessa progressão.

pt = int(input("Digite o primeiro termo: "))
raz = int(input("Digite a razão: "))
decimo = pt + (10 -1) * raz

for i in range(pt, decimo, raz):
    print('{}'.format(i))