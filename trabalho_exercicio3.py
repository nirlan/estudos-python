def cabecalho():
    """
    Função que imprime na tela o cabeçalho do jogo HOTEL DOS ANIMAIS
    :return: none
    """
    print('-' * 23)
    print('──────▄▀▄─────▄▀▄')
    print('─────▄█░░▀▀▀▀▀░░█▄')
    print('─▄▄──█░░░░░░░░░░░█──▄▄')
    print('█▄▄█─█░░▀░░┬░░▀░░█─█▄▄█')
    print('   HOTEL DOS ANIMAIS')
    print('-' * 23)
    print('Especificando posição:')
    print('[1,2,3,4]')
    print('[5,6,7,8]')


def imprime_quartos(quartos: list[list[str]]):
    """
    Função que imprime na tela os quartos disponíveis
    :param quartos: lista de listas contendo os quartos
    :return: none
    """
    print(quartos[0])
    print(quartos[1])


def posicoes_permitidas(quartos: list[list[str]]):
    """
    Função que recebe uma lista de listas de quartos e itera sobre
    elas procurando os quartos vazios, que é representado pela string '-'.
    Ao encontrar um quarto vazio a posição dele é armazenada em uma lista
    de posições.
    :param quartos: uma lista de listas contendo os quartos
    :return: a lista com os números das posições de quartos vazios
    """
    posicoes = []
    contador = 1
    for i in quartos:
        for j in i:
            if j in '-':
                posicoes.append(contador)
            contador += 1
    return posicoes


def valida_jogada(pergunta: str, posicoes: list[int]):
    """
    Função que valida a entrada do usuário. Enquanto o usuário não digitar
    uma das posições válidas o programa continua perguntando a entrada para
    o usuário.
    :param pergunta: pergunta que será impressa na tela para o usuário
    :param posicoes: lista com os números das posições válidas
    :return: uma posição válida digitada pelo usuário
    """
    while True:
        try:
            jogada = int(input(pergunta))
        except ValueError:
            print('Ops! Opção inválida... Digite uma posição válida...')
            continue
        else:
            for posicao in posicoes:
                if jogada == posicao:
                    return jogada


def atualiza_quartos(quartos: list[list[str]], jogadas: dict[int, str]):
    """
    Função que atualiza a ocupação dos quartos conforme a escolha feita pelo
    usuário.
    :param quartos: lista de listas com a disposição da ocupação dos quartos
    :param jogadas: dicionário contendo como chave a posição do hóspede que foi
    escolhida pelo usuário e como valor a string que representa o hóspede
    :return: uma lista com a configuração atualizada da ocupação dos quartos
    """
    contador = 1
    for i in range(len(quartos)):
        for j in range(len(quartos[i])):
            if quartos[i][j] in '-' and contador in jogadas.keys():
                quartos[i][j] = jogadas[contador]
            contador += 1
    return quartos


def ganhou(quartos: list[list[str]]):
    """
    Função que avalia se as condições de vitória em cada fase são satisfeitas,
    segundo as regras do jogo.
    :param quartos: lista com a configuração da ocupação dos quartos após todas
    as jogadas do usuário
    :return: retorna 1 se o usuário ganhou e 0 se o usuário perdeu
    """

    # Hóspedes
    cao = 'C'
    gato = 'G'
    rato = 'R'
    osso = 'O'
    queijo = 'Q'

    # Iteração sobre toda a lista de lista quartos buscando se há algum hóspede
    # que está numa posição incorreta segundo as regras do jogo. Se houver, uma
    # das condicionais é atendida e a função retorna 0
    for i in range(len(quartos)):
        for j in range(len(quartos[i])):
            if quartos[i][j] in cao:
                # Verifica as posições adjacentes na horizontal
                if j - 1 >= 0 and quartos[i][j-1] in gato + osso \
                        or j + 1 < len(quartos[i]) and quartos[i][j+1] in gato + osso:
                    return 0
                # Verifica as posições adjacentes na vertical
                elif i - 1 >= 0 and quartos[i-1][j] in gato + osso \
                        or i + 1 < len(quartos) and quartos[i+1][j] in gato + osso:
                    return 0
            elif quartos[i][j] in gato:
                if j - 1 >= 0 and quartos[i][j-1] in cao + rato \
                        or j + 1 < len(quartos[i]) and quartos[i][j+1] in cao + rato:
                    return 0
                elif i - 1 >= 0 and quartos[i-1][j] in cao + rato \
                        or i + 1 < len(quartos) and quartos[i+1][j] in cao + rato:
                    return 0
            elif quartos[i][j] in rato:
                if j - 1 >= 0 and quartos[i][j-1] in gato + queijo \
                        or j + 1 < len(quartos[i]) and quartos[i][j+1] in gato + queijo:
                    return 0
                elif i - 1 >= 0 and quartos[i-1][j] in gato + queijo \
                        or i + 1 < len(quartos) and quartos[i+1][j] in gato + queijo:
                    return 0
    return 1


