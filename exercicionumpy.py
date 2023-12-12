import numpy as np

nomes = []#Criando uma variável do tipo Lista vazia para receber os dados de nomes
idades = []
alturas = []
pesos = []

# Abrir e ler o arquivo CSV
with open('dados1.csv', 'r', encoding = 'ISO-8859-1') as batata:#
    lines = batata.readlines()


    for line in lines[1:]:  # Ignorar o cabeçalho
        nome, idade, altura, peso = line.strip().split(',')
        nomes.append(nome)
        idades.append(int(idade))
        alturas.append(int(altura))
        pesos.append(float(peso))

print(nomes)
print(idades)
print(alturas)
print(pesos)

nomes_nd = np.array(nomes)
idades_nd = np.array(idades)
alturas_nd = np.array(alturas)
pesos_nd = np.array(pesos)

#1-Qual é a média das idades das pessoas na base de dados
print('1-Qual é a média das idades das pessoas na base de dados')
media_idades = np.mean(idades)
print('1-Qual é a média das idades das pessoas na base de dados')
print(f'Média de idade ,{(media_idades)}\n')

#Qual é a altura máxima registrada entre as pessoas
print('2- Qual é a altura máxima registrada entre as pessoas')
altura_maxima = np.max(alturas)
pessoas_190 = np.argwhere(alturas == altura_maxima)#tras o array com os indices
pessoas_where = np.where(alturas == altura_maxima)#tras o array com os indices na horizontal
quantidade_pessoas_190 = np.count_nonzero(alturas == altura_maxima)

print(f'a altura maxima é: {altura_maxima}')#traz a altura maxima
print(f'indice das pessoas com 1.90:\n {pessoas_190}')
print(f'nomes das pessoas com 1.90: \n {np.array(nomes)[pessoas_190]}')
print(f' nome das pessoas com1.90 : c/where {np.array(nomes)[pessoas_where]}')
print('indice das pessoas com 1.90: c/ where', pessoas_where)
print(f'quantidade de pessoas com 1.90: {quantidade_pessoas_190}''\n')

# 3)Quantas pessoas possuem peso acima de 70 kg
lista_qtd = np.count_nonzero(np.array(pesos) > 70)
print('3-Quantas pessoas possuem peso acima de 70 kg')
print(f'Maiores de 70 Kg: {lista_qtd}\n')

#4) Qual é o desvio padrão das idades das pessoas:
dp_idade = np.std(idades)

#Opção
#desvio_idades = np.std(np.array(idades))

print('4-Qual é o desvio padrão das idades das pessoas:')
print(f'Desvio padrão é {dp_idade:.2f}\n')


#5) Quem é a pessoa mais velha na base de dados:
mais_idade = np.max(idades)
nome_mais_velho = np.where(idades == mais_idade)

print('5-Quem é a pessoa mais velha na base de dados:')
print(f'A(s) pessoa(s) mais velha: {np.array(nomes)[nome_mais_velho]}')
print('A pessoa mais velha tem', mais_idade, 'anos')
print('Qtd de pessoas: ', len(np.array(nomes)[mais_idade]),'pessoas\n')


#6) Qual é o Índice de Massa Corporal (IMC) médio das pessoas
imc_media = np.array([pesos[i] / ((alturas[i]/100)**2) for i in range(len(pesos))])
print('6-Qual é o Índice de Massa Corporal (IMC) médio das pessoas:')

print('media imc = ', np.mean(imc_media))


#7) Qual é a diferença de idade entre a pessoa mais nova e a mais velha?
dif = (np.max(idades)) - (np.min(idades))
"""dif = np.ptp(idades)
print(dif)"""

print('7-Qual é a diferença de idade entre a pessoa mais nova e a mais velha?')
print('A diferença de idade é', dif)
print(type(dif))


#8)Quem é a pessoa mais alta na base de dados?
mais_alta = np.max(alturas)
pessoa_mais_alta = np.argwhere(alturas == mais_alta)
pessoas_where = np.where(alturas == altura_maxima)

