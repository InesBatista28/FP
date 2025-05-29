def ispalindrome():
    x = input("Digite uma palavra: ")
    if x == x[::-1]:  #palavra escrita de trás para a frente
        print("É palíndromo")
    else:
        print("Não é palíndromo")