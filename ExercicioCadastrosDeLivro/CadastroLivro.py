#FUNÇÃO DO MENU PRINCIPAL
def menu_principal(id_global, lista_livro):

    #OPÇÕES PARA SELEÇÃO DO USUÁRIO
    print("-------------------------------- MENU PRINCIPAL --------------------------------")
    print("Escolha uma das opções abaixo:")
    print("1 - Cadastrar Livro")
    print("2 - Consultar Livro")
    print("3 - Remover Livro")
    print("4 - Encerrar o programa")

    #ENTRADA PARA VERIFICAR A OPÇÃO SELECIONADA
    validacao = int(input("Selecione uma opção: "))
    print("**************************************************************************************")

    #VERIFICAÇÃO DA OPÇÃO SELECIONADA E AS FUNÇÕES COM SEUS DESTINOS.
    if (validacao == 1):
        cadastrar_livro(id_global, lista_livro)
    elif (validacao == 2):
        consultar_livro(id_global, lista_livro)
    elif (validacao == 3):
        remover_livro(id_global, lista_livro)
    elif (validacao == 4):
        print("Encerrando o programa...")
    else:
        print("Opção inválida!")
        print("***********************************************************************************")

#FUNÇÃO DE CADASTRAMENTO DO LIVRO
def cadastrar_livro(id_global, lista_livro):

#ABERTURA DA LISTA PARA CRIAR A LISTA DE LIVROS DENTRO DELA.
    livros = {}
#VARIAVEL PARA ACRESCENTAR A ID DO LIVRO NO SEU CADASTRO.
    id_global = len(lista_livro) + 1

#CADASTRO DO LIVRO NA LISTA
    print("------------------------------ MENU CADASTRAR LIVROS ---------------------------------")
    livros['Id'] = id_global
    print("Id do livro {}" .format(id_global))
    livros['Nome'] = input("Qual o nome do Livro?: ")
    livros['Autor'] = input("Qual o nome do Autor?: ")
    livros['Editora'] = input("Qual o nome da Editora do livro?: ")
    lista_livro.append(livros.copy())

    print("Livro cadastrado!")
    print("********************************************************************************")
    menu_principal(id_global, lista_livro)

#FUNÇÃO DE CONSULTA DE LIVROS CADASTRADOS
def consultar_livro(id_global, lista_livro):

    #OPÇÕES DE TIPOS DE CONSULTA.
    print("------------------------------ MENU CONSULTAR LIVROS ---------------------------------")
    print("Escolha uma das opções abaixo:")
    print("1 - Consultar Todos")
    print("2 - Consultar por ID")
    print("3 - Consultar por Autor")
    print("4 - Retornar ao Menu")

    # ENTRADA PARA VERIFICAR A OPÇÃO SELECIONADA
    validacao = int(input("Selecione uma opção: "))
    print("********************************************************************************")

    #VERIFICAÇÃO DA OPÇÃO SELECIONADA COM SEUS DETERMINADOS DESTINOS.
    if (validacao == 1):

        #BUSCA TODOS OS LIVROS NA LISTA
        print("---------------------------------")
        for livro in lista_livro:
            for i,j in livro.items():
                print("{}: {}" .format(i,j))
        print("---------------------------------")

        consultar_livro(id_global, lista_livro)
    elif(validacao == 2):

        #BUSCA UM LIVRO ESPECIFICO BASEADO NA ID DE ENTRADA.

        ID = int(input("Qual o ID do livro que está procurando?: "))

        print("---------------------------------")
        for livro in lista_livro:
            if livro["Id"] == ID:
                for i, j in livro.items():
                    print("{}: {}".format(i, j))
                print("-----------------------------")


        consultar_livro(id_global, lista_livro)
    elif(validacao == 3):

        #BUSCA LIVROS ESPECIFICOS BASEADO NOS AUTORES CADASTRADOS NOS LIVROS.

        Autor = input("Digite o Autor que você está procurando: ")

        print("-------------------------------------")
        for livro in lista_livro:
            if livro["Autor"] == Autor:
                for i, j in livro.items():
                    print("{}: {}".format(i, j))
                print("-----------------------------")

        consultar_livro(id_global, lista_livro)

    elif (validacao == 4):

        #RETORNA AO MENU PRINCIPAL

        print("Retornando ao Menu Principal!")
        menu_principal(id_global, lista_livro)
    else:
        print("Opção inválida!")
        print("********************************************************************************")

#FUNÇÃO PARA REMOÇÃO DE LIVRO DA LISTA
def remover_livro(id_global, lista_livro):

    print("-------------------------------- MENU REMOVER LIVRO ---------------------------------")
    ID = int(input("Qual o ID do livro que deseja remover?: "))
    print("********************************************************************************")

    #REMOÇÃO DO LIVRO DA LISTA BASEADO NA ID DE ENTRADA
    #COMO O INDICE COMEÇA EM ZERO, PRECISAMOS COLOCAR A ID - 1
    for livro in lista_livro:
        if livro["Id"] == ID:
            del lista_livro[ID-1]

    menu_principal(id_global, lista_livro)


#PROGRAMA PRINCIPAL

#ABERTURA DE LISTA E TAMBÉM DA VARIÁVEL DE ID_GLOBAL DOS LIVROS
lista_livro = []
id_global = 0

#APRESENTAÇÃO DO ALUNO E INICIO NA FUNÇÃO DE MENU PRINCIPAL
print("Bem vindo ao controle de livros do Victor Eduardo do Prado Andrade - RU: 4059326")
print("********************************************************************************")
menu_principal(id_global, lista_livro)