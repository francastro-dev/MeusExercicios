#Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:

"""n = int(input("digite um numero: "))
f = 1
cont = 0

while n > 0:
    f = f * n
    n = n-1
    print(f'fatorial  {f} X {n} = {f*n}')
print('fatorial', f)"""

n =int(input('digite um numero: '))

f =1

for i in range(n, 0, -1):
    f = f * i

    print(f' X {i}', end='')
print('fatorial é', f)

