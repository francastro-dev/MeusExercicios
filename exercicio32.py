#Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

#É um número divisível por 4, mas não é divisível por 100.
#É um número divisível por 4, por 100 e por 400.

ano = int(input('Digite um ano para análise: '))

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano é bisexto')
else:
    print('O ano não é bisexto!!')

