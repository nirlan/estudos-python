# Variável de controle para continuar ou encerrar o programa.
continua = 1

# Enquanto 'continua' for igual a 1 o programa continuará no loop 'while'.
while continua:

    # Variável 'nomeAluno' recebe uma string do nome do aluno a partir de uma entrada do usuário.
    nomeAluno = input('Digite o nome do aluno: ')

    # Variável 'idadeAluno' recebe a idade da criança como um número inteiro a partir de uma entrada do usuário.
    idadeAluno = int(input('Digite a idade do aluno: '))

    # Valida a entrada do usuário: enquanto a idade não for maior ou igual a 1 ano e menor que 18 anos
    # o programa informa que a idade é inválida e solicita que digite uma nova idade.
    while idadeAluno < 1 or idadeAluno > 17:
        idadeAluno = int(input('Por favor, digite uma idade válida... ( 1 a 17 anos)\n'))

    # Condicionais aninhadas que checam o valor da variável 'idadeAluno':
    # a) se a idade do aluno for maior ou igual a 1 ano e menor que 6 anos
    #    a variável 'etapaEnsino' recebe uma string 'Ensino Infantil';
    if 1 <= idadeAluno < 6:
        etapaEnsino = 'Ensino Infantil'

    # b) se a idade do aluno for maior ou igual a 6 anos e menor que 11 anos
    #    a variável 'etapaEnsino' recebe uma string 'Ensino Fundamental I';
    elif 6 <= idadeAluno < 11:
        etapaEnsino = 'Ensino Fundamental I'

    # c) se a idade do aluno for maior ou igual a 11 anos e menor que 15 anos
    #    a variável 'etapaEnsino' recebe uma string 'Ensino Fundamental II';
    elif 11 <= idadeAluno < 15:
        etapaEnsino = 'Ensino Fundamental II'

    # d) senão atender nenhuma das condições acima conclui-se que a idade é maior que 15 anos
    #    e a variável 'etapaEnsino' recebe uma string 'Ensino Médio'.
    else:
        etapaEnsino = 'Ensino Médio'

    # Imprime na tela do usuário o nome do aluno, a sua idade e em qual etapa de ensino ele está.
    print('\nO(A) aluno(a) {} tem {} anos e está no {}\n'.format(nomeAluno, idadeAluno, etapaEnsino))

    # Pergunta para o usuário se ele quer continuar o programa, e solicita que digite '0' para encerrar o programa ou
    # '1' para continuar. A variável 'continua' recebe o input do número digitado pelo usuário.
    continua = int(input('Deseja continuar?\t0 - Não\t\t1 - Sim '))

    # Valida a entrada do usuário: se ele digitar um número que não seja '0' ou '1' o programa
    # informa o erro e solicita uma nova entrada.
    while continua != 0 and continua != 1:
        continua = int(input('\nOpção inválida. Digite uma opção válida...\n'
                             'Deseja continuar?\t0 - Não\t\t1 - Sim'))

    #  Se o usuário digitar '0' a variável 'continua' recebe o valor inteiro 0, o usuário é informado do encerramento
    #  do programa e o loop encerra porque o inteiro 0 é avaliado como False no loop 'while' do início do programa.
    #  Se o usuário digitar '1' a variável 'continua' recebe o valor inteiro 1 que é avaliado como True no loop 'while'
    #  do início do programa, recomeçando o loop.
    if not continua:
        print('Saindo do programa...')
