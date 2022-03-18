from Enemy import Enemy
from Level import Level
from colorama import Fore, Back, Style, init
init() #start the colorama function
init(autoreset=True) #makes sure each line's settings are unique

class LevelTen(Level):
	status = {
	"spawn": 0,
	"wutaiShrine": 0,
	"hiddenAltar": 0,
	"jinnCamp": 0,
	"wutaiSteppe": 0
	}
	
	levelStatus = True
	
	def __init__(self):
		self.levelStatus = True
		
	def move(self, curLoc, dir, player):
		if curLoc == 64:
			if dir == 65:
				self.wutaiShrine(player)
			if dir == 67:
				self.jinnCamp(player)
		if curLoc == 65:
			if dir == 64:
				self.spawn(player)
			if dir == 66:
				self.hiddenAltar(player)
		if curLoc == 66:
			if dir == 65:
				self.wutaiShrine(player)
		if curLoc == 67:
			if dir == 64:
				self.spawn(player)
			if dir == 68:
				self.wutaiSteppe(player)
		if curLoc == 68:
			if dir == 67:
				self.jinnCamp(player)
		
	def spawn(self, player):
		self.getTitle("Spawn")
		player.setLocation(64)
		player.reset()
		
		if self.status["spawn"] == 0:
			self.status["spawn"] = 1
			print("You wake up to the bright sun flashing on your face, you slowly get up and look around")
			print("You see two dark tall figures, you recognize them as Jinn, another race renowned for their religious beliefs.")
			print(Fore.YELLOW + "Jinn" + Fore.WHITE + ": \tYou probably are confused after everything that happened.")
			print("\tWe are from the Jinn capital and we have been hunting demons. \n\tIt seems you encountered one before us unfortunately")
			print("\tYou passed out in the fight but we came just in time to save you. We should get going to Wutaishen, our city.")
		else:
			print("The entrance to the cave can be seen, time to move on to Wutaishen though.")
		
	def wutaiShrine(self, player):
		self.getTitle("Wutai Shrine")
		player.setLocation(65)
		
		if self.status["wutaiShrine"] == 0:
			self.status["wutaiShrine"] = 1
			print(Fore.YELLOW + "Jinn" + Fore.WHITE + ": \tWe ask that you honor our diety with us, and kneel at the shrine")
			print("You kneel with the Jinn and a sensation flows through you! You gained 10 HP!")
			player.setHP(player.getHP() + 10)
			player.setTotalHP(player.getTotalHP() + 10)
		else:
			print("The Shrine is a large red gate that has intricate carvings all over.")
		
	def hiddenAltar(self, player):
		self.getTitle("Hidden Altar")
		player.setLocation(66)
		
		if self.status["hiddenAltar"] == 0:
			self.status["hiddenAltar"] = 1
			print("There is a hidden altar behind the shrine, it has an abandoned treasure chest under it")
		else:
			print("The altar is tucked away behind the shrine.")
		
	def jinnCamp(self, player):
		self.getTitle("Jinn Camp")
		player.setLocation(67)
		
		if self.status["jinnCamp"] == 0:
			self.status["jinnCamp"] = 1
			print(Fore.YELLOW + "Jinn" + Fore.WHITE + ": \tWe have been aware of the return of the demons.\n\tPeople have been going missing in every major civilization.")
			print("\tWe are not sure what the purpose of the kidnappings are but we are working on figuring it out.")
		else:
			print("There is a small camp with some Jinn soldiers")
		
	def wutaiSteppe(self, player):
		self.getTitle("Wutai Steppe")
		player.setLocation(68)
		
		if self.status["wutaiSteppe"] == 0:
			self.status["wutaiSteppe"] = 1
			print("As you approach the steppe a large burly yeti creature attacks your group.")
			yaoguai = Enemy()
			yaoguai.setName("Yaoguai")
			yaoguai.setHP(40)
			yaoguai.setTotalHP(40)
			self.fight(player, yaoguai)
			
			self.endLevel()
		else:
			print("The altar is tucked away behind the shrine.")
		