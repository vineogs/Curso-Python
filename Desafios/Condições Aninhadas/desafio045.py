from random import choice

jogadas = ["pedra", "papel", "tesoura"]

computador = choice(jogadas)

jogada = int(input("JOGUE!\n"
                   "1 - Pedra\n"
                   "2 - Papel\n"
                   "3 - Tesoura"))

if jogada == 1 and computador == "pedra" or jogada == 2 and computador == "papel" or jogada == 3 and computador == "tesoura":
    print("EMPATE")
    print("jogada do computador: {}".format(computador))
elif jogada == 1 and computador == "papel" or jogada == 2 and computador == "tesoura" or jogada == 3 and computador == "pedra":
    print("Você perdeu")
    print("jogada do computador: {}".format(computador))
elif jogada == 1 and computador == "tesoura" or jogada == 2 and computador == "pedra" or jogada == 3 and computador == "papel":
    print("Você vencdeu!")
    print("jogada do computador: {}".format(computador))