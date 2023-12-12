"""Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos."""
soma_idade = 0
media = 0
cont = 0
maior_idade = 0
nome_velho = ''

for i in range(1, 4):
    nome = str(input(f'Digite o {i}º nome: ')).strip()
    idade = int(input(f'Digite o {i}º idade: '))
    sexo = str(input(f'Digite o {i}º Sexo [M/F]: ')).strip().upper()


    soma_idade = soma_idade+idade
    media = soma_idade/3

    if sexo == 'F' and idade <20:
        cont +=1
    elif sexo == 'M' and idade > maior_idade:
        maior_idade = idade
        nome_velho = nome


print(f'a media de idade é ={media:.2f}')
print(' o nome do homem mais velho é ', nome_velho)
print('Há pelo menos', cont,'mulheres menores de 20 anos')