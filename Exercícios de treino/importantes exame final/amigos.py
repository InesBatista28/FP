dict = {}

def read_file(filename, dict):
    """Lê o ficheiro e extrai as pessoas e seus amigos para uma estrutura de dados adequada."""
    with open (filename, "r") as file:
        for line in file:
            line = line.strip()
            nomes = line.split(",")
            principal = nomes[0]
            amigos = nomes[1:]
            dict[principal] = amigos
    return dict

def add_friends(person):
    """Recebe um nome e pede amigos ao usuário, adicionando-os à pessoa."""
    n_amigos = []
    novos_amigos = input("Enter the new friends: ")
    while novos_amigos != "":
        n_amigos.append(novos_amigos)
        novos_amigos = input("Enter the new friends: ")
    if person in dict.keys():
        dict[person].extend(n_amigos)
    else:
        dict[person] = n_amigos
    return dict 

def remove_friend(person, friend):
    """Remove um amigo de uma pessoa."""
    if person in dict:
        if friend in dict[person]:
            dict[person].remove(friend)
    return dict

def count_friends():
    """Imprime quantos amigos cada pessoa tem."""
    for person in dict.keys():
        sum = 0
        for i in dict[person]:
            sum += 1
        print("A pessoa {} tem {} amigos".format(person, sum))

def count_reverse_friends(person):
    """Conta quantas pessoas têm a dada pessoa como amiga."""
    sum = 0
    for i in dict.keys():
        if person in dict[i]:
            sum += 1
    print("{} pessoas tem {} como amigo".format(sum, person))

def mutual_friends(person1, person2):
    """Retorna os amigos em comum entre duas pessoas."""
    lst = []
    for i in dict[person1]:
        for j in dict[person2]:
            if i == j:
                lst.append(i)
    print("Os amigos em comum entre {} e {} são {}".format(person1, person2, lst))

def most_popular_person():
    """Determina a pessoa com mais amigos na rede."""
    amigo = ""
    max = 0
    for pessoa in dict.keys():
        if len(dict[pessoa]) > 0:
            max = len(dict[pessoa])
            amigo = pessoa
    return amigo 




def main():
    # Chamadas de função e expected outputs (se aplicável)
    read_file("amigos.txt", dict)
    print(add_friends("Hugo"))  # Esperado: usuário insere amigos para Hugo
    remove_friend("Maria", "Joao")  # Esperado: João removido dos amigos de Maria
    count_friends()  # Esperado: imprime quantidade de amigos de cada um
    count_reverse_friends("Tiago")  # Esperado: imprime quantas pessoas têm Tiago como amigo
    mutual_friends("Hugo", "Maria")  # Esperado: retorna amigos em comum entre Hugo e Maria
    most_popular_person()  # Esperado: imprime a pessoa com mais amigos


if __name__ == "__main__":
    main()