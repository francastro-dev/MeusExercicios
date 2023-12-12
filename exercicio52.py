# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

n = int(input('Digite um número: '))
total = 0

for i in range(1,n+1):
    if n % i == 0:
        total += 1

if total == 2:
    print('o numero é primo ')
else:
    print('o numero não é primo ')

print('o numero contém', total,'divisores')