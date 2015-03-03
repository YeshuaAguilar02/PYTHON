Fa = int( input("Put the ºF:"))
C = round( float( 5 * ( Fa-32 ) // 9))
print("The temperature of", Fa, "ºF in Celsius is", C, "ºC")

if C >= 100:
    print("Water at this temperature boils down.")
else:
    print("Water at this temperature doesn't boil down.")
