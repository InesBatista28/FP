# Complete este programa como pedido no guião da aula.

def listContacts(dic):
    print("{:>12s} : {}".format("Numero", "Nome"))
    for num in dic:
        print("{:>12s} : {}".format(num, dic[num]))

def filterPartName(contactos, partName):
    search = {}
    for (number, name) in contactos:
        if partName in name[0]:
            search[number] = name
    return search

def menu():
    print()
    print("(L)istar contactos")
    print("(A)dicionar contacto")
    print("(R)emover contacto")
    print("Procurar (N)úmero")
    print("Procurar (P)arte do nome")
    print("(T)erminar")
    op = input("opção? ").upper()  
    return op

def main():
    contactos = {"234370200": "Universidade de Aveiro",
        "727392822": "Cristiano Aveiro",
        "387719992": "Maria Matos",
        "887555987": "Marta Maia",
        "876111333": "Carlos Martins",
        "433162999": "Ana Bacalhau"
        }

    op = ""
    while op != "T":
        op = menu()
        if op == "T":
            print("Fim")
        elif op == "L":
            print("Contactos:")
            listContacts(contactos)
        elif op == "A":
            number = int(input("Enter a number:"))
            name = input("Enter a name:")
            contactos[number] = name
        elif op == "R":
            number = int(input("Enter a number:"))
            del contactos[number]
        elif op == "N":
            number = int(input("Enter a number:"))
            if number in contactos:
                print("Contacto:", contactos[number])
            else:
                print("Contacto não existe!", number)
        elif op == "P":
            partName = input("Enter a part of the name:")
            filterPartName(contactos, partName)
        else:
            print("Não implementado!")
    

main()

