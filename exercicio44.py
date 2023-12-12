"""Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:

– à vista dinheiro/cheque: 10% de desconto
– à vista no cartão: 5% de desconto
– em até 2x no cartão: preço formal
– 3x ou mais no cartão: 20% de juros"""


valor = float(input("Qual o valor do produto? "))
print("""Digite a forma de pagamento:
[1] – à vista dinheiro / cheque: 10% de desconto
[2] – à vista no cartão: 5% de desconto
[3] – em até 2x no cartão: preço formal
[4] – 3x ou mais no cartão: 20% de juros
""")
opcao = int(input())

if opcao == 1:
    preco = valor*0.9
elif opcao == 2:
    preco = valor*0.95
elif opcao == 3:
    preco = valor
elif opcao == 4:
    preco = valor*1.2
else:
    print('opção invalida !!!')

print(f'o valor da mercadoria é R${valor} e o total será R${preco}')
