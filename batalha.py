# Exercicio 4 - batalha

import random

vida_jogador = 10
vida_pc = 10

while True:

    dano_jogador = ''
    dano_causado_jogador = ''
    dano_pc = ''
    dano_causado_pc = ''

    menu = input(f''' 
          Bem vindo ao RPG, escolha entre "Soco" e "Cabeçada" para atacar o inimigo,
          ou Sair para fugir.  ^.^
          Boa sorte!!!! 
          HP jogador {vida_jogador}
          HP PC      {vida_pc} 
  ''').upper()

    if menu == 'SAIR':
        print('Você fugiu !!! ')
        break
    elif menu == 'SOCO':
        dano_jogador = random.randint(1,6)
        print(f'Você escolheu "SOCO" e seu dano é de {dano_jogador}')
    elif menu == 'CABEÇADA':
        dano_jogador = 4
        print(f'Você escolheu "CABEÇADA" e seu dano é de {dano_jogador}')

    dano_pc = random.randint(1,6)
    print(f'O computador deu um soco e seu dano é de {dano_pc}')

    if dano_jogador > dano_pc:
        print('Seu dano é maior, você ataca...')
        if menu == 'SOCO':
            dano_causado_pc = random.randint(1,6)
            vida_pc -= dano_causado_pc
            print(f'Seu soco deu {dano_causado_pc} de dano ao PC')

        elif menu == 'CABEÇADA':
            vida_pc -= 3
            vida_jogador -= 1
            print(f'Sua cabeçada deu {3} de dano ao PC')

    elif dano_jogador == dano_pc:
        print('Empate ')
        continue
    else:
        dano_causado_jogador = random.randint(1,6)
        vida_jogador -= dano_causado_jogador
        print(f'O soco do PC te causa {dano_causado_jogador} de dano')

    if vida_jogador <= 0:
        print('Você perdeu, seu HP foi a zero')
        break
    elif vida_pc <= 0:
        print('Você derrotou o PC, levando o hp dele a 0')
        break
