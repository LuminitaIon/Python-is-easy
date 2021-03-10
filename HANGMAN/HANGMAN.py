# second project
import random

# WORDS
dataGame = ['prajitura', 'trandafir', 'osteoporoza', 'analgezic']

temp = ''
board = []
parts = 0

def Board(word):
	out = []
	for letter in word:
		obj = {'char': letter, 'show': False}
		out.append(obj)
	return out

def guess(letter):
	global parts
	fail = True
	for i in board:
		if i['char'] == letter:
			i['show'] = True
			fail = False
	if fail:
		parts += 1

def checkWin(board):
	out = True
	for i in board:
		if i['show'] == False:
			out = False
	return out

def printMAN(parts):
	man = [' ', 'O', ' ', '\n', '/', '|', u'\u2216','\n', '/',' ', u'\u2216', '\n']
	out = ''
	r = 0

	if parts == 1:
		r = 3
	elif parts == 2:
		r = 5
	elif parts == 3:
		r = 6
	elif parts == 4:
		r = 7
	elif parts == 5:
		r = 8
	elif parts == 6:
		r = 10
	elif parts == 7:
		r = 11
	else:
		r = 0

	for i in range(r):
		out += man[i]

	print(out)

def printBOARD(board):
	out = ''
	for i in board:
		c = '_'
		if i['show']:
			c = i['char']
		c += ' '
		out += c
	print(out)

for i in range(len(dataGame)):
	print(i+1, dataGame[i])

while len(board) == 0:
	print("\n Player 1 select a word: ")
	temp = int(input('> '))
	if temp - 1 in range(len(dataGame)):
		board = Board(dataGame[temp-1])
		print(chr(27) + "[2J")
		break
	else:
		print("Not a valid selection.")

while True:
	printMAN(parts)
	printBOARD(board)
	print('\nPlayer 2 select a letter: ')
	letter = input('> ')
	print('\n')
	guess(letter)
	if checkWin(board):
		printBOARD(board)
		print('\nPlayer 2 wins.')
		break
	elif parts == 7:
		printMAN(parts)
		print('\nPlayer1 wins.')
		break
