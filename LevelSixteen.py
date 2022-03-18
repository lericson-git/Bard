from Enemy import Enemy
from Level import Level
from colorama import Fore, Back, Style, init
init() #start the colorama function
init(autoreset=True) #makes sure each line's settings are unique

class LevelSixteen(Level):
	status = {
	"spawn": 0,
	"cottage": 0,
	"nymphCamp": 0,
	"cave": 0,
	"river": 0,
	"cauponaInn": 0,
	}
	
	levelStatus = True
	
	def __init__(self):
		self.levelStatus = True
		
	def move(self, curLoc, dir, player):
		if curLoc == 96:
			if dir == 97:
				self.cottage(player)
			if dir == 98:
				self.nymphCamp(player)
			if dir == 99:
				self.cave(player)
		if curLoc == 97:
			if dir == 96:
				self.spawn(player)
		if curLoc == 98:
			if dir == 96:
				self.spawn(player)
		if curLoc == 99:
			if dir == 100:
				self.river(player)
			if dir == 96:
				self.spawn(player)
		if curLoc == 100:
			if dir == 99:
				self.cave(player)
			if dir == 101:
				self.cauponaInn(player)
		if curLoc == 101:
			if dir == 100:
				self.river(player)
				
	def spawn(self, player):
		self.getTitle("Spawn")
		player.reset()
		player.setLocation(96)
		
		if self.status["spawn"] == 0:
			self.status["spawn"] = 1
			print("Your party approaces the magic pond")
			print("You notice a SP Potion floating in the pond! You gained one SP Potion!")
			player.addItem("SP Potion")
		else:
			print("The pond shimmers bright green. Nothing else is here")
		
	def cottage(self, player):
		self.getTitle("Cottage")
		player.setLocation(97)
		
		if self.status["cottage"] == 0:
			self.status["cottage"] = 1
			print("You approach a homey cottage in the jungle, it turns out to be abandoned")
			print("You search the interior and manage to find two HP Potions!")
			player.addItem("HP Potion")
			player.addItem("HP Potion")
		else:
			print("The abandoned cottage has been left to weather for quite some time")
			print(Fore.YELLOW + "Master Wu" + Fore.WHITE + ": The jungle has taken back what man stole from it.")
		
	def nymphCamp(self, player):
		self.getTitle("Nymph Camp")
		player.setLocation(98)
		
		if self.status["nymphCamp"] == 0:
			self.status["nymphCamp"] = 1
			print("You enter a nymph camp, they are slender botanical creatures")
			print("The Nymphs lie on stretchers and look beaten up")
			print(Fore.YELLOW + "Nymph" + Fore.WHITE + ": Be careful around here friends, the Oni are out.")
			print("\tThe Oni are a traitorous group of Nymphs who have abandoned Tiryns in search of power.\n\tThey've taken over a nearby inn, watch out!")
		else:
			print("You enter the camp of nymphs from before, they are all resting and healing.")
		
	def cave(self, player):
		self.getTitle("Cave")
		player.setLocation(99)
		
		if self.status["cave"] == 0:
			self.status["cave"] = 1
			print("As you walk through the jungle you see a small cave coming out of a raised hillside")
			print("You enter to find several dead Nymph soldiers and instantly see the pain on Master Wu's face.")
			print(Fore.YELLOW + "Master Wu" + Fore.WHITE + ": I have many Nymph friends, I cannot stand for this. \n\t   The Nymphs are known for their passive attitude and open friendliness, this is just wrong.")
			print(Fore.YELLOW + "Ragnar" + Fore.WHITE + ": While I honor their death greatly Wu, I feel like we should " + Style.BRIGHT + "look" + Style.NORMAL + " around for any loot.")
			print("\tThey would want us to use their items to stop the murderous traitors that slew them.")
		else:
			print("You enter the cave, the bodies from before upset you. Why is innocent life facing strife across the world? Demons are this powerful?")
		
	def river(self, player):
		self.getTitle("River")
		player.setLocation(100)
		
		if self.status["river"] == 0:
			self.status["river"] = 1
			print("You approach a wide lush river, surrounded by beautiful flowers and sweeping jungle vines.")
			print("A surprise ambush! Three Oni warriors attack your party")
			print(Fore.YELLOW + "Master Wu" + Fore.WHITE + ": They'll regret this!")
			
			oni = Enemy()
			oni.setName("Oni")
			oni.setHP(55)
			oni.setTotalHP(55)
			self.fight(player, oni)
		else:
			print("The river shimmers bright blue but is tainted with red blood.")
		
	def cauponaInn(self, player):
		self.getTitle("Caupona Inn")
		player.setLocation(101)
		
		if self.status["cauponaInn"] == 0:
			self.status["cauponaInn"] = 1
			print("As you walk through the jungle you find an inn, hopeful to rest you enter.")
			print("The inn is dark and crowded, you sit to have a drink and talk with Ragnar and Wu")
			print("Out of nowhere the fellow customers at the inn pull out swords and draw on you")
			print("The Oni have ambushed you again!")
			print(Fore.YELLOW + "Ragnar" + Fore.WHITE + ": To arms! I'm tired of these dirty tactics!")
			
			oni = Enemy()
			oni.setName("Oni")
			oni.setHP(55)
			oni.setTotalHP(55)
			self.fight(player, oni)
		else:
			print("The inn is trashed after the earlier fight.")
		
		self.endLevel()
		