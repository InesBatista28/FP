def ler_ficheiro(nome_ficheiro):
    lista_clubes = []
    with open(nome_ficheiro, 'r', encoding='utf-8') as ficheiro:
        linhas = ficheiro.readlines()
        for linha in linhas[1:]:  # Ignorar o cabeçalho
            dados = linha.strip().split(',')
            lista_clubes.append(tuple(dados))
    return lista_clubes

def imprimir_clubes_pais(lista_clubes, pais):
    for clube in lista_clubes:
        if clube[2] == pais:
            print(f"Clube: {clube[1]}, Ranking: {clube[0]}, Score Atual: {clube[3]}")

def escrever_clubes_pais(lista_clubes, pais, nome_ficheiro_output):
    with open(nome_ficheiro_output, mode='w', encoding='utf-8') as ficheiro:
        for clube in lista_clubes:
            if clube[2] == pais:
                ficheiro.write(f"Clube: {clube[1]}, Ranking: {clube[0]}, Score Atual: {clube[3]}\n")

def criar_dicionario_paises(lista_clubes):
    dicionario = {}
    for clube in lista_clubes:
        pais = clube[2]
        if pais not in dicionario:
            dicionario[pais] = []
        dicionario[pais].append(clube[1])
    return dicionario

def clube_que_mais_subiu(lista_clubes):
    clube_mais_subiu = None
    maior_subida = -float('inf')
    for clube in lista_clubes:
        subida = int(clube[4])
        if subida > maior_subida:
            maior_subida = subida
            clube_mais_subiu = clube
    return clube_mais_subiu

def procurar_clube(lista_clubes, nome_clube):
    for clube in lista_clubes:
        if clube[1] == nome_clube:
            print(f"Clube: {clube[1]}, País: {clube[2]}, Score Atual: {clube[3]}, Subida/Descida: {clube[4]}")
            return
    print("Clube não encontrado.")

def ranking_medio_paises(lista_clubes):
    rankings = {}
    for clube in lista_clubes:
        pais = clube[2]
        ranking = int(clube[0])
        if pais not in rankings:
            rankings[pais] = {'soma': 0, 'quantidade': 0}
        rankings[pais]['soma'] += ranking
        rankings[pais]['quantidade'] += 1
    for pais, dados in rankings.items():
        media = dados['soma'] / dados['quantidade']
        print(f"País: {pais}, Ranking Médio: {media:.2f}")

def ranking_medio_ordenado(lista_clubes):
    rankings = {}
    for clube in lista_clubes:
        pais = clube[2]
        ranking = int(clube[0])
        if pais not in rankings:
            rankings[pais] = {'soma': 0, 'quantidade': 0}
        rankings[pais]['soma'] += ranking
        rankings[pais]['quantidade'] += 1
    # Calcular médias
    medias = {pais: dados['soma'] / dados['quantidade'] for pais, dados in rankings.items()}
    # Ordenar por ranking médio
    for pais, media in sorted(medias.items(), key=lambda x: x[1]):
        print(f"País: {pais}, Ranking Médio: {media:.2f}")

def menu():
    lista_clubes = []
    while True:
        print("\n--- Menu ---")
        print("1. Ler ficheiro")
        print("2. Imprimir clubes de um país")
        print("3. Escrever clubes de um país num ficheiro")
        print("4. Criar dicionário de países e clubes")
        print("5. Encontrar clube que mais subiu no ranking")
        print("6. Procurar clube pelo nome")
        print("7. Calcular ranking médio por país")
        print("8. Imprimir países por ranking médio ordenado")
        print("0. Sair")
        opcao = input("Escolha uma opção: ")
        if opcao == '1':
            nome_ficheiro = input("Introduza o nome do ficheiro: ")
            lista_clubes = ler_ficheiro(nome_ficheiro)
        elif opcao == '2':
            pais = input("Introduza o nome do país: ")
            imprimir_clubes_pais(lista_clubes, pais)
        elif opcao == '3':
            pais = input("Introduza o nome do país: ")
            nome_ficheiro_output = input("Introduza o nome do ficheiro de output: ")
            escrever_clubes_pais(lista_clubes, pais, nome_ficheiro_output)
        elif opcao == '4':
            dicionario = criar_dicionario_paises(lista_clubes)
            for pais, clubes in dicionario.items():
                print(f"{pais}: {', '.join(clubes)}")
        elif opcao == '5':
            clube = clube_que_mais_subiu(lista_clubes)
            print(f"Clube que mais subiu: {clube[1]}, Subida: {clube[4]}")
        elif opcao == '6':
            nome_clube = input("Introduza o nome do clube: ")
            procurar_clube(lista_clubes, nome_clube)
        elif opcao == '7':
            ranking_medio_paises(lista_clubes)
        elif opcao == '8':
            ranking_medio_ordenado(lista_clubes)
        elif opcao == '0':
            break
        else:
            print("Opção inválida. Tente novamente.")