#Criamos uma função que retorna a soma de todos os números de 1 até n

def soma(n):
    if n == 0:
        return 0
    return n + soma(n-1)

print(soma(5))