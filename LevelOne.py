from Enemy import Enemy
from Level import Level
from colorama import Fore, Back, Style, init
init() #start the colorama function
init(autoreset=True) #makes sure each line's settings are unique

class LevelOne(Level):
	status = {
	"spawn": 0,
	"agrippaTent": 0,
	"miyajiTent": 0,
	"auraeTent": 0,
	"yourTent": 0
	}
	
	levelStatus = True
	
	def __init__(self):
		self.levelStatus = True
		
	def spawn(self, player):
		player.setLocation(0)
		print(Fore.YELLOW + "\t----------\n\tCampground\n\t----------")
		
		introString = ("\nYour name is " + player.getName() + ". You have lived your life peacefully as a bard and while you" +
		"\nwere born with the ability to bend, you have never trained it for combat. \nTo discover your past explore your tent and then visit the others" + 
		"\nYou are currently camping with your friends who you have spent many years with as bards. Catch up with them\n" +
		"to learn more about their backgrounds. To look at options of where to move, type \"directions\", \nand to move to a new location type a direction, e.g. \"North\"" + "\n" + Fore.YELLOW + "HINT: " + Fore.WHITE + "Use the \"help\" command for list of commands")
		
		revisitString = ("The center of camp, just a campfire with everyone's surrounding tents. Nothing much happening here.")
		
		if self.status["spawn"] == 1:
			print(revisitString)
		else:
			print(introString)
			self.status["spawn"] = 1
		
	def miyajiTent(self, player):
		player.setLocation(1)
		print(Fore.YELLOW + "\t-------------\n\tMiyaji's Tent\n\t-------------")
		if self.status["miyajiTent"] == 0:
			self.status["miyajiTent"] = 1
			print(Fore.YELLOW + "Miyaji:" + Fore.WHITE + " Hello " + player.getName() + ", I hope you are doing well today.")
			print("\tWe've come so far this band, I still remember by days in the Jinn capital of Wutaishen")
			print("\tMy people were dedicated to the forces and spirits that control this world, we always heed their ways.")
			print("\tI believe you will accomplish great things one day " + player.getName() + ", you will face many dangers too.")
			print("\tCome fight me! You will need the experience soon enough...")
			self.miyajiFight(player)
			print(Fore.YELLOW + "Miyaji: " + Fore.WHITE + "Good fighting " + player.getName() + ", you fight well for a bard! Go visit your tent if haven't already, it has your gear. ")
			print("\tAlso make sure you visit all three of the band members tents before we call it a night!")
		elif self.status["miyajiTent"] == 1:
			print("Miyaji seems to have called it a night, best to find somewhere else to go")
	
	def auraeTent(self, player):
		player.setLocation(2)
		print(Fore.YELLOW + "\t-------------\n\tAurae's Tent\n\t-------------")
		if self.status["auraeTent"] == 0:
			self.status["auraTent"] = 1
			print(Fore.YELLOW + "Aurae: " + Fore.WHITE + "Greetings " + player.getName() + "! I assume you wanted to learn about my past. I still remember it so clearly...")
			print("\tI am a nymph so I am sworn to protect and serve this earth, we are but a part of the much larger whole. \n\tNever forget that there are powers greater than you!")
			print("\tLet's test your scavenging skills... Search that backpack on the floor!")
		elif self.status["auraeTent"] == 1:
			print("Aurae has gone to bed, best not to disturb her")
			
	def agrippaTent(self, player):
		player.setLocation(4)
		print(Fore.YELLOW + "\t--------------\n\tAgrippa's Tent\n\t--------------")
		if self.status["agrippaTent"] == 0:
			self.status["agrippaTent"] = 1
			print(Fore.YELLOW + "Agrippa: " + Fore.WHITE + "Hey " + player.getName() + ", how you doing? I heard you talking about your past earlier, mine is very dark.")
			print("\tI'm a Shul, the people of ash. We live in volcanoes and take respite in heat, our kind has been locked \n\tin eternal combat with dark creatures of our lands; even demons.")
			print("\tI chose this life of music to escape the pain, I am thankful for this group and our joy.")
		elif self.status["agrippaTent"] == 1:
			print("Agrippa has gone to sleep for the night, best to follow suit")
	
	def yourTent(self, player):
		player.setLocation(3)
		print(Fore.YELLOW + "\t---------\n\tYour Tent\n\t---------")
		
		if self.status["yourTent"] == 0:
			self.status["yourTent"] = 1
			print("You enter your tent, it is simple and messy, instruments, maps, and miscellaneous items are laying all over the place.")
			print("It reminds you of how far you've come. From when you were seperated from your brother at the orphanage, to the bard college, to this camping trip with your band.")
			print("You find yourself wondering, how much more could you possibly experience?")
			print(Fore.YELLOW + "HINT" + Fore.WHITE + " Use the \"look\" command to find your weapon!")
		elif self.status["yourTent"] == 1:
			print("The room is the same as before, however using the \"look\" command might be beneficial...")
		elif self.status["yourTent"] == 2 and self.status["miyajiTent"] == 1 and self.status["auraeTent"] == 2 and self.status["agrippaTent"] == 1 and self.status["spawn"] == 1:
			user = input("You have finished the level, ready to continue? (Y/n)")
			if user == "Y" or "y":
				self.levelStatus = False
			else:
					print("Returning to level")
		else:
			print("There seems to be nothing else of importance here")
	
	def miyajiFight(self, player):
		print("\n\tCombat in this game is simple. You have abilities that you gain throughout the game")
		print("\tUsing abilities cost SP, when you run out of SP you can either use an item to restore it, or resort to weapons")
		print("\tWeapons are the other attack option. They do not cost SP but are normally also less powerful. Balancing weapons")
		print("\tand skills is key to victory. Let us practice!")
		miyaji = Enemy()
		miyaji.setName("Miyaji")
		self.fight(player, miyaji)
		
		
	def move(self, curLoc, dir, player):
		if curLoc == 0:
			if dir == 1:
				self.miyajiTent(player)
			elif dir == 2:
				self.auraeTent(player)
			elif dir == 3:
				self.yourTent(player)
			elif dir == 4:
				self.agrippaTent(player)
		elif curLoc == 1:
			if dir == 0:
				self.spawn(player)
		elif curLoc == 2:
			if dir == 0:
				self.spawn(player)
		elif curLoc == 3:
			if dir == 0:
				self.spawn(player)
		elif curLoc == 4:
			if dir == 0:
				self.spawn(player)
		
				