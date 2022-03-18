from Enemy import Enemy
from Level import Level
from colorama import Fore, Back, Style, init
init() #start the colorama function
init(autoreset=True) #makes sure each line's settings are unique

class LevelEighteen(Level):
	status = {
	"spawn": 0,
	"gardens": 0,
	"shop": 0,
	"priestTemple": 0,
	"feastHall": 0,
	}
	
	levelStatus = True
	
	def __init__(self):
		self.levelStatus = True
		
	def move(self, curLoc, dir, player):
		if curLoc == 108:
			if dir == 109:
				self.gardens(player)
		if curLoc == 109:
			if dir == 108:
				self.spawn(player)
			if dir == 110:
				self.shop(player)
			if dir == 111:
				self.priestTemple(player)
			if dir == 112:
				self.feastHall(player)
		if curLoc == 110:
			if dir == 109:
				self.gardens(player)
		if curLoc == 111:
			if dir == 109:
				self.gardens(player)
		if curLoc == 112:
			if dir == 109:
				self.gardens(player)
				
		
	def spawn(self, player):
		self.getTitle("Spawn")
		player.reset()
		player.setLocation(108)
		
		if self.status["spawn"] == 0:
			self.status["spawn"] = 1
			print("Your party enters the gates of Tiryns, it opens into a huge botanical city, \nbeautifully created from ancient trees and flowers.")
			print(Fore.YELLOW + "Master Wu" + Fore.WHITE + ": Let's rest up and restock at a shop and then we can get help from the Nymphs")
		else:
			print("The booming city gates are a massive waterfall that is split by Nymph technology to allow you through.\nIt is a remarkable sight.")
	
	def gardens(self, player):
		self.getTitle("Gardens")
		player.setLocation(109)
		
		print("The city gardens are breath taking, they have flowers as tall as mammoths and glowing trees, \nmassive sculptures of interwoven trees like you've never seen.")
		
		if self.status["gardens"] == 0:
			self.status["gardens"] = 1
			print(Fore.YELLOW + "Ragnar" + Fore.WHITE + ": This place is more beautiful than any girl I've ever dated! Ahaha!")
			print(Fore.YELLOW + "Master Wu" + Fore.WHITE + ": It makes the heart happy to see nature in such a beautiful state.")
			
			
	def shop(self, player):
		self.getTitle("Shop")
		player.setLocation(110)
		
		print(Fore.YELLOW + "Shopkeeper" + Fore.WHITE + ": Welcome to Tiryns traveller! How can I help you?")
		while True:
			print("\n\t-------Shop------\n\n\n[1] Purchase Wares\n[2] Sell Wares\n[3] Exit Shop")
			response = input("")
			if response == str(1):
				while True:
					print("\n\t-----------Purchasing----------\n\n\nYou have " + str(player.getGold()) + " gold.")
					print("[1] HP Potion - 2 Gold\n[2] SP Potion - 2 Gold\n[3] Runic Bow - 6 Gold\n[4] Exit Menu")
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
						if (player.getGold() - 6) > 0:
							player.addGold(-6)
							player.addWeapon("Runic Bow")
							print(Style.BRIGHT + "\nYou purchased the Runic Bow for 6 gold! You now have " + str(player.getGold()) + " gold remaining.")
							print(Style.BRIGHT + "The Runic Bow is carved from ancient world trees and enchanted with Nymph magic, it summons it's own arrows\nthat absorb natures nutrients, it deals 18 damage!")
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
		
	def priestTemple(self, player):
		self.getTitle("Priest Temple")
		player.setLocation(111)
		
		if self.status["priestTemple"] == 0:
			self.status["priestTemple"] = 1
			print("Your party enters an age old priest temple, you are greeted by a priestess.")
			print(Fore.YELLOW + "Nefeli" + Fore.WHITE + ": I am Great Priestess Nefeli, the kingdom knows of you're arrival and we want to help your cause.")
			print("\tI will share with you one of our most affective magics against demons.")
			print("\tThis spell is called Entangling of Blessings, it summons vines that wrap up the demon and through deep magic\n\tinterwoven into world trees it saps their strength.")
			print("\tNo foreigner has ever been tought this magic, but we know of your hidden power, how you healed Master Wu, \n\thow you survived the Demon attack.")
			print("\tThese demons were artifically created by a cult fanatic through chemistry, that man was \n\tyour father. He trialed experiments on both you and your brother as toddlers.")
			print("\tYour brother turned into a full fledged demon and has spread through \n\tlands increasing his numbers by turning innocent humans into them.")
			print("\tYou were placed in foster care and were too young to remember, but it \n\tseems the trials your father ran gave you the power to heal these demons.")
			print("\tHead to the feast hall, our king is there and is waiting for your arrival.")
			player.addSkill("Entangling of Blessings")
			print("\n" + Style.BRIGHT + "You learned the skill Entangling of Blessings! It costs 15 SP and deals between 40-50 damage to the target!")
		else:
			print("The priest temple is beautiful and channels magical energy to illuminate the temple with a beautiful golden light.")
			print(Fore.YELLOW + "Nefeli" + Fore.WHITE + ": Visit the king when you get the chance, he is at the feast hall to the west.")
			
	def feastHall(self, player):
		self.getTitle("Feast Hall")
		player.setLocation(112)
		
		if self.status["feastHall"] == 0:
			self.status["feastHall"] = 1
			print("Your party enters a raised treehouse building, you walk on woven tree branches up the stairs")
			print("A guard approaches and greets you")
			print(Fore.YELLOW + "Guard" + Fore.WHITE + ": We have been expecting you, please come with me to the king")
			print("You follow the guard to a golden chamber covered in glowing runes and riddled with battle plans.")
			print(Fore.YELLOW + "Apaethos" + Fore.WHITE + ": Hello " + player.getName() + " I am greatly pleased as to your arrival\n\tYou're power will be the key to defeating the demons.")
			print("\tWe want to save the demons, bring them back to their human selves that your brother stole from them. \n\tYou have that ability")
			print("\tWe can use a world tree to channel your magic and purify the whole demon population, are you with me?")
			print(Fore.YELLOW + player.getName() + Fore.WHITE + ": I have never agreed more, let's do this.")
		else:
			print("The feast hall chamber is empty right now, the king must have left.")
	
		self.endLevel()