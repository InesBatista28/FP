#0.12 por minuto 
#cobra ao segundo após primeiro minuto

duração = float(input("Digite a duração da chamada em segundos: "))
if duração < 60:
    print("O valor da chamada é de 0.12")
else:
    restante = duração - 60
    valor = 0.12 + (restante * 0.02)
    print("O valor da chamada é de", valor)