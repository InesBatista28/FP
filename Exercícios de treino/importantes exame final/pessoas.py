social_network = {}

def read_file(filename, social_network):
    """Lê o ficheiro e adiciona informações das pessoas à estrutura de dados."""
    with open(filename) as file:
        for line in file:
            line = line.strip()
            info = line.split(",")
            nome = info[0]
            idade = info[1]
            cidade = info[2]
            amigos = info[3:]
            social_network[nome] = {"idade":idade, "cidade":cidade, "amigos":amigos}
        return social_network
    
def add_person(name, age, city):
    """Adiciona uma nova pessoa à rede social."""
    if name not in social_network.keys():
        social_network[name] = {"idade":age, "cidade":city, "amigos":[]}  #adicionar amigos na próxima função
    return social_network

def add_friend(person, friend):
    """Adiciona um amigo a uma pessoa."""
    if person in social_network and friend in social_network:
        if friend not in social_network[person]["amigos"]:
            social_network[person]["amigos"].append(friend)
            social_network[friend]["amigos"].append(person)  #para serem amigos, ambos tem de ser seguir mutuamente (facebook, metodo muito antiquado :p)
    return social_network

def remove_friend(person, friend):
    """Remove um amigo de uma pessoa."""
    if person in social_network and friend in social_network[person]["amigos"]:
        social_network[person]["amigos"].remove(friend)
        social_network[friend]["amigos"].remove(person)
    return social_network

def most_popular_person():
    """Retorna a pessoa com mais amigos."""
    max_amigos  = 0
    popular = ""
    for person in social_network:
        if len(social_network[person]["amigos"])>max_amigos:
            max_amigos = len(social_network[person]["amigos"])
            popular = person
    return popular

def city_most_people():
    """Determina a cidade com mais pessoas na rede social."""
    cidades = {}
    for person in social_network:
        if social_network[person]["cidade"] not in cidades:
            cidades[social_network[person]["cidade"]] = 1
        else:
            cidades[social_network[person]["cidade"]] += 1
    return max(cidades, key = lambda x : cidades[x])

def main():
    read_file("pessoas.txt", social_network)
    print(add_person("Carlos", 30, "Lisboa"))  
    print(add_friend("Carlos", "Ana"))  
    print(remove_friend("Ana", "João"))  
    print(most_popular_person())
    print(city_most_people())

if __name__ == "__main__":
    main()