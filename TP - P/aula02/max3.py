x1 = float(input("number 1? "))
x2 = float(input("number 2? "))
x3 = float(input("number 3? "))
x4 = float(input("number 4? "))

if x1>x2:
    if x1>x3:
        if x1>x4:
            mx = x1
        else:
            mx = x4
    else:
        if x3>x4:
            mx = x3
        else:
            mx = x4
else:
    if x2>x3:
        if x2>x4:
            mx = x2
        else:
            mx = x4
    else:
        if x3>x4:
            mx = x3
        else:
            mx = x4
        
print("Maximum:", mx)