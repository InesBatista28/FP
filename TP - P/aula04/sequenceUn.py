print("n", "Un")
Un=100 
a=0                   # Un = each term of the sequence. Initially = U0
while Un>0:
   print(Un)
   Un = 1.01*Un + 100
   a += 1

print("The number of terms is", a)  