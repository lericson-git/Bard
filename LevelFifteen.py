from Enemy import Enemy
from Level import Level
from colorama import Fore, Back, Style, init
init() #start the colorama function
init(autoreset=True) #makes sure each line's settings are unique

class LevelFifteen(Level):
	status = {
	"spawn": 0,
	"zeppelin": 0,
	"clearing": 0,
	"jungleRoad": 0,
	"jungleEntrance": 0,
	"pond": 0,
	}
	
	levelStatus = True
	
	def __init__(self):
		self.levelStatus = True
		
	def move(self, curLoc, dir, player):
		if curLoc == 90:
			if dir == 91:
				self.zeppelin(player)
		if curLoc == 91:
			if dir == 90:
				self.spawn(player)
			if dir == 92:
				self.clearing(player)
		if curLoc == 92:
			if dir == 91:
				self.zeppelin(player)
			if dir == 93:
				self.jungleRoad(player)
			if dir == 94:
				self.jungleEntrance(player)
		if curLoc == 93:
			if dir == 92:
				self.clearing(player)
		if curLoc == 94:
			if dir == 92:
				self.clearing(player)
			if dir == 95:
				self.pond(player)
		if curLoc == 95:
			if dir == 94:
				self.jungleEntrance(player)
				
	def spawn(self, player):
		self.getTitle("Spawn")
		player.reset()
		player.setLocation(90)
		
		if self.status["spawn"] == 0:
			self.status["spawn"] = 1
			print("You see a large zeppelin land in the city, embroidered with Jinn insignias")
			print(Fore.YELLOW + "Master Wu" + Fore.WHITE + ": I called a zepellin to take us to Tiryns, we will need the help of the druids")
		else:
			print("The spawn is empty, just a part of the icy outskirt of town.")
		
	def zeppelin(self, player):
		self.getTitle("Zeppelin")
		player.setLocation(91)
		
		if self.status["zeppelin"] == 0:
			self.status["zeppelin"] = 1
			print("You board the large red and gold speckled zepellin and begin flying to Tiryns")
			print("You land in a clearing with an enormous jungle looming ahead")
		else:
			print("The Zeppelin has returned to where it came from, now it is just a vacated area")
		
	def clearing(self, player):
		self.getTitle("Clearing")
		player.setLocation(92)
		
		if self.status["clearing"] == 0:
			self.status["clearing"] = 1
			print("You move into the clearing as the Zeppelin takes off and leaves you behind")
			print(Fore.YELLOW + "Master Wu" + Fore.WHITE + ": The jungle ahead poses great danger")
			print(Fore.YELLOW + "Ragnar" + Fore.WHITE + ": You sound scared *chuckles*")
		else:
			print("The jungle looms ahead of the clearing")
		
	def jungleRoad(self, player):
		self.getTitle("Jungle Road")
		player.setLocation(93)
		
		if self.status["jungleRoad"] == 0:
			self.status["jungleRoad"] = 1
			print("The road is quickly surrounded by bandits!")
			print(Fore.YELLOW + "Master Wu" + Fore.WHITE + ": We've been ambushed!")
			
			bandit = Enemy()
			bandit.setHP(45)
			bandit.setTotalHP(45)
			bandit.setName("Bandit")
			self.fight(player, bandit)
			
		else:
			print("It is hard to see on this road due to the towering jungle trees")
		
	def jungleEntrance(self, player):
		self.getTitle("Jungle Entrance")
		player.setLocation(94)
		
		if self.status["jungleEntrance"] == 0:
			self.status["jungleEntrance"] = 1
			print("Out of the jungle a tiger attacks!")
			print(Fore.YELLOW + "Master Wu" + Fore.WHITE + ": Nature is a force to be reckoned with")
			
			tiger = Enemy()
			tiger.setHP(45)
			tiger.setTotalHP(45)
			tiger.setName("Tiger")
			self.fight(player, tiger)
			
		else:
			print("The massive jungle quickly blots out any view of the sky")
		
	def pond(self, player):
		self.getTitle("Pond")
		player.setLocation(95)
		
		print("The group approaches a pond with magical green water")
		self.endLevel()
		