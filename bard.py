from Player import Player
from LevelOne import LevelOne
from LevelTwo import LevelTwo
from LevelThree import LevelThree
from LevelFour import LevelFour
from LevelFive import LevelFive
from LevelSix import LevelSix
from LevelSeven import LevelSeven
from LevelEight import LevelEight
from LevelNine import LevelNine
from LevelTen import LevelTen
from LevelEleven import LevelEleven
from LevelTwelve import LevelTwelve
from LevelThirteen import LevelThirteen
from LevelFourteen import LevelFourteen
from LevelFifteen import LevelFifteen
from LevelSixteen import LevelSixteen
from LevelSeventeen import LevelSeventeen
from LevelEighteen import LevelEighteen
from LevelNineteen import LevelNineteen
from LevelTwenty import LevelTwenty
from LevelTwentyOne import LevelTwentyOne
from LevelTwentyTwo import LevelTwentyTwo
from LevelTwentyThree import LevelTwentyThree
from LevelTwentyFour import LevelTwentyFour
from LevelTwentyFive import LevelTwentyFive

import re
from colorama import Fore, Back, Style, init
init() #start the colorama function
init(autoreset=True) #makes sure each line's settings are unique

player = None

def run(player, command, level):
	if command != "":
		command = command.lower()
		if command == "dir" or command == "directions": #Directions command -- displays possible directions to move from current room
			location = player.getLocation()
			dirFile = open("directions.txt", "r") #Access datafile that tracks each location and its routes
			for line in dirFile:
				curLocRule = re.compile(r"^\d+")
				curLoc = (re.search(curLocRule, line)).group()
				if curLoc == str(location): #Match player location with same location in data file
					dirRule = re.compile(r"(?<=:)\w+") #regex expression to find direction
					dir = (re.search(dirRule, line)).group()
					locRule = re.compile(r"(?<=-)[a-zA-Z' ]+") #regex to find location name
					loc = (re.search(locRule, line)).group()
					print("\t" + dir + " - " + loc) #Output directions
			dirFile.close()
				
		elif command == "h" or command == "help": #Help command, displays basic commands and explanations
			print("---------------HELP---------------")
			#directions command
			print("\"directions\" or \"dir\" - Used to list possible routes from current location")
			#help command
			print("\"help\" or \"h\" - Used to list possible commands")
			#movement commands
			print("\"North\", \"East\", \"South\", \"West\" - Used to move to other locations. Directions can also be combined like \"Northeast\"")
			#look command
			print("\"look\" - searches the current location for any special objects (something that can be looted)")
			#loot command (chests and mobs)
			print("\"loot ___\" - when specified with a second keyword, loots the given keyword if possible. \n\tUse \"look\" to reveal lootable objects.")
			#items command
			print("\"items\" - displays all items in the players inventory")
			#Use command
			print("\"use ___\" - given an items number (use items command) this command uses that item if in inventory")
			#Add Save Code command
				
		elif command == "north" or command == "northeast" or command == "northwest" or command == "west" or command == "east" or command == "southeast" or command == "southwest" or command == "south": #Movement commands
			print("")
			location = player.getLocation()
			dirFile = open("directions.txt", "r") #Access datafile that tracks each location and its routes
			for line in dirFile:
				curLocRule = re.compile(r"^\d+")
				curLoc = (re.search(curLocRule, line)).group()
				if curLoc == str(location): #Match player location with same location in data file
					dirRule = re.compile(r"(?<=:)\w+") #regex expression to find direction
					dir = (re.search(dirRule, line)).group()
					if dir.lower() == command.lower():
						locRule = re.compile(r"\d+$") #regex to find location value
						loc = (re.search(locRule, line)).group()
						return loc
			
		elif command == "look": #Look command, searches for interactable objects in location
			level.look(player)
				
		elif command.split()[0] == "loot": #Loot command, can be used on interactable objects
			try:
				object = command.split()[1]
				level.loot(player, object)
			except:
				print("Invalid input!")
		elif command.split()[0] == "use":
			try:
				object = command.split()[1]
				player.useItem(object)
			except:
				print("Invalid input!")
		elif "".join(command) == "items": #Items command, displays items :)
			player.getItems("normal")
		else:
			print("Command not recognized. Type \"help\" for a list of usable commands.")
	return ""

