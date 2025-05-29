#Dada uma lista de números inteiros, retorna a soma de todos os números pares da lista
def soma_pares(lst):
    pares = []
    for i in lst:
        if i % 2 == 0:
            pares.append(i)
    print(sum(pares))

soma_pares([1, 2, 3, 4, 5, 6])  # Saída: 12


#Dado um tuplo de números inteiros, retorna o produto de todos os elementos.
def produto_tuplo(tuplo):
    sum = 1
    for i in tuplo:
        sum *= i
    print(sum)

produto_tuplo((2, 3, 4))  # Saída: 24