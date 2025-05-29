x1 = float(input("number? "))
x2 = float(input("number? "))

# Use a conditional statement instead of max function!
#mx = max(x1, x2)
if x1>x2:
    mx = x1
else:
    mx = x2

print("Maximum:", mx)

