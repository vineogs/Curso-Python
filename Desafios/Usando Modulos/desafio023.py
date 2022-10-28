valor = int(input("Digite um número entre 0 e 9999: "))
unidade = valor // 1 % 10
dezena = valor // 10 % 10
centena = valor // 100 % 10
milhar = valor // 1000 % 10
print("Unidade: {}\nDezena: {}\nCentena: {}\nMilhar: {}\n".format(unidade, dezena, centena, milhar))