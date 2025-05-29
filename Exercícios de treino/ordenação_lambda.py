#Dada uma lista de palavras, ordene-a pelo tamanho das palavras usando sorted() e uma expressão lambda.

def ordena_por_tamanho(palavras):
    return sorted(palavras, key = lambda x : (len(x), x[0]))


palavras = ["banana", "maçã", "kiwi", "abacaxi"]
ordenadas = ordena_por_tamanho(palavras)
print(ordenadas)  # Saída esperada: ['kiwi', 'maçã', 'banana', 'abacaxi']