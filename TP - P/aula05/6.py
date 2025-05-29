def abreviação():
    x = input('Digite um nome completo: ')
    x = x.split()
    abre = ""
    for i in x:
        if i[0].isupper():
            abre += i[0]
    print(abre)

abreviação()