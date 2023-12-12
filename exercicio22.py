# Crie um programa que leia o nome completo de uma pessoa e mostre:

# – O nome com todas as letras maiúsculas e minúsculas.

nome = input('Digite seu nome completo :')

print('Nome Maiusculo : ', nome.upper())
print('Nome Minusculo : ', nome.lower())

# – Quantas letras ao todo (sem considerar espaços).

print('quantas letras: ', len(nome)- nome.count(' '))

# – Quantas letras tem o primeiro nome.
print('seu primeiro nome tem', (nome.find(' ')))

separa = nome.split()
print('separado,', separa)


