# Exercício 3
# Crie um programa para ler o nome, ano de nascimento e sexo de diferentes
# pessoas.
# Armazene os dados em um dicionário com listas.
# Ao encerrar o cadastro, apresente:
#   - o total de cadastros efetuados
#   - a média das idades das pessoas
#   - uma lista de mulheres com menos de 30 anos
#   - uma lista de homens com idade acima da média

cadastro = {'nome':[],'sexo':[],'ano':[]}

while True:
    terminar = input('Deseja cadastrar uma pessoa? [S/N]: ')
    if terminar.upper() in 'N':
        break
    if terminar.upper() not in 'S':
        print('Digite S para SIM ou N para NÃO')
        continue

    nome = input('Qual seu nome?')
    sexo = input('Qual seu sexo [M/F]?')
    ano = int(input('Qual seu ano de nascimento?'))
    cadastro['nome'].append(nome)
    cadastro['sexo'].append(sexo.upper())
    cadastro['ano'].append(ano)

# Imprime na tela o total de cadastros efetuados
print('Total de cadastros efetuados:', len(cadastro['nome']))

# Calcula a média das idades das pessoas
soma = 0
count = 0
for ano in cadastro['ano']:
    soma += 2021 - ano
    count += 1
media = soma/count
print('Média das idades: {:.1f}'.format(media))

# Lista de mulheres com menos de 30 anos
mulheres30 = []
index = 0
for ano in cadastro['ano']:
    idade = 2021 - ano
    if idade < 30 and cadastro['sexo'][index] in 'F':
        mulheres30.append(cadastro['nome'][index])
    index += 1
print('LISTA DE MULHERES COM MENOS DE 30 ANOS:')
for mulher in mulheres30:
    print(mulher)

# Lista de homens com idade acima da média
homens_acima_media = []
index = 0
for ano in cadastro['ano']:
    idade = 2021 - ano
    if idade > media and cadastro['sexo'][index] in 'M':
        homens_acima_media.append(cadastro['nome'][index])
    index += 1
print('LISTA DE HOMENS COM IDADE ACIMA DA MÉDIA:')
for homem in homens_acima_media:
    print(homem)
