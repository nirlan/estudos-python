from random import randint

def cabecalho():
    """
    Imprime na tela o cabeçalho do programa
    :return: none
    """
    print('*' * 11, 'Menu', '*' * 11)
    print('1 - Nova inscrição')
    print('2 - Visualizar inscrição')
    print('0 - Encerrar')


def valida_opcao(texto: str, minimo: int, maximo: int):
    """
    Exibe um campo para o usuário entrar com um número dentre as opções
    exibidas no menu e valida a entrada do usuário.
    :param texto: texto do campo a ser preenchido pelo usuário
    :param minimo: número inteiro mínimo das opções do menu
    :param maximo: número inteiro máximo das opções do menu
    :return: número inteiro que representa a opção do usuário
    """
    # Pergunta e armazena a opção feita pelo o usuário
    while True:
        try:
            op = int(input(texto))
        except ValueError:
            print('Erro: digite uma opção válida!')
            continue
        else:
            if minimo <= op <= maximo:
                return op
            print('Erro: digite uma opção válida!')
            continue


def valida_nome(texto: str):
    """
    Valida o nome digitado pelo usuário. A função recebe como parâmetro o texto
    a ser impresso na tela para o usuário. Enquanto o usuário não digitar um
    nome válido, o programa informa o erro e solicita uma nova entrada.
    :param texto: texto que vai ser exibido para o usuário
    :return: nome do usuário
    """
    nome = ''
    # Enquanto não houver um nome o loop continuará
    while not nome:
        nome = input(texto)
        # O nome é dividido em uma lista de palavras com a função 'split(' ')'.
        # Cada palavra separada por um espaço em branco se torna um item da lista.
        # Cada palavra então pode ser avaliada individualmente pela função 'isalpha()'
        # para verificar a existência de caracteres que não correspondem a letras.
        # Se houver, é atribuída à variável 'nome' uma string vazia '' e realiza-se
        # o 'break' do laço 'for', fazendo o interpretador ir de volta para o início
        # do laço 'while'. Como a variável 'nome' se tornou vazia, ela é avaliada como
        # falsa (Falsy), e se reinicia o laço fazendo uma nova solicitação de nome ao
        # usuário.
        for palavra in nome.split(' '):
            if not palavra.isalpha():
                print('Erro: digite um nome válido!')
                nome = ''
                break
    # Se a condicional acima não for satisfeita para nenhuma das palavras do nome
    # a função retorna uma variável string contendo o nome digitado pelo usuário.
    return nome


def valida_email(texto: str):
    """
    Valida o email digitado pelo usuário. A função recebe como parâmetro o texto
    a ser impresso na tela para o usuário. Enquanto o usuário não digitar um
    email válido, o programa informa o erro e solicita uma nova entrada.
    :param texto: texto que vai ser exibido para o usuário
    :return: email do usuário
    """
    # Laço infinito
    while True:
        # Solicita uma entrada ao usuário
        email = input(texto)
        # Condicional simples que checa se a palavra inserida pelo usuário contém
        # ao menos um caractere '@' e '.', e nenhum espaço em branco.
        if email.find('@') != -1 and email.find('.') != -1 and email.find(' ') == -1:
            # Se a condicional for satisfeita a função retorna o email do usuário
            return email
        # Caso a condicional não for satisfeita, o programa imprime na tela a mensagem
        # de erro e o laço volta para o início da execução
        print('Erro: digite um email válido!')


def valida_telefone(texto: str):
    """
    Valida o telefone digitado pelo usuário. Enquanto não digitado um ou mais
    números inteiros o programa informa o erro e continua pedindo uma nova
    entrada.
    :param texto: texto que vai ser exibido para o usuário
    :return: telefone do usuário
    """
    while True:
        # Solicita uma entrada ao usuário
        try:
            telefone = int(input(texto))
        # Se o valor digitado não for um número é lançada esta exceção
        except ValueError:
            print('Erro: digite um telefone válido!')
            # Volta ao início do laço
            continue
        else:
            # Caso não seja lançada a exceção, o número do telefone é
            # retornado pela função
            return telefone


