#Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
from random import randint

computador = randint(0,10)
jogador = int(input('Tente acertar um número entre 0 e 10: '))

jogadas = 0

print('jogada do computador', computador)

while jogador != computador:
    jogador = int(input('tente novamente entre 0 e 10: '))
    jogadas += 1

    if jogador == computador:
        print('voce acertou')
    else:
        if jogador < computador:
            print('tente um numero maior')
        else:
            print('tente um numero menor')

print('Foram necessárias', jogadas, 'jogadas')

