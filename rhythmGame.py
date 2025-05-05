import time
import random
import keyboard
import threading
import os
from termcolor import colored

score = 0
missed = 0

color = 'red'

#delay of notes
speed = float(0.5)

ownedColors = {"red"}
ownedColorsList = list(ownedColors)

# the 'gameboard'
chart = [
		 ["0","0","0","0"],
		 ["0","0","0","0"],
		 ["0","0","0","0"],
		 ["0","0","0","0"],
		 ["0","0","0","0"],
		 ["0","0","0","0"],
		 ["0","0","0","0"],
		 ["0","0","0","0"]
		]

shopItems = [
	["green", "green", "10,000", False],
	["blue", "blue", "16,000", False],
	["magenta", "magenta", "25,000", False],
	["yellow", "yellow", "50,000", False],
	#["rainbow", "white", "100,000", False]
]
#Global variable for note positions
notePositions = []

#Draws the game board on the screen
def drawBoard():
	#goes through each element in the list
	print("spam [q] to leave.")
	print("keys go for each row in order.. [s][d][j][k]\n")
	for row in range(len(chart)):
		for element in range(len(chart[row])):
			# prints final chart
			print(chart[row][element], end=" ")
		print(f"		Score: {score}")	
	

#In charge of spawning notes
def spawnNotes():
	#for now, picking random spots on the board
	col = random.randrange(0, 4)
	notePositions.append((0, col)) #start the note at the top and add the note to the list
	chart[0][col] = colored("1", f'{color}')
	drawBoard() #draw the board

#moves the notes down
def moveNotes():
	global notePositions
	
	for i in range(len(notePositions)):
		row, col = notePositions[i]

		if row + 1 < len(chart): # this makes sure you dont exceed the index range
			chart[row][col] = "0"

			notePositions[i] = (row + 1, col)

			chart[row + 1][col] = colored("1", f'{color}')
		else:
			removeNotes(row, col, i)
			break

def removeNotes(row, col, i):
	# If the note is at the bottem then remove it
	notePositions.pop(i)
	chart[row][col] = "0" # clear the note
	moveNotes()

#Handles the key pressing
def notePress():
	global notePositions
	#key s is assigned to row 1
	#key d is assigned to row 2
	#key j is assigned to row 3
	#key k is assigned to row 4

	if keyboard.is_pressed('s'):
		detectNote(0)
	if keyboard.is_pressed('d'):
		detectNote(1)
	if keyboard.is_pressed('j'):
		detectNote(2)
	if keyboard.is_pressed('k'):
		detectNote(3)

def detectNote(colNum):
	global score
	global missed
	for i in range(len(notePositions)):
		if i < len(notePositions):
			row, col = notePositions[i]

			if row >= 7 and col == colNum:
				#removeNotes(row, col, i)
				score += 10
				chart[row][col] = colored("1", 'green')
			else:
				missed += 1

def startNotePressDetection():
	while True:
		notePress()
		time.sleep(0.01)

def main():
	notePressThread = threading.Thread(target=startNotePressDetection)
	notePressThread.daemon = True
	notePressThread.start()

	while True:
		if keyboard.is_pressed('q'):
			print("Stopping program...")
			time.sleep(1)
			clearConsole()
			highscoreRoom()
			break

		spawnNotes()
		moveNotes()
		notePress()
		#pauses it for (speed) seconds
		time.sleep(speed)
		#Clears the console
		clearConsole()

# The rooms of the game

def highscoreRoom():
	global score
	global missed
	print(f"Your score was {colored(score, 'green')}")
	time.sleep(1)
	print(f"You missed a total of {colored(int(missed / 20), 'red')} times")
	time.sleep(1)
	print("do you want to [leave] or play [again]?")

	decision = input("> ")

	if decision == "leave":
		print("Leaving room!!")
		time.sleep(1)
		lobbyRoom()
	elif decision == "again":
		print("Starting the game again...")
		time.sleep(1)
		main()
	else:
		print("invalid input...")
		time.sleep(1)
		clearConsole()
		highscoreRoom()

