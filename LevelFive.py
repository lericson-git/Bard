from Enemy import Enemy
from Level import Level
from colorama import Fore, Back, Style, init
init() #start the colorama function
init(autoreset=True) #makes sure each line's settings are unique

class LevelFive(Level):
	status = {
	"medegrothEntrance": 0,
	"noticeBoard": 0,
	"townSquare": 0,
	"colleseum": 0,
	"adventureShop": 0,
	"cityWall": 0,
	"alley": 0,
	"park": 0,
	"spawn": 0,
	"colleseumEntrance": 0,
	"arenaOne": 0,
	"arenaTwo": 0,
	"podium": 0
	}
	
	levelStatus = True
	
	def __init__(self):
		self.levelStatus = True
	
	def move(self, curLoc, dir, player):
		if curLoc == 18:
			if dir == 19:
				self.noticeBoard(player)
			if dir == 20:
				self.townSquare(player)
			if dir == 21:
				self.colleseum(player)
		if curLoc == 19:
			if dir == 18:
				self.medegrothEntrance(player)
		if curLoc == 20:
			if dir == 18:
				self.medegrothEntrance(player)
			if dir == 22:
				self.adventureShop(player)
			if dir == 23:
				self.cityWall(player)
			if dir == 24:
				self.alley(player)
		if curLoc == 21:
			if dir == 18:
				self.medegrothEntrance(player)
		if curLoc == 22:
			if dir == 20:
				self.townSquare(player)
		if curLoc == 23:
			if dir == 20:
				self.townSquare(player)
		if curLoc == 24:
			if dir == 20:
				self.townSquare(player)
			if dir == 26:
				self.park(player)
		if curLoc == 26:
			if dir == 24:
				self.alley(player)
			if dir == 27:
				self.spawn(player)
		if curLoc == 27:
			if dir == 26:
				self.park(player)
		if curLoc == 28:
			if dir == 29:
				self.arenaOne(player)
			if dir == 32:
				self.colleseum(player)
		if curLoc == 29:
			if dir == 28:
				self.colleseumEntrance(player)
			if dir == 30:
				self.arenaTwo(player)
		if curLoc == 30:
			if dir == 29:
				self.arenaOne(player)
			if dir == 31:
				self.podium(player)
		if curLoc == 31:
			if dir == 30:
				self.arenaTwo(player)
		if curLoc == 32:
			if dir == 28:
				self.colleseumEntrance(player)
			if dir == 18:
				self.medegrothEntrance(player)
				
	def medegrothEntrance(self, player):
		print(Fore.YELLOW + "\n\t------------------\n\tMedegroth Entrance\n\t------------------")
		player.setLocation(18)
		player.reset()
		
		if self.status["podium"] == 0:
			print("The entrance is held open but we have no reason to leave the city. I need to find the colleseum and win Ragnar's trust.")
		else:
			print("People have left the colleseum and filter out along the entrance. I should look for the city wall and get ready to find my friends")
	
	def noticeBoard(self, player):
		print(Fore.YELLOW + "\n\t------------\n\tNotice Board\n\t------------")
		player.setLocation(19)
		
		print("The notice board is still filled with missing person posters but none of them stand out. I hope everyone is okay...")
	
	def townSquare(self, player):
		print(Fore.YELLOW + "\n\t-----------\n\tTown Square\n\t-----------")
		player.setLocation(20)
		
		if self.status["townSquare"] == 0:
			self.status["townSquare"] = 1
			print("There are large crowds heading to the colleseum, some stores are closed for the event.")
		else:
			print("The square is typical, nothing stands out here but a constant bustle of shopping families and individuals.")
	
	def colleseum(self, player):
		print(Fore.YELLOW + "\n\t---------\n\tColleseum\n\t---------")
		player.setLocation(32)
		
		if self.status["podium"] == 0:
			print("People are crowding into the stands, Ragnar said I needed to prove my worth so I need to find the arena...")
		else:
			print("The colleseum outside towers up into the sky, but the tournement is over now and people are filing out.")
	
	def adventureShop(self, player):
		player.setLocation(22)
		print(Fore.YELLOW + "\n\t-----------------\n\tAdventurer's Shop\n\t-----------------")
		
		print(Fore.YELLOW + "Shopkeeper" + Fore.WHITE + ": Welcome to the adventurer's shop! How can I help you?")
		while True:
			print("\n\t-------Shop------\n\n\n[1] Purchase Wares\n[2] Sell Wares\n[3] Exit Shop")
			response = input("")
			if response == str(1):
				while True:
					print("\n\t-----------Purchasing----------\n\n\nYou have " + str(player.getGold()) + " gold.")
					print("[1] HP Potion - 2 Gold\n[2] SP Potion - 2 Gold\n[3] Dual Blades (12 Damage) - 5 Gold\n[4] Exit Menu")
					user = input("")
					if user == str(1):
						if (player.getGold() - 2) > -1:
							player.addGold(-2)
							player.addItem("HP Potion")
							print("You purchased one HP Potion for 2 gold! You now have " + str(player.getGold()) + " gold remaining.")
						else:
							print(Style.BRIGHT + "You do not have enough gold for that item!")
					elif user == str(2):
						if (player.getGold() - 2) > -1:
							player.addGold(-2)
							player.addItem("SP Potion")
							print("You purchased one SP Potion for 2 gold! You now have " + str(player.getGold()) + " gold remaining.")
						else:
							print(Style.BRIGHT + "You do not have enough gold for that item!")
					elif user == str(3):
						if player.getGold() > 4.0:
							player.addGold(-5)
							player.addWeapon("Dual Blades")
							print("You purchased the Dual Blades for 5 gold! You now have " + str(player.getGold()) + " gold remaining.")
						else:
							print(Style.BRIGHT + "You do not have enough gold for that item!")
					elif user == str(4):
						break
					else:
						print("Invalid input!")
			elif response == str(2):
				player.sellItems()
			elif response == str(3):
				print(Fore.YELLOW + "Shopkeeper" + Fore.WHITE + ": Thank you for coming!")
				break
		
	def cityWall(self, player):
		print(Fore.YELLOW + "\n\t---------\n\tCity Wall\n\t---------")
		player.setLocation(23)
		
		print("At the wall dozens of men are gathered preparing military supplies.")
		print("A young militia man with a serious look approaches you")
		if self.status["podium"] == 1:
			print(Fore.YELLOW + "Militia Man" + Fore.WHITE + ": Ragnar said you would come this way, rest here and we will launch the attack once supplies are ready")
			while True:
				user = input("\nYou have finished this level, ready to advance to the next? (Y/n)")
				if user == "Y" or user == "y":
					print("Level Finished")
					self.levelStatus = False
					break
				elif user.lower() == "n":
					print("Returning to level")
					break
				else:
					print("Invalid input!")
		else:
			print(Fore.YELLOW + "Militia Man" + Fore.WHITE + ": We are going to attack the werewolves tomorrow, talk to Ragnar to join on the mission")
	
	def alley(self, player): #status 2 and 3 is saved for level four, dont use it
		print(Fore.YELLOW + "\n\t-----\n\tAlley\n\t-----")
		player.setLocation(24)
		
		print("The alleyway is deserted today, seems everyone has gone another way")
	
	def park(self, player):
		print(Fore.YELLOW + "\n\t----\n\tPark\n\t----")
		player.setLocation(26)
		
		print("The park has more people today, they seem to be excited for the colleseum fights.")
	
	def spawn(self, player):
		print(Fore.YELLOW + "\n\t----------\n\tMilitia HQ\n\t----------")
		player.setLocation(27)
		
		if self.status["spawn"] == 0:
			self.status["spawn"] = 1
			print("You awaken the next day at the militia HQ, as you leave your room you hear swarms of noise. \nMen shouting, scurrying around and getting ready, Ragnar paces around beaming.")
			print("You approach Ragnar and he strikes up conversation,")
			print(Fore.YELLOW + "\nRagnar" + Fore.WHITE + ": Hello again " + player.getName() + "! So you're friends are missing? Welcome to Medegroth then, over the last couple months")
			print("\tpeople keep disappearing. We now know it is because werewolves have started kidnapping them. \n\tWe are launching a raid against them tomorrow. Rest assured we will do what we can.")
			print("\tOh you want to help? Haha I envy your youth, if you want to find your friends I will bring you along,\n\tbut I need to know I can trust you.")
			print("\tToday is the day of righteous combat at the colleseum, prove your worth there and I will help you.")
		else:
			print(Fore.YELLOW + "Ragnar" + Fore.WHITE + ": See you at the colleseum friend.")
		
	def colleseumEntrance(self, player):
		print(Fore.YELLOW + "\n\t------------------\n\tColleseum Entrance\n\t------------------")
		player.setLocation(28)
		
		if self.status["podium"] == 0:
			print("As you enter the colleseum you spot Ragnar by a staircase.")
			print(Fore.YELLOW + "Ragnar" + Fore.WHITE + ": So you had the courage to show up huh, alright there is two arenas,\n\tif you can emerge victorious in each you will have earned my trust.")
			print("\tBest of luck friend, hope you don't need it.")
		else:
			print("The entrance is empty, everyone is leaving and food vendors are closing down shop.")
		
	def arenaOne(self, player):
		print(Fore.YELLOW + "\n\t---------\n\tArena One\n\t---------")
		player.setLocation(29)
		
		if self.status["arenaOne"] == 0:
			self.status["arenaOne"] = 1
			print("You enter the first arena, it is large with copious crowds watching from above. You walk out onto the floor and greet your enemy")
			tiger = Enemy()
			tiger.setName("Tiger")
			tiger.setHP(30)
			tiger.setTotalHP(30)
			self.fight(player, tiger)
			print("\nYou have vanquished the tiger! The crowd goes loud with applause and you feel a sense of triumph rush through you.\nTime for the next arena")
		else:
			print("The arena is vacated now, some money has been thrown onto the arena floor from the audience.")
		
	def arenaTwo(self, player):
		print(Fore.YELLOW + "\n\t---------\n\tArena Two\n\t---------")
		player.setLocation(30)
		
		if self.status["arenaTwo"] == 0:
			self.status["arenaTwo"] = 1
			print("As you enter arena two you feel dwarfed, the crowd is massive and the arena is immense as well. Thousands of citizens gather to watch.")
			print("Your enemy approaches, a hulking man in armor, he remains silent but stares you down intensely.")
			
			gladiator = Enemy()
			gladiator.setName("Gladiator")
			gladiator.setHP(40)
			gladiator.setTotalHP(40)
			self.fight(player, gladiator)
			print("\nAs you topple the gladiator thunderous applause echoes throughout the Colosseum. Ragnar stands at the podium\n awaiting you with a wide grin")
		else:
			print("The arena is empty from your prior fight, but stirs a feeling of accomplishment within you nonetheless.")
			
	def podium(self, player):
		print(Fore.YELLOW + "\n\t-----\n\tPodium\n\t-----")
		player.setLocation(31)
		
		if self.status["podium"] == 0:
			self.status["podium"] = 1
			print("Ragnar puts his hands on your shoulder and gives you a friendly pat")
			print(Fore.YELLOW + "Ragnar" + Fore.WHITE + ": Amazing work " + player.getName() + "! Truly spectacular fighting if I say so myself.")
			print("\tI trust you and your strength now, sorry for the trouble. At the city wall we are gathering\n\tfor an expedition tomorrow\n\tIf you want to find your friends meet there and we will work together on this.")
		else:
			print("The podium is vacant, the militia have gone to the city wall to prepare and the people have returned home for the day.")