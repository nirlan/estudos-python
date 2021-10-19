# Exercício 1
# Escreva um algoritmo que crie uma tupla com 10 palavras. Encontre dentro
# dessa tupla as vogais de cada palavra. Faça um print na tela com o nome
# da palavra e suas respectivas vogais.

palavras = ('abacate', 'mamao', 'melancia', 'abobora', 'gengibre',
         'morango', 'framboesa', 'abrico', 'ameixa', 'manjericao')

for palavra in palavras:
    print('\nPalavra: {}. Vogais: '.format(palavra.upper()), end='')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(letra.upper(), end=' ')
