from Enemy import Enemy
from colorama import Fore, Back, Style, init
init() #start the colorama function
init(autoreset=True) #makes sure each line's settings are unique

class Level():
	levelStatus = True

	def __init__(self):
		self.levelStatus = True
		
	def look(self, player):
		if player.getLocation() == 3 and self.status["yourTent"] != 2:
			print("Your " + Fore.CYAN + "shortsword" + Fore.WHITE + " lies on the ground next to your instruments")
			print(Fore.YELLOW + "HINT" + Fore.WHITE + " use the \"loot\" command with the keyword " + "\"" + Fore.CYAN + "shortsword" + Fore.WHITE + "\"")
		elif player.getLocation() == 2 and self.status["auraeTent"] != 2:
			print("A " + Fore.CYAN + "backpack" + Fore.WHITE + " lies on the ground of Aurae's tent")
		elif player.getLocation() == 6 and self.status["yourTent"] != 2:
			print("There might be something useful in your " + Fore.CYAN + "chest" + Fore.WHITE + "...")
		elif player.getLocation() == 6 and self.status["yourTent"] == 2:
			print("You have already retrieved everything there is here.")
		elif player.getLocation() == 8 and self.status["wolvesDen"] != 2:
			print("You can loot the " + Fore.CYAN + "werewolf" + Fore.WHITE + "'s body!")
		elif player.getLocation() == 9:
			print("There are clear marks of blood stains coming down from the north, probably should avoid that route...")
		elif player.getLocation() == 21: #colleseum
			print("There is a poster of a man named Ragnar, it reads:")
			print("Ragnar, the champion of the arena is holding a tournament tomorrow, 1 gold for admission!")
			print("Sounds like someone I need to talk to. Lets find Ragnar")
		elif player.getLocation() == 24 and self.status["alley"] == 2:
			print("The mans " + Fore.CYAN + "pockets" + Fore.WHITE + " can be looted")
		elif player.getLocation() == 29 and self.status["arenaOne"] == 1:
			print("The " + Fore.CYAN + "coins" + Fore.WHITE + " thrown onto the arena floor can be looted")
		elif player.getLocation() == 35 and self.status["clearing"] == 1:
			print("The " + Fore.CYAN + "bodies" + Fore.WHITE + " of the bandits can be looted")
		elif player.getLocation() == 36 and self.status["abandonedShack"] != 1:
			print("The " + Fore.CYAN + "floorboards" + Fore.WHITE + " of the shack seem raised. Maybe \nsomething is stuck beneaths them?")
		elif player.getLocation() == 40 and self.status["deepForest"] != 2:
			print("The " + Fore.CYAN + "bodies" + Fore.WHITE + " of the werewolves can be looted!")
		elif player.getLocation() == 43 and self.status["caveOne"] != 2:
			print("The " + Fore.CYAN + "bodies" + Fore.WHITE + " of the enemies can be looted!")
		elif player.getLocation() == 66 and self.status["hiddenAltar"] != 2:
			print("The " + Fore.CYAN + "chest" + Fore.WHITE + " can be looted.")
		elif player.getLocation() == 89 and self.status["cave"] != 2:
			print("The " + Fore.CYAN + "chest" + Fore.WHITE + " can be looted.")
		elif player.getLocation() == 99 and self.status["cave"] != 2:
			print("The " + Fore.CYAN + "soldiers" + Fore.WHITE + " can be looted.")
		elif player.getLocation() == 135 and self.status["oniCamp"] != 2:
			print("The " + Fore.CYAN + "tents" + Fore.WHITE + " can be looted.")
		else:
			print("Nothing special seems to be around here...")
		
	def loot(self, player, object):
		if player.getLocation() == 3:
			if object.lower() == "shortsword":
				print("You have acquired the shortsword weapon!")
				player.addWeapon("Shortsword")
				self.status["yourTent"] = 2
			else:
				print("Error, " + object + " cannot be found!")
		elif player.getLocation() == 2:
			if object == "backpack":
				player.addItem("HP Potion")
				print("You have gained one HP Potion!")
				self.status["auraeTent"] = 2
		elif player.getLocation() == 6 and self.status["yourTent"] != 2:
			if object.lower() == "chest":
				print("You loot the chest and receive one SP Potion!")
				player.addItem("SP Potion")
				self.status["yourTent"] = 2
			else:
				print("Error, " + object + " cannot be found!")
		elif player.getLocation() == 8 and self.status["wolvesDen"] != 2:
			if object.lower() == "werewolf":
				print("You loot the werewolf and receive one gold!")
				player.addGold(1)
				self.status["wolvesDen"] = 2
		elif player.getLocation() == 14 and self.status["ForestPath"] != 0:
			print("The " + Fore.CYAN + "bodies " + Fore.WHITE + "of the bandits can be searched for loot")
		elif player.getLocation() == 14 and self.status["ForestPath"] != 0:
			if object.lower() == "bodies":
				player.addItem("HP Potion")
				player.addGold(3)
				player.addWeapon("Bandit Dagger")
				print("You received 5 gold, an HP Potion, and a new weapon! The Bandit Dagger!")
			else:
				print("That object is not present or cannot be looted!")
		elif player.getLocation() == 24 and self.status["alley"] == 2:
			print("You loot the mans pockets, all he has is an empty wallet with nothing but a picture of a boy who is presumably his son.")
			self.status["alley"] = 3
		elif player.getLocation() == 29 and self.status["arenaOne"] == 1:
			if object == "coins":
				self.status["arenaOne"] = 2
				print("You loot the coins from the ground and gain two gold!")
				player.addGold(2)
			else:
				print("That object cannot be found")
		elif player.getLocation() == 35 and self.status["clearing"] == 1:
			if object == "bodies":
				self.status["clearing"] = 2
				print("You loot the bodies for 4 gold!")
				player.addGold(4)
			else:
				print("That object cannot be found")
		elif player.getLocation() == 36 and self.status["abandonedShack"] != 1:
			if object == "floorboards":
				self.status["abandonedShack"] = 21
				print("You pry apart the floorboards to find 2 HP Potions!")
				player.addItem("HP Potion")
				player.addItem("HP Potion")
				
			else:
				print("That object cannot be found")
		elif player.getLocation() == 40 and self.status["deepForest"] != 2:
			if object == "bodies":
				self.status["deepForest"] = 2
				print("You loot the pockets of the bodies and find an HP Potion!")
				player.addItem("HP Potion")
				
			else:
				print("That object cannot be found")
		elif player.getLocation() == 43 and self.status["caveOne"] != 2:
			if object == "bodies":
				self.status["caveOne"] = 2
				print("You loot the pockets of the bodies and find an SP Potion!")
				player.addItem("SP Potion")
				
			else:
				print("That object cannot be found")
		elif player.getLocation() == 66 and self.status["hiddenAltar"] != 2:
			if object == "chest":
				self.status["hiddenAltar"] = 2
				print("You loot the treasure chest and receive 4 gold!")
				player.addGold(4)
			else:
				print("That object cannot be found")
		elif player.getLocation() == 89 and self.status["cave"] != 2:
			if object == "chest":
				self.status["cave"] = 2
				print("You loot the chest and receive 4 gold!")
				player.addGold(4)
			else:
				print("That object cannot be found")
		elif player.getLocation() == 99 and self.status["cave"] != 2:
			if object == "soldiers":
				self.status["cave"] = 2
				print("You search the soldiers and receive an HP and SP Potion!")
				player.addItem("HP Potion") 
				player.addItem("SP Potion")
			else:
				print("That object cannot be found")
		elif player.getLocation() == 135 and self.status["oniCamp"] != 2:
			if object == "tents":
				self.status["oniCamp"] = 2
				print("You search the tents and find two HP and two SP Potions!")
				player.addItem("HP Potion")
				player.addItem("HP Potion")
				player.addItem("SP Potion")
				player.addItem("SP Potion")
			else:
				print("That object cannot be found")
		else:
			print("There is nothing to loot here...")
		
	def spawn(self, player):
		pass
		
	def endLevel(self):
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
		
	def reset(self, player, status):
		player.setHP(player.getTotalHP())
		player.setSP(player.getTotalSP())
		for room in status:
			status[room] = 0
		
	def isRunning(self):
		if self.levelStatus == True:
			return True
		else:
			return False
			
	def getStatus(self):
		return self.status
	
	def getTitle(self, name):
		sum = 0
		for ch in name:
			sum = sum + 1
		print(Fore.YELLOW + "\n\t", end = "")
		for i in range(sum):
			print(Fore.YELLOW + "-", end = "")
		print(Fore.YELLOW + "\n\t" + name)
		print(Fore.YELLOW + "\t", end = "")
		for i in range(sum):
			print(Fore.YELLOW + "-", end = "")
		print("\n")
		
	def fight(self, player, enemy):
		print("\n-----------------------------------------------------------------------")
		print("\t\t" + Fore.GREEN + player.getName() + Fore.WHITE + " vs. " + Fore.RED + enemy.getName())
		turnCount = 0
		while True:
			if player.getHP() > 0:
				print("Status:")
				player.getStatus() #Displays HP and SP
				print("\nEnemy Status:")
				enemy.getStatus() #Displays enemy HP and SP
				print("\nChoose an action")
				action = input(("[1] Use Weapon\n[2] Use Skill\n[3] Use Item\n" + player.getName() + ": "))
				if enemy.getSP() == -1337: #Code to check if demon fight is over
					print("The Demon lands on you and strangles you with his brute strength")
					print("You fall hard to the floor and everything fades to black.")
					print("You grasp onto hope that you might survive, and lose consciousness")
					break
				if action == "1" and player.getWeapons(""):
					while True:
						weaponID = input(player.getName() + ": ")
						if not weaponID.isdigit() or int(weaponID) > player.getNumWeapons():
							print("Invalid input! Try again.")
						else:
							weaponID = int(weaponID)
							player.useWeapon(weaponID, enemy)
							break
				elif action == "2" and player.getSkills():
					while True:
						skillID = input(player.getName() + ": ")
						if not skillID.isdigit() or int(skillID) > player.getNumSkills():
							print("Invalid input! Try again.")
						else:
							skillID = int(skillID) #Maybe add player name like other commands
							player.useSkill(skillID, enemy)
							break
				elif action == "3" and player.getItems(""):
					itemID = int(input(""))
					player.useItem(itemID)
				else:
					print("Invalid input!")
				if enemy.getHP() <= 0:
					print("\n" + Style.BRIGHT + Fore.RED + enemy.getName() + Fore.WHITE + " is defeated!")
					break
				
				print("\n-----------------------------------------------------------------------")
				if enemy.getHP() > 0:
					if action == 3 and player.getItems("") == True:
						enemy.fight(player)
					elif action != 3:
						enemy.fight(player)
					else:
						print("You have no items")
			else:
				break