from Enemy import Enemy
from Level import Level
from colorama import Fore, Back, Style, init
init() #start the colorama function
init(autoreset=True) #makes sure each line's settings are unique

class LevelTwentyFive(Level):
	status = {
	"spawn": 0
	}
	
	levelStatus = True
	
	def __init__(self):
		self.levelStatus = True
		
	def spawn(self, player):
		player.reset()
		self.getTitle("Mount Vashar")
		player.setLocation(143)
		
		print("At the top of the summit the group is horrified as they see a giant pile of dried and drained bodies.")
		print(Fore.YELLOW + "Master Wu" + Fore.WHITE + ": Impossible! He's been sucking the life force out of his victims to summon demons within them!")
		print(Fore.YELLOW + "Ragnar" + Fore.WHITE + ": How many innocent people have to die!? I will destroy this Morfix")
		print(Fore.RED + "\nMorfix" + Fore.WHITE + ": It is funny how frail you beings are, are you gonna cry for your friends now? Ahahaha!")
		print("\tI will destroy this world just as my father destroyed me.")
		print("\nMorfix notices you and a look of shock takes his face.")
		print("\n" + Fore.RED + "Morfix" + Fore.WHITE + ": So you are alive still brother? I guess I will have to fix that.\n\tI will give this world the pain our father gave us, what he gave me!")
		print("\n" + Fore.YELLOW + player.getName() + Fore.WHITE + ": I will save you brother, and I will save this world too!")
		print("\n" + Fore.RED + "Morfix" + Fore.WHITE + ": I'm done playing, I will end you all now.")
		
		morfix = Enemy()
		morfix.setName("Morfix")
		morfix.setHP(150)
		morfix.setTotalHP(150)
		self.fight(player, morfix)
		
		print(Style.BRIGHT + "After significantlly weakening Morfix you sprint and leap into the air, making contact with his head")
		print(Style.BRIGHT + "The moment your touch reaches him, Morfix glows an intense white and begins to shift into your brother.")
		print(Style.BRIGHT + "You are reunited at long last!")
		print(Fore.YELLOW + "Brother" + Fore.WHITE + ": Thank you brother... By the way you're friends are alive...")
		print("After muttering those words your brother passes out from exhaustion, but he gives you hope.")
		print("\n" + Fore.YELLOW + "Apaethos" + Fore.WHITE + ": " + player.getName() + ", you know what to do now.")
		print(Style.BRIGHT + "You place the embued gemstone on to a staff Master Wu gives you.")
		print(Style.BRIGHT + "The gemstone emits a sky covering white light, it floats up into the air and explodes releasing a shockwave")
		print(Style.BRIGHT + "Everyone cheers as the blast echos across the world, using your magic to bring \n\tall the demons back to their original form.")
		print(Fore.CYAN + Style.BRIGHT + "Congratulations! You beat the game!")
		self.levelStatus = False
		