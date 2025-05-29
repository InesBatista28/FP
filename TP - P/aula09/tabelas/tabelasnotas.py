def printReport(alunos):
    print("Tabela de Notas")
    print(f"{'Nome':<15} {'Matemática':<15} {'Físca':<10} {'Química':<12} {'Média':<10} {'Situação':<10}")
    students_sorted = sorted(alunos, key=lambda x: (x[1] + x[2] + x[3]) / 3, reverse=True)
    for i in students_sorted:
        nome, matemática, física, química = i
        média = (matemática + física + química) / 3
        if média >= 60:
            situação = "Aprovado"
        else:
            situação = "Reprovado"
        print(f"{nome:<15} {matemática:<15.1f} {física:<10.1f} {química:<12.1f} {média:<10.1f} {situação:<10}")

def main():
    alunos = [
        ("João", 78.0, 81.5, 79.0),
        ("Maria", 85.5, 92.0, 88.5),
        ("Ana", 45.5, 50.0, 52.0),
        ("Carlos", 60.0, 62.5, 61.0)
    ]
    printReport(alunos)
main()