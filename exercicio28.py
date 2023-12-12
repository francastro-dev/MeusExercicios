#Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
from time import sleep
computador = randint(0,5)

jogador = int(input('Tente advinhar qual numero o computador vai chutar entre 0 e 5:  '))
print('PROCESSANDO ......')
sleep(3)
if computador == jogador:
    print('Parabéns,voce digitou o numero ', jogador, 'o numero escolhido pelo computador também foi o',computador, ', você acertou!!!')
else:
    print('Você chutou o numero', jogador, ',mas eu escolhi o número', computador, ', eu venci!!!')
