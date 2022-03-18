from Enemy import Enemy
from Level import Level
from colorama import Fore, Back, Style, init
init() #start the colorama function
init(autoreset=True) #makes sure each line's settings are unique

class LevelTwenty(Level):
	status = {
	"spawn": 0,
	"drawbridge": 0,
	"castleCenter": 0,
	"ballroom": 0,
	"ymirChamber": 0
	}
	
	levelStatus = True
	
	def __init__(self):
		self.levelStatus = True
		
	def move(self, curLoc, dir, player):
		if curLoc == 117:
			if dir == 118:
				self.drawbridge(player)
		if curLoc == 118:
			if dir == 117:
				self.spawn(player)
			if dir == 119:
				self.castleCenter(player)
		if curLoc == 119:
			if dir == 117:
				self.drawbridge(player)
			if dir == 120:
				self.ballroom(player)
		if curLoc == 120:
			if dir == 119:
				self.castleCenter(player)
			if dir == 121:
				self.ymirChamber(player)
		if curLoc == 121:
			if dir == 120:
				self.ballroom(player)
				
	def spawn(self, player):
		player.reset()
		self.getTitle("Spawn")
		player.setLocation(117)
		
		if self.status["spawn"] == 0:
			self.status["spawn"] = 1
			print("You enter the monastery and Master Wu approaches you")
			print(Fore.YELLOW + "Apaethos" + Fore.WHITE + ": The time has come, defeating Ymir is key to saving the world.")
			print(Fore.YELLOW + "Ragnar" + Fore.WHITE + ": I will give my life for this cause!")
		else:
			print("The gates into the castle are empty, you've defeated everyone around here.")
			
	def drawbridge(self, player):
		self.getTitle("Drawbridge")
		player.setLocation(118)
		
		if self.status["drawbridge"] == 0:
			self.status["drawbridge"] = 1
			print("You approach a large drawbridge into the castle center")
			print(Fore.YELLOW + "Apaethos" + Fore.WHITE + ": They've spotted us, prepare yourselves!")
			print(Fore.YELLOW + "Ragnar" + Fore.WHITE + ": To the death!")
			
			bandit = Enemy()
			bandit.setName("Ymir Bandit")
			bandit.setHP(70)
			bandit.setTotalHP(70)
			self.fight(player, bandit)
		else:
			print("You have defeated the guards at the drawbridge.")
			
	def castleCenter(self, player):
		self.getTitle("Castle Center")
		player.setLocation(119)
		
		if self.status["castleCenter"] == 0:
			self.status["castleCenter"] = 1
			print("As you enter the center of the castle the guards are aware of your attack, they quickly come to fight.")
			print(Fore.YELLOW + "Master Wu" + Fore.WHITE + ": You will pay for your crimes!")
			print(Fore.YELLOW + "Ragnar" + Fore.WHITE + ": CHARGE!")
			
			bandit = Enemy()
			bandit.setName("Ymir Bandit")
			bandit.setHP(70)
			bandit.setTotalHP(70)
			self.fight(player, bandit)
		else:
			print("You have defeated the guards at the drawbridge.")
			
	def ballroom(self, player):
		self.getTitle("Ballroom")
		player.setLocation(120)
		
		if self.status["ballroom"] == 0:
			self.status["ballroom"] = 1
			print("You enter into a masive ballroom, the guards drop their weapons.")
			print(Fore.YELLOW + "Ragnar" + Fore.WHITE + ": Surrendering so soon?")
			print(Fore.YELLOW + "Ymir Soldier" + Fore.WHITE + ": Ymir himself desires to slay you all, you can pass into his chamber.")
			print(Fore.YELLOW + "Master Wu" + Fore.WHITE + ": This battle may be difficult, here take some potions.")
			print(Style.BRIGHT + "\nYou gained two SP and two HP Potions!")
			
			player.addItem("SP Potion")
			player.addItem("SP Potion")
			player.addItem("HP Potion")
			player.addItem("HP Potion")
		else:
			print("The guards allow you to pass into Ymir's chamber")
			
	def ymirChamber(self, player):
		self.getTitle("Ymir's Chamber")
		player.setLocation(121)
		
		if self.status["ymirChamber"] == 0:
			self.status["ymirChamber"] = 1
			print("You enter into an icy room where Ymir, a muscular giant of a man, awaits you in his throne.")
			print(Fore.YELLOW + "Ymir" + Fore.WHITE + ": I am the strongest! You are fools to attack me here, I will end you all my self.")
			print(Fore.YELLOW + "Ragnar" + Fore.WHITE + ": What an arrogant bufoon")
			
			ymir = Enemy()
			ymir.setName("Ymir")
			ymir.setHP(100)
			ymir.setTotalHP(100)
			self.fight(player, ymir)
			
			print("The magical gemstone was embedded in Ymir's chestplate, Apaethos takes it and gives you a look.")
			print(Fore.YELLOW + "Apaethos" + Fore.WHITE + ": You are truly a great warrior, we can stop the demons once and for all with this.")
		else:
			print("You have slain Ymir already! The castle is yours!")
			
		self.endLevel()