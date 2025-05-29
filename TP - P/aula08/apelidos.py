with open("names.txt", "r") as file:
    dict = {}
    for linha in file:
        nomes = linha.split()
        apelido = nomes[-1]
        pnome = nomes[0]
        if apelido not in dict:
            dict[apelido] = set()
        dict[apelido].add(pnome)

for apelido, nomes in dict.items():
    print(f"{apelido} : {nomes}")