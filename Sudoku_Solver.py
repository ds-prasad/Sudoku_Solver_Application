"""
Created by Prasad DS
Updated on 27th September 2019
Python, Backtracking Algorithm
"""



def board_generator(board1):
	"""A function that takes a list of 9 lists, 
	each being a list of 9 numbers and 
	prints the elements of the lists 
	similar to sudoku board"""

	row_length=len(board1)
	column_length=len(board1[0])

	for r in range(row_length):
		if r!=0 and r%3==0 :
			print("----------------------")				#Print horizonal rows
		
		for c in range(column_length):
			if c!=0 and c%3==0:
				print("|",end=" ")						#Print vertical columns

			if c==8:
				print(board1[r][c])						#Print sudoku numbers
			else:
				print(board1[r][c],end=" ")



def find_empty_square(board1):
	"""Function to find an empty entry in squares of 
	the board and return the address of the empty square.
	Such empty squares are denoted by number zero[0] for 
	reference purpose of the program"""

	row_length=len(board1)
	column_length=len(board1[0])

	for r in range(row_length):
		for c in range(column_length):
			if board1[r][c]==0:
				return (r,c)							#Returns address of the empty square in form of tuple

	return None											#If no empty squares are found on sudoku board



def validate_newly_filled_square(board1,test_num,position_tuple):
	"""Function to check if the number newly inserted at certain square
	on sudoku board is valid or not by checking row-wise,column-wise,
	and small sudoku square of size 3x3 where the square is located"""

	row_length=len(board1)
	column_length=len(board1[0])

	r1=position_tuple[0]
	c1=position_tuple[1]

	for c in range(column_length):						#Checking row for repetitive numbers
		if board1[r1][c]==test_num and c1!=c:			#To skip position of newly inserted number
			return False

	for r in range(row_length):							#Checking column for repetitive numbers
		if board1[r][c1]==test_num and r1!=r:			#To skip position of newly inserted number
			return False

	"""To check the small sudoku square of size 3x3 where the square
	is located. First, extract starting edges of square row-wise and
	column-wise. Then, begin searching within the 3x3 sized square"""

	small_square_row=r1//3
	small_square_row*=3									#Extract the starting row of the small square
	small_square_column=c1//3
	small_square_column*=3								#Extract the starting column of the small square

	for r in range(small_square_row,small_square_row+3):
		for c in range(small_square_column,small_square_column+3):
			if board1[r][c]==test_num and (r,c)!=(r1,c1):					#Checking every number inside the small sudoku square of size 3x3 where the square is located
				return False												#of size 3x3 where the square is located for repetitive numbers

	return True



def sudoku_solver(board1):
	"""Function implemented using backtracking algorithm.
	Intially a base case scenario where whole board is solved.
	Then grabbing location of empty squares and trying to fit
	a valid number and moving to next empty square by calling 
	sudoku_solver function, which in turn calls another function
	that returns location of next empty square. "return False"
	statement to backtrack and reset previous square entry to zero"""

	empty_square=find_empty_square(board1)
	if not empty_square:								#Base case scenario where whole board is solved
		return True										#No empty squares are present

	else:
		r=empty_square[0]								#Extracting address of empty square(if it exists)
		c=empty_square[1]


	for num in range(1,10):									#Trying to fill a number to the empty square found
		if validate_newly_filled_square(board1,num,(r,c)):	#Checking if the number entry in empty square is valid or not
			board1[r][c]=num 								#If found valid, setting the number to the empty square

			if sudoku_solver(board1):					#Recursively call sudoku_solver function to find next empty square
				return True								#and attempt to solve it. Return true if no more squares are empty.

			board1[r][c]=0								#Helps reset previous square entry to zero using backtracking

	return False										#Return False if no number fits validly in the empty square

	"""If the above statement returns false, basically sudoku_solver(board1)
	returns false. Then lines 110-111 would be skipped. The previous square
	entry would be reset to zero and whole process repeats again"""



#Board object
test_board=[
				[5,3,0,0,7,0,0,0,0],
				[6,0,0,1,9,5,0,0,0],
				[0,9,8,0,0,0,0,6,0],
				[8,0,0,0,6,0,0,0,3],
				[4,0,0,8,0,3,0,0,1],
				[7,0,0,0,2,0,0,0,6],
				[0,6,0,0,0,0,2,8,0],
				[0,0,0,4,1,9,0,0,5],
				[0,0,0,0,8,0,0,7,9]
           ]



#Calling the functions to generate and print sudoku board and later solve it
print("Sudoku before solving:")
board_generator(test_board)
sudoku_solver(test_board)
print("\nSudoku after solving:")
board_generator(test_board)


"""Testing validate_newly_filled_square Function
print(validate_newly_filled_square(test_board,4,(2,8)))
print(validate_newly_filled_square(test_board,8,(3,3)))
print(validate_newly_filled_square(test_board,5,(7,2)))
print(validate_newly_filled_square(test_board,7,(6,5)))
print(validate_newly_filled_square(test_board,2,(8,3)))
True	False	False	True	True"""