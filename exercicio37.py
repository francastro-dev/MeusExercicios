#Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

n = int(input("Digite um número para conversão: "))

opcao = int(input('Escolha qual será a base de conversão:\n [1] para binário \n [2] para octal \n [3] para hexadecimal '))

if opcao == 1:
    print(f' o {n} convertido em binário é ==> {bin(n)[2:]}')
elif opcao == 2:
    print(f' o {n} convertido em octal é ==> {oct(n)[2:]}')
elif opcao == 3:
    print(f' o número {n} convertido em hexadecimal é ==> {hex(n)[2:]}')
else:
    print('Opção inválida!!')

