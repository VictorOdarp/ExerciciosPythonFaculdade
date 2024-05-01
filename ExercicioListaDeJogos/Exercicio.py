def cadastrarJogo(nomeArquivo):

    nome = input("Qual o nome do jogo?: ")
    nomeVideoGame = input("Qual o nome do VideoGame?: ")
    print()

    try:
        arquivo = open(nomeArquivo, 'at')
    except:
        print("Erro ao abrir o arquivo!")
    else:
        arquivo.write("Nome do jogo: {} | Nome do VideoGame: {} \n" .format(nome, nomeVideoGame))
    finally:
        arquivo.close()

def existeArquivo(nomeArquivo):

    try:
        arquivo = open(nomeArquivo, 'rt')
        arquivo.close()

    except FileNotFoundError:
        return False
    else:
        return True

def criarArquivo(nomeArquivo):

    try:
        arquivo = open(nomeArquivo, 'wt+')
        arquivo.close()
    except:
        print("Erro na criação do arquivo!")
    else:
        print("Arquivo {} foi criado com sucesso!\n" .format(nomeArquivo))

def listarArquivo(nomeArquivo):
    try:
        arquivo = open(nomeArquivo, 'rt')
    except:
        print("Erro ao ler o arquivo")
    else:
        print(arquivo.read())
    finally:
        arquivo.close()

def limparArquivo(nomeArquivo):

    try:
        arquivo = open(nomeArquivo, 'wt')
    except:
        print("Erro ao abrir o arquivo!")
    else:
        print("A lista foi limpada com sucesso!")
    finally:
        arquivo.close()




#Programa Principal
arquivo = "games.txt"

if (existeArquivo(arquivo)):
    print("Arquivo localizado no computador!")
else:
    arquivo = input("Qual no nome do seu arquivo? (Exemplo: arquivo.txt): ")
    criarArquivo(arquivo)

while True:
    print("Menu [Cadastro de jogos]\n")
    print("1 - Cadastrar novo jogo")
    print("2 - Listar todos os jogos")
    print("3 - Limpar a lista de jogos")
    print("4 - Sair")
    print()

    validacao = input("Qual a opção desejada?: ")
    print()

    if (validacao == "1"):
        print("[Selecionada a opção de cadastrar um novo jogo!]\n")
        cadastrarJogo(arquivo)

    elif (validacao == "2"):
        print("[Selecionada a opção de listar seus jogos cadastrados!]")
        listarArquivo(arquivo)
    elif (validacao == "3"):
        print("[Selecionada a opção de limpar a lista de seus jogos cadastrados!]")
        limparArquivo(arquivo)
    elif (validacao == "4"):
        print("Encerrando o programa...")
        break
    else:
        print("Opção inválida!")
        continue