def primeira_fase():
    """
    Essa função executa a primeira fase do jogo. Primeiro ela imprime na tela
    as instruções da fase 1, define uma lista de listas que contém a organização
    dos quartos e imprime na tela essa lista. Em seguida ela define uma lista de
    posições permitidas e pergunta para o usuário a primeira jogada. A primeira
    jogada é removida da lista de jogadas possíveis e em seguida é solicitado
    ao usuário a segunda jogada. Se a segunda jogada for igual à posição 6,
    isso quer dizer que o GATO ficou ao lado do RATO, o que não pode pelas
    regras do jogo, e a função retorna 0. Caso contrário a função retorna 1.
    :return: 0 se o usuário perder o jogo e 1 se passar de fase
    """
    print('\nBem vindos a fase 1!')
    print('Na Fase 1, o jogador deve alocar o RATO e o GATO na seguinte matriz que '
          'representa os quartos:')

    # Define a lista de listas da organização dos quartos
    quartos = [['*', '*', '-', 'G'],
               ['R', '-', '*', '*']]
    imprime_quartos(quartos)

    # Define uma lista com as posições dos quartos vazios
    posicoes = posicoes_permitidas(quartos)

    # Dicionário para armazenar as strings dos hóspedes ('G' = gato, 'R' = rato,
    # 'C' = cão, 'O' = osso, 'Q' = queijo) e a posição em que foram jogadas.
    jogadas = {}
    # Primeira jogada
    jogada1 = valida_jogada('em qual posição quer alocar o RATO?', posicoes)
    # Adiciona o par {[chave: valor]} ao dicionário 'jogadas'
    jogadas[jogada1] = 'R'

    # Retira a primeira jogada da lista de jogadas permitidas
    posicoes.remove(jogada1)

    # Segunda jogada
    jogada2 = valida_jogada('em qual posição quer alocar o GATO?', posicoes)
    jogadas[jogada2] = 'G'

    quartos = atualiza_quartos(quartos, jogadas)

    # Se a segunda jogada for igual a 6, significa que o GATO ficou do lado do RATO
    # e portanto o usuário perdeu o jogo, a condicional abaixo é satisfeita e a
    # função retorna 0
    if not ganhou(quartos):
        print('Game over!!!')
        return 0

    print('Resposta correta!!!')

    # Retorna 1 se a condicional simples acima não for satisfeita
    return 1


def segunda_fase():
    """
    Essa função executa a segunda fase do jogo. Primeiro ela imprime na tela
    as instruções da fase 2, define uma lista de listas que contém a organização
    dos quartos e imprime na tela essa lista. Em seguida ela define uma lista de
    posições permitidas e pergunta para o usuário a primeira jogada. A primeira
    jogada é removida da lista de jogadas possíveis e em seguida é solicitado
    ao usuário a segunda jogada e assim por diante. Se a terceira jogada for
    diferente da posição 1, isso quer dizer que o OSSO ficou ao lado de um CÃO,
    o que não pode pelas regras do jogo, e a função retorna 0. Caso contrário
    a função retorna 1.
    :return: 0 se o usuário perder o jogo e 1 se passar de fase
    """
    print('\nBem vindos a fase 2!')
    print('Na Fase 2, o jogador deve alocar o CÃO, outro CÃO e o OSSO na seguinte matriz que '
          'representa os quartos:')
    quartos = [['-', '*', '*', '*'],
               ['*', 'C', '-', '-']]
    imprime_quartos(quartos)
    posicoes = posicoes_permitidas(quartos)
    jogadas = {}
    jogada1 = valida_jogada('em qual posição quer alocar o CÃO?', posicoes)
    jogadas[jogada1] = 'C'
    posicoes.remove(jogada1)
    jogada2 = valida_jogada('em qual posição quer alocar o outro CÃO?', posicoes)
    jogadas[jogada2] = 'C'
    posicoes.remove(jogada2)
    jogada3 = valida_jogada('em qual posição quer alocar o OSSO?', posicoes)
    jogadas[jogada3] = 'O'
    quartos = atualiza_quartos(quartos, jogadas)
    if not ganhou(quartos):
        print('Game over!!!')
        return 0

    print('Resposta correta!!!')
    return 1


