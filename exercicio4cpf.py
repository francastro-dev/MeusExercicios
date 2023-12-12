#4)	Faça um programa que o usuário digite um CPF (exemplo: 123.456.789-10) e o sistema valide se os dois dígitos verificadores estão corretos (no caso do exemplo, o número 4 e número 0 após o traço).

cpf = input('Digite seu cpf: ')

cpf_9 = cpf[:9]
cpf_10 = cpf[:10]
cpf_digito = cpf[-2]
cpf_digito_2 = cpf[-1]

valor = 0
valor_2 = 0

for i in range(len(cpf_9)):
    valor += int(cpf_9[i])*(10 - i)

for i in range(len(cpf_10)):
    valor_2 += int(cpf_10[i])*(11 - i)

valor_2 = valor_2 *10
valor_2 = valor_2 % 11


valor = valor *10
valor = valor % 11

if valor_2 > 9:
    valor_2 = 0

if valor > 9:
    valor = 0

if valor == int(cpf_digito) and valor_2 == int(cpf_digito_2):
    print('Cpf Válido')
else:
    print('Cpf Inválido')