print('8)Quem é a pessoa mais alta na base de dados?')
#print(np.array(nomes)[pessoa_mais_alta]) - opção de exibir lista
print(f'Nomes: {np.array(nomes)[pessoas_where]}')
print(f'qtd de pessoas = {len(pessoa_mais_alta)}''\n')

#9) Qual é a altura média das pessoas com idade entre 25 e 30 anos?
print('9- Qual é a altura média das pessoas com idade entre 25 e 30 anos?')
altura_media_25_30 = np.array([alturas for x in idades if x >=25 and x <=30])

#print(altura_media_25_30)

print(f'A média de Altura é {(np.mean(altura_media_25_30)/100):.2f}m\n')

#10) Quantas pessoas têm IMC acima de 25 (indicando sobrepeso)?
print('10 - Quantas pessoas têm IMC acima de 25 (indicando sobrepeso)?')
imc_25 = np.count_nonzero(imc_media>25)
print(f'Qtd de pessoas com IMC >25: {imc_25}\n')

#11)Quais são os nomes das pessoas com altura acima de 170 cm?
pessoas_170 = np.where(alturas_nd > 170)
print('11)Quais são os nomes das pessoas com altura acima de 170 cm?')
print('Qtde', np.count_nonzero(pessoas_170))
print(nomes_nd[pessoas_170])


"""#12) Qual é a idade média das pessoas com peso abaixo de 70 kg?
print('12 -Qual é a idade média das pessoas com peso abaixo de 70 kg?')
peso_70=np.where(pesos_nd < 70)
media_70 = idades_nd[pesos_70].mean()
#ou media_70 = np.mean(idade_nd[pesos_70])

#pessoas_70 = np.array([idades for x in pesos if x <70])
print(f'Média = {media_70:.2f}')"""

#13) Quantas pessoas têm idade ímpar na base de dados?
print('13 - Quantas pessoas têm idade ímpar na base de dados?')
idade_impar = np.count_nonzero(idades_nd % 2 !=0)
print('Qtd de pessoas',idade_impar)

#Caso queira mostrar os nomes
#idade_impar_index = np.where((idades_nd % 2 !=0))
#print (nomes_nd[idade_impar_index])

#14) Quem é a pessoa cuja altura está mais próxima da média (175 cm)?
print('14) Quem é a pessoa cuja altura está mais próxima da média (175 cm)?')
pessoa_175 = np.abs(alturas_nd - 175)
print(nomes_nd[pessoa_175])
print(np.count_nonzero(pessoa_175))

#15) Calcule e liste os IMCs de todas as pessoas na base de dados.
imc_media


#16) Quem é a pessoa mais pesada na base de dados?
print('16) Quem é a pessoa mais pesada na base de dados?')
mais_pesada = np.max(pesos_nd)
pessoa_mais = np.where(pesos == mais_pesada)#traz o indice da pessoa mais pesada

maior_peso = np.argmax(pesos_nd)#confirmar a posição na planilha
print(maior_peso)

print(mais_pesada)
print(pessoa_mais)
print(nomes_nd[pessoa_mais])#tras o nome

#17) Quais pessoas estão com sobrepeso (IMC > 25)?
print('Quais pessoas estão com sobrepeso (IMC > 25)?')
imc_25_nomes =np.where(imc_media > 25)
imc_25_nomes = nomes_nd[imc_25_nomes]
print(imc_25_nomes)

#18) Qual é a média das idades das pessoas que têm mais de 170 cm de altura?
print('18) Qual é a média das idades das pessoas que têm mais de 170 cm de altura?')
pessoas_170 = np.where(alturas_nd >170)
media_idade_170 = idades_nd[pessoas_170]
media_3 = np.mean(media_idade_170)
print(media_3)

#19) Quantas pessoas têm idade entre 25 e 30 anos e altura abaixo de 170 cm?

'resposta 36'

#20) Quem é a pessoa mais leve na base de dados?
print('Quem é a pessoa mais leve na base de dados?')
peso_leve = np.min(pesos_nd)
peso_leve= np.count_nonzero(pesos_nd == peso_leve)

peso_leve_pos = np.argmin(pesos_nd)

print(nomes[peso_leve])