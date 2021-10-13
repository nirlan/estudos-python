# Solicita que o usuário digite um nome
nome = input('Digite um nome: ')

# Converte o nome digitado para maiúsculas com o uso da função upper()
nome = nome.upper()

# Imprime na tela o nome digitado convertido em maiúsculas
print(nome)

# Itera sobre cada letra da variável string 'nome' com uso de um laço 'for' pois é possível saber antecipadamente qual o
# comprimento da string utilizando a função 'len()'.# Esse laço inicia com 'i = 0' e vai até 'i = comprimento da
# string'. Dessa forma, utilizando o valor de 'i' para acessar cada caractere da string eu posso testar cada caractere
# utilizando estrutura condicional de múltipla escolha para avaliar se é ou não igual aos caracteres procurados.
for i in range(len(nome)):

    # Se o caractere em nome[i] for igual ao caractere procurado, utilizo o fatiamento '[:]' e a concatenação '+' de
    # strings para substituir o caractere e atualizar o valor da variável string 'nome'.
    if nome[i] == 'A':
        nome = nome[:i] + '@' + nome[i+1:]
    elif nome[i] == 'E':
        nome = nome[:i] + '&' + nome[i+1:]
    elif nome[i] == 'I':
        nome = nome[:i] + '!' + nome[i+1:]
    elif nome[i] == 'O':
        nome = nome[:i] + '#' + nome[i+1:]
    elif nome[i] == 'U':
        nome = nome[:i] + '*' + nome[i+1:]

# Imprime na tela a variável string 'nome' já com os caracteres convertidos
print(nome)
