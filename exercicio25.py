#Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.

nome = str(input("Digite seu nome: ")).strip()
if "SILVA" in nome.upper():
    print('VERDADEIRO')

else:
    print('Falso')

