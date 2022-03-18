from Enemy import Enemy
from Level import Level
from colorama import Fore, Back, Style, init
init() #start the colorama function
init(autoreset=True) #makes sure each line's settings are unique

class LevelTwentyTwo(Level):
	status = {
	"spawn": 0,
	"fairyHome": 0,
	"nest": 0,
	"branch": 0,
	"summit": 0
	}
	
	levelStatus = True
	
	def __init__(self):
		self.levelStatus = True
		
	def move(self, curLoc, dir, player):
		if curLoc == 127:
			if dir == 128:
				self.fairyHome(player)
		if curLoc == 128:
			if dir == 127:
				self.spawn(player)
			if dir == 129:
				self.nest(player)
		if curLoc == 129:
			if dir == 128:
				self.fairyHome(player)
			if dir == 130:
				self.branch(player)
		if curLoc == 130:
			if dir == 129:
				self.nest(player)
			if dir == 131:
				self.summit(player)
		if curLoc == 131:
			if dir == 130:
				self.branch(player)
				
	def spawn(self, player):
		self.getTitle("Spawn")
		player.setLocation(127)
		player.reset()
		
		if self.status["spawn"] == 0:
			self.status["spawn"] = 1
			print("You approach the gigantic tree and start your trek up from carved in staircases.")
			print(Fore.YELLOW + "Apaethos" + Fore.WHITE + ": Watch your step carefully friends.")
			print(Fore.YELLOW + "Ragnar" + Fore.WHITE + ": I know what I'm doing pal.")
		else:
			print("The world tree dominates the landscape, its massive height breaches the clouds.")
			
	def fairyHome(self, player):
		self.getTitle("Fairy Home")
		player.setLocation(128)
		
		if self.status["fairyHome"] == 0:
			self.status["fairyHome"] = 1
			print("As you climb the world tree you unfortunately come across a home carved into the tree,\nit's populated with fairies who notice you soon after.")
			print(Fore.YELLOW + "Master Wu" + Fore.WHITE + ": This won't end well.")
			print(Fore.YELLOW + "Ragnar" + Fore.WHITE + ": I've been itching for a fight anyway.")
			print(Fore.YELLOW + "Fairy" + Fore.WHITE + ": Get out of our home!")
			
			fairy = Enemy()
			fairy.setName("Fairy")
			fairy.setHP(90)
			fairy.setTotalHP(90)
			self.fight(player, fairy)
			
			print("The fairies flee after you defeat them.")
		else:
			print("The fairy house is abandoned.")
			
	def nest(self, player):
		self.getTitle("Nest")
		player.setLocation(129)
		
		if self.status["nest"] == 0:
			self.status["nest"] = 1
			print("As you climb the world tree you come across a giant hole in the trunk.")
			print(Fore.YELLOW + "Master Wu" + Fore.WHITE + ": A giant woodpecker nest! This must be centuries old.")
			print(Fore.YELLOW + "Ragnar" + Fore.WHITE + ": Surely no creature could be this big.")
			print("The nest is empty, maybe something is inside.")
			print("You enter the nest and find a giant woodpecker inside, it is easily as large as a boat.")
			print(Fore.YELLOW + "Woodpecker" + Fore.WHITE + ": Hello travelers, I know of your quarrel with the demons, to protect this world I will aid you.")
			print("\t    I will grant you an ancient blessing, this tree gives me the power to do so.")
			print("\t    best of luck on your further venture, the world depends on you.")
			print(Style.BRIGHT + "\nYou receive the woodpecker's blessing! Your HP and SP is now set to 85!")
			player.setHP(85)
			player.setTotalHP(85)
			player.setSP(85)
			player.setTotalSP(85)
		else:
			print("The nest is abandoned.")
			
	def branch(self, player):
		self.getTitle("Branch")
		player.setLocation(130)
		
		if self.status["branch"] == 0:
			self.status["branch"] = 1
			print("As you ascend the tree you come across a group of fairies flying around a branch.")
			print(Fore.YELLOW + "Master Wu" + Fore.WHITE + ": More fairies ahead!")
			print(Fore.YELLOW + "Ragnar" + Fore.WHITE + ": These pixie looking pinheads can buzz off.")
			
			fairy = Enemy()
			fairy.setName("Fairy")
			fairy.setHP(90)
			fairy.setTotalHP(90)
			self.fight(player, fairy)
			
			print("The fairies flee after you defeat them.")
		else:
			print("The branch is immense and sticks out of the tree for what seems like miles.")
	
	def summit(self, player):
		self.getTitle("Summit")
		player.setLocation(131)
		
		if self.status["summit"] == 0:
			self.status["summit"] = 1
			print("You reach the top of the tree, from here you can see a field of clouds below")
			print("There is an ancient looking pedestal with a divet in it.")
			print(Fore.YELLOW + "Master Wu" + Fore.WHITE + ": Place the stone in the divet and embue it when ancient magic.")
			print(Fore.YELLOW + "Ragnar" + Fore.WHITE + ": This magic is all too confusing for me.")
			print("\nYou place the stone into the pedestal and it begins to glow a bright white.")
			print(Fore.YELLOW + "Apaethos" + Fore.WHITE + ": We have the power, now we just need to travel to the highest point in the world. Mount Vashar.")
		else:
			print("The treetop gives a stunning view of miles of tree that you've climbed. You have surpassed even the clouds.")
			
		self.endLevel()