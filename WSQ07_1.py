x = int( input("Introduce a lower number:"))
y = int( input("Introduce a higher number:"))
z = 0
for w in range( x, y + 1):
	z = z + w
print ("The sum of numbers from", x, "to", y, "is:", z)