def terceira_fase():
    """
    Essa função executa a terceira fase do jogo. Primeiro ela imprime na tela
    as instruções da fase 3, define uma lista de listas que contém a organização
    dos quartos dessa fase e imprime na tela essa lista. Em seguida ela define
    uma lista de posições permitidas e pergunta para o usuário a primeira jogada.
    A primeira jogada é removida da lista de jogadas possíveis e em seguida é
    solicitado ao usuário a segunda jogada e assim por diante. Se a terceira
    jogada for diferente da posição 1, isso quer dizer que o OSSO ficou ao lado
    de um CÃO, o que não pode pelas regras do jogo, e a função retorna 0. Caso
    contrário a função retorna 1.
    :return: 0 se o usuário perder o jogo e 1 se passar de fase
    """
    print('\nBem vindos a fase 3!')
    print('Na Fase 3, o jogador deve alocar o GATO, o RATO e o OSSO na seguinte matriz que '
          'representa os quartos:')
    quartos = [['-', '*', '*', '*'],
               ['-', 'G', '-', '*']]
    imprime_quartos(quartos)
    posicoes = posicoes_permitidas(quartos)
    jogadas = {}
    jogada1 = valida_jogada('em qual posição quer alocar o GATO?', posicoes)
    jogadas[jogada1] = 'G'
    posicoes.remove(jogada1)
    jogada2 = valida_jogada('em qual posição quer alocar o RATO?', posicoes)
    jogadas[jogada2] = 'R'
    posicoes.remove(jogada2)
    jogada3 = valida_jogada('em qual posição quer alocar o OSSO?', posicoes)
    jogadas[jogada3] = 'O'
    quartos = atualiza_quartos(quartos, jogadas)
    if not ganhou(quartos):
        print('Game over!!!')
        return 0

    print('Resposta correta!!!')
    return 1


def quarta_fase():
    """
    Essa função executa a quarta fase do jogo. Primeiro ela imprime na tela
    as instruções da fase 4, define uma lista de listas que contém a organização
    dos quartos dessa fase e imprime na tela essa lista. Em seguida ela define
    uma lista de posições permitidas e pergunta para o usuário a primeira jogada.
    A primeira jogada é removida da lista de jogadas possíveis e em seguida é
    solicitado ao usuário a segunda jogada e assim por diante. Se a terceira
    jogada for diferente da posição 1, isso quer dizer que o OSSO ficou ao lado
    de um CÃO, o que não pode pelas regras do jogo, e a função retorna 0. Caso
    contrário a função retorna 1.
    :return: 0 se o usuário perder o jogo e 1 se passar de fase
    """
    print('\nBem vindos a fase 4!')
    print('Na Fase 4, o jogador deve alocar o QUEIJO, outro QUEIJO e o OSSO na seguinte matriz que '
          'representa os quartos:')
    quartos = [['-', '-', '-', '*'],
               ['*', 'R', '*', '*']]
    imprime_quartos(quartos)
    posicoes = posicoes_permitidas(quartos)
    jogadas = {}
    jogada1 = valida_jogada('em qual posição quer alocar o QUEIJO?', posicoes)
    jogadas[jogada1] = 'Q'
    posicoes.remove(jogada1)
    jogada2 = valida_jogada('em qual posição quer alocar o outro QUEIJO?', posicoes)
    jogadas[jogada2] = 'Q'
    posicoes.remove(jogada2)
    jogada3 = valida_jogada('em qual posição quer alocar o OSSO?', posicoes)
    jogadas[jogada3] = 'O'
    quartos = atualiza_quartos(quartos, jogadas)
    if not ganhou(quartos):
        print('Game over!!!')
        return 0
    print('Resposta correta!!!')
    return 1


# Programa principal

# Imprime na tela o cabeçalho do jogo
cabecalho()
# Se o usuário passar por todas as fases ele ganha o jogo
if primeira_fase() \
        and segunda_fase() \
        and terceira_fase() \
        and quarta_fase():
    print('Parabéns! Você ganhou o jogo!!!')
