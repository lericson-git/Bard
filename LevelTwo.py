from Enemy import Enemy
from Level import Level
from colorama import Fore, Back, Style, init
init() #start the colorama function
init(autoreset=True) #makes sure each line's settings are unique

class LevelTwo(Level):
	status = {
	"spawn": 0,
	"yourTent": 0,
	"forestFloorOne": 0,
	"wolvesDen": 0,
	"river": 0,
	"forestFloorTwo": 0
	}
	
	levelStatus = True
	
	def __init__(self):
		self.levelStatus = True
		
	def getStatus(self):
		return self.status
		
	def move(self, curLoc, dir, player):
		if curLoc == 5:
			if dir == 6:
				self.yourTent(player)
			if dir == 7:
				self.forestFloor(player)
		if curLoc == 6:
			if dir == 5:
				self.spawn(player)
		if curLoc == 7:
			if dir == 5:
				self.spawn(player)
			if dir == 8:
				self.wolvesDen(player)
		if curLoc == 8:
			if dir == 7:
				self.forestFloor(player)
			if dir == 9:
				self.river(player)
		if curLoc == 9:
			if dir == 8:
				self.wolvesDen(player)
			if dir == 10:
				self.forestFloorTwo(player)
			if dir == 11:
				self.trap(player)
		if curLoc == 10:
			if dir == 9:
				self.river(player)
		if curLoc == 11:
			if dir == 9:
				self.river(player)
		

		
	def spawn(self, player):
		player.setLocation(5)
		player.reset()
		print(Fore.YELLOW + "\n\t----------\n\tCampground\n\t----------")
		
		if self.status["spawn"] == 0:
			self.status["spawn"] = 1
			print("It is the next morning, however something is wrong, it is too quiet...")
			print("As you look around the campsite you realize something happened. Everyone is gone and there are marks of a scuffle.")
			print("To the northeast you notice what looks like drag marks and disturbed shrubbery")
		else:
			print("The camp is barren, your friends are gone and your heart is weary")
		
	def yourTent(self, player):
		player.setLocation(6)
		print(Fore.YELLOW + "\t---------\n\tYour Tent\n\t---------")
		
		if self.status["yourTent"] != 2:
			self.status["yourTent"] = 1
			print("Your tent is the same as the night before, somehow you were the only one spared by whatever took place.")
			print("Before setting off it would be wise to look around for anything you might need")
		else:
			print("Your tent is the same as before, there is nothing significant left here")
			
		
		
	def forestFloor(self, player):
		player.setLocation(7)
		print(Fore.YELLOW + "\t----------------\n\tForest Floor One\n\t----------------")
		
		print("Trails of blood lead further to the northeast")
	
	def wolvesDen(self, player):
		player.setLocation(8)
		print(Fore.YELLOW + "\t----------\n\tWolves Den\n\t----------\n")
		if self.status["wolvesDen"] == 0:
			self.status["wolvesDen"] = 1
			print("As you approach the den a wolf jumps out and attacks you")
			wolf = Enemy()
			wolf.setName("Wolf")
			self.fight(player, wolf)
			print("\nAs the wolf lies lifeless on the floor it begins to convulse and morph, soon it towers and stands up like a human")
			print(Fore.YELLOW + "Werewolf" + Fore.WHITE + ": You underestimated me weak one")
			werewolf = Enemy()
			werewolf.setName("Werewolf")
			self.fight(player, werewolf)
		elif self.status["wolvesDen"] == 1:
			print("The werewolf's carcass lies on the floor, maybe you can loot it?")
		elif self.status["wolvesDen"] == 2:
			print("The werewolf has been looted and lies dead, there is nothing else here for you")
		
	def river(self, player):
		player.setLocation(9)
		print(Fore.YELLOW + "\t-----\n\tRiver\n\t-----\n")
		print("A sign with a warning lies ahead:")
		print("Careful traveler, one path from here leads to ruin, and one to treasure")
	
	def forestFloorTwo(self, player):
		player.setLocation(10)
		print(Fore.YELLOW + "\t---------\n\tForest Floor Two\n\t---------\n")
		print("There is what remains of a previous party with items strewn about the forest")
		user = input("You have finished the level, ready to continue? (Y/n)")
		if user == "Y" or user == "y":
			self.levelStatus = False
			print("Level Finished")
		else:
			print("Returning to level")
		
	def trap(self, player):
		player.setLocation(11)
		print(Fore.YELLOW + "\t-----\n\tTrap\n\t-----\n")
		print("While heading north the ground below gives way to a pit fall trap! You lose 25 HP!")
		player.setHP(player.getHP() - 25)
		
	#Haralds Gorge and down has become level three