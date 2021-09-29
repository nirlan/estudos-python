# Exercício 2
# Escreva um programa que pergunte a quantidade de km percorridos por um carro
# alugado pelo usuário, assim como a quantidade de dias pelos quais o carro foi
# alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60,00 por dia
# e R$ 0,15 por km rodado.

km_percorrido = float(input('Digite a quantidade de quilômetros percorridos: '))
dias_alugado = int(input('Digite a quantidade de dias alugado: '))

preco = 60.0*dias_alugado + 0.15*km_percorrido
print('Dias alugados: %d dias' % dias_alugado, '\nDistância percorrida: %.2f km' % km_percorrido)
print('Preço a pagar: R$ %.2f' % preco)