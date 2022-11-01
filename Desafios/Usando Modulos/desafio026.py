#Exercício Python 026: Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A", em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

frase = str(input("Digite uma frase: ")).lower().strip()

print("Quantidades de letras A: {}".format(frase.count("a")))
print("A Primeira letra A apareceu na posição: {}".format(frase.find("a")+1))
print("A Primeira letra A apareceu na posição: {}".format(frase.rfind("a")+1))
