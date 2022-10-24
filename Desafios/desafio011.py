largura = float(input("Digite a largura da parede: "))
altura = float(input("Digite a altura da parede: "))

area = largura * altura
tinta = area/2

print("A area da parede é de {}m2 e será necessario {} litros de tinta".format(area,tinta))