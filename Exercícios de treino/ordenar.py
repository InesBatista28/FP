#Dada uma lista de tuplas contendo (nome, nota), ordene os alunos pela nota em ordem decrescente usando lambda
def ordena_alunos(alunos):
    return sorted(alunos, key = lambda x : x[1], reverse = True)

alunos = [("Alice", 8.5), ("Bruno", 9.2), ("Carlos", 7.8)]
ordenados = ordena_alunos(alunos)
print(ordenados)
# Saída esperada: [('Bruno', 9.2), ('Alice', 8.5), ('Carlos', 7.8)]