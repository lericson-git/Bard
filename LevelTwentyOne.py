from Enemy import Enemy
from Level import Level
from colorama import Fore, Back, Style, init
init() #start the colorama function
init(autoreset=True) #makes sure each line's settings are unique

class LevelTwentyOne(Level):
	status = {
	"spawn": 0,
	"frostCliffs": 0,
	"bridge": 0,
	"boat": 0,
	"worldTree": 0
	}
	
	levelStatus = True
	
	def __init__(self):
		self.levelStatus = True
		
	def move(self, curLoc, dir, player):
		if curLoc == 122:
			if dir == 123:
				self.frostCliffs(player)
		if curLoc == 123:
			if dir == 122:
				self.spawn(player)
			if dir == 124:
				self.bridge(player)
		if curLoc == 124:
			if dir == 123:
				self.frostCliffs(player)
			if dir == 125:
				self.boat(player)
		if curLoc == 125:
			if dir == 124:
				self.boat(player)
			if dir == 126:
				self.worldTree(player)
		if curLoc == 126:
			if dir == 125:
				self.boat(player)
			
	def spawn(self, player):
		player.reset()
		self.getTitle("Spawn")
		player.setLocation(122)
		
		if self.status["spawn"] == 0:
			self.status["spawn"] = 1
			print("You leave Ymir's castle after defeating him for the next leg of your journey")
			print(Fore.YELLOW + "Apaethos" + Fore.WHITE + ": Now that we have the gemstone, we need the power of a world tree")
			print(Fore.YELLOW + "Ragnar" + Fore.WHITE + ": The nearest world tree is a rough journey through icy lands though")
			print(Fore.YELLOW + "Master Wu" + Fore.WHITE + ": We have no choice, to save the people we must use natures deepest power")
		else:
			print("The castle of Ymir is destroyed and ransacked after his defeat.")
			
	def frostCliffs(self, player):
		self.getTitle("Frost Cliffs")
		player.setLocation(123)
		
		if self.status["frostCliffs"] == 0:
			self.status["frostCliffs"] = 1
			print("You near the edge of giant ice cliffs, below you can see the basin of a sea and in the far distance you can see\nthe infamously tall world tree stretching into the clouds.")
			print(Fore.YELLOW + "Apaethos" + Fore.WHITE + ": There's our destination friends!")
			print(Fore.YELLOW + "Ragnar" + Fore.WHITE + ": Onward!")
		else:
			print("From the top of an icy cliff you can see down to a sea and across the sea to a world tree.")
	
	def bridge(self, player):
		self.getTitle("Bridge")
		player.setLocation(124)
		
		if self.status["bridge"] == 0:
			self.status["bridge"] = 1
			print("You approach a bridge to the port where you plan to search for a way across the sea.")
			print(Fore.YELLOW + "Apaethos" + Fore.WHITE + ": Look out! Yaoguai!")
			print(Fore.YELLOW + "Master Wu" + Fore.WHITE + ": Give me a break already!")
			
			yaoguai = Enemy()
			yaoguai.setName("Yaoguai")
			yaoguai.setHP(60)
			yaoguai.setTotalHP(60)
			self.fight(player, yaoguai)
		else:
			print("The gates into the castle are empty, you've defeated everyone around here.")
			
	def boat(self, player):
		self.getTitle("Boat")
		player.setLocation(125)
		
		if self.status["boat"] == 0:
			self.status["boat"] = 1
			print("Your group uses their status to get a boat and you board to head across the sea.")
			print(Fore.YELLOW + "Apaethos" + Fore.WHITE + ": Once we reach the shore we will have to climb to the top.\n\tThat is where we will place the gemstone to embue it with power.")
			print(Fore.YELLOW + "Ragnar" + Fore.WHITE + ": Sounds like a lot of work, hmph!")
			print("\nAll of a sudden your group hears a crash below the deck.")
			print("Stoaways have invaded the ship! They rush at you with a cutlass!")
			
			pirate = Enemy()
			pirate.setName("Pirate")
			pirate.setHP(80)
			pirate.setTotalHP(80)
			self.fight(player, pirate)
		else:
			print("You take the boat back across the sea.")
			
	def worldTree(self, player):
		self.getTitle("World Tree")
		player.setLocation(126)
		
		if self.status["worldTree"] == 0:
			self.status["worldTree"] = 1
			print("You arrive on the coast in amazement. The world tree climbs into the sky for miles, it breaks through the clouds.")
			print(Fore.YELLOW + "Apaethos" + Fore.WHITE + ": We have arrived men, the next stage won't be easy we need to climb to the world tree.")
			print(Fore.YELLOW + "Master Wu" + Fore.WHITE + ": We will be fighting fairies on our way up, get ready.")
			print("You set out for the world tree.")
		else:
			print("The world tree is absolutely jaw dropping, it bounds into the sky seeming impossibly tall")
			
		self.endLevel()