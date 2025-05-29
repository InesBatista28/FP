def inputFloatList():
    lst = []
    N = input("Enter a random number: ")
    while N != "":
        N = int(N)
        lst.append(N)
        N = input("Enter a random number: ")
    print(lst)
    return lst 

def countLower(lst, v):
    lst_inferiores = []
    v = int(v)
    for i in lst:
        if i < v:
            lst_inferiores.append(i)
    print("O número de elementos inferiores a", v, "é", len(lst_inferiores))

def minmax(lst):
    minimo = lst[0]
    for i in range(len(lst)):
        if lst[0] > lst[i]:
            minimo = lst[i]
    maximo = lst[0]
    for i in range(len(lst)):
        if lst[0] < lst[i]:
            maximo = lst[i]
    print("O mínimo da lista é {} e o é máximo {}".format(minimo, maximo))
    media = (minimo + maximo) / 2
    total = 0
    for i in range(len(lst)):
        if lst[i] < media:
            total += 1
    print("O número de elementos inferiores à média {} é {}".format(media, total))
    return minimo, maximo, total



def main():
    v = input("Enter V: ")
    lst = inputFloatList()
    countLower(lst, v)
    minmax(lst)

main()