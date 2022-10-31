valorCasa = float(input("Qual o valor da casa: "))
salario = float(input("Qual o salario: "))
parcelas = int(input("Vai ser parcelado em quantos anos: "))

meses = 12 * parcelas
valorMensal = valorCasa / meses

if valorMensal > salario * 0.3:
    print("Você não tem condições de comprar essa casa")
elif valorMensal < salario * 0.3:
    print("Você é capaz de comprar essa casa")
