preco = float(input("Qual o valor do produto? "))

dinheiroCheque = preco - (preco * .1)
vistaCartao = preco - (preco * .05)
cartao3x = preco + (preco * 0.2)

escolha = int(input("Escolha o metodo de pagamento:\n"
      "1 - A vista (Dinheiro ou Cheque) 10% desconto\n"
      "2 - A vista (Cartão) 5% desconto\n"
      "3 - Cartão (2x) Preço normal\n"
      "4 - Cartão (3x) 20% de juros\n"))

if(escolha == 1):
    print("Preço do produto: R${:.2f}".format(dinheiroCheque))
elif(escolha == 2):
    print("Preço do produto: R${:.2f}".format(vistaCartao))
elif(escolha == 3):
    print("Preço do produto: R${:.2f}\n"
          "R${:.2f} por mês".format(preco, preco/2))
elif(escolha == 4):
    print("Preço do produto: R${:.2f}\n"
          "R${:.2f}".format(cartao3x, cartao3x/3))