#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

n1 = int(input("digite o primeiro número = "))
n2 = int(input("digite o segundo número = "))
n3 = int(input("digite o terceiro número = "))

menor = n1

if n2 < n1 and n2 < n3:
    menor = n2

if n3 < n1 and n3 < n2:
    menor = n3

print('o menor número é o :', menor)

maior = n1

if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3

print('o maior número é o :', maior)

####################################################

# opção de calcular com função min e max
print("="*30)
print('o menor número é o :', min(n1,n2,n3))
print('o maior número é o :', max(n1,n2,n3))