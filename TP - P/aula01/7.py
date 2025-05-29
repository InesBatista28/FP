import math 

A = float(input("Digite o valor do cateto A: "))
B = float(input("Digite o valor do cateto B: "))

hipotenusa = math.sqrt(A**2 + B**2)
angulo = math.sin(A/hipotenusa)
ang = (180 * angulo ) / math.pi

print(f"A hipotenusa é {hipotenusa:.2f} e o ângulo entre a mesma e o cateto A é {ang:.2f}")