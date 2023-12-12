#Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

lista = []

for i in range(1, 6):
    kg = float(input(f'Digite o {i}º peso: '))
    peso = lista.append(kg)
    i += 1
print(f'o maior peso foi {max(lista)} e o menor peso foi {min(lista)}')

