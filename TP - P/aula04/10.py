def finobacci():
    lst = [0, 1]
    while True:
        N = input("Digite o número de termos: ")
        if N == "":
            print("Fim do programa")
            break
        else:
            N = int(N)
            for i in range(2, N):
                novo = lst[-1] + lst[-2]
                lst.append(novo)
            print(lst)

finobacci()
            