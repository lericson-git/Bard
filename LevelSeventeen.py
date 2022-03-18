from Enemy import Enemy
from Level import Level
from colorama import Fore, Back, Style, init
init() #start the colorama function
init(autoreset=True) #makes sure each line's settings are unique

class LevelSeventeen(Level):
	status = {
	"spawn": 0,
	"hiddenPath": 0,
	"cliffSide": 0,
	"oceanCoast": 0,
	"lighthouse": 0,
	"cityGates": 0
	}
	
	levelStatus = True
	
	def __init__(self):
		self.levelStatus = True
		
	def move(self, curLoc, dir, player):
		if curLoc == 102:
			if dir == 103:
				self.hiddenPath(player)
		if curLoc == 103:
			if dir == 102:
				self.spawn(player)
			if dir == 104:
				self.cliffside(player)
		if curLoc == 104:
			if dir == 103:
				self.hiddenPath(player)
			if dir == 105:
				self.oceanCoast(player)
			if dir == 106:
				self.lighthouse(player)
		if curLoc == 105:
			if dir == 104:
				self.cliffside(player)
		if curLoc == 106:
			if dir == 104:
				self.cliffside(player)
			if dir == 107:
				self.cityGates(player)
		if curLoc == 107:
			if dir == 106:
				self.lighthouse(player)
				
	def spawn(self, player):
		self.getTitle("Spawn")
		player.reset()
		player.setLocation(102)
		
		if self.status["spawn"] == 0:
			self.status["spawn"] = 1
			
			print("You rested for the night at the inn, you awaken and prepare to reach Tiryns, the Nymph capital")
			print("You leave the inn and head into the jungle.")
			print(Fore.YELLOW + "Master Wu" + Fore.WHITE + ": I remember a hidden path around here from a previous visit, perhaps we can find it.")
		else:
			print("The inn is empty")
		
	def hiddenPath(self, player):
		self.getTitle("Hidden Path")
		player.setLocation(103)
		
		if self.status["hiddenPath"] == 0:
			self.status["hiddenPath"] = 1
			
			print("Master Wu leads you onto a hidden path that helps guide you through the jungle")
			print(Fore.YELLOW + "Ragnar" + Fore.WHITE + ": I'm feeling antsy here, the has jungle too many ambush spots")
		else:
			print("The hidden path is shrouded in jungle vines and shrubs, it is hot and humid.")
			
	def cliffside(self, player):
		self.getTitle("Cliff side")
		player.setLocation(104)
		
		if self.status["cliffSide"] == 0:
			self.status["cliffSide"] = 1
			
			print("You emerge out of the jungle onto a steep cliff side, you can see the ocean and a lighthouse in the distance.")
			print("When you turn to head down the cliff to the ocean another Oni team ambushes you!")
			print(Fore.YELLOW + "Oni Soldier" + Fore.WHITE + ": The best about killing you is that I only do it for fun")
			oni = Enemy()
			oni.setName("Oni")
			oni.setHP(55)
			oni.setTotalHP(55)
			self.fight(player, oni)
		else:
			print("The view is amazing, it overlooks a steep drop into the ocean with beautiful shores")
			
	def oceanCoast(self, player):
		self.getTitle("Ocean Coast")
		player.setLocation(105)
		
		if self.status["oceanCoast"] == 0:
			self.status["oceanCoast"] = 1
			
			print("You continue to Tiryns along a beautiful coastline, you can see the tower of a lighthouse in the distance")
			print("As you walk along the coast you find a bedazzling shell, you keep it.")
		else:
			print("The coastline is riddled with Nymphs fishing and camping")
			
	def lighthouse(self, player):
		self.getTitle("Lighthouse")
		player.setLocation(106)
		
		if self.status["lighthouse"] == 0:
			self.status["lighthouse"] = 1
			
			print("As you near Tiryns you reach a great lighthouse made from a massive tree. \nIt towers above the cliffs and surrounding landscape.")
			print(Fore.YELLOW + "Msater Wu" + Fore.WHITE + ": This lighthouse is renowned as a symbol of Tiryn culture")
			print(Fore.YELLOW + "Ragnar" + Fore.WHITE + ": You try really hard to sound sophisticated don't you?")
			print(Fore.YELLOW + "Master Wu" + Fore.WHITE + ": I do not believe engaging in aggresive discourse will help the situation.")
		else:
			print("The infamous Tiryns lighthouse carved from an ancient towering tree dwarves the landscape")
			
	def cityGates(self, player):
		self.getTitle("City Gates")
		player.setLocation(102)
			
		print("You reach Tiryns, it is a magestic grown city, buildings are woven from living trees \nand skyscrapers are carved from massive trees.")
			
		self.endLevel()	