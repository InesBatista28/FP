funcionarios = {
    "TI": {"Carlos": 5000, "Ana": 5500, "Lucas": 4800},
    "RH": {"Mariana": 4200, "Pedro": 4300, "João": 4100},
    "Financeiro": {"Fernanda": 6000, "Gabriel": 6500, "Paula": 6200}
}

#Calcular o salário médio de um departamento
# Encontrar o funcionário com o maior salário da empresa

def medio_departamento(funcionarios):
    for departamento, info in funcionarios.items():
        sum = 0
        trabalhadores = 0
        for trabalhador, salario in info.items():
            sum += salario
            trabalhadores += 1
        salario_medio = sum / trabalhadores
        salario_medio_r = round(salario_medio, 2)
        print("Salário médio do {}: {}".format(departamento, salario_medio_r))

medio_departamento(funcionarios)


def maior_salário(funcionarios):
    lst = []
    for departamento, info in funcionarios.items():
        for trabalhador, salario in info.items():
            lst.append((trabalhador, salario))
    melhor_trabalhador, maior_salario = max(lst,key= lambda x : x[1])
    print("O trabalhador com o maior salário é {} ({})".format(melhor_trabalhador, maior_salario))

maior_salário(funcionarios)

