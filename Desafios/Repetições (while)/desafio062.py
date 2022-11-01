#Exercício Python 062: Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.

pt = int(input("Digite o primeiro termo: "))
raz = int(input("Digite a razão: "))
contador = 0

termos = 10

while contador < termos:
    print(pt)
    pt += raz
    contador += 1
    if contador == termos:
        termos = int(input("Voce quer mais quantos termos: "))
        contador = 0