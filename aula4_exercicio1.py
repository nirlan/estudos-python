# # Realize a sequência de print com for e while:
# # a) inteiros de 3 até 12, com 12 incluso
# i = 3
# while i < 13:
#     print(i)
#     i += 1
# for i in range (3,13,1):
#     print(i)
# # b) inteiros de 0 até 9, excluindo 9, com passo de 2
# i = 0
# while i < 9:
#     print(i)
#     i += 2
# for i in range(0,10,2):
#     print(i)
###############################################################################
###############################################################################

# Exercício 2
# Escreva um algoritmo que leia dois valores numéricos e que pergunte ao
# usuário qual operação ele deseja realizar: adição (+), subtração (-),
# multiplicação (*) , divisão (/) e sair('s'). Exiba na tela o resultado da operação
# desejada, e repita até que a opção saída seja escolhida.

op = ''
while op != 's':
    op = input('Qual operação deseja realizar?\n'
               '\t1. adição (+)\n'
               '\t2. subtração (-)\n'
               '\t3. multiplicação (*)\n'
               '\t4. divisão (/)\n'
               '\t5. SAIR (s)')
    if op == 's':
        break
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
