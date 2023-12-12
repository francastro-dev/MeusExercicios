# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import date

ano_atual = date.today().year
menor = 0
maior = 0

for i in range(1,8):
    nascimento = int(input('Em que ano você nasceu: '))
    idade = ano_atual - nascimento

    if idade < 18:
        menor += 1
    else:
        maior += 1
if maior >= 1:
    print(f'há {maior} pessoas maiores de idade.')
if menor >= 1:
    print(f'há {menor} pessoas menores de idade.')