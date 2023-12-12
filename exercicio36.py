#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

valor = float(input('Digite o valor do imóvel:  '))
salario = float(input('Digite a sua renda salarial:  '))
anos = int(input('Em quanto anos deseja finaciar o seu imóvel?  '))

prestacao = valor / (anos*12)
limite = salario*30/100

if prestacao <= limite:
    print(f'Seu empréstimo foi aprovado,\n O valor da sua prestação será de R${prestacao:.2f}, \n No total de {anos*12} prestações')
else:
    print(f'Empréstimo negado!!!,\n Rua renda precisa ser maior, \n E sua prestação seria R${prestacao:.2f} ')


