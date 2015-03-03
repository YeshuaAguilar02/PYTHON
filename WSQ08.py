def add ( x, y):
	z = x + y
	print( "The sum between", x, "and", y, "is:", z)
def diff ( x, y):
	w = x - y
	print( "The difference between", x, "and", y, "is:", w)
def prd (x, y):
	t = x * y
	print( "The product between", x, "and", y, "is:", t)
def div ( x, y):
	u = int(x / y)
	print( "The division between", x, "and", y, "is:", u)
def rmd ( x, y):
	r = x % y
	print( "The remainder between", x, "and", y, "is:", r)

x = int( input("Put a number:"))
y = int( input("Put another number:"))

add ( x, y)
diff ( x, y)
prd ( x, y)
div ( x, y)
rmd ( x, y)
