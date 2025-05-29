def lista_equipas():   #a)
    lst = []
    while True:
        equipa = input("Enter a team name: ")
        if equipa == "":
            break
        else:
            lst.append(equipa)
    print("Lista de todas as equipas: ", lst)
    return lst

def lista_jogos(lst):  #b)
    lst_jogos = []
    for i in lst:
        for j in lst:
            if i != j:
                lst_jogos.append((i, j))
    print("Lista de todos os jogos: ", lst_jogos)
    return lst_jogos

def resultados_jogos(lst_jogos):  #c)
    resultados = {}
    for i in lst_jogos:
        print("Jogo: ", i)
        team1, team2 = i
        r1 = int(input("Enter the result for {}: ".format(team1)))
        r2 = int(input("Enter the result for {}: ".format(team2)))
        resultados[i] = (r1, r2)
    print("Lista dos resultados obtidos nos jogos: ", resultados)
    return resultados 

def calculo_pontos_equipas(resultados):  # c) e d)
    pontos = {}
    for i in resultados.items():
        equipas, golos = i
        team1, team2 = equipas
        g1, g2 = golos

        if team1 not in pontos:
            pontos[team1] = [0, 0, 0, 0, 0, 0]   #[Vitórias, Empates, Derrotas, Marcados, Sofridos, Pontos]
        else:
            pontos[team1][3] += g1  #golos marcados
            pontos[team1][4] += g2  #golos sofridos (golos marcados pela equipa adversária)
        
        if team2 not in pontos:
            pontos[team2] = [0, 0, 0, 0, 0, 0]
        else:
            pontos[team2][3] += g2 
            pontos[team2][4] += g1 

        if g1 > g2:
            pontos[team1][0] += 1  # + 1 vitória
            pontos[team1][5] += 3  #cada vitória equivale a 3 pontos 
            pontos[team2][2] += 1  # + 1 derrota 
        elif g1 < g2:
            pontos[team2][0] += 1  
            pontos[team2][5] += 3  
            pontos[team1][2] += 1  
        else:
            pontos[team1][1] += 1  # + 1 empate
            pontos[team2][1] += 1  
            pontos[team1][5] += 1  #cada empate equivale a 1 ponto
            pontos[team2][5] += 1

    print("Tabela das clalificações: ")
    print(f"{'Equipa':<15} {'Vitórias':<10}{'Empates':<10}{'Derrotas':<10}{'Golos Marcados':<10}{'Golos Sofridos':<10}{'Pontos':<10}")
    for i in pontos.items():
        vit, emp, der, gm, gs, pts = i[1]
        print(f"{i[0]:<15}{vit:<10}{emp:<10}{der:<10}{gm:<10}{gs:<10}{pts:<10}")


equipas = lista_equipas()
jogos = lista_jogos(equipas)
resultados = resultados_jogos(jogos)
calculo_pontos_equipas(resultados)
    


