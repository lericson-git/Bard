from Enemy import Enemy
from Level import Level
from colorama import Fore, Back, Style, init
init() #start the colorama function
init(autoreset=True) #makes sure each line's settings are unique

class LevelFourteen(Level):
	status = {
	"spawn": 0,
	"snowPath": 0,
	"snowMound": 0,
	"igloo": 0,
	"cave": 0
	}
	
	levelStatus = True
	
	def __init__(self):
		self.levelStatus = True
		
	def move(self, curLoc, dir, player):
		if curLoc == 85:
			if dir == 86:
				self.snowPath(player)
		if curLoc == 86:
			if dir == 85:
				self.spawn(player)
			if dir == 87:
				self.snowMound(player)
		if curLoc == 87:
			if dir == 86:
				self.snowPath(player)
			if dir == 88:
				self.igloo(player)
			if dir == 89:
				self.cave(player)
		if curLoc == 88:
			if dir == 87:
				self.snowMound(player)
		if curLoc == 89:
			if dir == 87:
				self.snowMound(player)
				
	def spawn(self, player):
		self.getTitle("Spawn")
		player.reset()
		player.setLocation(85)
		
		if self.status["spawn"] == 0:
			self.status["spawn"] = 1
			print("You enter the monastery and Master Wu approaches you")
			print(Fore.YELLOW + "Master Wu" + Fore.WHITE + ": Ragnar told me your friends have gone missing, we have had similar reports")
			print("\t   all across the four kingdoms. I think I can help you friend, but first I need your help.")
			print("\t   I will accompany you to Tiryns, the kingdom of druids, in search of answers.")
			print("\t   But first I need to address the problem at home, these Yaoguai are out of control!")
			print("\t   Come with me and slay the nearby Yaoguai in town and I will return the favor!")
		else:
			print("I need Master Wu's help, best to help him with his Yaoguai problem first.")
			if self.status["cave"] != 0:
				self.endLevel()
		
	def snowPath(self, player):
		self.getTitle("Snow Path")
		player.setLocation(86)
		
		if self.status["snowPath"] == 0:
			self.status["snowPath"] = 1
			print("Master Wu, Ragnar, and you go out searching for the threatening Yaoguai.")
			print("As you approach a snowy path into the outskirts of town three Yaoguai jump into your way")
			print(Fore.YELLOW + "Ragnar" + Fore.WHITE + ": Bout time I got to killing something!")
			
			yaoguai = Enemy()
			yaoguai.setName("Yaoguai")
			yaoguai.setHP(45)
			yaoguai.setTotalHP(45)
			self.fight(player, yaoguai)
			
			print(Fore.YELLOW + "Master Wu" + Fore.WHITE + ": You are a great warrior for one who became a bard")
		else:
			print("There is some militia men removing the bodies of the Yaoguai from before, \nhere they always give them a proper burial.")
		
	def snowMound(self, player):
		self.getTitle("Snow Mound")
		player.setLocation(87)
		
		if self.status["snowMound"] == 0:
			self.status["snowMound"] = 1
			print("You further along the route and find some tracks")
			print("You follow the tracks and find a huge Yaoguai")
			print(Fore.YELLOW + "Ragnar" + Fore.WHITE + ": Woh steady boy, we've got a behemoth here!")
			
			yaoguai = Enemy()
			yaoguai.setName("Yaoguai")
			yaoguai.setHP(55)
			yaoguai.setTotalHP(55)
			self.fight(player, yaoguai)
			
			print(Fore.YELLOW + "Master Wu" + Fore.WHITE + ": Must have been several hundred years old to be that big, amazing")
		else:
			print("The snow mound seems to be an old lair for that large Yaoguai from earlier.")
		
	def igloo(self, player):
		self.getTitle("Igloo")
		player.setLocation(88)
		
		if self.status["igloo"] == 0:
			self.status["igloo"] = 1
			print("You come across a friendly abode, a small family igloo!")
			print("You find a family outside and they offer you two HP Potions!")
			print(Fore.YELLOW + "Villager" + Fore.WHITE + ": We know how hard it is out here, we were raised to fight Yaoguai!")
			print("\tTake this potion we have plenty, good luck out there!")
			player.addItem("HP Potion")
		else:
			print("The family waves at you while you pass by the igloo")
		
	def cave(self, player):
		self.getTitle("Cave")
		player.setLocation(89)
		
		if self.status["cave"] == 0:
			self.status["cave"] = 1
			print("You find a cave in the icy mountainside")
			print("Inside you can see a chest behind a Yaoguai")
			print(Fore.YELLOW + "Master Wu" + Fore.WHITE + ": Time to get that treasure!")
			
			yaoguai = Enemy()
			yaoguai.setName("Yaoguai")
			yaoguai.setHP(50)
			yaoguai.setTotalHP(50)
			self.fight(player, yaoguai)
			print(Fore.YELLOW + "Ragnar" + Fore.WHITE + ": Treasure!")
		else:
			print("The cave must have been a fort for the Yaoguai")
			
		