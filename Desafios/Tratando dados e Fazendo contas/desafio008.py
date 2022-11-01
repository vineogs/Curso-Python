#Exercício Python 008: Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

metros = float(input('Informe um valor em metros: '))

cent = metros * 100
mil = metros * 1000

print("{} metros são: {} centimetros e {} milimetros".format(metros,cent,mil))