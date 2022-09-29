import random

turn = ' '
player = True
matrix = [ [" " , " " , " "], [" ", " ", " "], [" ", " ", " "] ]

start = 0
if start == 0:
	print("You will play first.")
else:
	print("I will play first.")
print("O for computer, X for you.")

def hard():
	print("+---+---+---+")
	print("+",matrix[0][0],"+",matrix[0][1],"+",matrix[0][2],"+")
	print("+---+---+---+")
	print("+",matrix[1][0],"+",matrix[1][1],"+",matrix[1][2],"+")
	print("+---+---+---+")
	print("+",matrix[2][0],"+",matrix[2][1],"+",matrix[2][2],"+")
	print("+---+---+---+")
			
hard()
print("\n\n")

while player: #user turn
		if start == 0:
			x,y = input("Enter a board position (row#:0..2, col#:0..2): ").split(" ",1)
			
			x = int(x)
			y = int(y)
		
			if x>2 or x<0:
				print("You entered a wrong position. Try again!")
			elif y>2 or y<0:
				print("You entered a wrong position. Try again!")
			elif matrix[x][y] == "X" or matrix[x][y] == "O":
				print("You entered a wrong position. Try again!")
			
				hard()
				print('\n')
				continue
			if matrix[x][y] == " ":
				matrix[x][y] = "X"
			start = 1
			
			hard()
			print("\n")
		
		if matrix[0][0] != " " and matrix[0][1] != " " and matrix[0][2] != " " and matrix[1][0] != " " and matrix[1][1] != " " and matrix[1][2] != " " and matrix[2][0] != " " and matrix[2][1] != " " and matrix[2][2] != " ":
			hard()
			print("Draw. Try again.")
			player = False
			break
		for i in range(0,3):
			if matrix[i][0] == matrix[i][1] == matrix[i][2] == "X":
				hard()
				print("Congratulation. You win.")
				player = False
				break
			elif matrix[i][0] == matrix[i][1] == matrix[i][2] == "O":
				hard()
				print("I win. Try again.")
				player = False
				break
		for i in range(0,3):
			if matrix[0][i] == matrix[1][i] == matrix[2][i] == "X":
				hard()
				print("Congratulation. You win.")
				player = False
				break
			elif matrix[0][i] == matrix[1][i] == matrix[2][i] == "O":
				hard()
				print("I win. Try again.")
				player = False
				break
		if (matrix[0][0] == matrix[1][1] == matrix[2][2]) or (matrix[0][2] == matrix[1][1] == matrix[2][0]): 
			if matrix[1][1] == "X":
				hard()
				print("Congratulation. You win.")
				player = False
				break
			elif matrix[1][1] == "O":
				hard()
				print("I win. Try again.")
				player = False
				break
			

#가로 수비 
		if matrix[0][0] == "X" and matrix[0][1] == "X" and matrix[0][2] == " ":
			matrix[0][2] = "O"
		
		elif matrix[1][0] == "X" and matrix[1][1] == "X" and matrix[1][2] == " ":
			matrix[1][2] = "O"
		
		elif matrix[2][0] == "X" and matrix[2][1] == "X" and matrix[2][2] == " ":
			matrix[2][2] = "O"
		
		elif matrix[0][2] == "X" and matrix[0][1] == "X" and matrix[0][0] == " ":
			matrix[0][0] = "O"
		
		elif matrix[1][2] == "X" and matrix[1][1] == "X" and matrix[1][0] == " ":
			matrix[1][0] = "O"
		
		elif matrix[2][2] == "X" and matrix[2][1] == "X" and matrix[2][0] == " ":
			matrix[2][0] = "O"
		
		elif matrix[0][0] == "X" and matrix[0][2] == "X" and matrix[0][1] == " ":
			matrix[0][1] = "O"
		
		elif matrix[1][0] == "X" and matrix[1][2] == "X" and matrix[1][1] == " ":
			matrix[1][1] = "O"
		
		elif matrix[2][0] == "X" and matrix[2][2] == "X" and matrix[2][1] == " ":
			matrix[2][1] = "O"
		
	
#세로 수비 
		elif matrix[0][0] == "X" and matrix[1][0] == "X" and matrix[2][0] == " ":
			matrix[2][0] = "O"
		
		elif matrix[0][1] == "X" and matrix[1][1] == "X" and matrix[2][1] == " ":
			matrix[2][1] = "O"
		
		elif matrix[0][2] == "X" and matrix[1][2] == "X" and matrix[2][2] == " ":
			matrix[2][2] = "O"
		
		elif matrix[2][0] == "X" and matrix[1][0] == "X" and matrix[0][0] == " ":
			matrix[0][0] = "O"
	
		elif matrix[2][1] == "X" and matrix[1][1] == "X" and matrix[0][1] == " ":
			matrix[0][1] = "O"
	
		elif matrix[2][2] == "X" and matrix[1][2] == "X" and matrix[0][2] == " ":
			matrix[0][2] = "O"
		
		elif matrix[0][0] == "X" and matrix[2][0] == "X" and matrix[1][0] == " ":
			matrix[1][0] = "O"
		
		elif matrix[0][1] == "X" and matrix[2][1] == "X" and matrix[1][1] == " ":
			matrix[1][1] = "O"
	
		elif matrix[0][2] == "X" and matrix[2][2] == "X" and matrix[1][2] == " ":
			matrix[1][2] = "O"
		
#대각 수비
		elif matrix[0][0] == "X" and matrix[1][1] == "X" and matrix[2][2] == " ":
			matrix[2][2] = "O"
		
		elif matrix[2][2] == "X" and matrix[1][1] == "X" and matrix[0][0] == " ":
			matrix[0][0] = "O"
		
		elif matrix[0][2] == "X" and matrix[1][1] == "X" and matrix[2][0] == " ":
			matrix[2][0] = "O"
		
		elif matrix[2][0] == "X" and matrix[1][1] == "X" and matrix[0][2] == " ":
			matrix[0][2] = "O"
	
		elif matrix[0][0] == "X" and matrix[2][2] == "X" and matrix[1][1] == " ":
			matrix[1][1] = "O"
		
		elif matrix[0][2] == "X" and matrix[2][0] == "X" and matrix[1][1] == " ":
			matrix[1][1] = "O"
		
		
		elif matrix[x][y] == " ":
			matrix[x][y] = "O"
	
		else:
			while True:
				x = random.randrange(0,3)
				y = random.randrange(0,3)
				if matrix[x][y] == "O" or matrix[x][y] == "X":
					continue
				elif matrix[x][y] == " ":
					matrix[x][y] = "O"
					break
	
		start = 0
		hard()
		print("\n")