#Crie uma função pesquisa(lista, valor) que recebe uma lista de números e um valor a ser encontrado. 
# A função deve retornar o índice da primeira ocorrência do valor na lista ou -1 caso o valor não esteja presente.

def pesquisa(lista, valor):
    for i in range(len(lista)):
        if lista[i] == valor:
            return i
    return -1  
        
# Testes
print(pesquisa([3, 7, 2, 8, 4], 8))  # Saída: 3
print(pesquisa([1, 2, 3, 4, 5], 10))  # Saída: -1