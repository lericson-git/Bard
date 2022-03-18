from colorama import Fore, Back, Style, init
import random
init() #start the colorama function
init(autoreset=True) #makes sure each line's settings are unique
weapon = ""
hp = 0
sp = 0
totalHP = 50
totalSP = 50


class Enemy:
	name = ""

	def __init__(self):
		self.hp = 15
		self.sp = 10
		self.totalHP = 15
		self.totalSP = 10
		
	def getHP(self):
		return self.hp
		
	def setHP(self, health):
		self.hp = health
		
	def getSP(self):
		return self.sp
		
	def setSP(self, value):
		self.sp = value
		
	def getName(self):
		return self.name
	
	def setName(self, name):
		self.name = name
		
	def setTotalHP(self, value):
		self.totalHP = value
		
	def setTotalSP(self, value):
		self.totalSP = value
		
	def getTotalHP(self):
		return self.totalHP
		
	def getTotalSP(self):
		return self.totalSP
		
	def getStatus(self):
		print(Fore.RED + Style.BRIGHT + self.getName() + " HP: " + str(self.getHP()) + " / " + str(self.getTotalHP()))
		#print(Fore.CYAN + Style.BRIGHT + self.getName() + " SP: " + str(self.getSP()) + " / " + str(self.getTotalSP()))
		
	def fight(self, player):
		if self.getName() == "Miyaji": #Miyaji Enemy
			print(Fore.RED + "\nMiyaji whirls around and whips you in the face with a roundhouse kick!")
			print(Fore.RED + "The kick deals 5 damage!")
			player.setHP(player.getHP() - 5)
		elif self.getName() == "Wolf": #Wolf Enemy
			print(Fore.RED + "\nThe wolf ferociously sinks it's teeth into your leg!")
			print(Fore.RED + "The bite deals 5 damage!")
			player.setHP(player.getHP() - 5)
		elif self.getName() == "Werewolf": #Werewolf Enemy
			attack = random.randint(0, 2)
			if attack == 0:
				print(Fore.RED + "The werewolf picks you up and slams you to the ground!")
				print(Fore.RED + "The slam deals 10 damage!")
				player.setHP(player.getHP() - 10)
			elif attack == 1:
				print(Fore.RED + "The werewolf lunges and swipes at your torso!")
				print(Fore.RED + "The swipe deals 6 damage!")
				player.setHP(player.getHP() - 6)
			else:
				print(Fore.RED + "The werewolf bites a chunk out of your shoulder!")
				print(Fore.RED + "The bite deals 8 damage!")
				player.setHP(player.getHP() - 8)
		elif self.getName() == "Bandit": #Bandit Enemy
			attack = random.randint(0, 1)
			if attack == 0:
				print(Fore.RED + "The bandit slashes at you with a knife!")
				print(Fore.RED + "The swipe deals 8 damage!")
				player.setHP(player.getHP() - 8)
			elif attack == 1:
				print(Fore.RED + "The bandit chucks a throwing dagger at you!")
				print(Fore.RED + "It deals 4 damage!")
				player.setHP(player.getHP() - 4)
		elif self.getName() == "Drunken Man": #Drunken Man Enemy
			self.setTotalHP(25)
			self.setHP(25)
			attack = random.randint(0, 1)
			if attack == 0:
				print(Fore.RED + "The Drunken Man swings an uppercut at you!\nIt deals 10 damage!")
				player.setHP(player.getHP() - 10)
			elif attack == 1:
				print(Fore.RED + "The Drunken Man runs at you and dropkicks you!\nIt deals 14 damage!")
				player.setHP(player.getHP() - 14)
		elif self.getName() == "Tiger": #Tiger enemy
			attack = random.randint(0, 4)
			if attack == 0 or attack == 1:
				print(Fore.RED + "The Tiger lunges at you and swipes its immense claws, it shreds through your apparel and deals 15 damage!")
				player.setHP(player.getHP() - 15)
			if attack == 2:
				print(Fore.RED + "The Tiger attempts to bite you but you barely dodge it! You take no damage!")
			if attack == 3 or attack == 4:
				print(Fore.RED + "The Tiger sinks it's jaw into your ankle and drags you until you break free. It deals 10 damage!")
				player.setHP(player.getHP() - 10)
		elif self.getName() == "Gladiator": #Gladiator Enemy
			attack = random.randint(0, 2)
			if attack == 0:
				print(Fore.RED + "The Gladiator drops his shoulder and rushes you, he collides with intense power\nIt deals 13 damage!")
				player.setHP(player.getHP() - 13)
			elif attack == 1:
				print(Fore.RED + "The Gladiator grabs your head and headbutts you with no hesitation.\nIt deals 10 damage!")
				player.setHP(player.getHP() - 10)
			else:
				print(Fore.RED + "The Gladiator sneaks a quick slash with a dagger in, you manage to dodge it but still get scraped.\nIt deals 6 damage!")
				player.setHP(player.getHP() - 6)
		elif self.getName() == "Demon": #Demon Enemy
			if player.getLocation() < 100:
				if (player.getHP() - 40) < 1:
					self.setSP(-1337)
			attack = random.randint(0, 2)
			if attack == 0:
				print(Fore.RED + "The Demon swoops at you with his wings and sends you flying. You collide with the ground hard!\nIt deals 25 damage!")
				player.setHP(player.getHP() - 25)
			elif attack == 1:
				print(Fore.RED + "The Demon summons an orb of fire and casts it at you, it singes your body dealing 18 damage!")
				player.setHP(player.getHP() - 18)
			elif attack == 2:
				print(Fore.RED + "The Demon launches a red scythe at you like a boomerang, it cuts along your shoulder dealing 23 damage!")
				player.setHP(player.getHP() - 23)
		elif self.getName() == "Yaoguai": #Yaoguai Enemy
			attack = random.randint(0, 2)
			if attack == 0:
				print(Fore.RED + "The Yaoguai emits a freezing breath that freezes your nerves.\nIt deals 14 damage!")
				player.setHP(player.getHP() - 14)
			elif attack == 1:
				print(Fore.RED + "The Yaoguai hurls ice at you!\nIt deals 10 damage!")
				player.setHP(player.getHP() - 10)
			elif attack == 2:
				print(Fore.RED + "The Yaoguai uses a spell to heal himself!\nIt heals 10 HP.")
				if self.getHP() > 30:
					self.setHP(40)
				else:
					self.setHP(self.getHP() + 10)
		elif self.getName() == "Jinn": #Jinn Enemy
			attack = random.randint(0, 2)
			if attack == 0:
				print(Fore.RED + "The Jinn soldier smacks you with the butt of his sword\nIt deals 15 damage!")
				player.setHP(player.getHP() - 15)
			elif attack == 1:
				print(Fore.RED + "The Jinn fires an orb of wind energy at you\nIt misses you!")
			elif attack == 2:
				print(Fore.RED + "The Jinn soldier dashes at you slamming his palms into your gut.\nIt deals 17 damage!")
				player.setHP(player.getHP() - 17)
		elif self.getName() == "Oni": #Oni Enemy
			attack = random.randint(0, 2)
			if attack == 0:
				print(Fore.RED + "The Oni soldier summons roots trapping your feet, you can't move!\nHe charges you and slashes your side!\nIt deals 15 damage!")
				player.setHP(player.getHP() - 15)
			elif attack == 1:
				print(Fore.RED + "The Oni cloaks his sword in fire and strikes! It deals 16 damage!")
				player.setHP(player.getHP() - 16)
			elif attack == 2:
				print(Fore.RED + "The Oni and you clash blades, you block his strike but he stomps your leg!\nIt deals 17 damage!")
				player.setHP(player.getHP() - 17)
		elif self.getName() == "Ymir Bandit": #Ymir Bandit Enemy
			attack = random.randint(0, 1)
			if attack == 0:
				print(Fore.RED + "The bandit slashes at you with a knife!")
				print(Fore.RED + "The swipe deals 17 damage!")
				player.setHP(player.getHP() - 17)
			elif attack == 1:
				print(Fore.RED + "The bandit chucks a throwing dagger at you!")
				print(Fore.RED + "It deals 19 damage!")
				player.setHP(player.getHP() - 19)
		elif self.getName() == "Ymir": #Ymir Boss Enemy
			attack = random.randint(0, 1)
			if attack == 0:
				print(Fore.RED + "Ymir emulates a light from his chestplate, it shoots out and cuts you!")
				print(Fore.RED + "The swipe deals 17 damage!")
				player.setHP(player.getHP() - 17)
			elif attack == 1:
				print(Fore.RED + "Ymir pulls out a mace and slams it into your armor!")
				print(Fore.RED + "It deals 19 damage!")
				player.setHP(player.getHP() - 19)
		elif self.getName() == "Ymir": #Pirate Enemy
			attack = random.randint(0, 1)
			if attack == 0:
				print(Fore.RED + "The Pirate slashes at you with his cutlass!")
				print(Fore.RED + "The swipe deals 17 damage!")
				player.setHP(player.getHP() - 17)
			elif attack == 1:
				print(Fore.RED + "The Pirate pulls out a flintlock pistol and fires! It grazes you!")
				print(Fore.RED + "It deals 19 damage!")
				player.setHP(player.getHP() - 19)
		elif self.getName() == "Fairy": #Fairy Enemy
			attack = random.randint(0, 1)
			if attack == 0:
				print(Fore.RED + "The Fairy magically pulls the surrounding leaves and shoots them at you!")
				print(Fore.RED + "They pierce you and deal 17 damage!")
				player.setHP(player.getHP() - 17)
			elif attack == 1:
				print(Fore.RED + "The Fairy launches pixie dust at you!")
				print(Fore.RED + "It deals 19 damage!")
				player.setHP(player.getHP() - 19)
		elif self.getName() == "Morfix": #Morifx, final boss
			attack = random.randint(0, 4)
			if attack == 0:
				print(Fore.RED + "Morfix swoops in with his huge demonic wings and slams into you!")
				print(Fore.RED + "It deals 20 damage!")
				player.setHP(player.getHP() - 20) 
			elif attack == 1:
				print(Fore.RED + "Morfix fires an orb of raw demon energy at you!")
				print(Fore.RED + "Right before it hits Apaethos blocks it with a magical ward!")
			elif attack == 2:
				print(Fore.RED + "Morfix summons a demonic whip and catches your ankle, it sears your skin!")
				print(Fore.RED + "It deals 19 damage!")
				player.setHP(player.getHP() - 19)
			elif attack == 3:
				print(Fore.RED + "Morfix bends the lava from the volcano top and whirls it at you!")
				print(Fore.RED + "It deals 22 damage!")
				player.setHP(player.getHP() - 22)
			elif attack == 4:
				print(Fore.RED + "Morfix grabs you and flies into the air holding you, then he whips around and body slams you!")
				print(Fore.RED + "It deals 25 damage!")
				player.setHP(player.getHP() - 25)