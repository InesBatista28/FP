
print("Índice de Massa Corporal")

altura = float(input("Altura (m)? "))
peso = float(input("Peso (kg)? "))

imc = peso / altura**2

print("IMC:", imc, "kg/m2")

if imc < 18.5:
    categoria = "Magro"
elif 18.5 <= imc < 25:
    categoria = "Saudável"
elif 25 <= imc < 30:
    categoria = "Forte"
else:
    categoria = "Obeso"
    
print("Categoria:", categoria)

