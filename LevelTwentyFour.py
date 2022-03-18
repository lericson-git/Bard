from Enemy import Enemy
from Level import Level
from colorama import Fore, Back, Style, init
init() #start the colorama function
init(autoreset=True) #makes sure each line's settings are unique

class LevelTwentyFour(Level):
	status = {
	"spawn": 0,
	"nymphStairs": 0,
	"volcanoRidge": 0,
	"demonCamp": 0,
	"volcanoSummit": 0
	}
	
	levelStatus = True
	
	def __init__(self):
		self.levelStatus = True
		
	def move(self, curLoc, dir, player):
		if curLoc == 138:
			if dir == 139:
				self.nymphStairs(player)
		if curLoc == 139:
			if dir == 138:
				self.spawn(player)
			if dir == 140:
				self.volcanoRidge(player)
		if curLoc == 140:
			if dir == 139:
				self.nymphStairs(player)
			if dir == 141:
				self.demonCamp(player)
		if curLoc == 141:
			if dir == 140:
				self.volcanoRidge(player)
			if dir == 142:
				self.volcanoSummit(player)
		if curLoc == 142:
			if dir == 141:
				self.demonCamp(player)
	
	def spawn(self, player):
		self.getTitle("Spawn")
		player.reset()
		player.setLocation(138)
		
		if self.status["spawn"] == 0:
			self.status["spawn"] = 1
			print("In front of you looms Mount Vashar, it is the largest structure you've ever seen.")
			print(Fore.YELLOW + "Master Wu" + Fore.WHITE + ": This is where we finish this!")
			print(Fore.YELLOW + "Ragnar" + Fore.WHITE + ": To avenge our comrades, we must win this battle.")
		else:
			print("Mount Vashar dwarves the surrounding landscape, spewing magma down miles of volcano rock.")
			
	def nymphStairs(self, player):
		self.getTitle("Nymph Stairs")
		player.setLocation(139)
		
		if self.status["nymphStairs"] == 0:
			self.status["nymphStairs"] = 1
			print("You approach a set of stairs guarded by allied forces.")
			print(Fore.YELLOW + "Apaethos" + Fore.WHITE + ": We ordered forces to secure and construct a staircase up the base of the volcano")
			print(Fore.YELLOW + "Ragnar" + Fore.WHITE + ": You think being a king makes you so interesting don't you?")
		else:
			print("The large staircase constructed from allied forces ascends into the distance.")
			
	def volcanoRidge(self, player):
		self.getTitle("Volcano Ridge")
		player.setLocation(140)
		
		if self.status["volcanoRidge"] == 0:
			self.status["volcanoRidge"] = 1
			print("The stair case goes on quite a ways but does not make it all the way up the volcano")
			print("It ends at a ridge where you decide to rest for a minute.")
			print(Fore.YELLOW + "Demon" + Fore.WHITE + ": Why hello there weaklings.")
			print(Fore.YELLOW + "Master Wu" + Fore.WHITE + ": Demons! Take arms brothers we have a mission to do!")
			
			demon = Enemy()
			demon.setName("Demon")
			demon.setHP(100)
			demon.setTotalHP(100)
			self.fight(player, demon)
		else:
			print("The ridge overlooks a vast beautiful landscape for miles to see.")
			
	def demonCamp(self, player):
		self.getTitle("Demon Camp")
		player.setLocation(141)
		
		if self.status["demonCamp"] == 0:
			self.status["demonCamp"] = 1
			print("You near a campout of a troop of demons")
			print(Fore.YELLOW + "Master Wu" + Fore.WHITE + ": Strike first, strike true, and strike swift!")
			print(Fore.YELLOW + "Apaethos" + Fore.WHITE + ": We are near the summit, give it your all!")
			print(Fore.YELLOW + "Ragnar" + Fore.WHITE + ": CHAAAARGE!")
			
			demon = Enemy()
			demon.setName("Demon")
			demon.setHP(110)
			demon.setTotalHP(110)
			self.fight(player, demon)
		else:
			print("The remains of an epic battle between the allied races and the demons are left.")
			
	def volcanoSummit(self, player):
		self.getTitle("Volcano Summit")
		player.setLocation(142)
		
		if self.status["volcanoSummit"] == 0:
			self.status["volcanoSummit"] = 1
			print("You finally reach the peak of the volcano, from here you see something terrifying.")
			print(Fore.YELLOW + "Apaethos" + Fore.WHITE + ": This is horrifying! Now my blood's really boiling!")
			print(Fore.YELLOW + "Master Wu" + Fore.WHITE + ": What in heavens name has Morfix done?")
			print(Fore.YELLOW + "Ragnar" + Fore.WHITE + ": I will save these people, I will avenge my brothers!")
		else:
			print("You approach the summit to see something truly terrifying...")
			
		self.endLevel()