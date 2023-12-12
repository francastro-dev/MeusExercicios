#Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos:

#exemplos - APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.

frase = str(input('Digite uma frase: '))
separado = frase.split()
junto = ''.join(separado)
inverso = junto[::-1]

if inverso == junto:
    print('é palindromo')
else:
    print('não é palindromo')