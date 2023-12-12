#Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a digitação novamente até ter um valor correto.
sexo = ''

sexo = str(input('Digite seu sexo [ M / F] ')).strip().upper()[0]

while sexo != 'M' and sexo != 'F':
    sexo = str(input('Opção Inválida, digite o sexo [M ou F]')).strip().upper()[0]

print(f'Sexo {sexo} registrado com sucesso!!!')
    





