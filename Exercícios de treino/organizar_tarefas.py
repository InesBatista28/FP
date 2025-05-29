#retornar um dicionário com 3 listas, cada uma com as tarefas de prioridade diferente

tarefas = [
    {"descricao": "Comprar pão", "prioridade": "baixa"},
    {"descricao": "Estudar Python", "prioridade": "alta"},
    {"descricao": "Limpar a casa", "prioridade": "média"},
    {"descricao": "Fazer exercícios", "prioridade": "alta"}
]
 
def prioridade(tarefas):
    prioridades = {'alta':[], 'média':[], 'baixa':[]}
    for i in tarefas:
        prioridade = i["prioridade"]
        descrição = i["descricao"]
        prioridades[prioridade].append(descrição)
    return prioridades

print(prioridade(tarefas))
