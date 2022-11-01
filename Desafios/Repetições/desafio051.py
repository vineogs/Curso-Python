pt = int(input("Digite o primeiro termo: "))
raz = int(input("Digite a razão: "))
decimo = pt + (10 -1) * raz

for i in range(pt, decimo, raz):
    print('{}'.format(i))