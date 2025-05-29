#Calcular o total de vendas realizadas, o vendedor com o maior numero de vendas, lista de vendedores que realizaram vendas acima de um determinado valor
vendas = [
    {"vendedor": "Ana", "valor": 200},
    {"vendedor": "João", "valor": 350},
    {"vendedor": "Ana", "valor": 150},
    {"vendedor": "João", "valor": 100},
    {"vendedor": "Maria", "valor": 400}
]

def analise_vendas(vendas):
    total_vendas = 0
    vendedores = {}
    for i in vendas:
        total_vendas += i["valor"]
        vendedor = i["vendedor"]
        venda = i["valor"]
        if vendedor not in vendedores:
            vendedores[vendedor] = venda
        else:
            vendedores[vendedor] += venda

    melhor_vendedor = max(vendedores, key=vendedores.get)   #.get vai retornar as partes do valores do dicionário, deixando sempre os nomes associados(chat - dúvida com .values)
    
    minímo = int(input("Enter a random value: "))
    lst = []
    for i in vendedores:
        if vendedores[i] > minímo:
            lst.append(i)


    print(total_vendas)
    print(melhor_vendedor)
    print(lst)
    return total_vendas, melhor_vendedor, lst
    

analise_vendas(vendas)