def menu():
	print(Fore.MAGENTA + Style.BRIGHT + """

 
 ▄▀▀█▄▄   ▄▀▀█▄   ▄▀▀▄▀▀▀▄  ▄▀▀█▄▄  
▐ ▄▀   █ ▐ ▄▀ ▀▄ █   █   █ █ ▄▀   █ 
  █▄▄▄▀    █▄▄▄█ ▐  █▀▀█▀  ▐ █    █ 
  █   █   ▄▀   █  ▄▀    █    █    █ 
 ▄▀▄▄▄▀  █   ▄▀  █     █    ▄▀▄▄▄▄▀ 
█    ▐   ▐   ▐   ▐     ▐   █     ▐  
▐                          ▐        

	   
\n""")
	while True: #Loop through main menu options
		decision = input("[1] Start New Game\n[2] Exit Game ")
		if decision == "1": return startGame()
		elif decision == "2": break
		else:
			print("Not valid input!")
		
def startGame():
	print("\nCharacter Creation:\n------------------------------------")
	name = input("Character Name: ")
	player = Player()
	player.setName(name)
	return player
	
def runLevel(player, level): #Driver method for level one. Note: Very messy
	level.spawn(player) #Start player in spawn
	while(level.isRunning() == True): #Loop through level commands
		location = player.getLocation()
		command = input(player.getName() + ": ")
		temp = run(player, command, level) #Run method takes user input and runs it through checks for each command in the game, uses return statements to tell which commands were run
		if not temp is None and temp.isdigit(): #if returning a digit, know that it means they issued a movement command
			level.move(location, int(temp), player) #takes current location and new one and runs the next location method in the level class
		if player.getHP() < 1:
			print("\n-----------------------------------------------------------")
			print(Style.BRIGHT + "\nYou have died! You have been granted one HP Potion to help get through the level\nRestarting level from spawn...\n\n\n")
			player.addItem("HP Potion")
			level.reset(player, level.getStatus())
			level.spawn(player)
			
		
player = menu()
levelOne = LevelOne()
levelTwo = LevelTwo()
levelThree = LevelThree()
levelFour = LevelFour()
levelFive = LevelFive()
levelSix = LevelSix()
levelSeven = LevelSeven()
levelEight = LevelEight()
levelNine = LevelNine()
levelTen = LevelTen()
levelEleven = LevelEleven()
levelTwelve = LevelTwelve()
levelThirteen = LevelThirteen()
levelFourteen = LevelFourteen()
levelFifteen = LevelFifteen()
levelSixteen = LevelSixteen()
levelSeventeen = LevelSeventeen()
levelEighteen = LevelEighteen()
levelNineteen = LevelNineteen()
levelTwenty = LevelTwenty()
levelTwentyOne = LevelTwentyOne()
levelTwentyTwo = LevelTwentyTwo()
levelTwentyThree = LevelTwentyThree()
levelTwentyFour = LevelTwentyFour()
levelTwentyFive = LevelTwentyFive()

runLevel(player, levelOne)
runLevel(player, levelTwo)
runLevel(player, levelThree)
runLevel(player, levelFour)
runLevel(player, levelFive)
runLevel(player, levelSix)
runLevel(player, levelSeven)
runLevel(player, levelEight)
runLevel(player, levelNine)
runLevel(player, levelTen)
runLevel(player, levelEleven)
runLevel(player, levelTwelve)
runLevel(player, levelThirteen)
runLevel(player, levelFourteen)
runLevel(player, levelFifteen)
runLevel(player, levelSixteen)
runLevel(player, levelSeventeen)
runLevel(player, levelEighteen)
runLevel(player, levelNineteen)
runLevel(player, levelTwenty)
runLevel(player, levelTwentyOne)
runLevel(player, levelTwentyTwo)
runLevel(player, levelTwentyThree)
runLevel(player, levelTwentyFour)
runLevel(player, levelTwentyFive)