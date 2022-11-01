nome = []
idade = []
sexo = []

soma = 0

for i in range(4):
    nome.append(input("Digite o nome: "))
    idade.append(int(input("Digite a idade: ")))
    sexo.append(input("Sexo: (F) (M)").lower())

for a in range(4):
    soma += idade[a]
media = soma / 4

velho = idade[0]
Mvelho = nome[0]

for b in range(4):
    if sexo[b] == "m":
        if idade[b] > velho:
            velho = idade[b]
            Mvelho = nome[b]
novas = 0

for c in range(4):
    if sexo[c] == "f":
        if idade[c] < 20:
            novas += 1

print("A média de idade do grupo é {}\n"
      "o homem mais velho é {}\n"
      "tem {} mulheres com menos de 20 anos.".format(media, Mvelho, novas))
