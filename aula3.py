# Expressões booleanas
# Escreva as seguintes expressões booleanas em linguagem Python:

# a) o somatório de 2 com 2 é menor do que 4
res = 2 + 2 < 4
print('a)', res)

# b) o valor 7 // 3 é igual a 1 + 1
res = 7 // 3 == 1 + 1
print('b)', res)

# c) a soma de 3 elevado ao quadrado com 4 elevado ao quadrado é igual a 25
res = 3**2 + 4**2 == 25
print('c)', res)

# d) a soma de 2, 4 e 6 é maior do que 12
res = 2 + 4 + 6 > 12
print('d)', res)

# e) 1387 é divisível por 19
res = 1387 % 19 == 0
print('e)', res)

# f) 31 é par
res = 31 % 2 == 0
print('f)', res)

# g) o menor valor entre: 34, 29 e 31 é menor do que 30
res = 34 < 30 or 29 < 30 or 31 < 30
print('g)', res)

# Condicionais simples
# Traduza as afirmações a seguir para condicionais em Python:

# a) se idade é maior que 60, escreva: "Você tem direitos aos benefícios"
idade = 64
if idade > 60:
    print('Você tem direito aos benefícios')

# b) se dano é maior do que 10 e escudo é igual a 0, escreva:
# "Você está morto!"
dano = 11
escudo = 0
if dano > 10 and escudo == 0:
    print('Você está morto!')

# c) se pelo menos uma das variáveis booleanas norte, sul, leste e oeste
# resultarem em True, escreva: "Você escapou!"

norte, sul, leste, oeste = False, True, False, False
if norte or sul or leste or oeste:
    print('Você escapou!')

# Condicionais compostas
# a) se ano é divisível por 4, escreva: "Pode ser um ano bissexto". Caso
# contrário, escreva: "Definitivamente não é um ano bissexto"
ano = 1982
if ano % 4 == 0:
    print('Pode ser um ano bissexto')
else:
    print('Definitivamente não é um ano bissexto')

# b) se ambas as variáveis booleanas cima e baixo forem True, escreva:
# "Decida-se!", caso contrário, escreva: "Você escolheu um caminho!"
cima, baixo = True, False
if cima and baixo:
    print('Decida-se!')
else:
    print('Você escolheu um caminho!')

