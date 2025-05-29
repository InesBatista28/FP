ctp = float(input("CTP? "))
cp = float(input("CP? "))

nf = 30% ctp + 70% cp

if ctp>=6.5 and cp>=6.5:
 nf = 30/100 * ctp + 70/100 * cp
 nf=round(nf,1)
 print("A nota final é ",nf)

elif nf < 10.0:
    print("O aluno reprova por nota mínima")
    atpr = float(input("ATPR? "))
    apr = float(input("APR? "))

    coiso=max(ctp,atpr)
    coisa=max(cp,apr)

    nr = 30/100 * coiso + 70/100 * coisa
    nr = round(nr,1)
    print("A nota de recurso é ",nr) 

else:
 atpr = float(input("ATPR? "))
 apr = float(input("APR? "))

nr = 30/100 * max(ctp, atpr) + 70/100 * max(cp, apr)
nr = round(nr,1)
print("A nota de recurso é ",nr)