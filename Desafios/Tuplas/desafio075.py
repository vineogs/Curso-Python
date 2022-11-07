n1 = int(input("Digite um numero: "))
n2 = int(input("Digite um numero: "))
n3 = int(input("Digite um numero: "))
n4 = int(input("Digite um numero: "))

tupla = (n1, n2, n3, n4)

print(f'O numero 9 apareceu {tupla.count(9)} vezes')
if n1 == 3 or n2 == 3 or n3 == 3 or n4 == 3:
    print(f'A primeira vez que o numero 3 apareceu foi na casa {tupla.index(3)}')
else:
    print('Nao teve numero 3')
print(f'O numeros pares foram: ', end= " ")
for i in tupla:
    if i % 2 == 0:
        print(i, end=" ")