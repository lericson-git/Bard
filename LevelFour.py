from Enemy import Enemy
from Level import Level
from colorama import Fore, Back, Style, init
init() #start the colorama function
init(autoreset=True) #makes sure each line's settings are unique

class LevelFour(Level):
	status = {
	"spawn": 0,
	"noticeBoard": 0,
	"townSquare": 0,
	"colleseum": 0,
	"adventureShop": 0,
	"cityWall": 0,
	"alley": 0,
	"sjornnsPub": 0,
	"park": 0,
	"militiaHQ": 0
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
				self.spawn(player)
		if curLoc == 20:
			if dir == 18:
				self.spawn(player)
			if dir == 22:
				self.adventureShop(player)
			if dir == 23:
				self.cityWall(player)
			if dir == 24:
				self.alley(player)
		if curLoc == 21:
			if dir == 18:
				self.spawn(player)
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
				self.militiaHQ(player)
		if curLoc == 27:
			if dir == 26:
				self.park(player)
		
	def spawn(self, player):
		player.reset()
		player.setLocation(18)
		print(Fore.YELLOW + "\n\t----------------\n\tMedegroth Center\n\t----------------")
		
		if self.status["spawn"] == 0:
			self.status["spawn"] = 1
			print("As you enter Medegroth you are reminded of happy times with your friends")
			print("The city was always brimming with optimism and friendliness, yet now it is quiet")
			print("The gleaming of joy seems to have been replaced with anxiety, lets ask around for the band")
		else:
			print("Medegroth Square is usually packed, but it seems empty and quiet. Something is happening...")
			
	def noticeBoard(self, player):
		player.setLocation(19)
		self.status["noticeBoard"] = 1
		print(Fore.YELLOW + "\n\t------------\n\tNotice Board\n\t------------")
		
		print("As you approach the notice board you see at least twenty different missing posters, you read one\n")
		print("\t**************************")
		print("\tNOTICE: MISSING DOG")
		print("\tWhite Lab")
		print("\tSmall puppy")
		print("\tBlack spot over right eye")
		print("\tContact Ragnar for reward!")
		print("\t**************************\n")
		print("Maybe if I speak to the militia I can post my friends on the notice board...")
	
	def colleseum(self, player):
		player.setLocation(21)
		print(Fore.YELLOW + "\n\t---------\n\tColleseum\n\t---------")
		
		print("You cannot enter the building, a sign reads \"CLOSED TODAY\" and some posters are on the wall")
		
	def townSquare(self, player):
		player.setLocation(20)
		print(Fore.YELLOW + "\n\t-----------\n\tTown Square\n\t-----------")
		
		print("Large towering buildings surround a center with vendors and shops.")
		print("The square is busy, but not nearly as much as usual.")
		print("A sense of dread looms over the town, you get the chills")
		
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
						if (player.getGold() - 5) > -1:
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
		player.setLocation(23)
		print(Fore.YELLOW + "\n\t----------\n\tCity Wall\n\t----------")
		
		print("There is a soldier in tattered armor leaning against the city wall.")
		print(Fore.YELLOW + player.getName() + Fore.WHITE + ": Are you doing okay sir?")
		print("The man looks at you with a broken spirit, he looks desolate and distraught.")
		print(Fore.YELLOW + "Soldier" + Fore.WHITE + ": I've lost my son, nothing matters now...")
		print("The man covers his face with his helment and turns away.")
	
	def alley(self, player):
		player.setLocation(24)
		print(Fore.YELLOW + "\n\t-----\n\tAlley\n\t-----")
		
		if self.status["alley"] == 0:
			self.status["alley"] = 1
			print("As you enter the alleyway a drunk man approaches you and swings at you. He looks distraught and has tears on his face.")
			print(Fore.YELLOW + "Drunken Man" + Fore.WHITE + ": I feel like slugging one out! Ahahaha!")
			while True:
				print("Please choose an option:\n[1] Attack him\n[2] Subdue him")
				user = input("")
				if user != str(1) and user != str(2):
					print("That is not a valid input!")
				elif user == str(1):
					drunk = Enemy()
					drunk.setName("Drunken Man")
					self.fight(player, drunk)
					self.status["alley"] = 2
					print("The man falls to the floor, dead.")
					break
				elif user == str(2):
					print("After subduing the man a figure approaches, it is an older man")
					print(Fore.YELLOW + "Elder" + Fore.WHITE + ": I am so sorry about my son, he is terrible with alcohol! Thank you for not hurting him!")
					print("The man gives you 4 gold pieces for the trouble.")
					player.addGold(4)
					break
		elif self.status["alley"] == 1:
			print("The alleyway is deserted, there is nothing of importance here.")
		elif self.status["alley"] == 2:
			print("The body from the man you killed lies in the alleyway. Now there is a woman kneeled by it.")
			print(Fore.YELLOW + "Woman" + Fore.WHITE + ": How could this happen? He was still getting over the loss of his child...\n\t What monster would hurt a man who has already hurt so much.")
			self.status["alley"] = 3
		else:
			print("The woman lays sobbing next the the man's body...")
		
	def park(self, player):
		player.setLocation(26)
		print(Fore.YELLOW + "\n\t----\n\tPark\n\t----")
		
		if self.status["park"] != 2:
			self.status["park"] = 1
			while True:
				print("\nThere is a dog with a spotted eye and a leash attached running by itself.")
				user = input("Would you like to approach the dog? (Y/n)")
				if user.lower() == "y" and self.status["noticeBoard"] == 1:
					print("\nYou recognize the dog from the missing poster! You grab it's leash and take it with you.")
					self.status["park"] = 2
					break
				elif user.lower() == "y":
					print("\nThe dog runs off, maybe there is somewhere in town for missing posters. If the dog is posted we could turn it in for a reward, should look around first.")
					break
				elif user.lower() == "n":
					print("\nThe dog runs off and you continue to the park")
					print("The park has some families eating on the grass, but no sign of leads on my friends")
					break
				else:
					print("Not valid input!")
		else:
			print("The park has some families eating on the grass, but no sign of leads on my friends")
	
	def militiaHQ(self, player):
		player.setLocation(27)
		print(Fore.YELLOW + "\t----------\n\tMilitia HQ\n\t----------\n")
		
		print("You walk into a grand stone building. It has red banners on on either side of the door")
		print("It opens into a large feast hall and a man approaches you.")
		if self.status["park"] == 2 and self.status["militiaHQ"] != 1:
			print(Fore.YELLOW + "\nRagnar" + Fore.WHITE + ": You found my dog! Thank you so much, I will grant you this new ability in return.")
			print(Style.BRIGHT + "\nYou have gained the " + Fore.CYAN + "Trigram Jabs" + Fore.WHITE + " ability!")
			print(Style.BRIGHT + "This ability has a random chance to hit between 4 and 8 times. It deals 3 damage each hit.")
			player.addSkill("Trigram Jabs")
			self.status["militiaHQ"] = 1
		else:
			print(Fore.YELLOW + "\nRagnar" + Fore.WHITE + ": Any chance you seen my dog out there? I'm teaching whoever finds him my new fighting skill!")
		
		while True:
			user = input("\nRagnar offers you a room to stay in at the Militia HQ, would you like to take it? (Y or N, Advances to next level)")
			if user == "Y" or user == "y":
				print("Level Finished")
				self.levelStatus = False
				break
			elif user.lower() == "n":
				print("Returning to level")
				break
			else:
				print("Invalid input!")
							
							