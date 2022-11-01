#Exercício Python 065: Crie um programa que leia vários números inteiros pelo teclado. No final da execução,
# mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

valor = 0
contador = 1
soma = 0
exec = 1
valores = []
media = 0
i = 0

valor = int(input("Digite um valor: "))

maior = valor
menor = valor

while exec == 1:

    soma += valor

    valores.append(valor)

    for i in range(len(valores)):
        if valores[i] > maior:
            maior = valores[i]
        if valores[i] < menor:
            menor = valores[i]

    continuar = input("Quer continuar? (S/N)").upper()
    if continuar == 'S':
        valor = int(input("Digite um valor: "))
        contador += 1
    elif continuar == 'N':
        exec = 0
    else:
        print("Valor invalido")

media = soma / contador
print("Voce digitou {} valores, a soma total foi {} a media {} o maior valor {} e o menor {}".format(contador, soma, media, maior, menor))