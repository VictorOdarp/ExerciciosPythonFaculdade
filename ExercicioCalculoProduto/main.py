# Boas-vindas e Identificação do Aluno.
print("Bem-Vindo a Loja do Victor Eduardo do Prado Andrade - RU: 4059326")

# Entrada do valor unitário do produto.
produto = float(input("Entre com o valor unitário do produto: R$ "))
# Entrada da quantidade do produto.
quantidade = int(input("Entre com a quantidade do produto: "))
# Operação de multiplação entre a quantidade e o produto, buscando o valor total bruto.
result = produto * quantidade

# Condicional de que se o valor total bruto abaixo de 2500, o desconto será de 0%.
if (result < 2500.00):

    print("O valor do produto sem desconto foi R${}".format(result))

    desconto = 0
    valorFinal = result - (result / 100) * desconto
    print("O valor do produto com desconto foi R${} (desconto {}%)".format(valorFinal, desconto))

# Condicional de que se o valor total bruto for maior ou igual a 2500 e abaixo de 6000, o desconto será de 4%.
elif (result >= 2500.00 and result < 6000.00):

    print("O valor do produto sem desconto foi R${}".format(result))

    desconto = 4
    valorFinal = result - (result / 100) * desconto
    print("O valor do produto com desconto foi R${} (desconto {}%)".format(valorFinal, desconto))

# Condicional de que se o valor total bruto for maior ou igual a 6000 e abaixo de 10000, o desconto será de 7%.
elif (result >= 6000.00 and result < 10000.00):

    print("O valor do produto sem desconto foi R${}".format(result))

    desconto = 7
    valorFinal = result - (result / 100) * desconto
    print("O valor do produto com desconto foi R${} (desconto {}%)".format(valorFinal, desconto))

# Condicional final.
# Se o valor total bruto for maior ou igual que 10000, o desconto será de 11%
# As condicionais acima nos trazem está condição final.
else:

    print("O valor do produto sem desconto foi R${}".format(result))

    desconto = 11
    valorFinal = result - (result / 100) * desconto
    print("O valor do produto com desconto foi R${} (desconto {}%)".format(valorFinal, desconto))