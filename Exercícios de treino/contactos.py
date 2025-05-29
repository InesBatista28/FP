contatos = {
    "Carlos": {"telefone": "91234-5678", "email": "carlos@email.com"},
    "Ana": {"telefone": "92345-6789", "email": "ana@email.com"},
    "Pedro": {"telefone": "93456-7890", "email": "pedro@email.com"}
}


def procurar_contacto(contatos):   #com o nome do contacto, devolver o número do mesmo
    nome = input("Enter the name: ")
    if nome in contatos:
        info = contatos[nome]
        telefone = info["telefone"]
        return telefone
    else:
        return False
    
def adicionar_coontactos(contatos):
    nome = input("Enter the name: ")
    telefone = input("Enter the phone number: ")
    email = input("Enter the mail: ")
    info = {}
    info["telefone"] = telefone
    info["email"] = email
    contatos[nome] = info
    return contatos

print(adicionar_coontactos(contatos))
    