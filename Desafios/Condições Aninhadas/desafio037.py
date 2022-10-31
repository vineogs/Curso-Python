valor = int(input("Digite um valor"))

escolha = int(input("Conversão: \n1 - Binario\n2 - Octal\n3 - Hexadecimal"))

if escolha == 1:
    print("{} convertido para binario é {}".format(valor, bin(valor) [2:]))
elif escolha == 2:
    print("{} convertido para octal é {}".format(valor, oct(valor) [2:]))
elif escolha == 3:
    print("{} convertido para hexadecimal é {}".format(valor, hex(valor)[2:]))