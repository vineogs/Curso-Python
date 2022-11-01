#Exercício Python 014: Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

cel = float(input("Digite o valor em celsius: "))

far = (cel * (9/5)) + 32

print("{}C são {}F".format(cel, far))