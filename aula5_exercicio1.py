# Exercício 1
# Escreva uma função que calcule o fatorial de um número recebido como parâmetro
# e retorne o seu resultado.
# Faça uma validação dos dados por meio de uma outra função, permitindo que
# somente valores positivos sejam aceitos.
# Crie o help da sua função.

def valida_int(pergunta, min, max):
    x = int(input(pergunta))
    while x < min or x > max:
        x = int(input(pergunta))
    return x


def fatorial(num):
    """
    Função que calcula a fatorial de um número.
    :param num: número que será calculado a sua fatorial
    :return: fatorial do número
    """
    fat = 1
    if num == 0:
        return fat
    for num in range(1, num + 1, 1):
        fat *= num
    return fat


# Programa principal
x = valida_int('Digite um valor para calcular a fatorial: ', 0, 99999)
print('{}! = {}'.format(x, fatorial(x)))
help(fatorial)
