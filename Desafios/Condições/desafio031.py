distancia = float(input("Informe a distancia da viagem: "))

if distancia <= 200:
    passagem = distancia * 0.5
else:
    passagem = distancia * 0.45
print("O preço da passagem é de: R${:.2f}".format(passagem))
