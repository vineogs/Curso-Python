#Exercício Python 058: Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

import random
random.seed

numero = random.randint(0, 10)
acertou = 0
tentativas = 1

while acertou == 0:
    chute = int(input("Digite seu chute: "))

    if chute == numero:
        print("Voce acertou")
        acertou = 1
    else:
        print("Voce errou, tente novamente.")
        tentativas += 1

print("Voce terminou com {} tentativas.".format(tentativas))