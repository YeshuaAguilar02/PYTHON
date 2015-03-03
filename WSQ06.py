import random
x = int( input("Put a number between 1 and 100:"))
y = random.randint( 0, 100)
tries = 0
lives = 10
while (x != y and lives > 0):
	if x > y:
		tries = tries + 1
		lives = lives - 1
		print ("Too high.", x, "is not the right number")
		print ("Number of lives remaining:", lives)
	elif x < y:
		tries = tries + 1
		lives = lives - 1
		print ("Too low.", x, "is not the right number")
		print ("Number of lives remaining:", lives)
	if( lives > 0):
		x = int( input("Try again:"))

if lives == 0:
	print ("You've ran out of lives! Lives:", lives)
	print ("The right number was", y)
	print ("GAME OVER")
else:
	print ("You made it. You guessed the right number. It was", y)
	print ("Number of tries taken:", tries)
	print ("Number of lives remaining:", lives)
	print ("GAME OVER")
