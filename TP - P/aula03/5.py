def max2(a, b):
    if a > b:
        return a
    else:
        return b
    
def max3(a, b, c):
    if a>b:
        if a>c:
            return a
        else: 
            return c 
    else:
        if b>c:
            return b
        else:
            return c
    
def main():
    numero1 = int(input("Digite o primeiro número: "))
    numero2 = int(input("Digite o segundo número: "))
    numero3 = int(input("Digite o terceiro número: "))
    print("O maior número é", max2(numero1, numero2))
    print("O maior número é", max3(numero1, numero2, numero3))

main()