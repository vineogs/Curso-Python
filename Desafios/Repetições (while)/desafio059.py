#Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
#[ 1 ] somar
#[ 2 ] multiplicar
#[ 3 ] maior
#[ 4 ] novos números
#[ 5 ] sair do programa
#Seu programa deverá realizar a operação solicitada em cada caso.

exec = 1
num1 = 0
num2 = 0

num1 = int(input("Informe um valor: "))
num2 = int(input("Informe outro valor: "))

while exec == 1:
    escolha = int(input("Escolha:\n"
                        "1 - Somar os valores\n"
                        "2 - Multiplicar os valores\n"
                        "3 - Mostrar o maior numero\n"
                        "4 - Digitar novos numeros\n"
                        "5 - Sair do programa"))

    if escolha == 1:
        conta = num1 + num2
        print(conta)
    elif escolha == 2:
        conta = num1 * num2
        print(conta)
    elif escolha == 3:
        if num1 > num2:
            print(num1)
        else:
            print(num2)
    elif escolha == 4:
        num1 = int(input("Informe um valor: "))
        num2 = int(input("Informe outro valor: "))
    elif escolha == 5:
        print("Fim do programa!")
        exec = 0
    else:
        print("Opcao invalida, digite novamente")