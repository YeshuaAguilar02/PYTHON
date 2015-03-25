# Yeshua Joel Aguilar Jiménez
# A00569141

def T(n):
	for x in range(1, n + 1, +1):
		print ("T" * x)
		
	for z in range(n - 1, 0, -1):
		print ("T" * z)

n = int( input("Put a value:"))
T(n)
