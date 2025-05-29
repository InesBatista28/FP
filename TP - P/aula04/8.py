
def soma():
    a = 0
    total = 0
    while True:
        s = input("Digite um número: ")
        a += 1
        if s == "":
            break
        else:
            s = float(s)
            total += s
            m = total / a
    return m

def main():
    m = soma()
    print("A média dos números é ", m) 

if __name__ == "__main__":
    main()
