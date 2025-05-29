#calcular a média de cada aluno cadastrado 

alunos = [
    {"nome": "Carlos", "notas": [8, 7, 6]},
    {"nome": "Luiza", "notas": [9, 9, 10]},
    {"nome": "Pedro", "notas": [5, 6, 5]},
]

for i in alunos:
    notas = 0
    for j in i["notas"]:
        notas += j
    media = notas / 3
    media_arrendondada = round(media, 2)
    print("A média de notas de ", i["nome"], "é", media_arrendondada)