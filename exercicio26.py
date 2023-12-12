#Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

frase = str(input("digite uma frase: ")).upper().strip()

print('A lestra A aparece', frase.count('A'), 'vezes')
print('A primeira letra A aparece na ', (frase.find('A')+1), 'posição')
print('A ultima letra A aparece na ', (frase.rfind('A')+1), 'posição')