def valida_curso(texto: str):
    """
       Valida o curso digitado pelo usuário. A função recebe como parâmetro o texto
       a ser impresso na tela para o usuário. Enquanto o usuário não digitar um
       curso válido, o programa informa o erro e solicita uma nova entrada.
       :param texto: texto que vai ser exibido para o usuário
       :return: curso do usuário
       """
    curso = ''
    # Enquanto não houver um curso o loop continuará
    while not curso:
        curso = input(texto)
        # O curso é dividido em uma lista de palavras com a função 'split(' ')'.
        # Cada palavra separada por um espaço em branco se torna um item da lista.
        # Cada palavra então pode ser avaliada individualmente pela função 'isalnum()'
        # para verificar a existência de caracteres que não correspondem a letras e
        # números. Se houver, é atribuída à variável 'curso' uma string vazia '' e
        # realiza-se o 'break' do laço 'for', fazendo o interpretador ir de volta para o
        # início do laço 'while'. Como a variável 'curso' se tornou vazia, ela é avaliada
        # como falsa (Falsy), e se reinicia o laço fazendo uma nova solicitação de curso
        # ao usuário.
        for palavra in curso.split(' '):
            if not palavra.isalnum():
                print('Erro: digite um curso válido!')
                curso = ''
                break
    # Se a condicional acima não for satisfeita para nenhuma das palavras do curso
    # a função retorna uma variável string contendo o curso digitado pelo usuário.
    return curso.upper()


def gera_voucher(cadastros: list):
    """
    Gera um número único para o voucher e armazena em um dicionário.
    :param cadastros: lista de pessoas cadastradas
    :return: dicionário contendo um voucher único, ex.{'voucher': 123}
    """
    # Cria dicionário para armazenar os dados do novo inscrito
    inscricao = {}
    # Se a lista de cadastro estiver vazia (primeiro inscrito), é gerado um voucher
    # de modo randômico entre o número 100 (inclusive) e 400 (inclusive), esse número
    # é armazenado no dicionário 'inscrição' com a chave 'voucher', que é retornada
    # pela função
    if not cadastros:
        voucher = randint(100, 400)
        inscricao['voucher'] = voucher
        return inscricao
    # Declara e inicializa com valor 0 (Falsy) a variável voucher que será a variável de
    # controle do laço 'while'
    voucher = 0
    # Enquanto 'voucher' for False o laço se repete, pois 'not False == True'
    while not voucher:
        # Gera um número de voucher aleatório
        voucher = randint(100, 400)
        # Itera sobre a lista de dicionários em cadastro buscando se já existe um voucher
        # com o mesmo número. Se houver, a variável 'voucher' recebe novamente o valor 0
        # e o laço 'for' é encerrado (break), fazendo o interpretador voltar ao início do
        # laço 'while'. Como 'voucher' tem valor 0, a condicional do laço é not 'voucher'
        # a condicional é avaliada como 'True' e o laço se repete.
        for cadastro in cadastros:
            if cadastro['voucher'] == voucher:
                voucher = 0
                break
    # Caso o voucher gerado não esteja já presente em nenhum dicionário da lista 'cadastros'
    # o número do voucher é adicionado ao dicionário 'inscricao' com a chave 'voucher', que
    # é retornada pela função
    inscricao['voucher'] = voucher
    return inscricao


# Programa principal

# Lista de dicionários para armazenar as informações de todos os inscritos
cadastros = []

while True:
    # Imprime na tela o cabeçalho
    cabecalho()

    # Valida e armazena a opção escolhida pelo usuário
    opcao = valida_opcao('Opção escolhida: ', 0, 2)

    # Opção 1 selecionada ('Nova inscrição')
    if opcao == 1:
        # Gera e armazena o código único do voucher dentro de um dicionário
        # 'inscricao', onde serão armazenadas as informações individuais
        # de cada inscrito.
        inscricao = gera_voucher(cadastros)
        # Valida e armazena o nome inserido pelo usuário
        nome = valida_nome('Digite seu nome: ')
        inscricao['nome'] = nome
        # Valida e armazena o email inserido pelo usuário
        email = valida_email('Digite email: ')
        inscricao['email'] = email
        # Valida e armazena o telefone inserido pelo usuário
        telefone = valida_telefone('Digite telefone: ')
        inscricao['telefone'] = telefone
        # Valida e armazena o curso inserido pelo usuário
        curso = valida_curso('Digite curso: ')
        inscricao['curso'] = curso

        # Acrescenta o novo inscrito à lista de cadastros
        cadastros.append(inscricao)

    # Opção 2 selecionada ('Visualizar inscrição')
    elif opcao == 2:
        print('-' * 20, 'Lista inscritos', '-' * 20)
        # Para cada dicionário cadastro na lista de dicionários cadastros
        for cadastro in cadastros:
            # Para cada item {i: j} do dicionário cadastro
            for i, j in cadastro.items():
                # Imprime na tela a lista dos usuários inscritos
                print('{}\t:\t{}'.format(i, j))
            print('-' * 20)

    # Opção 0 selecionada ('Encerrar')
    elif opcao == 0:
        print('Encerrando o programa...')
        break
