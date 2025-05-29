A = int(input("Quantos andares tem o prédio? "))
M = int(input("Quantos moradores tem um andar? "))

metros_dia = 0
while A>0:
    metros_dia += 3*2*M*A #altura do andar * 2=sobre e desce * número de moradores * número de andares 
    A -= 1

metros_ano = metros_dia * 365
km_ano = metros_ano / 1000
print("O elevador percorre {} metros por dia e {} km por ano".format(metros_dia, km_ano))

#v = d / t
segundos_ano = metros_ano / 1
horas_ano = segundos_ano / 3600
print("O elevador demora {} horas por ano a percorrer a distância".format(horas_ano))