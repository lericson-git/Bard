from Enemy import Enemy
from Level import Level
from colorama import Fore, Back, Style, init
import random
init() #start the colorama function
init(autoreset=True) #makes sure each line's settings are unique

class LevelEight(Level):
	status = {
	"spawn": 0,
	"caveEntrance": 0,
	"caveOne": 0,
	"caveTwo": 0,
	"caveThree": 0,
	"caveFour": 0,
	"caveFive": 0,
	"caveSix": 0,
	"caveSeven": 0,
	"caveEight": 0,
	"caveNine": 0,
	"caveTen": 0,
	"caveEleven": 0,
	"caveTwelve": 0,
	"caveExit": 0
	}
	
	levelStatus = True
	
	def __init__(self):
		self.levelStatus = True
		
	def move(self, curLoc, dir, player):
		if curLoc == 45:
			if dir == 46:
				self.caveEntrance(player)
		if curLoc == 46:
			if dir == 45:
				self.spawn(player)
			if dir == 47:
				self.caveTwo(player)
		if curLoc == 47:
			if dir == 46:
				self.caveEntrance(player)
			if dir == 48:
				self.caveThree(player)
			if dir == 53:
				self.caveTen(player)
			if dir == 59:
				self.caveOne(player)
		if curLoc == 48:
			if dir == 47:
				self.caveTwo(player)
			if dir == 49:
				self.caveFour(player)
		if curLoc == 49:
			if dir == 48:
				self.caveThree(player)
		if curLoc == 50:
			if dir == 54:
				self.caveEleven(player)
			if dir == 52:
				self.caveNine(player)
		if curLoc == 51:
			if dir == 56:
				self.caveSix(player)
			if dir == 52:
				self.caveNine(player)
		if curLoc == 52:
			if dir == 51:
				self.caveTwelve(player)
			if dir == 50:
				self.caveFive(player)
		if curLoc == 53:
			if dir == 47:
				self.caveTwo(player)
		if curLoc == 54:
			if dir == 50:
				self.caveFive(player)
			if dir == 55:
				self.caveExit(player)
		if curLoc == 55:
			if dir == 54:
				self.caveEleven(player)
		if curLoc == 56:
			if dir == 51:
				self.caveTwelve(player)
			if dir == 57:
				self.caveSeven(player)
		if curLoc == 57:
			if dir == 56:
				self.caveSix(player)
			if dir == 58:
				self.caveEight(player)
		if curLoc == 58:
			if dir == 59:
				self.caveOne(player)
			if dir == 57:
				self.caveSeven(player)
		if curLoc == 59:
			if dir == 58:
				self.caveEight(player)
			if dir == 47:
				self.caveTwo(player)
		
	def generateCave(self):
		num = random.randint(0, 3)
		if num == 1:
			print("This cave is short and dark, but featureless like the rest.")
		elif num == 2:
			print("This cave at least has some breathing room, still dull and gray though.")
		elif num == 3:
			print("This cave is really stuffy and cramped, I hate this.")
		else:
			print("Gray, featureless, uninteresting, fun stuff")
		
	def spawn(self, player):
		self.getTitle("Spawn")
		player.reset()
		player.setLocation(45)
	
		if self.status["spawn"] == 0:
			self.status["spawn"] = 1
			print("As the militia reorganizes after the attack Ragnar approaches you")
			print(Fore.YELLOW + "Ragnar" + Fore.WHITE + ": " + player.getName() + ", I have found a secret tunnel we believe they were using to smuggle\n\tkidnapped humans. I want to follow it and find why this is happening.")
			print("\n\tFollow me to the entrance, we can find where this leads and get some answers.")
		else:
			print("The werewolf camp is calm now and the militia have started heading back")
			
	def caveEntrance(self, player):
		self.getTitle("Cave Entrance")
		print(Fore.YELLOW + "Ragnar" + Fore.WHITE + ": It looks like some sort of maze in there, we won't have any clue where we are going!")
		player.setLocation(46)
		
		print("The maze ahead is dark and narrow, we might be here a while")
		
	def caveOne(self, player):
		self.getTitle("Cave")
		player.setLocation(59)
		
		self.generateCave()		
		
	def caveTwo(self, player):
		self.getTitle("Cave")
		player.setLocation(47)
		
		self.generateCave()		
	
	def caveThree(self, player):
		self.getTitle("Cave")
		player.setLocation(48)
		
		self.generateCave()		
	
	def caveFour(self, player):
		self.getTitle("Cave")
		player.setLocation(49)
		
		self.generateCave()	
	
	def caveFive(self, player):
		self.getTitle("Cave")
		player.setLocation(50)
		
		self.generateCave()	
	
	def caveSix(self, player):
		self.getTitle("Cave")
		player.setLocation(56)
		
		self.generateCave()	
	
	def caveSeven(self, player):
		self.getTitle("Cave")
		player.setLocation(57)
		
		self.generateCave()	
	
	def caveEight(self, player):
		self.getTitle("Cave")
		player.setLocation(58)
		
		self.generateCave()	
	
	def caveNine(self, player):
		self.getTitle("Cave")
		player.setLocation(52)
		
		self.generateCave()	
	
	def caveTen(self, player):
		self.getTitle("Cave")
		player.setLocation(53)
		
		self.generateCave()	
	
	def caveEleven(self, player):
		self.getTitle("Cave")
		player.setLocation(54)
		
		self.generateCave()	
	
	def caveTwelve(self, player):
		self.getTitle("Cave")
		player.setLocation(51)
		
		self.generateCave()	
	
	def caveExit(self, player):
		self.getTitle("Cave Exit!!")
		player.setLocation(55)
		
		print("We found the exit! Finally!")
		self.endLevel()
		
	
	
	