#Exercício Python 031: Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

distancia = float(input("Informe a distancia da viagem: "))

if distancia <= 200:
    passagem = distancia * 0.5
else:
    passagem = distancia * 0.45
print("O preço da passagem é de: R${:.2f}".format(passagem))
