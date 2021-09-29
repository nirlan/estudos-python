# Exercício 3
# Crie uma variável string que receba uma frase qualquer. Crie uma segunda variável,
# agora contendo a metade da string digitada. Imprima na tela somente os dois últimos
# caracteres da segunda variável do tipo string.

frase = input('Digite uma frase: ')
print(frase)
tam = len(frase)

indice = int(tam/2)
print(indice)

metade = frase[0:indice]
print(metade)

# usando o sinal negativo o índice é contado de trás para frente
# nesse exemplo o índice 0 seria o último caractere, inclusive,
# que fica do lado direito do parâmetro, e o índice 1 seria o
# penúltimo, que é dado pelo '-2' exclusivo
print(metade[-2:])