#Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
soma = 0
cont = 0

for i in range(1,7):
    n= int(input(f'Digite um valor {i}'))
    if n % 2==0:
        soma = soma+n
        cont = cont+1
print('A soma dos numeros pares é', soma)
print('Foram', cont, 'numeros pares')

