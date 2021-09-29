# Exercício 3
# Escreva um programa que calcule o preço a pagar pelo fornecimento de energia
# elétrica. Pergunte a quantidade de kWh consumida e o tipo de instalação:
# R para residências, I para indústrias e C para comércios.
# Calcule o preço de acordo com a tabela:
#      _________________________________________________
#      | Tipo         | Faixa (kWh)       | Preço (R$) |
#      |------------------------------------------------
#      | Residencial  | Até 500           | 0,40       |
#      |              | Acima de 500      | 0,65       |
#      |------------------------------------------------
#      | Comercial    | Até 100           | 0,55       |
#      |              | Acima de 1000     | 0,60       |
#      |------------------------------------------------
#      | Industrial   | Até 5000          | 0,55       |
#      |              | Acima de 5000     | 0,60       |
#      |______________|___________________|____________|

tipo = input('Digite o tipo da instalação:\n'
             'R - residencial\n'
             'I - industrial\n'
             'C - comercial\n')
consumo = int(input('Digite a quantidade consumida (kWh): '))

str_template = 'Quantidade consumida: {} kWh / Valor a pagar: R$ {:.2f}'

if tipo == 'R':
    if consumo <= 500:
        print(str_template.format(consumo, 0.4 * consumo))
    else:
        print(str_template.format(consumo, 0.65 * consumo))
elif tipo == 'C':
    if consumo <= 100:
        print(str_template.format(consumo, 0.55 * consumo))
    else:
        print(str_template.format(consumo, 0.60 * consumo))
elif tipo == 'I':
    if consumo <= 5000:
        print(str_template.format(consumo, 0.55 * consumo))
    else:
        print(str_template.format(consumo, 0.60 * consumo))
else:
    print('Tipo inválido')
print('Encerrando o programa...')