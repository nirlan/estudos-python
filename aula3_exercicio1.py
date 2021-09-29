# Exercício 1
# Faça um algoritmo que receba três valores, representando os lados de um
# triângulo fornecidos pelo usuário. Verifique se os valores formam um
# triângulo e classifique como:
# a) Equilátero (três lados iguais)
# b) Isósceles (dois lados iguais)
# c) Escaleno (três lados diferentes)
# Lembre-se que para formar um triângulo, nenhum dos lados pode ser igual
# a zero, e um lado não pode ser maior do que a soma dos outros dois

print('Digite os três lados do triângulo:')
x = int(input('Lado 1: '))
y = int(input('Lado 2: '))
z = int(input('Lado 3: '))

print(x, y, z)
if x > 0 and y > 0 and z > 0:
    if x < y + z and y < x + z and z < x + y:
        if x != y and x != z and y != z:
            print('O triângulo é escaleno')
        elif x == y and x == z:
            print('O triângulo é equilátero')
        else:
            print("O triângulo é isósceles")
    else:
        print('Não é um triângulo!')
else:
    print('Não é um triângulo!')
