from Enemy import Enemy
from Level import Level
from colorama import Fore, Back, Style, init
init() #start the colorama function
init(autoreset=True) #makes sure each line's settings are unique

class LevelTwentyThree(Level):
	status = {
	"spawn": 0,
	"allyCamp": 0,
	"mill": 0,
	"oniCamp": 0,
	"base": 0,
	"volcano": 0
	}
	
	levelStatus = True
	
	def __init__(self):
		self.levelStatus = True
		
	def move(self, curLoc, dir, player):
		if curLoc == 132:
			if dir == 133:
				self.allyCamp(player)
		if curLoc == 133:
			if dir == 132:
				self.spawn(player)
			if dir == 134:
				self.mill(player)
		if curLoc == 134:
			if dir == 133:
				self.allyCamp(player)
			if dir == 135:
				self.oniCamp(player)
		if curLoc == 135:
			if dir == 134:
				self.mill(player)
			if dir == 136:
				self.base(player)
		if curLoc == 136:
			if dir == 135:
				self.oniCamp(player)
			if dir == 137:
				self.volcano(player)
		if curLoc == 137:
			if dir == 136:
				self.base(player)
				
	def spawn(self, player):
		self.getTitle("Spawn")
		player.setLocation(132)
		player.reset()
		
		if self.status["spawn"] == 0:
			self.status["spawn"] = 1
			print("You descend the tree top to the base of the world tree")
			print(Fore.YELLOW + "Apaethos" + Fore.WHITE + ": We can make it to Mount Vashar in a day's travel.")
			print(Fore.YELLOW + "Ragnar" + Fore.WHITE + ": No time to dally then!")
		else:
			print("The world tree dominates the landscape, its massive height breaches the clouds.")
			
	def allyCamp(self, player):
		self.getTitle("Ally Camp")
		player.setLocation(133)
		
		if self.status["allyCamp"] == 0:
			self.status["allyCamp"] = 1
			print("After traveling for a while you enter an allied force camp.")
			print("There is a mix of Nymphs, Humans, and Jinn soldiers banded togeter to lead an attack on Mount Vashar.")
			print(Fore.YELLOW + "Apaethos" + Fore.WHITE + ": These men will struggle against the demon forces as we ascend the volcano")
		else:
			print("The allied camp is an ensemble of forces banded together to bring down the demons.")
			
	def mill(self, player):
		self.getTitle("Mill")
		player.setLocation(134)
		
		if self.status["mill"] == 0:
			self.status["mill"] = 1
			print("You stop at a mill after traveling for a while to rest up.")
			print(Fore.YELLOW + "Apaethos" + Fore.WHITE + ": Be careful, I've started sensing traces of demon magic.")
			print(Fore.YELLOW + "Master Wu" + Fore.WHITE + ": Yeah, speaking of that, they're ambushing us.")
			print("A horde of demons attack your party and the allied forces that followed with you.")
			
			demon = Enemy()
			demon.setName("Demon")
			demon.setHP(100)
			demon.setTotalHP(100)
			self.fight(player, demon)
		else:
			print("The mill is disaster after the earlier battle.")
			
	def oniCamp(self, player):
		self.getTitle("Oni Camp")
		player.setLocation(135)
		
		if self.status["oniCamp"] == 0:
			self.status["oniCamp"] = 1
			print("You come across an Oni camp, they must have mobilized to assist the demons.")
			print(Fore.YELLOW + "Master Wu" + Fore.WHITE + ": These traitors will pay!")
			
			oni = Enemy()
			oni.setName("Oni")
			oni.setHP(100)
			oni.setTotalHP(100)
			self.fight(player, oni)
			
			print("Maybe the camp has some loot")
		else:
			print("The oni camp has been ransacked by your earlier fight.")
			
	def base(self, player):
		self.getTitle("Base")
		player.setLocation(136)
		
		print("You reach another temporary base set up by allied forced.")
		print(Fore.YELLOW + "Apaethos" + Fore.WHITE + ": This is our last chance to buy goods before our final assault")
		
		print(Fore.YELLOW + "Shopkeeper" + Fore.WHITE + ": Welcome to Tiryns traveller! How can I help you?")
		while True:
			print("\n\t-------Shop------\n\n\n[1] Purchase Wares\n[2] Sell Wares\n[3] Exit Shop")
			response = input("")
			if response == str(1):
				while True:
					print("\n\t-----------Purchasing----------\n\n\nYou have " + str(player.getGold()) + " gold.")
					print("[1] HP Potion - 2 Gold\n[2] SP Potion - 2 Gold\n[3] Exit Menu")
					user = input("")
					if user == str(1):
						if (player.getGold() - 2) > -1:
							player.addGold(-2)
							player.addItem("HP Potion")
							print("You purchased one HP Potion for 2 gold! You now have " + str(player.getGold()) + " gold remaining.")
						else:
							print(Style.BRIGHT + "You do not have enough gold for that item!")
					elif user == str(2):
						if (player.getGold() - 2) > -1:
							player.addGold(-2)
							player.addItem("SP Potion")
							print("You purchased one SP Potion for 2 gold! You now have " + str(player.getGold()) + " gold remaining.")
						else:
							print(Style.BRIGHT + "You do not have enough gold for that item!")
					elif user == str(3):
						break
					else:
						print("Invalid input!")
			elif response == str(2):
				player.sellItems()
			elif response == str(3):
				print(Fore.YELLOW + "Shopkeeper" + Fore.WHITE + ": Thank you for coming!")
				break
		
	def volcano(self, player):
		self.getTitle("Mount Vashar")
		player.setLocation(137)
		
		if self.status["volcano"] == 0:
			self.status["volcano"] = 1
			print("You arrive at the base of Mount Vashar and prepare for you last leg of the journey.")
			print(Fore.YELLOW + "Apaethos" + Fore.WHITE + ": I wouldn't be surprised if Morfix shows himself to try and stop us.")
			print(Fore.YELLOW + "Ragnar" + Fore.WHITE + ": We will face whatever we have to.")
			print(Fore.YELLOW + "Master Wu" + Fore.WHITE + ": Agreed my friend, for those who have been lost we will fight!")
		else:
			print("Mount Vashar is an insurmountably massive volcano, magma streams down it's rocky face.")
		
		self.endLevel()