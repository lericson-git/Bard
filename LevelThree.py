from Enemy import Enemy
from Level import Level
from colorama import Fore, Back, Style, init
init() #start the colorama function
init(autoreset=True) #makes sure each line's settings are unique

class LevelThree(Level):
	status = {
	"spawn": 0,
	"HaraldsGorge": 0,
	"ForestPath": 0,
	"BanditCamp": 0,
	"GorgeExit": 0,
	"Medegroth": 0
	}
	
	levelStatus = True
	
	def move(self, curLoc, dir, player):
		if curLoc == 12:
			if dir == 13:
				self.haraldsGorge(player)
		if curLoc == 13:
			if dir == 12:
				self.spawn(player)
			if dir == 14:
				self.forestPath(player)
			if dir == 16:
				self.gorgeExit(player)
		if curLoc == 14:
			if dir == 13:
				self.haraldsGorge(player)
			if dir == 15:
				self.banditCamp(player)
		if curLoc == 15:
			if dir == 14:
				self.forestPath(player)
		if curLoc == 16:
			if dir == 13:
				self.haraldsGorge(player)
			if dir == 17 and self.status["BanditCamp"] != 0:
				self.medegroth(player)
			else:
				print("The guards will not let you pass!")
		if curLoc == 17:
			if dir == 16:
				self.gorgeExit(player)
	
	def __init__(self):
		self.levelStatus = True
		
	def getStatus(self):
		return self.status
		
	def spawn(self, player):
		player.setLocation(12)
		player.reset()
		print(Fore.YELLOW + "\n\t------------\n\tForest Floor\n\t------------")
		print("There seems to be the remains of a previous camp here, trash and leftover food is strewn about the place.")
		print("It seems like a party was here, but something forced them to leave quickly. What happened to the band?")
		
	def haraldsGorge(self, player):
		player.setLocation(13)
		print(Fore.YELLOW + "\n\t--------------\n\tHarald's Gorge\n\t--------------")
		if self.status["HaraldsGorge"] == 0:
			self.status["HaraldsGorge"] = 1
			print("You approach a massive gorge in the forest, as you enter you can see it split two directions.")
			print("Around the gorge lie tents and signs of a community, however no one is around.")
			
	def gorgeExit(self, player):
		player.setLocation(16)
		print(Fore.YELLOW + "\n\t----------\n\tGorge Exit\n\t----------")
		if self.status["GorgeExit"] == 0:
			if self.status["BanditCamp"] == 0:
				print("As you approach the exit armed men stop you.")
				print(Fore.YELLOW + "Minuteman" + Fore.WHITE + ": Sorry, we aren't letting anyone through until we find our boss Harald.")
				print("\tHe runs this gorge and guards it, no one gets through until we know he is safe")
			elif self.status["BanditCamp"] == 1:
				print(Fore.YELLOW + "Minuteman" + Fore.WHITE + ": Harald! You're alive! Thank you so much " + player.getName() + "!")
				print(Fore.YELLOW + "Harald" + Fore.WHITE + ": These men have saved me from the bandits, to honor the debt we will let them through to Medegroth!")
			
	def medegroth(self, player):
		player.setLocation(17)
		print(Fore.YELLOW + "\n\t----------\n\tMedegroth\n\t----------")
		print("You enter the city of medegroth")
		self.endLevel()
			
	def forestPath(self, player):
		player.setLocation(14)
		print(Fore.YELLOW + "\n\t----------\n\tForest Path\n\t----------")
		if self.status["ForestPath"] == 0:
			self.status["ForestPath"] = 1
			print("As you exit the gorge back into the forest you can see a group of men ahead blocking the path.")
			print("The closer you get the more worried of a feeling builds up inside of you, until you finally reach them...")
			print(Fore.YELLOW + "Bandit" + Fore.WHITE + ": Haha, look boys we found another prey! Kill him and take everything he has!")
			bandit = Enemy()
			bandit.setName("Bandit")
			self.fight(player, bandit)
		else:
			print("The aftermath of the bandit fight surrounds you...")
			
	def banditCamp(self, player):
		print(Fore.YELLOW + "\n\t----------\n\tBandit Camp\n\t----------")
		player.setLocation(15)
		if self.status["BanditCamp"] == 0:
			self.status["BanditCamp"] = 1
			print("As you enter the bandit camp you find a prison cell with a man inside.")
			print(Fore.YELLOW + "Harald" + Fore.WHITE + ": Please help me, I have men who can return the favor. The bandits have\nbeen torturing me here for answers.")
			print("*You smash the lock with your weapon*")
			print(Fore.YELLOW + "Harald" + Fore.WHITE + ": I will be forever grateful to you, let me journey with you back to the Gorge")
		elif self.status["BanditCamp"] == 1:
			print("Harald's cell sways open, the camp is deserted otherwise")