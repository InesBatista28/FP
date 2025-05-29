x1 = float(input("x1? "))
y1 = float(input("y1? "))
x2 = float(input("x2? "))
y2 = float(input("y2? "))

d = ((x2 - x1)**2 + (y2 - y1)**2)**(1/2)

print("Ponto 1: ({}, {})".format(x1, y1))
print("Ponto 2: ({}, {})".format(x2, y2))
print("Distância entre os pontos é {:.2f}".format(d))