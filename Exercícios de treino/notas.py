notas_alunos = {
    "João": {"Matemática": 8, "História": 7},
    "Mariana": {"Matemática": 9, "História": 10},
    "Lucas": {"Matemática": 6, "História": 5}
}

#Exibir as notas de um aluno especifico 
def notas(notas_alunos):
    nome = input("Enter the name: ")
    if nome in notas_alunos:
        notas = notas_alunos[nome]
    else:
        print("Aluno não existente")
    return notas

#Adicionar uma nova matéria e notas para um aluno
def nova_matéria(notas_alunos):
    nome = input("Enter the name: ")
    matéria = input("Enter the class: ")
    nota = int(input("Enter the mark: "))
    if nome in notas_alunos:
        info = notas_alunos[nome]
        info[matéria] = nota
        return notas_alunos
    else:
        print("Aluno não existente")

print(nova_matéria(notas_alunos))

