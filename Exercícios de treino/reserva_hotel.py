reservas = {
    "Quarto 101": {"hóspede": "Carlos", "noites": 3},
    "Quarto 102": {"hóspede": "Ana", "noites": 7},
    "Quarto 103": {"hóspede": "Mariana", "noites": 5},
    "Quarto 104": {"hóspede": "Lucas", "noites": 2}
}

#Exibir as informações de determinado hóspede
#Hospéde no quarto 104: Mariana, 5 noites
def informações(reservas):
    for i in reservas.keys():
        info = reservas[i]
        nome = info["hóspede"]
        noites = info["noites"]
        print("Hospéde no quarto {}: {}, {} noites".format(i, nome, noites))

informações(reservas)

#Hóspede com mais noites: Ana (7 noites)
def mais_noites(reservas):
    quarto_mais_noites = max(reservas, key=lambda x: reservas[x]["noites"])  
    hospede = reservas[quarto_mais_noites]["hóspede"]
    noites = reservas[quarto_mais_noites]["noites"]
    print("Hóspede com mais noites: {} ({} noites)".format(hospede, noites))

mais_noites(reservas)
        