from Enemy import Enemy
from Level import Level
from colorama import Fore, Back, Style, init
init() #start the colorama function
init(autoreset=True) #makes sure each line's settings are unique

class LevelSeven(Level):
	status = {
	"spawn": 0,
	"deepForest": 0,
	"road": 0,
	"caveEntrance": 0,
	"caveOne": 0,
	"caveTwo": 0
	}
	
	levelStatus = True
	
	def __init__(self):
		self.levelStatus = True
		
	def move(self, curLoc, dir, player):
		if curLoc == 39:
			if dir == 40:
				self.deepForest(player)
		if curLoc == 40:
			if dir == 39:
				self.spawn(player)
			if dir == 41:
				self.road(player)
		if curLoc == 41:
			if dir == 42:
				self.caveEntrance(player)
			if dir == 40:
				self.deepForest(player)
		if curLoc == 42:
			if dir == 41:
				self.road(player)
			if dir == 43:
				self.caveOne(player)
		if curLoc == 43:
			if dir == 42:
				self.caveEntrance(player)
			if dir == 44:
				self.caveTwo(player)
		if curLoc == 44:
			if dir == 43:
				self.caveOne(player)
		
	def spawn(self, player):
		self.getTitle("Spawn")
		player.reset()
		player.setLocation(39)
		
		if self.status["spawn"] == 0:
			self.status["spawn"] = 1
			print("You arise after having rested with the group. You approach Ragnar to start the day")
			print(Fore.YELLOW + "Ragnar" + Fore.WHITE + ": Morning " + player.getName() + "! We should head out immediately, there is no time to spare.")
		else:
			print("The treehouse has marks of the earlier encampment, but it is time to press ahead.")
		
	def deepForest(self, player):
		self.getTitle("Deep Forest")
		player.setLocation(40)
		
		if self.status["deepForest"] == 0:
			self.status["deepForest"] = 1
			print("As you enter the deep forest unusual sounds catch your attention.")
			print("In the midst of interweaving trees you see werewolves rushing your way!")
			print("The group is ambushed by werewolves and you turn to fight one\n")
			
			ww = Enemy()
			ww.setName("Werewolf")
			ww.setHP(30)
			ww.setTotalHP(30)
			self.fight(player, ww)
		else:
			print("The werewolves remains lie on the floor, a sign of whats to come.")
		
	def road(self, player):
		self.getTitle("Road")
		player.setLocation(41)
		
		print("As you search through the forest you come across a path, along the sides of the path \nnumerous dead bodies have been ditched.")
		if self.status["road"] == 0:
			self.status["road"] = 1
			print(Fore.YELLOW + "Ragnar" + Fore.WHITE + ": What in the world happened here? This is outrageous! \n\tSo many innocent people from Medegroth, they will pay for this!")
		
		
	def caveEntrance(self, player):
		self.getTitle("Cave Entrance")
		player.setLocation(42)
		
		if self.status["caveEntrance"] == 0:
			self.status["caveEntrance"] = 1
			print("You follow the path to the entrance of a cave, from your position you can make out\nobvious signs of werewolves living here.")
			print(Fore.YELLOW + "Ragnar" + Fore.WHITE + ": We've finally found their base, now is the time to get payback for what has happened to my people.")
			print("\t" + player.getName() + ", if you're friends are anywhere, it is here. Let's save them!")
		else:
			print("The entrance to the cave is spotted with blood, there is nothing left for us here.")
		
	def caveOne(self, player):
		self.getTitle("Cave Depths One")
		player.setLocation(43)
		
		if self.status["caveOne"] == 0:
			self.status["caveOne"] = 1
			print("Your party ambushes the werewolf camp, rushing into the cave and taking up arms.")
			print("A large werewolf with claws that are larger than your face turns on you!")
			
			ww = Enemy()
			ww.setName("Werewolf")
			ww.setHP(30)
			ww.setTotalHP(30)
			self.fight(player, ww)
			
			print("After vanquishing the werwolf you desperately look around for your friends but they are not among the prisoners.")
			
		else:
			print("Massacred werewolves lie all over the cave, but your friends are not here")
		
	def caveTwo(self, player):
		self.getTitle("Cave Depths Two")
		player.setLocation(44)
		
		if self.status["caveTwo"] == 0:
			self.status["caveTwo"] = 1
			print("You enter the bottom depth of the cave to find a hulking red werewolf")
			print("It's massive figure approaches you, you can feel the power of this beast from far away")
			
			ww = Enemy()
			ww.setName("Werewolf")
			ww.setHP(50)
			ww.setTotalHP(50)
			self.fight(player, ww)
			
			print("After vanquishing the werewolf you desperately look around for your friends but they are not among the prisoners.")
			
		else:
			print("The leader werewolf lies dead on the floor, nothing else is here.")
		
		self.endLevel()
		
	
	