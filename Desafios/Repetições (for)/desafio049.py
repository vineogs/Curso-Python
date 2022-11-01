#Exercício Python 049: Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora
# utilizando um laço for.

valor = int(input("Digite um valor: "))

print("Tabudada de {}".format(valor))
for i in range(1 , 11):
    print("{} * {} = {}".format(valor, i, valor * i))