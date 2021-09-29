# Exercício 2
# Escreva um algoritmo que leia dois valores numéricos e que pergunte ao
# usuário qual operação ele deseja realizar: adição (+), subtração (-),
# multiplicação (*) ou divisão (/).Exiba na tela o resultado da operação
# desejada.

op = input('Qual operação deseja realizar?\n'
           '\t1. adição (+)\n'
           '\t2. subtração (-)\n'
           '\t3. multiplicação (*)\n'
           '\t4. divisão (/)\n')

if op == '+' or op == '-' or op == '*' or op == '/':
    x = int(input('Digite um número inteiro: '))
    y = int(input('Digite outro número inteiro: '))

if op == '+':
    print(x + y)
elif op == '-':
    print(x - y)
elif op == '*':
    print(x * y)
elif op == '/':
    print(x / y)
else:
    print('Operação inválida')

print('Encerrando o programa...')
