alunos = {
    "João": {"Matemática": [8, 7, 9], "História": [7, 6, 8], "Ciências": [9, 8, 7]},
    "Mariana": {"Matemática": [9, 10, 10], "História": [10, 9, 10], "Ciências": [10, 9, 9]},
    "Lucas": {"Matemática": [6, 5, 7], "História": [6, 5, 6], "Ciências": [7, 6, 6]}
}

# Calcular a média de um aluno em todas as matérias
#Média de João: 7.67
#Encontrar o aluno com maior média geral 
#Aluno com maior média: Mariana (9.56) 
def medias(alunos):
    lst = []
    for aluno, classes in alunos.items():
        soma = 0
        numero = 0
        for materia, notas in classes.items():
            for i in notas:
                soma += i
                numero += 1
        media = soma / numero 
        media_nova = round(media, 2)
        lst.append((aluno, media_nova))
        print("Média de {}: {}".format(aluno, media_nova))
    m_aluno, m_media = max(lst, key= lambda x : x[1])
    print("Aluno com maior média: {} ({})".format(m_aluno, m_media))

medias(alunos)







