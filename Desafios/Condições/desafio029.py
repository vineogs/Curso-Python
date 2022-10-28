velocidade = float(input("Velocidade do carro: "))

if velocidade > 80:
    print("Você foi multado!")
    multa = (velocidade - 80) * 7
    print("O valor da multa é de: R${:.2f}".format(multa))

