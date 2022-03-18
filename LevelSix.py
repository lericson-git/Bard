from Enemy import Enemy
from Level import Level
from colorama import Fore, Back, Style, init
init() #start the colorama function
init(autoreset=True) #makes sure each line's settings are unique

class LevelSix(Level):
	status = {
	"spawn": 0,
	"crossroads": 0,
	"clearing": 0,
	"abandonedShack": 0,
	"pond": 0,
	"treehouse": 0
	}
	
	levelStatus = True
	
	def __init__(self):
		self.levelStatus = True
		
	def move(self, curLoc, dir, player):
		if curLoc == 33:
			if dir == 34:
				self.crossroads(player)
		if curLoc == 34:
			if dir == 33:
				self.spawn(player)
			if dir == 38:
				self.treehouse(player)
			if dir == 37:
				self.pond(player)
			if dir == 35:
				self.clearing(player)
		if curLoc == 35:
			if dir == 34:
				self.crossroads(player)
			if dir == 36:
				self.abandonedShack(player)
		if curLoc == 36:
			if dir == 35:
				self.clearing(player)
		if curLoc == 37:
			if dir == 34:
				self.crossroads(player)
		if curLoc == 38:
			if dir == 34:
				self.crossroads(player)
	
	def spawn(self, player):
		self.getTitle("Spawn")
		player.reset()
		player.setLocation(33)
		
		if self.status["spawn"] == 0:
			self.status["spawn"] == 1
			print("You awaken after a nap, the forces have been readied and you set out with Ragnar and his men.")
			print("Ragnar allows you to take the lead, they will follow you throughout the level.")
			print(Fore.YELLOW + "\nRagnar" + Fore.WHITE + ": Make sure to be careful of fairies and werewolves ahead, \n\tthey both often prove to be formidable foes.")
		else:
			print("There is nothing left here, time to move on.")
		
	def crossroads(self, player):
		self.getTitle("Crossroads")
		player.setLocation(34)
		print("There is a three way split crossroad, no one is around \nand the landscape begins to disappear into forest.")
			
	def clearing(self, player):
		self.getTitle("Clearing")
		player.setLocation(35)
		
		if self.status["clearing"] == 0:
			self.status["clearing"] = 1
			print("While you are moving through a clearing in the woods \na group of bandits attacks the group!")
			bandit = Enemy()
			bandit.setName("Bandit")
			bandit.setHP(35)
			bandit.setTotalHP(35)
			self.fight(player, bandit)
			
			print("\n" + Fore.YELLOW + "Ragnar" + Fore.WHITE + ": Great fighting " + player.getName() + "!")
			print("The bandits are defeated by the group allowing you to move on.")
		else:
			print("The bandits lie defeated in the clearing, nothing else stands out at this location.")
			
	def abandonedShack(self, player):
		self.getTitle("Abandoned Shack")
		player.setLocation(36)
		
		if self.status["abandonedShack"] == 0:
			print("The shack is empty, but something here feels off...")
		else:
			print("There is nothing left in this abandoned rotting shack")
			
	def pond(self, player):
		self.getTitle("Pond")
		player.setLocation(37)
		
		if self.status["pond"] == 0:
			self.status["pond"] == 1
			print("As you approach this pond in the landscape the air grows heavy and warm\nas if some sort of energy flowed through it.")
			print(Fore.YELLOW + "\nRagnar" + Fore.WHITE + ": This place is densely populated with fairy magic, it is said drinking from\n\ttheir magical ponds grants powers.")
			print("\tHowever, this power comes at a price, fairies will attack those who have stolen\n\ttheir magic.")
			
			while True:
				print("Would you like to drink the magical water? (Y/n)")
				user = input("")
				
				if user.lower() == "y":
					player.setHP(65)
					player.setTotalHP(65)
					player.setTotalSP(60)
					player.setSP(60)
					player.addSkill("Fairy Beam")
					print("Your total HP has been increased to 65!")
					print("Your total SP has been increased to 60!")
					print("You learned the new ability " + Fore.CYAN + "Fairy Beam" + Fore.WHITE + ". This spell uses all the player's SP\nto instantly kill the enemy, however it caps at 30 damage")
					break
				elif user.lower() == "n":
					print("You choose not to drink the water and leave")
					break
		else:
			print("The pond is magical as it illuminates from the bright sun")
			
	def treehouse(self, player):
		self.getTitle("Treehouse")
		player.setLocation(38)
	
		if self.status["clearing"] != 0:
			print("As you approach the treehouse the sun begins to set below the skyline.")
			print(Fore.YELLOW + "Ragnar" + Fore.WHITE + ": We've should stop for the night.")
			self.endLevel()
		else:
			print(Fore.YELLOW + "\nRagnar" + Fore.WHITE + ": Let's look around some more before coming here.")