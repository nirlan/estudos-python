# LISTAS
# Dada uma lista contendo as notas de alunos em uma disciplina, escreva uma
# expressão para:
#                   notas = [9,7,7,10,3,9,6,6,2]
# a) Encontrar quantos alunos tiraram nota 7
# b) Alterar a última nota para 4
# c) Encontra a maior nota
# d) Ordenar a lista de notas
# e) A média das notas

# a)
notas = [9, 7, 7, 10, 3, 9, 6, 6, 2]
print(notas.count(7))

# b)
notas[-1] = 4
print(notas)

# c)
x = 0
for nota in notas:
    if x < nota:
        x = nota
print('A maior nota é:', x)

# d)
notas.sort()
print('Lista ordenada de notas:', notas)

# e)
soma = 0
for nota in notas:
    soma += nota
print('A média das notas é {:.2f}'.format(soma/len(notas)))
