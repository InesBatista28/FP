print("Kryptonite phase classifier")

T = float(input("Temperature (K)? "))
P = float(input("Pressure (kPa)? "))

# Determine the phase. (This is wrong. Fix to match the phase diagram.)
if P > 50.0 and T<400.0:
    phase = "SOLID"
elif T > 400.0 and P>50.0:
    phase = "LIQUID"
elif T<400.0 and P<50.0 and P>T/8:
    phase= "SOLID"
else:
    phase = "GAS"
T=round(T,1)
P=round(P,3)

print("At {} K and {} kPa, Kryptonite is in the {} phase.".format(T, P, phase))