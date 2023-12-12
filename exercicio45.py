# Crie um programa que faça o computador jogar Jokenpô com você.
from random import randint
from time import sleep
itens = ['PEDRA', 'PAPEL', 'TESOURA']

print("""Digite a sua opção :
[1] PEDRA 
[2] PAPEL
[3] TESOURA""")

computador = randint(1,3)
opcao = int(input('Qual a sua jogada? ' ))

print('JO')
sleep(1)
print('kEN')
sleep(1)
print('PO')

if opcao == computador:
    print(f'Você jogou {itens[opcao+1]}')
    print(f'O computador jogou {itens[computador+1]}')
    print('Empate')

elif opcao == 1 and computador == 2:
    print(f'Você jogou  ==> PEDRA \n O computador jogou PAPEL')
    print('você perdeu!!!')
elif opcao == 1 and computador == 3:
    print(f'Você jogou  ==> PEDRA \n O computador jogou TESOURA')
    print('você ganhou!!!')
elif opcao == 2 and computador == 1:
    print(f'Você jogou  ==> PAPEL \n O computador jogou PEDRA')
    print('você ganhou!!!')
elif opcao == 2 and computador == 3:
    print(f'Você jogou  ==> PEDRA \n O computador jogou TESOURA')
    print('você perdeu!!!')
elif opcao == 3 and computador == 1:
    print(f'Você jogou  ==> TESOURA \n O computador jogou PEDRA')
    print('você perdeu!!!')
elif opcao == 3 and computador == 2:
    print(f'Você jogou  ==> TESOURA \n O computador jogou PAPEL')
    print('você ganhou!!!')



