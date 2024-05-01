#FUNÇÃO PARA ESCOLHA DO SERVIÇO DA COPIADORA, RETORNANDO O VALOR DO MESMO.
def escolha_servico():

    #LAÇO DE REPETIÇÃO PARA SELEÇÃO DO SERVIÇO
    while True:

        print("Escolha o tipo de serviço desejado")
        print("DIG - Digitalização")
        print("ICO - Impressão Colorida")
        print("IPB - Impressão Preto e Branco")
        print("FOT - Fotocópia")

        servico = input("Serviço desejado: ")

        valorServico = 0

        if (servico == "DIG"):

            print()
            valorServico = 1.10
            return valorServico
        elif (servico == "ICO"):

            print()
            valorServico = 1.00
            return valorServico

        elif (servico == "IPB"):

            print()
            valorServico = 0.40
            return valorServico

        elif (servico == "FOT"):

            print()
            valorServico = 0.20
            return valorServico

        #CASO O USUÁRIO NÃO ESCOLHA UMA OPÇÃO VÁLIDA O LOOPING CONTINUA.
        else:
            print("Escolha inválida!")
            print("Entre com o tipo de serviço desejado novamente... \n")
            continue



#FUNÇÃO PARA DEFINIR O NÚMERO DE PAGINAS E TAMBÉM RETORNAR O VALOR TOTAL E O DESCONTO.
def num_pagina():

    #ESTRUTURA TRY/EXPECT PARA QUANDO O USUÁRIO DIGITAR UM VALOR NÃO NÚMERICO.
    try:
        #LAÇO DE REPETIÇÃO PARA A ESCOLHA DAS PÁGINAS
        while True:

            paginas = int(input("Entre com o número de páginas: "))

            desconto = 0
            valorSemDesconto = 0
            valorPaginas = 0

            #CASO O USUÁRIO EXCEDA O NÚMERO DE PÁGINAS O LAÇO CONTINUA EM LOOPING
            if (paginas >= 20000):

                print("Não aceitamos tantas páginas de uma vez.")
                print("Por favor entre com o numero de páginas novamente.\n")
                continue
            elif (paginas < 20):

                desconto = 0
                valorSemDesconto = servico * paginas
                valorPaginas = valorSemDesconto - (valorSemDesconto / 100 * desconto)
                return paginas, desconto, valorPaginas

            elif (paginas >= 20 and paginas < 200):

                desconto = 15
                valorSemDesconto = servico * paginas
                valorPaginas = valorSemDesconto - (valorSemDesconto / 100 * desconto)
                return paginas, desconto, valorPaginas

            elif (paginas >= 200 and paginas < 2000):

                desconto = 20
                valorSemDesconto = servico * paginas
                valorPaginas = valorSemDesconto - (valorSemDesconto / 100 * desconto)
                return paginas, desconto, valorPaginas

            elif (paginas >= 2000 and paginas < 20000):

                desconto = 25
                valorSemDesconto = servico * paginas
                valorPaginas = valorSemDesconto - (valorSemDesconto / 100 * desconto)
                return paginas, desconto, valorPaginas
    except ValueError:
        print("[ERRO] Valor não númerico!")

#FUNÇÃO PARA DEFINIR SE O USUÁRIO DESEJA UM SERVIÇO EXTRA DA COPIADORA, RETORNANDO O VALOR DO MESMO.
def servico_extra():
    #ESTRUTURA TRY/EXPECT PARA QUANDO O USUÁRIO DIGITAR UM VALOR NÃO NÚMERICO.
    try:
        #LAÇO DE REPETIÇÃO PARA A ESCOLHA DO SERVIÇO EXTRA.
        while True:

            print("Deseja adicionar mais um serviço?")
            print("1 - Encardernação Simples - R$ 15,00")
            print("2 - Encardernação Capa Dura - R$ 40,00")
            print("0 - Não desejo mais nada.")

            validacao = int(input("Selecione uma opção: "))

            if (validacao == 1):

                servicoExtra = 15.00
                return servicoExtra

            elif (validacao == 2):

                servicoExtra = 40.00
                return servicoExtra

            elif (validacao == 0):

                break
            # CASO O USUÁRIO NÃO ESCOLHA UMA OPÇÃO VÁLIDA O LOOPING CONTINUA.
            else:
                print("Opção inválida!")
                print("Entre com a opção desejada novamente...\n")
                continue
    except ValueError:
        print("[ERRO] Valor não númerico!")

#PROGRAMA PRINCIPAL

#BOAS VINDAS E IDENTIFICAÇÃO DO ALUNO.
print("Bem-Vindo aos Serviços de Copiadora do Victor Eduardo do Prado Andrade - RU: 4059326")

#DEFININDO AS VARIAVEIS COM BASE NOS VALORES RETORNADOS DA FUNÇÃO.
servico = escolha_servico()
paginas, desconto, valorPaginas = num_pagina()

#PRINT PARA ESPAÇAMENTO E ORGANIZAÇÃO DO PROGRAMA EM CONSOLE.
print()

#VARIAVEIS DEFINIDAS COM BASE NOS VALORES RETORNADOS E SOMA DESSES VALORES PARA CHEGARMOS AO VALOR FINAL.
servicoExtra = servico_extra()
valorTotal = valorPaginas + servicoExtra

#EXIBIÇÃO NO CONSOLE, COM TOTAL DO SERVIÇO, VALOR SOMENTE DO SERVIÇO, PAGINAS E SERVIÇO EXTRA.
#VALOR DO SERVIÇO COM AS PÁGINAS JÁ ESTÁ COM O DESCONTO DEFINIDO COM BASE NO NÚMERO DE PÁGINAS.
print("Total (R$): {} (Serviço({}) * Paginas({}): {} + Extra(s): {})".format(valorTotal, servico, paginas,
                                                                                 valorPaginas,
                                                                                 servicoExtra))