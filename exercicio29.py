#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

velocidade = float(input('Digite a Velocidade:  '))

if velocidade > 80:
    valor = velocidade - 80
    multa = valor * 7
    print(f'Você foi multado!!!, A velocidade máxima permitida é 80Km/h')
    print(f'O valor da multa será de RS{multa:.2f}')
else:
    print('Você não tem multas a pagar!!!\n')

print('='* 30)
print('   Dirija com segurança!!!')