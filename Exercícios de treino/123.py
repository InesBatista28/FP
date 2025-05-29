produtos = [
    {"nome": "Teclado", "preco": 150, "estoque": 10},
    {"nome": "Monitor", "preco": 800, "estoque": 5},
    {"nome": "Mouse", "preco": 100, "estoque": 20},
    {"nome": "Cadeira", "preco": 600, "estoque": 8},
]
  
#Ordenar produtos por preço
ordenado_por_preco = sorted(produtos, key = lambda x : x["preco"])
print("Ordenados por preço: ", [x["nome"] for x in ordenado_por_preco])

#Ordenar pelo estoque
ordenado_por_estoque = sorted(produtos, key = lambda x : x["estoque"], reverse = True)
print("Ordenados por estoque: ", [x["nome"] for x in ordenado_por_estoque])

#Ordenado por nome 
ordenado_por_nome = sorted(produtos, key = lambda x : x["nome"])
print("Ordenados por nome: ", [x["nome"] for x in ordenado_por_nome])