#função para receber texto e fazer contagem da frequência de cada palavra

def palavras():
    frase = input("Enter a random phrase: ")
    palavras = frase.split()   #dúvida, como tiar pontuação
    contagem = {}
    for i in palavras:
        if i.isalpha():
            if i not in contagem:
                contagem[i] = 1
            else:
                contagem[i] += 1
    return contagem

print(palavras())
