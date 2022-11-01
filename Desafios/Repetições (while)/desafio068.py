#Exercício Python 68: Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint

vitorias = 0

while True:

    parImpar = int(input('Escolha Par(1) ou Impar(2): '))

    jogadaComputador = randint(1, 10)

    jogadaJogador = int(input('Faça sua jogada: '))

    soma = jogadaComputador + jogadaJogador

    print(f'\nJogada do jogador {jogadaJogador} x Jogada do Computador {jogadaComputador}\n'
          f'Resultado = {soma}')

    if parImpar == 1:
        if soma % 2 == 0:
            vitorias += 1
            print("Jogador Venceu!\n")
            print("PROXIMA RODADA!")
        elif soma % 2 != 0:
            print('Jogador Perdeu!')
            break
    elif parImpar == 2:
        if soma % 2 != 0:
            vitorias += 1
            print("Jogador Venceu!\n")
            print("PROXIMA RODADA!")
        else:
            print('Jogador Perdeu!')
            break

print(f'Fim de jogo, jogador ganhou {vitorias} rodadas consecutivas')