def clearConsole():
	clear = lambda: os.system('cls')
	clear()

def lobbyRoom():
	clearConsole()
	print(f"There is an arcade in front of you, breakroom(setting) to your left, and a store to your right, your score is {score}")
	print("Where do you want to go? [front, left, right, leave]")
	direction = input("> ")
	if direction == "front":
		print("heading to the arcade...")
		time.sleep(1)
		clearConsole()
		arcadeRoom()
	elif direction == "left":
		print("heading to the breakroom...")
		time.sleep(1)
		clearConsole()
		closetRoom()
	elif direction == "right":
		print("heading to the store....")
		time.sleep(1)
		clearConsole()
		shopRoom()
	elif direction == "leave":
		quit()
	else:
		print("Not a valid input...")
		time.sleep(1)
		lobbyRoom()

def closetRoom():
	print("Looks like there is a couple of things you can change here..")
	print("You can change the speed of the game and your note color !")
	print("Which setting do you want to change? [speed] or [color]")
	decision = input("> ")

	if decision == "speed":

		print("Great!")
		time.sleep(1)
		clearConsole()
		print("The speed is based on seconds.")
		print("the higher the number, the lower the speed of the game.")
		print("How fast do you want it? (Able to go down to decimals)")
		global speed
		speed = float(input("> "))
		print(f"okay the speed is now {speed} seconds!")
		leaveCloset(2)

	if decision == "color":
		global color
		print("Your available colors are..\n")
		for colors in range(len(ownedColorsList)):
			print(f"[{colored(ownedColorsList[colors], f'{ownedColorsList[colors]}')}]")
		colorChoice = input("> ")
		if colorChoice == "":
			print("not a valid response....")
			time.sleep(1)
			clearConsole()
			closetRoom()
		else:
			color = colorChoice
			print(f"Your note color is now {color}!")
			leaveCloset(2)
	else:
		leaveCloset(1)
	

def leaveCloset(sec):
	print("Okay then! leaving the room now....")
	time.sleep(sec)
	clearConsole()
	lobbyRoom()

def arcadeRoom():
	clearConsole()
	print("Looks like there is a fun rhythm game here, should we play it?")
	print("yes or no?")
	decision = input("> ")
	if decision == "yes":
		main()
	else:
		print("Leaving the room...")
		time.sleep(1)
		clearConsole()
		lobbyRoom()

def shopRoom():
	global score
	print("Welcome to the shop!")
	print("We have colors for the notes here!")
	print("What would you like to purchase?\n")

	for color in range(len(shopItems)):
		print(f"[{colored(shopItems[color][0], f'{shopItems[color][1]}')}]? Price:{colored(shopItems[color][2], 'green')}")
		time.sleep(0.5)
	print(f"\nYour current amount of score is {colored(f'{score}', 'green')}")
	print(f"Want to leave the store? type [leave]")

	shopChoice = input("> ")

	for colors in range(len(shopItems)):
		if shopChoice == shopItems[colors][1]:
			if score >= int(shopItems[colors][2].replace(',', '')):
				if shopItems[colors][3] == True:
					print("You already own this color!")
					time.sleep(1)
					clearConsole()
					shopRoom()
					break
				print(f"Congrats!! You bought {shopItems[colors][0]}!!")
				score -= int(shopItems[colors][2].replace(',',''))
				print("You can head to the breakroom to change your color!")
				ownedColorsList.append(shopItems[colors][1])
				shopItems[colors][3] = True
				time.sleep(2)
				clearConsole()
				lobbyRoom()
				break
			else:
				print("You don't have enough for this color...")
				print("come back again when you do..")
				time.sleep(2)
				clearConsole()
				shopRoom()
		elif shopChoice == "leave":
			print("Leaving the room now....")
			time.sleep(1)
			clearConsole()
			lobbyRoom()
		elif colors == len(shopItems) - 1:
			print("Not a valid choice...")
			time.sleep(1)
			clearConsole()
			shopRoom()
lobbyRoom()