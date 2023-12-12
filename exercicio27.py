#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

nome = str(input("Digite seu nome completo")).strip()

n = nome.split()

print('seu primeiro nome é :', n[0])
print('seu ultima nome é :', (n[len(n)-1]))

