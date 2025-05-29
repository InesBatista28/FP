chamadas = []

def validar_numero(numero):
    if numero.startswith('+'):
        numero = numero[1:]
    return numero.isalpha() and len(numero) >= 3

def registar_chamada(numero):
    telefone_origem = input("Telefone origem? ")
    while not validar_numero(telefone_origem):
        telefone_origem = input("Telefone origem? ")
    telefone_destino = input("Telefone destino? ")
    while not validar_numero(telefone_destino):
        telefone_destino = input("Telefone destino? ")
    duração = int(input("Duração (s)?"))
    chamada = {"origem":telefone_origem, "destino":telefone_destino, "duração":duração}
    chamadas.append(chamada)

def ler_ficheiro(filename):
    with open(filename) as file:
        for line in file:
            line = line.split()
            origem = line[0]
            destino = line[1]
            duração = line[2]
            chamada = {"origem":origem, "destino":destino, "duração":duração}
            chamadas.append(chamada)

def listar_clientes():
    clientes = []
    for chamada in chamadas:
        origem = chamadas[chamada]["origem"]
        clientes.append(origem)
    for cliente in clientes:
        print(cliente)

def fatura():
    # Pede o número do cliente
    cliente = input("Cliente? ")
    
    # Filtra as chamadas feitas pelo cliente
    chamadas_cliente = [chamada for chamada in chamadas if chamada["origem"] == cliente]
    
    # Se não houver chamadas, exibe uma mensagem e retorna
    if not chamadas_cliente:
        print(f"O cliente {cliente} não fez nenhuma chamada.")
        return
    
    # Inicializa o custo total
    custo_total = 0
    
    # Exibe o cabeçalho da fatura
    print(f"\nFatura do cliente {cliente}")
    print("{:<20} {:<10} {:<10}".format("Destino", "Duração", "Custo"))
    
    # Processa cada chamada
    for chamada in chamadas_cliente:
        destino = chamada["destino"]
        duracao = chamada["duracao"]
        
        # Calcula o custo com base no destino
        if destino.startswith("+"):  # Chamadas internacionais
            custo = duracao * (0.80 / 60)  # 0.80€ por minuto = 0.0133€ por segundo
        elif destino.startswith("2"):  # Rede fixa
            custo = duracao * (0.02 / 60)  # 0.02€ por minuto = 0.00033€ por segundo
        elif destino[:2] == cliente[:2]:  # Mesma rede (2 primeiros dígitos iguais)
            custo = duracao * (0.04 / 60)  # 0.04€ por minuto = 0.00067€ por segundo
        else:  # Outros destinos
            custo = duracao * (0.10 / 60)  # 0.10€ por minuto = 0.00167€ por segundo
        
        # Arredonda o custo para 2 casas decimais
        custo = round(custo, 2)
        
        # Adiciona ao custo total
        custo_total += custo
        
        # Exibe os detalhes da chamada
        print("{:<20} {:<10} {:<10.2f}".format(destino, duracao, custo))
    
    # Exibe o custo total
    print(f"\nTotal: {custo_total:.1f}€")

# Função principal do programa
def main():
    while True:
        print("\nMenu:")
        print("1) Registar chamada")
        print("2) Ler ficheiro")
        print("3) Listar clientes")
        print("4) Fatura")
        print("5) Terminar")
        opcao = input("Opção? ")

        if opcao == "1":
            registar_chamada()
        elif opcao == "2":
            ler_ficheiro("chamadas1.txt")
        elif opcao == "3":
            listar_clientes()
        elif opcao == "4":
            fatura()
        elif opcao == "5":
            print("A terminar o programa...")
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()