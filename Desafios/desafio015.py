km = float(input("Informe os quilometros rodados: "))
dias = int(input("Quantos dias foram alugados: "))

aluguel = (km * 0.15) + (dias * 60)

print("O valor do aluguel fica de R${}".format(aluguel))
