#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
import math
num = float(input('Digite um numero: '))


print(f'O valor digitado é{num} e sua porção inteira é: {math.trunc(num)}')

#exercicio 17

co = float(input('digite o cateto oposto:'))
ca = float(input('digite o cateto adjacente:'))
hip = math.hypot(co,ca)
print(f'A hipotenusa é: {hip:.2f}')

#