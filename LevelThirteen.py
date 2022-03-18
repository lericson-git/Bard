from Enemy import Enemy
from Level import Level
from colorama import Fore, Back, Style, init
init() #start the colorama function
init(autoreset=True) #makes sure each line's settings are unique

class LevelThirteen(Level):
	status = {
	"spawn": 0,
	"wutaishenEntrance": 0,
	"courtyard": 0,
	"barracks": 0,
	"housingDistrict": 0
	}
	
	levelStatus = True
	
	def __init__(self):
		self.levelStatus = True
		
	def move(self, curLoc, dir, player):
		if curLoc == 80:
			if dir == 81:
				self.housingDistrict(player)
		if curLoc == 81:
			if dir == 82:
				self.courtyard(player)
			if dir == 80:
				self.spawn(player)
		if curLoc == 82:
			if dir == 81:
				self.housingDistrict(player)
			if dir == 83:
				self.barracks(player)
			if dir == 84:
				self.wutaishenEntrance(player)
		if curLoc == 83:
			if dir == 82:
				self.courtyard(player)
		if curLoc == 84:
			if dir == 82:
				self.courtyard(player)
				
	def spawn(self, player):
		self.getTitle("Spawn")
		player.setLocation(80)
		player.reset()
		
		if self.status["spawn"] == 0:
			self.status["spawn"] = 1
			print("You enter the monastery to see Master Wu waiting with his weapon drawn. He looks sickly and pale, almost as if possessed")
			print(Fore.YELLOW + "Master Wu" + Fore.WHITE + ": I am sorry, cant... control...")
			print("\n" + Fore.RED + "Master Wu lunges at you with the blade as if being forced to move his body.")
			print(Fore.GREEN + "You narrowly dodge the attack, all of a sudden you get an urge to help Master Wu")
			print("You reach out and grab Master Wu's shoulder, a light pulses from your hand and the\ncolor on Master Wu begins to restore.")
			print("A magical spell releases Master Wu and he explains how he was corrupted by a demon.")
			print("Somehow you have a power to combat this? More questions than I need right now...")
			print(Style.BRIGHT + "\nExplore town and visit the shop, return here to progress the story when ready.")
		else:
			print("The Monastery is empty")
			self.endLevel()
		
	def wutaishenEntrance(self, player):
		self.getTitle("Wutaishen Entrance")
		player.setLocation(84)
		
		print("There is a street performer balancing on a rope. He begins to start juggling at the same time")
		print("Marvelous!")
		
	def courtyard(self, player):
		self.getTitle("Courtyard")
		player.setLocation(82)
		
		print("You arrive in the busy courtyard, people are returning after the chaos has cleared.")
		print("A traveling merchant has set up shop!")
			
		print(Fore.YELLOW + "Shopkeeper" + Fore.WHITE + ": Welcome to the traveling shop! How can I help you?")
		while True:
			print("\n\t-------Shop------\n\n\n[1] Purchase Wares\n[2] Sell Wares\n[3] Exit Shop")
			response = input("")
			if response == str(1):
				while True:
					print("\n\t-----------Purchasing----------\n\n\nYou have " + str(player.getGold()) + " gold.")
					print("[1] HP Potion - 2 Gold\n[2] SP Potion - 2 Gold\n[3] Air Katana [SKILL] - 5 Gold\n[4] Exit Menu")
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
						if (player.getGold() - 5) > 0:
							player.addGold(-5)
							player.addSkill("Air Katana")
							print(Style.BRIGHT + "\nYou purchased the Air Katana skill for 5 gold! You now have " + str(player.getGold()) + " gold remaining.")
							print(Style.BRIGHT + "The Air Katana skill summons a large air current in the form of a katana that slices through the enemy!")
							print(Style.BRIGHT + "It deals 20 - 24 damage and costs 10 SP")
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
		
	def barracks(self, player):
		self.getTitle("Barracks")
		player.setLocation(83)
		
		if self.status["barracks"] == 0:
			self.status["barracks"] = 1
			print("The barracks are full of rowdy soldiers. When you approach they all lower their heads in shame")
			print(Fore.YELLOW + "Soldier" + Fore.WHITE + ": We are terrible sorry we did not realize Master Wu was possessed.")
			print("\tWe have learned not to question Master Wu but we apologize deeply for attacking you.")
			
			print(Fore.YELLOW + "\nRagnar" + Fore.WHITE + ": They better be sorry, use some common sense people.")
		else:
			print("You can see that the barracks is packed with soldiers drinking and talking.")
		
	def housingDistrict(self, player):
		self.getTitle("Housing District")
		player.setLocation(81)
		
		print("The housing district is stunning, the architechure and design holds an ancient beauty.")
		print("People filter in and out of the neighborhoods and onto the exquisite parks connecting them")
		print("The Jinn truly have a wonderful city")
		