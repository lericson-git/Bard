from Enemy import Enemy
from Level import Level
from colorama import Fore, Back, Style, init
init() #start the colorama function
init(autoreset=True) #makes sure each line's settings are unique

class LevelNine(Level):
	status = {
	"spawn": 0,
	"caveOne": 0,
	"caveTwo": 0,
	"caveThree": 0,
	"caveFour": 0,
	"caveFive": 0,
	"caveSix": 0,
	"bossFight": 0
	}
	
	levelStatus = True
	
	def __init__(self):
		self.levelStatus = True
		
	def move(self, curLoc, dir, player):
		if curLoc == 144:
			if dir == 145:
				self.caveOne(player)
			if dir == 146:
				self.caveTwo(player)
		if curLoc == 145:
			if dir == 148:
				self.caveFour(player)
			if dir == 144:
				self.spawn(player)
		if curLoc == 146:
			if dir == 144:
				self.spawn(player)
			if dir == 147:
				self.caveThree(player)
		if curLoc == 147:
			if dir == 146:
				self.caveTwo(player)
			if dir == 149:
				self.caveFive(player)
		if curLoc == 148:
			if dir == 145:
				self.caveOne(player)
			if dir == 150:
				self.caveSix(player)
		if curLoc == 149:
			if dir == 147:
				self.caveThree(player)
			if dir == 151:
				self.bossFight(player)
		if curLoc == 150:
			if dir == 151:
				self.bossFight(player)
			if dir == 148:
				self.caveFour(player)
		if curLoc == 151:
			if dir == 150:
				self.caveSix(player)
			if dir == 149:
				self.caveFive(player)
			
	def spawn(self, player):
		self.getTitle("Spawn")
		player.reset()
		player.setLocation(144)
		
		if self.status["bossFight"] == 0:
			print("As you march deeper into the cave you look behind you and realize everyone is gone.")
			print(Fore.YELLOW + "Unknown" + Fore.WHITE + ": aaaahhhhhhhhh!")
			print("Someone's screams echo through the cave. Something's wrong.")
		else:	
			print("There is nothing here")
		
	def caveOne(self, player):
		self.getTitle("Cave One")
		player.setLocation(145)
		
		if self.status["bossFight"] == 0:
			print("You catch a glimpse of a large demon figure running at the end of the cave.")
			print("You freeze in terror, the demon runs northwest")
		else:	
			print("There is nothing here")
		
	def caveTwo(self, player):
		self.getTitle("Cave Two")
		player.setLocation(146)
		
		if self.status["bossFight"] == 0:
			print("You hear thunderous booms and what you believe to be the sizzle of fire. The cave gets hotter.")
			print("Rock itself begins to heat up around you")
		else:	
			print("There is nothing here")
	
	def caveThree(self, player):
		self.getTitle("Cave Three")
		player.setLocation(147)
		
		if self.status["bossFight"] == 0 and self.status["caveThree"] == 0:
			self.status["caveThree"] = 1
			print("You see a demon figure ahead throw Ragnar like a doll and carry him in the northwest direction")
			print("You flicker to images of fiery scorched earth and hordes of demon creatures in your head")
		else:	
			print("There is nothing here")
	
	def caveFour(self, player):
		self.getTitle("Cave Four")
		player.setLocation(148)
		
		if self.status["bossFight"] == 0 and self.status["caveFour"] == 0:
			self.status["caveFour"] = 1
			print("You trip on something while running, when you get up you realize it is a couple of dead militia men")
			print("You grab their HP Potions while running, it might be rough but you need to survive")
			print("You gained 2 HP Potions!")
			player.addItem("HP Potion")
			player.addItem("HP Potion")
		else:	
			print("There is nothing here")
	
	def caveFive(self, player):
		self.getTitle("Cave Five")
		player.setLocation(149)
		
		if self.status["bossFight"] == 0 and self.status["caveFive"] == 0:
			self.status["caveFive"] = 1
			print("You can feel the demon's presence, your whole body feels off. Everything around you is burning hot \nbut somehow it doesn't hurt you")
			print("As you push on looking for Ragnar you catch glimpses and visions in your head of strange locations and creatures")
			print("Why has this triggered flashbacks?")
		else:	
			print("There is nothing here")
	
	def caveSix(self, player):
		self.getTitle("Cave Six")
		player.setLocation(150)
		
		if self.status["bossFight"] == 0 and self.status["caveSix"] == 0:
			self.status["caveSix"] = 1
			print("As you hustle through the cave system you see blood splattered on te walls\n it causes flashbacks of blood stained walls and pain.")
			print("What happened to me? Why is this happening now?")
		else:	
			print("There is nothing here")
	
	def bossFight(self, player):
		self.getTitle("Boss Fight")
		player.setLocation(151)
		
		if self.status["bossFight"] == 0:
			self.status["bossFight"] = 1
			print("You reach a huge open room, it was destroyed and carved out of the rock with what looks like explosives.")
			print("A demon blasts through a rock wall and into the room, it is a towering maroon figure with devilish horns.")
			print(Fore.RED + "Demon" + Fore.WHITE + ": You know not what you are, you vile mix of impurity. I hope you can save your friends!")
			print("\tThe demons are returning to power again, the King needs many souls to restore his former glory.")
			print("\tYou will be the next sacrifice added to our future")
			demon = Enemy()
			demon.setName("Demon")
			demon.setHP(100)
			demon.setTotalHP(100)
			self.fight(player, demon)
			
			self.levelStatus = False
	