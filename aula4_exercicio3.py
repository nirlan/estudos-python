# Exercício 3
# Um cinema cobra preços diferentes para os ingressos de acordo com a idade
# de uma pessoa. Se a pessoa tiver menos de 3 anos de idade, o ingresso
# será gratuito, se tiver entre 3 e 12 anos, o ingresso custará R$ 15,
# se tiver mais de 12 anos, custará R$ 30

# Escreva um laço que pergunte a idade e informe o preço dos ingressos.
# Encerre o laço com break quando o usuário digitar 'sair'.
# Após encerrar o laço, apresente na tela o total de pessoas que
# compraram ingressos, o total de dinheiro arrecadado e a média de idade
# das pessoas.

gratuito, meia, inteira, somaidade, pessoas = 0, 0, 0, 0, 0
while True:
    idade = input('Qual a sua idade?\n'
                  'Digite "sair" para encerrar o programa...')
    if idade == 'sair':
        break
    idade = int(idade)
    if idade <= 3:
        gratuito += 1
        somaidade += idade
        pessoas += 1
    elif 3 < idade <= 12:
        meia += 1
        somaidade += idade
        pessoas += 1
    else:
        inteira += 1
        somaidade += idade
        pessoas += 1
print('Total de pessoas: {}\n'
      'gratuidades = {}\n'
      'meias = {}\n'
      'inteiras = {}'.format(pessoas, gratuito, meia, inteira))
print('Valor arrecadado: R$ {:.2f}'.format(meia*15 + inteira*30))
print('Média de idade das pessoas: {}'.format(somaidade / pessoas))
print('Encerrando o programa...')
