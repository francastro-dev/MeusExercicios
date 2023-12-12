#Crie um programa que leia dois valores e mostre um menu na tela:
"""[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa"""

n1 = int(input("Digite o primeiro valor: "))
n2 = int(input("Digite o segundo valor: "))

escolha = 0

while escolha != 5:
    print("""
    Digite sua escolha
    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa """)

    escolha = int(input('digite sua escolha: '))

    if escolha == 1:
        soma = n1+ n2
        print('A soma é :', soma)
    elif escolha == 2:
        mult = n1 * n2
        print('A multiplicação é :', mult)
    elif escolha == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('o maior numero é:', maior)
    elif escolha == 4:
        print('Escolha os numeros novamente: ')
        n1 = int(input("Digite o primeiro valor: "))
        n2 = int(input("Digite o segundo valor: "))
    elif escolha == 5:
        print("Fim")

    else:
        print('Opção invalida, tente novamente!!!')

