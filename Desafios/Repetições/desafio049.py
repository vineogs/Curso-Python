valor = int(input("Digite um valor: "))

print("Tabudada de {}".format(valor))
for i in range(1 , 11):
    print("{} * {} = {}".format(valor, i, valor * i))