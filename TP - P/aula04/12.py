def divisores():
    N = int(input("Digite um número: "))
    b = 0
    for i in range(1, N+1):
        if N % i == 0:
            b += i
            print(i)
    print("A soma dos dividores de {} é {}".format(N, b))
    if b > N:
        print("{} é um número abundante".format(N))
    elif b == N:
        print("{} é um número perfeito".format(N))
    else:
        print("{} é um número deficiente".format(N))

divisores()