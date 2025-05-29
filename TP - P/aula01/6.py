segundos=int(input("Digite o tempo em segundos: "))
h = segundos//3600
h_t = segundos%3600
m = h_t//60
s = h_t%60

print("{:02d}:{:02d}:{:02d}".format(h, m, s))