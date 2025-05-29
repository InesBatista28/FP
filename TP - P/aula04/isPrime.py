def isPrime(n):
    if n < 2: 
        return 0
    for i in range(2, int(n**0.5) + 1):  #dividimos até à raiz quadrada de n 
        if n % i == 0: 
            return 0
    return 1  

def main():
    for i in range(1, 101):
        if isPrime(i) == 1:
            print(f"{i}: Primo")
        else:
            print(f"{i}: Não primo")

main()
