import random
random.seed

numero = random.randint(0, 5)

chute = int(input("Digite seu chute: "))

if chute == numero:
    print("PARABENS, você ganhou!!!")
else:
    print("Sinto muito, você perdeu!")
