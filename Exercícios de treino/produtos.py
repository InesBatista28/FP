estoque = {
    "Camiseta": {"Loja A": 20, "Loja B": 15, "Loja C": 10},
    "Calça": {"Loja A": 5, "Loja B": 8, "Loja C": 12},
    "Tênis": {"Loja A": 7, "Loja B": 3, "Loja C": 6}
}

#Exibir a quantidade de um produto em uma loja específica
def quantidades(estoque):
    nome = input("Qual o nome do produto?")
    if nome in estoque:
        info = estoque[nome]
        loja = input("Qual a loja que pretende (A/B/C): ")
        quantidade = info[loja]
        print("A quantidade de produtos {} no estoque escolhido é {}".format(nome, quantidade))
        return quantidade
    else:
        print("O produto não está em stock")

quantidades(estoque)

# Somar o total de produtos disponíveis de um item em todas as lojas
def total(estoque):
    nome = input("Nome do Produto: ")
    soma = 0
    if nome in estoque:
        for loja, quantidade in estoque[nome].items():
            soma += quantidade
        print("O número total do estoque do produto {} é {}".format(nome, soma))
        return quantidade
    else:
        print("O produto não está em stock")

total(estoque)


