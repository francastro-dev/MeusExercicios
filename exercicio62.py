#Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.

primeiro_termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
termo = primeiro_termo
cont = 1

while cont <=10:
    print(termo)
    termo = termo + razao
    cont += 1

    mais = int(input('Quanto termos vc quer mostrar a  mais? '))