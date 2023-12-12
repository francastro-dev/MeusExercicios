#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo, e qual é o tipo de triangulo.

lado1 = float(input('Digite o primeiro lado:'))
lado2 = float(input('Digite o segundo lado:'))
lado3 = float(input('Digite o terceiro lado:'))

if lado1 < (lado2+lado3) and lado2 < (lado1 + lado3) and lado3 < (lado1+lado2):
    soma = lado1 +lado2 + lado3

    #Analisar se o tringulo é escaleno, isosceles ou equilatero:
    if lado1 == lado2 ==lado3:
        print('O triangulo é equilátero')
    elif (lado1 != lado2 and lado1 !=lado3) and (lado3!=lado2 and lado3 != lado1) and (lado2!=lado1 and lado2 !=lado3):
        print('O triangulo é escaleno')
    elif (lado1 == lado2 or lado1 ==lado3) or (lado3==lado2 or lado3 == lado1) or (lado2==lado1 or lado2 ==lado3):
        print('O triangulo é isósceles')

else:
    print('\n')
    print('Não é possivel formar um triangulo com estas medidas!!!')