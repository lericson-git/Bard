from Enemy import Enemy
from Level import Level
from colorama import Fore, Back, Style, init
init() #start the colorama function
init(autoreset=True) #makes sure each line's settings are unique

class LevelTwelve(Level):
	status = {
	"spawn": 0,
	"wutaishenEntrance": 0,
	"courtyard": 0,
	"barracks": 0,
	"housingDistrict": 0,
	"monastery": 0
	}
	
	levelStatus = True
	
	def __init__(self):
		self.levelStatus = True
		
	def move(self, curLoc, dir, player):
		if curLoc == 74:
			if dir == 75:
				self.wutaishenEntrance(player)
		if curLoc == 75:
			if dir == 76:
				self.courtyard(player)
			if dir == 74:
				self.spawn(player)
		if curLoc == 76:
			if dir == 75:
				self.wutaishenEntrance(player)
			if dir == 77:
				self.barracks(player)
			if dir == 78:
				self.housingDistrict(player)
		if curLoc == 77:
			if dir == 76:
				self.courtyard(player)
		if curLoc == 78:
			if dir == 76:
				self.courtyard(player)
			if dir == 79:
				self.monastery(player)
		if curLoc == 79:
			if dir == 78:
				self.housingDistrict(player)
				
	def spawn(self, player):
		player.reset()
		self.getTitle("Spawn")
		player.setLocation(74)
		
		if self.status["spawn"] == 0:
			self.status["spawn"] = 1
			print(Fore.YELLOW + "Master Wu" + Fore.WHITE + ": I guess I never really introduced myself, I am Master Wu and I am the king of Wutaishen.")
			print("\t   Don't worry, we have plans for your arrival")
			print("\nYou notice something amiss with Master Wu, he seems different \nthan from before. His skin is paler and he seems to have lost his composure.")
		else:
			print("The outskirt of the city, nothing important here.")
		
	def wutaishenEntrance(self, player):
		self.getTitle("Wutaishen Entrance")
		player.setLocation(75)
		
		if self.status["wutaishenEntrance"] == 0:
			self.status["wutaishenEntrance"] = 1
			print("As you enter the city the guards on post seem confused. They look at each other and seem to argue about what to do.")
			print("You overhear some questioning orders")
			print("Sounds sketchy, maybe a coup or something has been staged?")
		else:
			print("The entrance to the city, no one is around right now.")
		
	def courtyard(self, player):
		self.getTitle("Courtyard")
		player.setLocation(76)
		
		if self.status["courtyard"] == 0:
			self.status["courtyard"] = 1
			print("When you enter the courtyard you see a large group of Jinn warriors.")
			print("One of them yells towards you:")
			print(Fore.YELLOW + "Soldier" + Fore.WHITE + ": Wu aims to betray you! Get out of here quick! Something is wrong with him!")
			print("\nAfter that shout the rest of the guards turn on you with uncertain faces, however one leads an attack.")
			
			jinn = Enemy()
			jinn.setName("Jinn")
			jinn.setHP(45)
			jinn.setTotalHP(45)
			self.fight(player, jinn)
		else:
			print("The courtyard is vacated, the trouble must have caused everyone to hide.")
		
	def barracks(self, player):
		self.getTitle("Barracks")
		player.setLocation(77)
		
		if self.status["barracks"] == 0:
			self.status["barracks"] = 1
			print("As you approach the barracks two soldiers jump out at you. Ragnar takes one and you fight off the other.")
			
			jinn = Enemy()
			jinn.setName("Jinn")
			jinn.setHP(45)
			jinn.setTotalHP(45)
			self.fight(player, jinn)
			
			print(Fore.YELLOW + "Ragnar" + Fore.WHITE + ": Great fighting as usual bard! Something is wrong here, \n\tWu doesn't seem like the kind of guy to start this.")
		else:
			print("The barracks seem to be emptied.")
		
	def housingDistrict(self, player):
		self.getTitle("Housing District")
		player.setLocation(78)
		
		print("The housing district is stunning, the architechure and design holds an ancient beauty.")
		print("However, everyone seems to be hiding because of the conflict...")
		
	def monastery(self, player):
		self.getTitle("Monastery")
		player.setLocation(79)
		
		print("You approach a huge monastery, with several shrines to dietys and offering altars surrounding it.")
		self.endLevel()
		