#Player Class
import re
import random
from colorama import Fore, Back, Style, init
init() #start the colorama function
init(autoreset=True) #makes sure each line's settings are unique

class Player:
	weapons = []
	hp = 0
	sp = 0
	totalHP = 0
	totalSP = 0
	name = ""
	location = 0
	skills = []
	items = { "HP Potion": 0, "SP Potion": 0 }
	gold = 0
	
	def __init__(self):
		self.hp = 50
		self.sp = 50
		self.totalHP = 50
		self.totalSP = 50
		self.weapons.append("Fists")
		self.skills.append("Lute Smash")
		self.gold = 10
		
	def reset(self):
		self.hp = self.totalHP
		self.sp = self.totalSP
		
	def setHP(self, value):
		self.hp = value
		
	def setSP(self, value):
		self.sp = value
		
	def setTotalHP(self, value):
		self.totalHP = value
		
	def setTotalSP(self, value):
		self.totalSP = value
		
	def getHP(self):
		return self.hp
		
	def getSP(self):
		return self.sp
		
	def getTotalHP(self):
		return self.totalHP
		
	def getTotalSP(self):
		return self.totalSP
		
	def getLocation(self):
		return self.location
		
	def setLocation(self, num):
		self.location = num
		
	def setName(self, name):
		self.name = name
		
	def getName(self):
		return self.name
		
	def getNumWeapons(self):
		return len(self.weapons)
		
	def getNumSkills(self):
		return len(self.skills)
		
	def addGold(self, num):
		self.gold = self.gold + num
		
	def getGold(self):
		return self.gold
		
	def getWeapons(self, flag):
		count = 0
		print("\nWeapons:")
		if len(self.weapons) > 0:
			for weapon in self.weapons:
				print("[" + str(count + 1) + "]" + self.weapons[count])
				count = count + 1
			return True
		else:
			print("You have no weapons")
			return False
			
	def addWeapon(self, weapon):
		self.weapons.append(weapon)
		
	def useWeapon(self, weaponID, enemy):
		weapon = self.weapons[weaponID - 1]
		if weapon == "Shortsword":
			enemy.setHP(enemy.getHP() - 5)
			print(Fore.GREEN + "You thrust at " + enemy.getName() + " with your shortsword, it deals 5 damage.")
		elif weapon == "Fists":
			enemy.setHP(enemy.getHP() - 2)
			print(Fore.GREEN + "You attack " + enemy.getName() + " with your bare fists. It deals 2 damage.")
		elif weapon == "Bandit Dagger":
			enemy.setHP(enemy.getHP() - 8)
			print(Fore.GREEN + "You slash at " + enemy.getName() + " with the Bandit Dagger. It deals 8 damage!")
		elif weapon == "Dual Blades":
			enemy.setHP(enemy.getHP() - 12)
			print(Fore.GREEN + "You spin in the air flashing your dual blades, you slash " + enemy.getName() + " for 12 damage!")
		elif weapon == "Runic Bow":
			enemy.setHP(enemy.getHP() - 18)
			print(Fore.GREEN + "The Nymph runes on your bow glow white as it summons a magical arrow and flies into " + enemy.getName() + " for 18 damage!")
			
			
	def addSkill(self, skillName):
		self.skills.append(skillName)
			
	def useSkill(self, skillID, enemy):
		skill = self.skills[skillID - 1]
		if skill == "Lute Smash": #Attacks with loot for 7 damage and costs 5 SP
			if self.getSP() > 4:
				enemy.setHP(enemy.getHP() - 7)
				self.setSP(self.getSP() - 5)
				print(Fore.GREEN + "You use 5 SP to smash " + enemy.getName() + " with your lute, it deals 7 damage")
			else:
				print(Fore.YELLOW + Style.BRIGHT + "You do not have enough SP for that!")
		elif skill == "Trigram Jabs": #Attacks randomly between 4 and 8 times for 3 damage each for 8 SP
			if self.getSP() > 7:
				num = random.randint(4, 8)
				damage = num * 3
				enemy.setHP(enemy.getHP() - damage)
				self.setSP(self.getSP() - 8)
				print(Fore.GREEN + "You use 8 SP to quickly jab " + enemy.getName() + " " + str(num) + " times for " + str(damage) + " damage")
			else:
				print(Fore.YELLOW + Style.BRIGHT + "You do not have enough SP for that spell!")
		elif skill == "Fairy Beam":
			if self.getSP() > 0:
				if enemy.getTotalHP() > 30:
					enemy.setHP(enemy.getHP() - 30)
					print(Fore.GREEN + "You use all of your SP to deliver a 30 damage beam at the enemy!")
				else:
					enemy.setHP(enemy.getHP() - enemy.getTotalHP())
					print(Fore.GREEN + "You use all of your SP to take all of the enemies HP!\nYou fire a beam of purple fairy energy killing the enemy!")
				self.setSP(0)
			else:
				print(Fore.YELLOW + Style.BRIGHT + "You do not have enough SP to do that!")
		elif skill == "Air Katana":
			if self.getSP() > 9:
				self.setSP(self.getSP() - 10)
				print(Fore.GREEN + "You use 10 SP to cast Air Katana! A huge air current slashes through the enemy!")
				num = random.randint(20, 24)
				print(Fore.GREEN + "It deals " + str(num) + " damage!")
				enemy.setHP(enemy.getHP() - num)
			else:
				print(Fore.YELLOW + Style.BRIGHT + "You do not have enough SP to do that!")
		elif skill == "Entangling of Blessings":
			if self.getSP() > 15:
				self.setSP(self.getSP() - 15)
				print(Fore.GREEN + "You use 15 SP to cast Entangling of Blessings! The enemy is wrapped in magical vines that absorb their power!")
				num = random.randint(40, 50)
				print(Fore.GREEN + "It deals " + str(num) + " damage!")
				enemy.setHP(enemy.getHP() - num)
			else:
				print(Fore.YELLOW + Style.BRIGHT + "You do not have enough SP to do that!")
			
	def getSkills(self):
		count = 0
		if len(self.skills) > 0:
			for skill in self.skills:
				print("[" + str(count + 1) + "]" + self.skills[count])
				count = count + 1
			return True
		else:
			print("You have no skills")
			return False
			
	def getItems(self, flag):
		count = 0
		if len(self.items) > 0:
			for item, quantity in self.items.items():
				print("[" + str(count + 1) + "]" + item + " x" + str(quantity))
				count = count + 1
			if flag == "shop":
				for weapon in self.weapons:
					print(weapon)
			return True
		else:
			return False
			
	def getPrice(self, item):
		value = 0
		if item == "HP Potion":
			value = 0.5
		elif item == "SP Potion":
			value = 0.5
		elif item == "Shortsword":
			value = 0.5
		elif item == "Bandit Dagger":
			value = 1
		elif item == "Dual Blades":
			value = 3
		return value
			
	def sellItems(self):
		count = 0
		while True:
			print("\t--------Selling-------\n\nYou have " + str(self.getGold()) + " gold")
			print("[1] HP Potion - " + str(self.getPrice("HP Potion")) + " gold")
			print("[2] SP Potion - " + str(self.getPrice("SP Potion")) + " gold")
			print("[3] Shortsword - " + str(self.getPrice("Shortsword")) + " gold")
			print("[4] Bandit Dagger - " + str(self.getPrice("Bandit Dagger")) + " gold")
			print("[5] Dual Blades - " + str(self.getPrice("Dual Blades")) + " gold")
			print("[6] Exit ")
			count = 0
			user = input("")
			user = int(user)
			if user == 1 and self.items["HP Potion"] > 0:
				print("You sold one HP Potion for " + str(self.getPrice("HP Potion")) + " gold")
				self.addGold(self.getPrice("HP Potion"))
				self.items["HP Potion"] = self.items["HP Potion"] - 1
			elif user == 2 and self.items["SP Potion"] > 0:
				print("You sold one SP Potion for " + str(self.getPrice("HP Potion"))  + " gold")
				self.addGold(self.getPrice("SP Potion"))
				self.items["SP Potion"] = self.items["SP Potion"] - 1
			elif user == 3 and "Shortsword" in self.weapons:
				print("You sold Shortsword for " + str(self.getPrice("HP Potion")) + " gold")
				self.addGold(self.getPrice("Shortsword"))
				self.removeWeapon("Shortsword")
			elif user == 4 and "Bandit Dagger" in self.weapons == True:
				print("You sold Bandit Dagger for " + str(self.getPrice("HP Potion")) + " gold")
				self.addGold(self.getPrice("Bandit Dagger"))
				self.removeWeapon("Bandit Dagger")
			elif user == 5 and "Dual Blades" in self.weapons == True:
				print("You sold Dual Blades for " + str(self.getPrice("HP Potion")) + " gold")
				self.addGold(self.getPrice("Dual Blades"))
				self.removeWeapon("Dual Blades")
			elif user == 6:
				break
			else:
				print("\n\nYou either do not have that item or did not input valid information! Try again!")
			print("\n")
			
	def useItem(self, item):
		item = int(item)
		if item == 1 and self.items["HP Potion"] > 0:
			self.items["HP Potion"] = self.items["HP Potion"] - 1
			if self.getHP() + 50 < self.getTotalHP():
				self.setHP(self.getHP() + 50)
			else:
				self.setHP(self.getTotalHP())
			print("You used an HP Potion, it restores 25 health\nYou now have " + str(self.getHP()) + " HP.")
		elif item == 2 and self.items["SP Potion"] > 0:
			self.items["SP Potion"] = self.items["SP Potion"] - 1
			self.setSP(self.getSP() + 50)
			print("You used an SP Potion, it restored 50 SP")
		else:
			print("You do not have any of that item!")
			
	def addItem(self, item):
		self.items[item] = self.items[item] + 1
		
	def removeWeapon(self, weapon):
		self.weapons.remove(weapon)
			
	def getStatus(self):
		print(Fore.RED + Style.BRIGHT + "HP: " + str(self.getHP()) + " / " + str(self.getTotalHP()))
		print(Fore.CYAN + Style.BRIGHT + "SP: " + str(self.getSP()) + " / " + str(self.getTotalSP()))