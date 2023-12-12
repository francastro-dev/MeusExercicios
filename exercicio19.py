# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

import random

n1 = input('primeiro nome: ')
n2 = input('segundo nome: ')
n3 = input('terceiro nome: ')
n4 = input('quarto nome: ')

nomes = [n1, n2, n3, n4]
escolhido = random.choice(nomes)

print(" o escolhido foi: ", escolhido)

#O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

n1 = input('primeiro nome: ')
n2 = input('segundo nome: ')
n3 = input('terceiro nome: ')
n4 = input('quarto nome: ')

nomes = [n1, n2, n3, n4]

random.shuffle(nomes)
print('A ordem de apresentação será', nomes)
