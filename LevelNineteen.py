from Enemy import Enemy
from Level import Level
from colorama import Fore, Back, Style, init
init() #start the colorama function
init(autoreset=True) #makes sure each line's settings are unique

class LevelNineteen(Level):
	status = {
	"spawn": 0,
	"outpost": 0,
	"banditCamp": 0,
	"castleEntrance": 0
	}
	
	levelStatus = True
	
	def __init__(self):
		self.levelStatus = True
		
	def move(self, curLoc, dir, player):
		if curLoc == 113:
			if dir == 114:
				self.outpost(player)
		if curLoc == 114:
			if dir == 113:
				self.spawn(player)
			if dir == 115:
				self.banditCamp(player)
		if curLoc == 115:
			if dir == 114:
				self.outpost(player)
			if dir == 116:
				self.castleEntrance(player)
		if curLoc == 116:
			if dir == 115:
				self.outpost(player)
				
	def spawn(self, player):
		self.getTitle("Spawn")
		player.reset()
		player.setLocation(113)
		
		if self.status["spawn"] == 0:
			self.status["spawn"] = 1
			print("Apaethos takes the party out of the Kingdom")
			print(Fore.YELLOW + "Apaethos" + Fore.WHITE + ": We need the ancient gemstone at Ymir's bandit camp, it will allow us")
			print("\tIt will allow us to harness the energy of the world tree and store it. Then we can\n\ttravel to the highest point in the world and use the magic to purify the demons.")
			print(Fore.YELLOW + "Ragnar" + Fore.WHITE + ": Bandit Ymir? He is very feared where I come from.")
			
			print(Fore.YELLOW + "Master Wu" + Fore.WHITE + ": Strong or not, he has committed heinous crimes.")
		else:
			print("Tiryns is as beautiful as ever")
			
	def outpost(self, player):
		self.getTitle("Outpost")
		player.setLocation(114)
		
		if self.status["outpost"] == 0:
			self.status["outpost"] = 1
			print("Apaethos takes the group to a Nymph outpost")
			print(Fore.YELLOW + "Apaethos" + Fore.WHITE + ": This is as close as we can get without leaving Nymph territory")
			print("\tFrom here on out it will be us against Ymir's men.")
			print(Fore.YELLOW + "Ragnar" + Fore.WHITE + ": Sounds like a blast!")
		else:
			print("The Nymph outpost is buzzing with soldiers as they prepare to assist in the demon invasion.")
			
	def banditCamp(self, player):
		self.getTitle("Bandit Camp")
		player.setLocation(115)
		
		if self.status["banditCamp"] == 0:
			self.status["banditCamp"] = 1
			print("You approach a camp of Ymir soldiers, time to strike.")
			print(Fore.YELLOW + "Apaethos" + Fore.WHITE + ": Fight swift and fight hard!")
			
			bandit = Enemy()
			bandit.setName("Ymir Bandit")
			bandit.setHP(70)
			bandit.setTotalHP(70)
			self.fight(player, bandit)
		else:
			print("The remains of the battle are on display amongst the bodies in the camp.")
		
	def castleEntrance(self, player):
		self.getTitle("Castle Entrance")
		player.setLocation(116)
		
		if self.status["castleEntrance"] == 0:
			self.status["castleEntrance"] = 1
			print("You approach the entrance to an immense frozen castle on a lake.")
			print(Fore.YELLOW + "Apaethos" + Fore.WHITE + ": Prepare for combat!")
			
			bandit = Enemy()
			bandit.setName("Ymir Bandit")
			bandit.setHP(70)
			bandit.setTotalHP(70)
			self.fight(player, bandit)
		else:
			print("The castle entrance is heavily guarded and you prepare for more conflict ahead.")
		
		self.endLevel()
	