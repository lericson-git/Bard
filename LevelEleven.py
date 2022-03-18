from Enemy import Enemy
from Level import Level
from colorama import Fore, Back, Style, init
init() #start the colorama function
init(autoreset=True) #makes sure each line's settings are unique

class LevelEleven(Level):
	status = {
	"spawn": 0,
	"mountainBase": 0,
	"mountainSlope": 0,
	"mountainSummit": 0,
	"Wutaishen": 0
	}
	
	levelStatus = True
	
	def __init__(self):
		self.levelStatus = True
		
	def move(self, curLoc, dir, player):
		if curLoc == 69:
			if dir == 70:
				self.mountainBase(player)
		if curLoc == 70:
			if dir == 69:
				self.spawn(player)
			if dir == 71:
				self.mountainSlope(player)
		if curLoc == 71:
			if dir == 70:
				self.mountainBase(player)
			if dir == 72:
				self.mountainSummit(player)
		if curLoc == 72:
			if dir == 71:
				self.mountainSlope(player)
			if dir == 73:
				self.wutaishen(player)
		if curLoc == 73:
			if dir == 72:
				self.mountainSlope(player)
				
	def spawn(self, player):
		self.getTitle("Spawn")
		player.setLocation(69)
		player.reset()
		
		if self.status["spawn"] == 0:
			self.status["spawn"] = 1
			print(Fore.YELLOW + "Jinn" + Fore.WHITE + ": \tCareful up ahead this is heavy Yaogaui territory.\n\tThey are well known around here as ancient ice creatures.\n\tWe have had conflicts with them for ages.")
		
	def mountainBase(self, player):
		self.getTitle("Mountain Base")
		player.setLocation(70)
		
		print("You approach the large Wutai mountain, it is towered with snowy tundra terrain.")
		if self.status["mountainBase"] == 0:
			self.status["mountainBase"] = 1
			
			print("Out of the snow a Yaoguai approaches!")
			yaoguai = Enemy()
			yaoguai.setName("Yaoguai")
			yaoguai.setHP(40)
			yaoguai.setTotalHP(40)
			self.fight(player, yaoguai)
		else:
			print("The mountain base is chilly and snowy, but otherwise calm.")
		
	def mountainSlope(self, player):
		self.getTitle("Mountain Slope")
		player.setLocation(71)
		
		print("On the mountain slope everything is steep and freezing. It is tough living for those who don't know the land")
		if self.status["mountainSlope"] == 0:
			self.status["mountainSlope"] = 1
			
			print("Out of the snow a Yaoguai approaches!")
			print(Fore.YELLOW + "Jinn" + Fore.WHITE + ": \tTo arms men!")
			yaoguai = Enemy()
			yaoguai.setName("Yaoguai")
			yaoguai.setHP(40)
			yaoguai.setTotalHP(40)
			self.fight(player, yaoguai)
		else:
			print("The mountain slope is freezing and piled with snow. Just moving is difficult.")
		
	def mountainSummit(self, player):
		self.getTitle("Mountain Summit")
		player.setLocation(72)
		
		print("The summit of the mountain is beautiful. An icy cap looking over all the land. You can see Wutaishen city in the distance.")
		if self.status["mountainSummit"] == 0:
			self.status["mountainSummit"] = 1
			
			print("Out of the snow a third Yaoguai approaches!")
			print(Fore.YELLOW + "Jinn" + Fore.WHITE + ": \tThere sure is a lot of competition for the mountain these days, *chuckles*")
			yaoguai = Enemy()
			yaoguai.setName("Yaoguai")
			yaoguai.setHP(40)
			yaoguai.setTotalHP(40)
			self.fight(player, yaoguai)
		else:
			print("The mountain base is chilly and snowy, but otherwise calm.")
		
	def wutaishen(self, player):
		self.getTitle("Wutaishen")
		player.setLocation(73)
		
		print("You approach the doors of Wutaishen, an ancient Jinn city dedicated to faith and balance.")
		self.endLevel()
			
		