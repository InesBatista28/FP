#Dado um dicionário com nomes e idades, ordene as pessoas pela idade em ordem crescente usando sorted() e uma expressão lambda.

def ordena_por_idade(pessoas):
    return sorted(pessoas.items(), key = lambda x : x[1])   #x[1] == idade no dicionário

pessoas = {"Ana": 25, "Bruno": 30, "Carlos": 22}
ordenadas = ordena_por_idade(pessoas)
print(ordenadas)  