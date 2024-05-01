#DECLARAÇÃO DE VARIÁVEIS.
valor = 0
valorTotal = 0

#APRESENTAÇÃO E CARDÁPIO DA LOJA.
print("Bem-Vindo a Loja de Gelados do Victor Eduardo do Prado Andrade - RU: 4059326")
print("------------------Cárdapio----------------------")
print("----| Tamanho | Cupuaçu (CP) |  Açai (AC)  |----")
print("----|    P    |   R$ 10,00   |   R$ 12,00  |----")
print("----|    M    |   R$ 15,00   |   R$ 17,00  |----")
print("----|    G    |   R$ 19,00   |   R$ 21,00  |----")
print("------------------------------------------------")

#ABERTURA DE LOOP PARA VERIFICAÇÕES.
while True:

    #VERIFICAÇÃO DE SABOR DO PRODUTO.
    sabor = input("Entre com o sabor desejado (CP/AC): ")
    if(sabor != "AC" and sabor != "CP"):
        print("Sabor inválido. Tente novamente")
        continue
    elif (sabor == "CP"):
        sabor = "Cupuaçu"
    elif (sabor == "AC"):
        sabor = "Açai"
    print()

    #VERIFICAÇÃO DE TAMANHO DO PRODUTO.
    tamanho = input("Entre com o tamanho desejado (P/M/G): ")
    if(tamanho != "P" and tamanho != "M" and tamanho != "G"):
        print("Tamanho inválido. Tente novamente.")
        continue
    elif (tamanho == "P"):
        tamanho = "P"
    elif (tamanho == "M"):
        tamanho = "M"
    elif (tamanho == "G"):
        tamanho = "G"

    #VERIFICAÇÃO FINAL DE SABOR E TAMANHO PARA A PRECIFICAÇÃO DOS ITENS.
    if (sabor == "Açai" and tamanho == "P"):
        valor = 12.00
        valorTotal += valor
        print("Você pediu {} no tamanho {}: R$ {}" .format(sabor, tamanho, valor))
    if (sabor == "Açai" and tamanho == "M"):
        valor = 17.00
        valorTotal += valor
        print("Você pediu {} no tamanho {}: R$ {}" .format(sabor, tamanho, valor))
    if (sabor == "Açai" and tamanho == "G"):
        valor = 21.00
        valorTotal += valor
        print("Você pediu {} no tamanho {}: R$ {}".format(sabor, tamanho, valor))
    if (sabor == "Cupuaçu" and tamanho == "P"):
        valor = 10.00
        valorTotal += valor
        print("Você pediu {} no tamanho {}: R$ {}".format(sabor, tamanho, valor))
    if (sabor == "Cupuaçu" and tamanho == "M"):
        valor = 15.00
        valorTotal += valor
        print("Você pediu {} no tamanho {}: R$ {}".format(sabor, tamanho, valor))
    if (sabor == "Cupuaçu" and tamanho == "G"):
        valor = 19.00
        valorTotal += valor
        print("Você pediu {} no tamanho {}: R$ {}".format(sabor, tamanho, valor))

    #VALIDAÇÃO PARA ENTENDER SE O USUÁRIO QUER FAZER UM NOVO PEDIDO OU FECHAR A CONTA.
    validacao = input("Deseja mais alguma coisa? (S/Digite outra tecla)?: ")
    if(validacao == "S"):
        continue
    else:
        print()
        print("O valor total a ser pago: R$ {}" .format(valorTotal))
        break